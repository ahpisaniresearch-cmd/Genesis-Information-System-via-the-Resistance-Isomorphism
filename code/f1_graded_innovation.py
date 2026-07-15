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

"""F1 — graded-innovation echo (self-authored). Idempotence as the hinge.
Three FROZEN measures (committed before run):
  M1 irreducibility (binary, quantity-free): 1 if F has no decomposition, else 0.
  M2 decomposition-normalised (quantity-free): 1/(1+|Dec(F)|).
  M3 generator-power indicator (BOUNDARY CONTROL, reads generator id + multiplicity,
     deliberately circular): 1/k if F = g^k for a single generator g, else 0.
Arm A: classical logic on {p,q}, rule = AND (idempotent) -> powers collapse. Predicted NULL.
Arm B: resource tensor on {a,b}, formulas = multisets deg<=6, rule = multiset-sum. Predicted shading.
Circularity guard: the tensor monoid IS the factorization monoid (tautological); the only
non-circular content is whether a quantity-free measure (M1/M2) lands on the Lambda shape.
"""
from fractions import Fraction
from itertools import product

DEG = 6

# ================= Arm B: resource tensor on {a,b} =================
# formula = (na, nb), 1 <= na+nb <= DEG.  atoms (1,0),(0,1). rule: componentwise sum.
formsB = [(na, nb) for na in range(DEG+1) for nb in range(DEG+1) if 1 <= na+nb <= DEG]

def dec_B(F):
    na, nb = F
    pairs = set()
    for xa in range(na+1):
        for xb in range(nb+1):
            X = (xa, xb)
            if X == (0, 0) or X == F:
                continue
            Y = (na-xa, nb-xb)
            pairs.add(frozenset([X, Y]) if X != Y else frozenset([X]))
    return pairs

def M1_B(F): return 1 if len(dec_B(F)) == 0 else 0
def M2_B(F): return Fraction(1, 1+len(dec_B(F)))
def M3_B(F):
    na, nb = F
    if na == 0 or nb == 0:            # single generator -> a power g^k
        return Fraction(1, na+nb)
    return Fraction(0)

def typ(F):
    na, nb = F
    if na+nb == 1: return 'atom'
    if na == 0 or nb == 0: return 'pure-power'
    return 'mixed'

print("="*70)
print("ARM B  (resource tensor, non-idempotent; predicted shading)")
print("="*70)
print(f"formulas (multisets deg<= {DEG}): {len(formsB)}")
# summarise M1/M2/M3 by type
from collections import defaultdict
byT = defaultdict(list)
for F in formsB:
    byT[typ(F)].append(F)
print("\nInnovation by measure and type (Arm B):")
for T in ['atom','pure-power','mixed']:
    fs = sorted(byT[T], key=lambda F:(F[0]+F[1], F))
    m1 = sorted(set(M1_B(F) for F in fs))
    print(f"\n  {T}  ({len(fs)} formulas)")
    print(f"    M1 values: {m1}")
    # M2 and M3 per degree, showing spread
    for F in fs:
        na,nb=F
        lbl = f"a^{na}" if nb==0 else (f"b^{nb}" if na==0 else f"a^{na}b^{nb}")
        print(f"      {lbl:<8} deg{na+nb} rank{na+nb-1}:  M1={M1_B(F)}  M2={str(M2_B(F)):>5}  M3={str(M3_B(F)):>5}")

print("\n--- Arm B shape check ---")
powers = [ (k, M3_B((k,0)), M2_B((k,0))) for k in range(1,DEG+1) ]
print("  pure powers a^k:  M3 = 1/k (Lambda-like)?  ", all(M3_B((k,0))==Fraction(1,k) for k in range(1,DEG+1)))
print("  mixed all M3 = 0 (Lambda-like)?            ", all(M3_B(F)==0 for F in byT['mixed']))
print("  mixed all M2 = 0 ?                          ", all(M2_B(F)==0 for F in byT['mixed']),
      " (M2 mixed values:", sorted(set(M2_B(F) for F in byT['mixed'])), ")")
print("  M2 separates pure vs mixed?                ",
      set(M2_B(F) for F in byT['pure-power'] if (F[0]+F[1])>=2).isdisjoint(set(M2_B(F) for F in byT['mixed'])))
print("  M1 binary (only atoms innovate)?           ", all(M1_B(F)==0 for F in formsB if typ(F)!='atom'))

# ================= Arm A: classical logic on {p,q}, rule = AND =================
# valuations (pv,qv); class = truth-set. label by generating atom-subset.
VAL = list(product([0,1], repeat=2))   # (p,q)
p_set = frozenset(v for v in VAL if v[0]==1)
q_set = frozenset(v for v in VAL if v[1]==1)
# closure under intersection from {p,q}
label = {p_set: frozenset(['p']), q_set: frozenset(['q'])}
frontier = [p_set, q_set]
changed = True
while changed:
    changed = False
    cur = list(label.keys())
    for X in cur:
        for Y in cur:
            Z = X & Y
            if Z not in label:
                label[Z] = label[X] | label[Y]
                changed = True
derivA = list(label.keys())

def rule_A(X, Y): return X & Y
def dec_A(F):
    pairs = set()
    for X in derivA:
        if X == F: continue
        for Y in derivA:
            if Y == F: continue
            if rule_A(X, Y) == F:
                pairs.add(frozenset([X, Y]) if X != Y else frozenset([X]))
    return pairs
def M1_A(F): return 1 if len(dec_A(F))==0 else 0
def M2_A(F): return Fraction(1, 1+len(dec_A(F)))
def M3_A(F):
    # single generator (idempotent -> no powers): |atom-label|==1 -> g^1
    return Fraction(1,1) if len(label[F])==1 else Fraction(0)

print("\n"+"="*70)
print("ARM A  (classical AND, idempotent; predicted NULL/binary)")
print("="*70)
print(f"Lindenbaum-Tarski classes reachable by AND-closure from {{p,q}}: {len(derivA)}")
for F in sorted(derivA, key=lambda s: (len(label[s]), sorted(label[s]))):
    lab = "&".join(sorted(label[F]))
    print(f"    class [{lab:<5}] rank{len(label[F])-1}:  M1={M1_A(F)}  M2={str(M2_A(F)):>5}  M3={str(M3_A(F)):>5}")
print("\n--- Arm A shape check ---")
print("  M1 binary (only atoms innovate)? ", all(M1_A(F)==0 for F in derivA if len(label[F])>1))
print("  any graded power ladder?          ", "NO — idempotence collapses powers (no g^k for k>=2 exists)")

print("\n"+"="*70)
print("SUMMARY")
print("="*70)
print("  M1 (quantity-free): BINARY in both arms — atoms 1, all composites 0.")
print("  M2 (quantity-free): Arm B graded but NOT Lambda (mixed != 0; pure/mixed not separated);")
print("                      Arm A trivial (one composite at 1/2).")
print("  M3 (boundary control, circular): Arm B = clean Lambda (1/k powers, 0 mixed);")
print("                      Arm A = binary (idempotence destroys powers).")
