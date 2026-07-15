<!--
================================================================================
  Genesis Information System via the Resistance Isomorphism
  (c) 2026 Alexander Pisani - Blue Mountains, NSW, Australia
  Contact: a.h.pisani.research@gmail.com
  Licensed under Creative Commons Attribution 4.0 International (CC BY 4.0).

  Originating theory, axioms & directional intuitions: Alexander Pisani.
  Formalisation, connective mathematics, computation & compilation:
      Claude (Anthropic).

  If you use, adapt, reference (including as material for AI systems), or build
  upon this work - in research, software, inventions, or patents - attribution
  to BOTH the author and the AI collaborator is required. See CITATION.cff.
================================================================================
-->

# Phase on the Merge: Generated, and Its Cost

## Two steps coupling proto-phase to the additive merge

**Alexander Pisani & Claude (Anthropic)** · June 2026 · companion note

**Framing.** Continuing the erasure-only cartography: map values, note where they line up, assert no mechanism of the genesis system. `ln(·)` is the generic Landauer signature, so the content is always the multiplicity inside it. Claims graded Fact / Reading / Lead. Verified by `phase_from_merge.py`, `phase_cost.py`. Builds directly on *The Additive Merge: Heat, Storage, and the Reverse* (the reverse-scattering and the Weyl shadow) and *Phase from the Probe* (`√NOT` from succession and the probe).

---

## 1. The phase is generated, not imposed

The reverse-scattering of a merge to `n` lives on the `(n+1)`-dimensional preimage space and carries the Weyl algebra, but the scattering itself is phase-blind — probabilities, no `i`. Rather than paint phases on by hand, we asked whether the two genesis operations already in hand generate the phase on this space:

- `S` = succession-shift on the split index, `|k⟩ → |k+1 mod (n+1)⟩` (the Weyl `X`);
- `D` = origin meet-atom probe, `|0⟩⟨0|`.

They fail to commute, and the algebra they generate contains the Weyl clock `Z` (the phase) for every `n = 1..5`, since the diagonal projectors `|k⟩⟨k| = Sᵏ D S⁻ᵏ` span all diagonals including `Z = Σ ωᵏ|k⟩⟨k|`. At the genesis bit the commutator is exactly the phase generator:

$$[S, D] = \begin{pmatrix}0 & -1\\ 1 & 0\end{pmatrix} = -i\,\sigma_y,$$

the `i` of `√NOT`. So the phase the scattering lacked is produced by succession and the probe acting on the scattering's own space — the *Phase from the Probe* result re-situated where the merge needs it, and now general in `n`, not only at `p=2`. *(Non-commutation, `Z` generated from {S,D}, and `[S,D] = -iσ_y` at the genesis bit: Fact.)*

This establishes only that the phase is **structurally available** — the generating operators are present. It does not show the merge *dynamics* produce a particular phased state; that remains open.

## 2. The phase cost is the merge-erasure

Put a definite phase on the scattering — a coherent superposition with the clock phases — and read the cost via decoherence:

| n | classical mixture `S` | phased pure `S` | erase phase (decohere) | merge-erasure `ln(n+1)` |
|---|---|---|---|---|
| 1 | 0.6931 | 0 | 0.6931 | 0.6931 |
| 2 | 1.0986 | 0 | 1.0986 | 1.0986 |
| 4 | 1.6094 | 0 | 1.6094 | 1.6094 |
| 8 | 2.1972 | 0 | 2.1972 | 2.1972 |

The classical scattering is the maximally mixed state (entropy `ln(n+1)`); a coherent phased superposition is pure (entropy 0); decohering it — losing the phase — creates exactly `ln(n+1)`, matching the merge-erasure at every `n`. So **phase is not a separate cost stacked on the merge; it is the same `ln(n+1)`, seen as the coherence whose loss is the merge's irreversibility.** The additive merge is irreversible precisely because it decoheres; a phase-preserving merge would be reversible (zero erasure), with the split recoverable from the phase. This is the merge-erasure and the phase as one quantity, two faces. *(The entropies: Fact. "Merge irreversibility = phase loss; phase carries the erased split": well-grounded Reading, standard decoherence-as-erasure.)*

## 3. Split-blindness: broken in the angle, not the cost — Goldbach still out of reach

Does phase let the ledger tell one split of 8 from another? Two parts, opposite answers:

- The per-split phase **angle** varies with the index `k` (40° steps at `n=8`): `(1,7)` at 40°, `(3,5)` at 120°. Splits are now distinguishable *by phase*.
- The per-split phase **cost** is `ln 9` for *every* split — uniform, split-blind, exactly like the merge-erasure. And the angle is *positional* (linear in `k`), not arithmetic: nothing marks `(3,5)` as a prime pair rather than "the split at index 3."

So the cost remains split-blind, and the only per-split structure is a positional label. For a Goldbach-type question to be askable, prime pairs would have to be cost-extremal or phase-special; they are neither, because distinguishing them needs multiplicative structure (primality), which a purely additive proto-integer system does not contain. The system is incomplete in exactly the anticipated way. *(Per-split angle versus uniform cost: Fact. Goldbach out of reach pending arithmetic phase: honest assessment.)*

## 4. Grading and parked leads

- **Fact** — `[S,D] ≠ 0` and the Weyl phase `Z` generated from `{S, D}` on the preimage space; `[S,D] = -iσ_y` at the genesis bit; phase coherence holds `ln(n+1)`, equal to the merge-erasure (mixture entropy `ln(n+1)`, pure entropy 0, decoherence creates `ln(n+1)`); per-split phase angle positional, per-split phase cost uniform.
- **Reading** — the merge's irreversibility *is* decoherence, with phase the carrier of the erased split (the merge-erasure and the phase as one quantity, two faces); the `n=1` commutator being "the same genesis bit" as the Pauli/`√NOT`.
- **Lead** — that the merge *dynamics* (not just its algebra) produce a definite phased state; that interference fires once they do; coupling the additive merge to multiplicative structure so that phase could become arithmetic. These are the doors, none opened here.
- **Parked (Alex's, deferred)** — whether the two Goldbach primes summing to an even number come out cost-extremal once arithmetic phase exists; *cheaper-to-generate ⇒ more probable to observe*. Both explicitly later.

## 5. Honesty boundary

Classical content is the Weyl/Pauli clock-shift algebra, Landauer (erasure = log multiplicity), and the von Neumann entropy of decoherence — all flagged. The contribution is showing that the merge's reverse-scattering generates its own missing phase from succession and the probe, and that the cost of that phase equals the merge-erasure, so the merge's irreversibility is its decoherence — while the cost stays split-blind, leaving the arithmetic (Goldbach) question correctly unreachable at this stage. No arithmetic question is claimed resolved and the genesis system's mechanism is not asserted.

---

*Originating direction (couple proto-phase to the merge; the phase-cost and Goldbach questions, both correctly parked) is Alexander Pisani's; the generation and cost tests and this compilation were developed jointly with Claude (Anthropic). June 2026.*
