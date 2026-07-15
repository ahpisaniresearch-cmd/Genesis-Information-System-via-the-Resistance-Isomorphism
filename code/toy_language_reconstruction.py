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

"""
GIP - toy-language reconstruction from erasure alone
====================================================
The crux test. Fix a hidden genesis semantics (primitive meanings = primes;
composite meanings = squarefree products). Expose ONLY erasures:
  - meet-erasure E(a,b): relate two meanings, keep the shared part (gcd),
    FORGET the symmetric difference. Observable = resistance of what was forgotten.
  - reset-erasure norm(a): forget a meaning entirely. Observable = its resistance.
Ask: can the meaning-skeleton (the overlap/gcd lattice and its dimension) be
reconstructed from these erasures? And what is NOT recoverable (the gauge)?
"""
import numpy as np
from math import log
from itertools import combinations

# ---------- hidden semantics (behind the barrier) ----------
primes = [2, 3, 5, 7, 11]                       # primitive meanings
lnp = {p: log(p) for p in primes}
chosen = [(2,3),(2,5),(3,5),(2,7),(5,7),(7,11),(2,3,5),(3,7,11),(2,11),(3,5,7)]
ent_set = {}
for s in chosen:
    n = 1
    for p in s: n *= p
    ent_set[n] = set(s)
ents = list(ent_set.keys()); K = len(ents)

# true feature vectors (hidden): u_a[p] = sqrt(ln p) if p | a
U = np.array([[(lnp[p]**0.5 if p in ent_set[n] else 0.0) for p in primes] for n in ents])

# ---------- the OBSERVABLE erasure trace ----------
# meet-erasure = resistance of the symmetric difference of prime-sets
E = np.array([[sum(lnp[p] for p in (ent_set[a] ^ ent_set[b])) for b in ents] for a in ents])
# reset-erasure = own resistance
norm = np.array([sum(lnp[p] for p in ent_set[a]) for a in ents])

# ---------- CRUX 1: meet-erasure IS squared distance in meaning-space ----------
Dtrue = np.array([[np.sum((U[i]-U[j])**2) for j in range(K)] for i in range(K)])
print("meet-erasure E(a,b) == squared distance in meaning-space:", np.allclose(E, Dtrue))

# ---------- CRUX 2: overlaps (shared meaning) recovered from erasures ----------
maxerr = max(abs((norm[i]+norm[j]-E[i,j])/2 - sum(lnp[p] for p in (ent_set[ents[i]]&ent_set[ents[j]])))
             for i, j in combinations(range(K), 2))
print(f"shared-meaning Omega(gcd) = (norm_a + norm_b - E)/2, max error vs truth: {maxerr:.1e}")

# ---------- reconstruct the skeleton by classical MDS on the erasures ----------
J = np.eye(K) - np.ones((K, K))/K
B = -0.5 * J @ E @ J
evals, evecs = np.linalg.eigh(B)
o = np.argsort(evals)[::-1]; evals, evecs = evals[o], evecs[:, o]
dim = int((evals > 1e-9).sum())
coords = evecs[:, :dim] * np.sqrt(evals[:dim])
print(f"\nrecovered # primitive meanings (MDS embedding dimension): {dim}   (true: {len(primes)})")
print(f"MDS eigenvalues: {np.round(evals[:dim+1], 3)}")

# ---------- the gauge: geometry recovered up to isometry, labels not fixed ----------
Uc, Cc = U - U.mean(0), coords - coords.mean(0)
Us, _, Vt = np.linalg.svd(Uc.T @ Cc); R = Vt.T @ Us.T
align_err = np.max(np.abs(Cc @ R - Uc))
print(f"\nafter optimal rotation (the gauge), recovered vs true features: {align_err:.1e}")
print("-> meaning-geometry recovered EXACTLY up to rotation/reflection (gauge);")
print("   the prime LABELS are the choice of axes inside that geometry - NOT fixed by erasure.")
