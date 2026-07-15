# =============================================================================
#  Genesis Information System via the Resistance Isomorphism
#  (c) 2026 Alexander Pisani - Blue Mountains, NSW, Australia
#  Contact: a.h.pisani.research@gmail.com
#  Licensed under Creative Commons Attribution 4.0 International (CC BY 4.0).
#
#  Originating theory & axioms: Alexander Pisani.
#  Code, formalisation & computation: Claude (Anthropic).
#
#  Attribution to BOTH the author and the AI collaborator is required for reuse,
#  adaptation, reference (including as material for AI systems), or incorporation
#  into software, inventions, or patents. See CITATION.cff.
# =============================================================================

"""F3 — runtime-step regression (self-authored). Completes the Note A section 5 kill
diagnosis: does the DYNAMIC act-count (#K discard steps) predict ln(fan-in) where the
STATIC license budget failed? Pre-registered: promote the refinement iff #K coef is
positive & dominant, #C ~ 0, and STABLE across caps 9 and 11. Machinery reused verbatim
from structural_rules_ledger.py; anchors (N, #NF, forgotten leg) reproduced first."""
import math
import numpy as np
from collections import defaultdict
import sys
sys.setrecursionlimit(100000)

# ---- Section-4 machinery, verbatim ----
_memo = {}
def gen(size, depth):
    key = (size, depth)
    if key in _memo: return _memo[key]
    out = []
    if size == 1:
        out = [('v', i) for i in range(depth)]
    else:
        out.extend(('l', b) for b in gen(size - 1, depth + 1))
        for s1 in range(1, size - 1):
            for f in gen(s1, depth):
                for x in gen(size - 1 - s1, depth):
                    out.append(('a', f, x))
    _memo[key] = out
    return out
def typable(term):
    subst = {}
    def prune(ty):
        while ty[0]=='var' and ty[1] in subst: ty = subst[ty[1]]
        return ty
    def occurs(vid, ty):
        ty = prune(ty)
        if ty[0]=='var': return ty[1]==vid
        return occurs(vid,ty[1]) or occurs(vid,ty[2])
    def unify(a,b):
        a,b = prune(a),prune(b)
        if a[0]=='var':
            if b[0]=='var' and b[1]==a[1]: return True
            if occurs(a[1],b): return False
            subst[a[1]]=b; return True
        if b[0]=='var': return unify(b,a)
        return unify(a[1],b[1]) and unify(a[2],b[2])
    nid=[0]
    def fresh():
        nid[0]+=1; return ('var',nid[0])
    def go(t,env):
        if t[0]=='v': return env[t[1]]
        if t[0]=='l':
            tv=fresh(); body=go(t[1],[tv]+env)
            return None if body is None else ('fun',tv,body)
        f=go(t[1],env)
        if f is None: return None
        x=go(t[2],env)
        if x is None: return None
        r=fresh()
        return r if unify(f,('fun',x,r)) else None
    return go(term,[]) is not None
def shift(t,d,c=0):
    if t[0]=='v': return ('v',t[1]+d) if t[1]>=c else t
    if t[0]=='l': return ('l',shift(t[1],d,c+1))
    return ('a',shift(t[1],d,c),shift(t[2],d,c))
def subst_t(t,s,i=0):
    if t[0]=='v':
        if t[1]==i: return shift(s,i)
        return ('v',t[1]-1) if t[1]>i else t
    if t[0]=='l': return ('l',subst_t(t[1],s,i+1))
    return ('a',subst_t(t[1],s,i),subst_t(t[2],s,i))
def count_var(t,i=0):
    if t[0]=='v': return 1 if t[1]==i else 0
    if t[0]=='l': return count_var(t[1],i+1)
    return count_var(t[1],i)+count_var(t[2],i)
def step(t):
    if t[0]=='a' and t[1][0]=='l':
        k=count_var(t[1][1]); kind='K' if k==0 else ('L' if k==1 else 'C')
        return subst_t(t[1][1],t[2]),kind
    if t[0]=='a':
        r=step(t[1])
        if r: return ('a',r[0],t[2]),r[1]
        r=step(t[2])
        if r: return ('a',t[1],r[0]),r[1]
        return None
    if t[0]=='l':
        r=step(t[1])
        if r: return ('l',r[0]),r[1]
    return None
