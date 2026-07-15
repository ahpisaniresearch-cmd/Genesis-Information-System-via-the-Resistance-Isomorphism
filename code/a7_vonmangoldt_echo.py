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

import math
from collections import defaultdict

def fstr(f):
    if isinstance(f, str):
        return f
    return "(" + fstr(f[1]) + u"\u2192" + fstr(f[2]) + ")"

ATOMS = ['p', 'q']
POOL0 = list(ATOMS)
POOL1 = [('->', a, b) for a in POOL0 for b in POOL0]
POOL = POOL0 + POOL1

def K(A, B): return ('->', A, ('->', B, A))
def S(A, B, C): return ('->', ('->', A, ('->', B, C)), ('->', ('->', A, B), ('->', A, C)))

axioms = set()
for A in POOL:
    for B in POOL: axioms.add(K(A, B))
for A in POOL0:
    for B in POOL:
        for C in POOL0: axioms.add(S(A, B, C))
axioms = sorted(axioms, key=fstr)
axiom_set = set(axioms)

SIZE_CAP = 11
counts = defaultdict(lambda: defaultdict(int))
for ax in axioms: counts[1][ax] = 1
for s in range(2, SIZE_CAP + 1):
    for s1 in range(1, s - 1):
        s2 = s - 1 - s1
        if s2 < 1: continue
        for f1, c1 in counts[s1].items():
            if not (isinstance(f1, tuple) and f1[0] == '->'): continue
            A, B = f1[1], f1[2]
            c2 = counts[s2].get(A, 0)
            if c2: counts[s][B] += c1 * c2

n_proofs = defaultdict(int)
min_size = {}
for s in range(1, SIZE_CAP + 1):
    for f, c in counts[s].items():
        n_proofs[f] += c
        if f not in min_size: min_size[f] = s

N = sum(n_proofs.values())
derivable = set(n_proofs.keys())
T = len(derivable)
print(f"Axiom instances: {len(axioms)};  proof trees N = {N};  theorems T = {T}")

def atoms_of(f):
    if isinstance(f, str): return {f}
    return atoms_of(f[1]) | atoms_of(f[2])
def subformulas(f):
    s = {f}
    if isinstance(f, tuple):
        s |= subformulas(f[1]); s |= subformulas(f[2])
    return s

p = {t: n_proofs[t] / N for t in derivable}
def H_subset(Sset):
    P = sum(p[t] for t in Sset)
    if P <= 0: return 0.0
    return -sum((p[t] / P) * math.log(p[t] / P) for t in Sset if p[t] > 0)

# (0) inference rank = MP-closure depth
rank = {ax: 0 for ax in axiom_set}
ranked = set(axiom_set)
k = 0
while True:
    k += 1
    new = set()
    for f1 in ranked:
        if isinstance(f1, tuple) and f1[0] == '->':
            A, B = f1[1], f1[2]
            if A in ranked and (B in derivable) and (B not in ranked): new.add(B)
    if not new: break
    for b in new: rank[b] = k
    ranked |= new
all_ranked = (ranked == derivable)
max_rank = max(rank.values())
print(f"\n(0) Inference rank (MP-closure depth): every theorem ranked = {all_ranked}; max rank = {max_rank}")
rank_hist = defaultdict(int)
for t in derivable: rank_hist[rank[t]] += 1
for r in range(max_rank + 1):
    n_ax = sum(1 for t in derivable if rank[t] == r and t in axiom_set)
    print(f"    rank {r}: {rank_hist[r]:>3} theorems  ({n_ax} axioms, {rank_hist[r]-n_ax} non-axioms)")

# (1) irreducible innovators (order-free, magnitude-free)
mp_derivable = set()
for f1 in derivable:
    if isinstance(f1, tuple) and f1[0] == '->':
        A, B = f1[1], f1[2]
        if A in derivable: mp_derivable.add(B)
irreducible = derivable - mp_derivable
redundant_axioms = mp_derivable & axiom_set
nonaxiom_derivable = mp_derivable - axiom_set
print("\n(1) Irreducible innovators (no MP derivation within the set -> must be axioms):")
print(f"    |irreducible| = {len(irreducible)};  all are axioms: {irreducible <= axiom_set}")
print(f"    |MP-derivable| = {len(mp_derivable)} = redundant axioms {len(redundant_axioms)} + non-axiom theorems {len(nonaxiom_derivable)}")
print(f"    check: {len(irreducible)} + {len(mp_derivable)} = {len(irreducible)+len(mp_derivable)} (T={T})")
print("    graded middle (partial innovators between full and none): NONE — innovation is binary")

# (2) symbolic-novelty check
mp_steps = 0; concl_is_subformula = 0; concl_new_atom = 0
for f1 in derivable:
    if isinstance(f1, tuple) and f1[0] == '->':
        A, B = f1[1], f1[2]
        if A in derivable:
            mp_steps += 1
            if B in subformulas(f1): concl_is_subformula += 1
            if atoms_of(B) - (atoms_of(A) | atoms_of(f1)): concl_new_atom += 1
print("\n(2) Symbolic novelty of MP conclusions (over all derivable premise pairs):")
print(f"    MP steps = {mp_steps}")
print(f"    conclusion is a subformula of the major premise: {concl_is_subformula}/{mp_steps} ({100*concl_is_subformula/mp_steps:.1f}%)")
print(f"    conclusion introduces a NEW atom: {concl_new_atom}/{mp_steps} ({100*concl_new_atom/mp_steps:.1f}%)")

# (3) innovation-by-rank
print("\n(3) Innovation-by-rank: cumulative proof-weighted conclusion entropy H(<=k), increments dH")
prevH = 0.0
for r in range(max_rank + 1):
    Sset = {t for t in derivable if rank[t] <= r}
    Hk = H_subset(Sset); dH = Hk - prevH
    massr = sum(p[t] for t in derivable if rank[t] == r)
    print(f"    rank<= {r}: H = {Hk:.4f}   dH = {dH:+.4f}   (proof-mass at rank {r} = {massr:.4f})")
    prevH = Hk
print("    NOTE: dH reflects theorem-count per rank, not irreducible novelty; verdict rests on (1).")

# (4) magnitude guard: sweep by MIN PROOF SIZE
print("\n(4) Magnitude guard — innovation swept by MIN-PROOF-SIZE (a magnitude):")
sizes_present = sorted(set(min_size[t] for t in derivable))
prevH = 0.0
for sz in sizes_present:
    Sset = {t for t in derivable if min_size[t] <= sz}
    Hk = H_subset(Sset); dH = Hk - prevH
    n_here = sum(1 for t in derivable if min_size[t] == sz)
    print(f"    size<= {sz}: H = {Hk:.4f}   dH = {dH:+.4f}   ({n_here} theorems first appear at size {sz})")
    prevH = Hk
print("    Any smooth gradation here is a proof-SIZE artifact; (1) has no size input and stays binary.")
