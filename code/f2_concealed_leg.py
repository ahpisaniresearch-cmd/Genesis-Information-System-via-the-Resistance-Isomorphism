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

"""F2 — ledger cost of hiding in HEAT currency (self-authored).
Concealed leg C = H(pattern) - H(heat) for cascade hiders. FROZEN measures:
 (1) raw C(d); (2) C/(s*ln2) [vs log #configs]; (3) phi = C/H(pattern) [added];
 (4) TV(hider,reference) [secondary]. Canonical exact cascades added for clarity.
Free-support machines have C=0 (outcome=heat). Expectation: park."""
import math
import numpy as np
from fractions import Fraction
from collections import defaultdict
from math import comb, ceil

LN2 = math.log(2)

def hbin(p):
    p = float(p)
    if p <= 0.0 or p >= 1.0: return 0.0
    return -p*math.log(p) - (1-p)*math.log(1-p)
def Hpattern(qs): return sum(hbin(q) for q in qs)
def pb_exact(qs):
    pmf = {0: Fraction(1)}
    for q in qs:
        new = defaultdict(Fraction)
        for m,w in pmf.items():
            new[m] += w*(1-q); new[m+1] += w*q
        pmf = dict(new)
    return pmf
def pb_float(qs):
    pmf = {0: 1.0}
    for q in qs:
        new = defaultdict(float)
        for m,w in pmf.items():
            new[m] += w*(1-q); new[m+1] += w*q
        pmf = dict(new)
    return pmf
def Hdist(pmf):
    return -sum(float(w)*math.log(float(w)) for w in pmf.values() if float(w) > 0)
def cums(pmf, order):
    mu = [0.0]*(order+1); mu[0]=1.0
    for r in range(1,order+1):
        mu[r] = sum((m**r)*float(w) for m,w in pmf.items())
    kap=[0.0]*(order+1)
    for n in range(1,order+1):
        s=mu[n]
        for m in range(1,n): s -= comb(n-1,m-1)*kap[m]*mu[n-m]
        kap[n]=s
    return kap[1:]
def TV(P,Q):
    keys=set(P)|set(Q)
    return 0.5*sum(abs(float(P.get(k,0))-float(Q.get(k,0))) for k in keys)

# ---------- Part 1: canonical cascades, EXACT ----------
print("="*74)
print("PART 1  Canonical cascades, exact rational distributions")
print("="*74)
print(f"{'family':<16}{'s':>2}{'H(pattern)':>12}{'H(heat)':>10}{'C':>10}{'C/(s ln2)':>11}{'phi=C/Hpat':>11}")
for name, qf in [("genesis 2^-k", lambda s:[Fraction(1,2**k) for k in range(1,s+1)]),
                 ("fair-coin 1/2", lambda s:[Fraction(1,2) for _ in range(s)])]:
    for s in range(2,7):
        qs=qf(s)
        Hp=Hpattern(qs); pmf=pb_exact(qs); Hh=Hdist(pmf); C=Hp-Hh
        print(f"{name:<16}{s:>2}{Hp:>12.5f}{Hh:>10.5f}{C:>10.5f}{C/(s*LN2):>11.5f}{(C/Hp if Hp>0 else 0):>11.5f}")

# ---------- Part 2: B6 matched pairs (reference vs hider), numerical ----------
print("\n"+"="*74)
print("PART 2  B6 matched pairs: (d+1)-stage reference vs hider matching kappa_1..kappa_d")
print("="*74)
print(f"{'d':>2}{'stages':>7}{'kmatch':>7}{'kdiff':>6}{'C_ref':>9}{'C_hid':>9}"
      f"{'Cref/(s ln2)':>13}{'phi_ref':>9}{'TV(ref,hid)':>12}")
for d in range(1,6):
    s=d+1
    b=np.linspace(0.2,0.8,s)
    poly=np.poly(b)
    hider=None
    for delta in (1e-2,3e-3,1e-3,3e-4,1e-4,3e-5,1e-5):
        p2=poly.copy(); p2[-1]+=delta
        r=np.roots(p2)
        if np.max(np.abs(r.imag))<1e-9:
            rr=np.sort(r.real)
            if rr.min()>1e-6 and rr.max()<1-1e-6 and np.max(np.abs(rr-np.sort(b)))>1e-9:
                hider=rr; break
    if hider is None:
        print(f"{d:>2}{s:>7}  no valid hider found"); continue
    pmfb=pb_float(b); pmfh=pb_float(hider)
    kb=cums(pmfb,d+1); kh=cums(pmfh,d+1)
    match=all(abs(kb[i]-kh[i])<1e-8 for i in range(d)); diff=abs(kb[d]-kh[d])>1e-8
    Cb=Hpattern(b)-Hdist(pmfb); Ch=Hpattern(hider)-Hdist(pmfh)
    Hpb=Hpattern(b); tv=TV(pmfb,pmfh)
    print(f"{d:>2}{s:>7}{str(match):>7}{str(diff):>6}{Cb:>9.4f}{Ch:>9.4f}"
          f"{Cb/(s*LN2):>13.4f}{Cb/Hpb:>9.4f}{tv:>12.6f}")

# ---------- Part 3: free-support contrast ----------
print("\n"+"="*74)
print("PART 3  Free-support hider contrast")
print("="*74)
for d in range(1,6):
    print(f"  d={d}: free-support machine needs ceil(d/2)+1 = {ceil(d/2)+1} points;  "
          f"outcome = count = heat  ->  H(pattern|heat) = 0  (no concealed leg)")

print("\n"+"="*74); print("READINGS"); print("="*74)
print("  C is dominated by H(pattern)=sum h(q_k); H(heat)<=log(s+1) grows only logarithmically.")
print("  C/(s ln2) -> the average stage entropy / ln2 (fair-coin -> ~1; genesis -> ->0 as it saturates).")
print("  => normalized concealed leg reduces to stage-count bookkeeping. Free-support C=0.")
