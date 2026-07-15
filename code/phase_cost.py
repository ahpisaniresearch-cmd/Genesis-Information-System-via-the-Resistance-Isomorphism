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
Genesis Information Project - the phase cost
============================================
The reverse-scattering of a merge to n is the classical mixture (maximally mixed,
entropy ln(n+1)). Using the phase generated last step, we put a DEFINITE phase on
it - a coherent superposition - and read the cost two ways:

  - how much information the phase coherence holds (entropy removed vs the mixture);
  - what erasing the phase costs (decohere the pure state -> entropy created).

Then we ask the split-blindness question both for the COST and for the per-split
phase ANGLE: does phase let the ledger tell (3,5) from (1,7) at n=8?
"""

import numpy as np
from math import log, pi


def vn_entropy(rho):
    ev = np.linalg.eigvalsh(rho)
    ev = ev[ev > 1e-12]
    return float(-np.sum(ev * np.log(ev)))


print("Phase cost of the scattering (all in nats):\n")
print(f"{'n':>3} | {'classical mix S':>15} | {'phased pure S':>13} | "
      f"{'erase phase (decohere)':>22} | {'merge-erasure ln(n+1)':>21}")
print("-" * 86)
for n in [1, 2, 3, 4, 8]:
    d = n + 1
    w = np.exp(2j * pi / d)
    rho_mix = np.eye(d) / d                                  # the classical scattering
    psi = np.array([w ** k for k in range(d)]) / np.sqrt(d)  # phased coherent superposition
    rho_pure = np.outer(psi, psi.conj())
    rho_dec = np.diag(np.diag(rho_pure))                     # lose the phase (off-diagonals -> 0)
    S_mix = vn_entropy(rho_mix)
    S_pure = vn_entropy(rho_pure)
    erase_phase = vn_entropy(rho_dec) - S_pure               # entropy created by losing phase
    print(f"{n:>3} | {S_mix:>15.4f} | {S_pure:>13.4f} | "
          f"{erase_phase:>22.4f} | {log(n + 1):>21.4f}")

print("\nDoes phase break the split-blindness at n=8?\n")
print(f"{'split (a, 8-a)':>14} | {'index k':>7} | {'phase angle':>11} | "
      f"{'phase cost':>10} | {'merge-erasure':>13}")
print("-" * 68)
d = 9
for k in range(9):
    print(f"{str((k, 8 - k)):>14} | {k:>7} | {360 * k / 9:>9.0f} d | "
          f"{'ln 9':>10} | {'ln 9 = 2.197':>13}")
print("\n  per-split phase ANGLE varies with k (positional) - splits are now distinguishable;")
print("  per-split phase COST is ln 9 for every split (uniform) - the COST is still split-blind;")
print("  and the angle is positional, not arithmetic: nothing marks (3,5) as a prime pair.")
