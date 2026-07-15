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
GIP - the natural-key test, in the ordinal frame
================================================
Reframe (Pisani): the genesis "rows" are plain ordinals 1,2,3,... in the system's
OWN frame - simple succession, nothing prime about them. What reaches us is the
ordinal combined with UNIQUENESS and IRREVERSIBILITY, and that shadow is the
inverse prime. So we ask: is the prime basis a NATURAL key (forced) or a
SURROGATE key (gauge)? And where does the forcing come from?
"""
import numpy as np
from math import log

N = 60

# 1) which resistances are IRREDUCIBLE: ln n NOT expressible as ln a + ln b (a,b>1)?
#    ln n reducible  <=>  n composite.  So irreducible resistances = primes.
irreducible = [n for n in range(2, N+1)
               if not any(n % a == 0 and 1 < a < n for a in range(2, n))]
print("irreducible resistances (natural-key atoms):", irreducible)
print("  -> exactly the primes up to", N, "\n")

# 2) do the prime-resistances ADDITIVELY GENERATE every ln n?  (unique factorisation)
def exps(n, primes):
    e, m = {}, n
    for p in primes:
        while m % p == 0:
            e[p] = e.get(p, 0) + 1; m //= p
    return e, m
maxerr, allrem1 = 0.0, True
for n in range(2, N+1):
    e, rem = exps(n, irreducible)
    maxerr = max(maxerr, abs(sum(c*log(p) for p, c in e.items()) - log(n)))
    allrem1 &= (rem == 1)
print(f"every ln n = sum of prime-resistances: max error {maxerr:.1e}, "
      f"factorisation always complete: {allrem1}")
print("the generator set is UNIQUE (unique factorisation) -> a natural key EXISTS.\n")

# 3) but where does the forcing come from? geometry vs discreteness.
primes = irreducible; P = len(primes)
def vec(n):
    e, _ = exps(n, primes)
    return np.array([e.get(p, 0) for p in primes], float)
V = np.array([vec(n) for n in range(2, N+1)])        # ordinals as integer lattice points

rng = np.random.default_rng(0)
Q, _ = np.linalg.qr(rng.standard_normal((P, P)))      # a random rotation (a gauge move)
Vrot = V @ Q

D_before = np.linalg.norm(V[:, None] - V[None, :], axis=2)
D_after = np.linalg.norm(Vrot[:, None] - Vrot[None, :], axis=2)
print("geometry vs discreteness:")
print(f"  rotation preserves ALL pairwise distances (the geometry): {np.allclose(D_before, D_after)}")
print(f"  ordinals are a non-negative integer lattice in the prime basis: {np.allclose(V, np.round(V))}")
print(f"  ... and after the rotation: {np.allclose(Vrot, np.round(Vrot))}")
print("\n  => distances (geometry) do NOT fix the basis - any rotation preserves them.")
print("     the INTEGER/DISCRETE structure does, and that discreteness is succession.")
print("     so the natural key (primes) is forced by uniqueness + discreteness (the filter),")
print("     NOT by the genesis data - the primes are the shadow of plain ordinals.")
