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
Genesis Information Project - the reverse of the merge, and the Weyl question
============================================================================
Forward: (a,b) -> n forgets the split. Force-reversing is one-to-many: n maps
back to all n+1 ordered splits. With no energy supplied the reverse spreads
uniformly over them - a scattering whose entropy is exactly ln(n+1), the erased
amount. Question: is that scattering the sqrt(NOT)/Weyl structure?

We test three things:
  1. the scattering entropy equals the erased ln(n+1);
  2. the (n+1)-dim preimage space carries the Weyl clock-shift algebra ZX = wXZ;
  3. at n=1 (the genesis bit, 2 preimages) it is exactly the Pauli algebra and
     sqrt(NOT) exists - and phase is a GENUINE addition: it enables interference
     the classical scattering (probabilities only) cannot.
"""

import numpy as np
from math import log, pi


def reverse_scattering(n):
    splits = [(a, n - a) for a in range(n + 1)]   # ordered preimages of merge -> n
    d = n + 1
    P = np.ones(d) / d                            # force-reverse, no energy: uniform
    H = -np.sum(P * np.log(P))                    # entropy of the scattering
    return splits, d, H


def weyl(d):
    w = np.exp(2j * pi / d)
    X = np.zeros((d, d), dtype=complex)
    for k in range(d):
        X[(k + 1) % d, k] = 1.0                   # shift  |k> -> |k+1 mod d>
    Z = np.diag([w ** k for k in range(d)]).astype(complex)   # clock |k> -> w^k|k>
    return X, Z, w


print("Part 1+2: scattering entropy = erased ln(n+1); the space carries the Weyl algebra\n")
print(f"{'n':>3} | {'preimages d=n+1':>15} | {'scatter entropy':>15} | "
      f"{'erased ln(n+1)':>14} | {'ZX = wXZ':>9}")
print("-" * 72)
for n in [1, 2, 3, 4, 5]:
    splits, d, H = reverse_scattering(n)
    X, Z, w = weyl(d)
    ok = np.allclose(Z @ X, w * (X @ Z))
    print(f"{n:>3} | {d:>15} | {H:>15.4f} | {log(n + 1):>14.4f} | {str(ok):>9}")

print("\nPart 3: n=1 (the genesis bit), d=2 -> the Pauli algebra and sqrt(NOT)")
X, Z, w = weyl(2)
print("  X (shift) =", X.real.astype(int).tolist(), " = sigma_x = NOT")
print("  Z (clock) =", Z.real.astype(int).tolist(), " = sigma_z")
sqrtNOT = 0.5 * np.array([[1 + 1j, 1 - 1j], [1 - 1j, 1 + 1j]])
print("  sqrt(NOT) =", np.round(sqrtNOT, 3).tolist())
print("  sqrt(NOT)^2 =", np.round((sqrtNOT @ sqrtNOT).real, 3).tolist(),
      " = NOT   (sqrt(NOT) carries i: this is phase, absent from the scattering)")

print("\nPart 4: phase is a genuine addition - it enables interference the scattering cannot")
plus = np.array([1, 1]) / np.sqrt(2)
minus = np.array([1, -1]) / np.sqrt(2)
print("  |+> and |-> classical probabilities:", (np.abs(plus) ** 2).round(3).tolist(),
      "-- identical")
print("  but <+|-> =", round(np.vdot(plus, minus).real, 3),
      " -> orthogonal; the phase carries a distinction probabilities cannot see")
s = (plus + minus)
print("  superposing them, amplitudes =", np.round(s, 3).tolist(),
      "-> the second outcome cancels to 0 (destructive interference)")
print("  classically, mixing (.5,.5)+(.5,.5) = (.5,.5): no cancellation is possible.")
