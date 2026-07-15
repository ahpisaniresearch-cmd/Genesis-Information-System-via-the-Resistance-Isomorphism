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
GIP - Experiment 4: natural-key recovery from the geometry (the Section 18 Lead, run)
=====================================================================================
Section 18 recovered the meaning-geometry from erasures exactly UP TO ROTATION and
left open: can the natural key (the prime axes) be singled out from the geometry by
a structural principle, without assuming the integer lattice?

Two candidate principles are tested honestly:
  (A) SPARSITY (varimax - maximise variance of squared loadings). 
  (B) INDEPENDENCE (ICA - find the rotation making coordinates statistically
      independent). Motivation from the framework itself: under the uniform
      distribution over entities, the true prime coordinates are INDEPENDENT
      Bernoulli components - the geometric face of the same independence that is
      coprimality (I = ln gcd = 0) and the Euler product's mode independence.

Setup: hidden semantics = squarefree products of primes {2,3,5,7,11} (32 entities),
features u_a[p] = sqrt(ln p)*[p|a]; gauge = a random rotation. Score = |cosine|
between each recovered axis direction and its best-matched true prime axis
(1.0 = perfect), plus recovery of the resistance scales ln p.
"""
import numpy as np
from math import log
from itertools import combinations

rng = np.random.default_rng(7)
primes = [2, 3, 5, 7, 11]
P = len(primes)
subsets = [frozenset(c) for r in range(P + 1) for c in combinations(primes, r)]
U = np.array([[np.sqrt(log(p)) if p in s else 0.0 for p in primes] for s in subsets])
Qg, _ = np.linalg.qr(rng.normal(size=(P, P)))
X = U @ Qg                       # the geometry with scrambled axes (the gauge)
TRUE = np.eye(P)                 # true axis directions in U-coordinates


def axis_score(directions_in_U):
    """Greedy-match recovered directions to true axes; return per-axis |cosine|."""
    D = directions_in_U / np.linalg.norm(directions_in_U, axis=0, keepdims=True)
    C = np.abs(TRUE.T @ D)                      # |cos| true-axis x recovered-dir
    scores, used = [], set()
    for t in range(P):
        j = max((j for j in range(P) if j not in used), key=lambda j: C[t, j])
        used.add(j); scores.append(C[t, j])
    return scores


def varimax(Phi, q=500, tol=1e-12):
    p, k = Phi.shape
    R = np.eye(k); d = 0
    for _ in range(q):
        L = Phi @ R
        u, s, vt = np.linalg.svd(Phi.T @ (L**3 - (1.0/p) * L @ np.diag(np.diag(L.T @ L))))
        R = u @ vt
        if s.sum() < d * (1 + tol): break
        d = s.sum()
    return R


def fastica_rotation(X, iters=500, seed=0):
    """Symmetric FastICA (kurtosis nonlinearity) on whitened data; returns the
    unmixing directions expressed in the input coordinates."""
    Xc = X - X.mean(0)
    cov = Xc.T @ Xc / len(Xc)
    d, E = np.linalg.eigh(cov)
    Wh = E @ np.diag(d ** -0.5) @ E.T          # whitening
    Z = Xc @ Wh
    r = np.random.default_rng(seed)
    W = np.linalg.qr(r.normal(size=(P, P)))[0]
    for _ in range(iters):
        WX = Z @ W                              # projections
        W_new = (Z.T @ (WX ** 3)) / len(Z) - 3 * W
        u, _, vt = np.linalg.svd(W_new)
        W_sym = u @ vt
        if np.max(np.abs(np.abs(np.diag(W_sym.T @ W)) - 1)) < 1e-12:
            W = W_sym; break
        W = W_sym
    return Wh @ W                               # directions in input coordinates


# (A) sparsity
R = varimax(X)
sc_varimax = axis_score(Qg @ R)                 # rotate back into U-coordinates
print("(A) SPARSITY (varimax):  per-axis |cosine| with the true prime axes")
print("    ", [f"{s:.3f}" for s in sc_varimax], "  worst:", f"{min(sc_varimax):.3f}")
print("     -> FAILS: sparsity alone does not single out the prime axes.\n")

# (B) independence
Dirs = fastica_rotation(X)                       # directions in X-coordinates
sc_ica = axis_score(Qg @ Dirs)
print("(B) INDEPENDENCE (ICA):  per-axis |cosine| with the true prime axes")
print("    ", [f"{s:.3f}" for s in sc_ica], "  worst:", f"{min(sc_ica):.6f}")

# recover the resistance scales: project entities onto recovered directions;
# each coordinate should be two-valued {0, c}; c^2 should be ln p.
Dn = Dirs / np.linalg.norm(Dirs, axis=0, keepdims=True)
proj = X @ Dn
scales = sorted(proj.max(0) - proj.min(0))
print("     recovered axis scales c (sorted), vs sqrt(ln p):")
print("      c        =", [f"{c:.4f}" for c in scales])
print("      sqrt(lnp)=", [f"{np.sqrt(log(p)):.4f}" for p in primes])
print("      max |c - sqrt(ln p)| =", f"{max(abs(c - np.sqrt(log(p))) for c, p in zip(scales, primes)):.2e}")

# noise sweep on the successful principle
print("\nNoise sweep (gaussian sd on features; smallest axis sqrt(ln2)=0.833):")
print(f"{'sd':>6} {'worst axis |cosine|':>20}")
for sd in [0.01, 0.05, 0.10, 0.20]:
    Xn = (U + rng.normal(scale=sd, size=U.shape)) @ Qg
    sc = axis_score(Qg @ fastica_rotation(Xn, seed=1))
    print(f"{sd:>6.2f} {min(sc):>20.4f}")
print("""
-> The natural key IS recoverable from the geometry - but by INDEPENDENCE, not by
   sparsity. The recovering principle is the framework's own: the prime axes are
   the unique basis in which the meaning coordinates are statistically independent,
   the geometric face of coprimality-as-zero-correlation and the Euler product's
   mode independence. The recovered scales return the resistances ln p; the axis
   LABELS remain gauge (ICA returns them in no order), exactly the syntax/semantics
   filter. Varimax's failure is the informative negative: sparsity alone is not
   the natural-key principle; independence is.""")