def normalize(t,fuel=2000):
    kinds={'K':0,'L':0,'C':0}
    while fuel>0:
        r=step(t)
        if r is None: return t,kinds
        t=r[0]; kinds[r[1]]+=1; fuel-=1
    raise RuntimeError("fuel")
def term_size(t):
    if t[0]=='v': return 1
    if t[0]=='l': return 1+term_size(t[1])
    return 1+term_size(t[1])+term_size(t[2])

def ols(X, y):
    """returns (coeffs incl intercept, standardized betas for non-intercept cols)"""
    n,k = X.shape
    Xd = np.column_stack([np.ones(n), X])
    beta,_,_,_ = np.linalg.lstsq(Xd, y, rcond=None)
    sy = y.std(ddof=0)
    stdbetas = []
    for j in range(k):
        sx = X[:,j].std(ddof=0)
        stdbetas.append(beta[j+1]*sx/sy if sy>0 and sx>0 else 0.0)
    return beta, stdbetas

def run(CAP):
    print("="*66); print(f"CAP {CAP}"); print("="*66)
    closed=[]
    for s in range(2,CAP+1): closed.extend(gen(s,0))
    terms=[t for t in closed if typable(t)]
    N=len(terms)
    nf_class=defaultdict(list); recs=[]
    for t in terms:
        nf,kinds=normalize(t); recs.append((t,nf,kinds)); nf_class[nf].append(t)
    fanin={}
    for nf,mem in nf_class.items():
        for t in mem: fanin[t]=len(mem)
    Hforgot=sum((len(m)/N)*math.log(len(m)) for m in nf_class.values())
    print(f"ANCHOR: typable N={N}; #NF={len(nf_class)}; forgotten leg H(term|NF)={Hforgot:.6f}")

    K=np.array([r[2]['K'] for r in recs],float)
    L=np.array([r[2]['L'] for r in recs],float)
    C=np.array([r[2]['C'] for r in recs],float)
    SZ=np.array([term_size(r[0]) for r in recs],float)
    Y=np.array([math.log(fanin[r[0]]) for r in recs],float)
    print(f"   step totals: K={int(K.sum())}, L={int(L.sum())}, C={int(C.sum())};  "
          f"C variance {'= 0 (no copies)' if C.std()==0 else '> 0'}")

    # RAW model: Y ~ K + L + C
    cols_raw = [K,L,C]; names_raw=['#K','#L','#C']
    # drop zero-variance predictors to avoid singularity, but report them as n/a
    keep=[i for i in range(3) if cols_raw[i].std()>0]
    Xr=np.column_stack([cols_raw[i] for i in keep])
    br,sbr=ols(Xr,Y)
    print("\n RAW  Y ~ #K + #L + #C   (unstandardized coef | standardized beta)")
    idx=0
    for i in range(3):
        if i in keep:
            print(f"    {names_raw[i]:>3}: coef {br[idx+1]:+.4f}   beta {sbr[idx]:+.4f}"); idx+=1
        else:
            print(f"    {names_raw[i]:>3}: n/a (zero variance)")

    # SIZE-CONTROLLED: Y ~ K + L + C + size
    cols=[K,L,C,SZ]; names=['#K','#L','#C','size']
    keep2=[i for i in range(4) if cols[i].std()>0]
    Xc=np.column_stack([cols[i] for i in keep2])
    bc,sbc=ols(Xc,Y)
    print("\n SIZE-CONTROLLED  Y ~ #K + #L + #C + size")
    idx=0
    for i in range(4):
        if i in keep2:
            print(f"    {names[i]:>4}: coef {bc[idx+1]:+.4f}   beta {sbc[idx]:+.4f}"); idx+=1
        else:
            print(f"    {names[i]:>4}: n/a (zero variance)")

run(9)
run(11)
