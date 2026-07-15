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
GIP - Experiment 3: the phase operationally carries the erased split
====================================================================
Section 12 established ENTROPICALLY that the phase cost equals the merge-erasure
(pure phased state, entropy 0; decohered, ln(n+1)). This experiment makes the
claim OPERATIONAL: if the phase carries the erased split, then a phase-preserving
merge must be reversible in the strongest sense - the split must be RECOVERABLE
from the phased state by a measurement, with certainty; and after decoherence the
same measurement must do no better than chance.

Construction: split k of n -> the coherent state |psi_k> = (1/sqrt d) sum_j w^{jk}|j>,
d = n+1, w = e^{2pi i/d} (the Fourier/clock basis - the phased superposition of
Section 12, one per split). Recovery = measurement in the Fourier basis.
"""
import numpy as np

print(f"{'n':>3} {'d':>3} {'min recovery prob (coherent)':>28} {'max recovery prob (decohered)':>30} {'chance 1/d':>10}")
for n in [1, 2, 4, 8, 12]:
    d = n + 1
    w = np.exp(2j * np.pi / d)
    F = np.array([[w ** (j * k) for j in range(d)] for k in range(d)]) / np.sqrt(d)  # rows = |psi_k>
    # coherent recovery: probability of outcome k when measuring |psi_k> in the Fourier basis
    probs_coherent = np.abs(F.conj() @ F.T) ** 2   # entry [k',k] = |<psi_k'|psi_k>|^2
    min_correct = min(probs_coherent[k, k].real for k in range(d))
    # decohered state of |psi_k>: diagonal rho = I/d (all position probabilities 1/d);
    # any measurement's success probability on it:
    rho = np.eye(d) / d
    max_after = max((F[k].conj() @ rho @ F[k]).real for k in range(d))
    print(f"{n:>3} {d:>3} {min_correct:>28.12f} {max_after:>30.12f} {1/d:>10.6f}")

print("""
-> from the COHERENT (phase-preserving) merge state, the split is recovered with
   probability 1 for every k at every n: the merge is reversible, the erased split
   is IN the phase. After decoherence the best recovery probability is exactly
   chance, 1/d: the split is gone, and the entropy created is ln d = ln(n+1) - the
   merge-erasure. The Section 12 identity is now an operational protocol, not only
   an entropy count.
""")
