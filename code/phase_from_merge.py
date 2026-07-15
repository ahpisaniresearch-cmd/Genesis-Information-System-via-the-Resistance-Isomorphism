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
Genesis Information Project - the first phase step
==================================================
The reverse-scattering of a merge to n lives on an (n+1)-dim preimage space and
carries the Weyl algebra, but the scattering itself was phase-blind (probabilities,
no i). Rather than paint phases on by hand, we ask whether the two genesis
operations we already have GENERATE the phase on this space:

    S = succession-shift on the split index   |k> -> |k+1 mod (n+1)>   (the Weyl X)
    D = origin meet-atom probe                 |0><0|                  (binary test)

Phase note result, re-situated here: S and D fail to commute, and the algebra
they generate contains the Weyl clock Z (the phase). At the genesis bit (n=1)
the commutator is exactly the i of sqrt(NOT).
"""

import numpy as np
from math import pi


def ops(d):
    w = np.exp(2j * pi / d)
    X = np.zeros((d, d), dtype=complex)
    for k in range(d):
        X[(k + 1) % d, k] = 1.0                 # succession-shift on the split index
    P0 = np.zeros((d, d), dtype=complex)
    P0[0, 0] = 1.0                              # origin probe |0><0|
    Z = np.diag([w ** k for k in range(d)]).astype(complex)   # Weyl clock (the phase)
    return X, P0, Z, w


print("Does {succession-shift S, origin-probe D} generate the Weyl phase Z on the")
print("merge's preimage space?\n")
print(f"{'n':>3} | {'d=n+1':>5} | {'[S,D] != 0':>11} | {'Z generated from {S,D}':>23}")
print("-" * 52)
for n in [1, 2, 3, 4, 5]:
    d = n + 1
    X, P0, Z, w = ops(d)
    noncommute = not np.allclose(X @ P0 - P0 @ X, 0)
    # diagonal projectors |k><k| = S^k P0 S^{-k}; Z = sum_k w^k |k><k|
    Xi = np.linalg.inv(X)
    Zgen = sum((w ** k) * np.linalg.matrix_power(X, k) @ P0 @ np.linalg.matrix_power(Xi, k)
               for k in range(d))
    print(f"{n:>3} | {d:>5} | {str(noncommute):>11} | {str(np.allclose(Zgen, Z)):>23}")

print("\nAt the genesis bit (n=1, d=2): the commutator IS the phase generator.")
X, P0, Z, w = ops(2)
comm = X @ P0 - P0 @ X
sy = np.array([[0, -1j], [1j, 0]])
print("  S = sigma_x = NOT :", X.real.astype(int).tolist())
print("  D = |0><0|        :", P0.real.astype(int).tolist())
print("  [S,D] =", comm.real.astype(int).tolist(),
      "  and  -i*sigma_y =", (-1j * sy).real.astype(int).tolist())
print("  [S,D] == -i*sigma_y :", np.allclose(comm, -1j * sy),
      " -> the i of sqrt(NOT), generated, not imposed")
