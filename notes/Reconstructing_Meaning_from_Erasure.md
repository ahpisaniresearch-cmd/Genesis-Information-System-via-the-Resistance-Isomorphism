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

# Reconstructing Meaning from Erasure: The Toy-Language Test

## The semantics reconstructs exactly; the labels are gauge

**Alexander Pisani & Claude (Anthropic)** · June 2026 · companion note

**Framing.** Tests the crux of the epistemic-barrier picture: if we observe *only* erasures, can the genesis system's semantics be reconstructed? A hidden semantics is fixed (primitive meanings = primes; composite meanings = squarefree products), then only its erasures are exposed and the meaning-skeleton is reconstructed. Verified by `toy_language_reconstruction.py`. Claims graded Fact / Reading / Lead.

---

## 1. Setup

Hidden semantics: primitive meanings are primes `{2,3,5,7,11}` (resistances `ln p`); composite meanings are squarefree products (entities). Observable erasures only:
- **meet-erasure** `E(a,b)` — relate two meanings, keep the shared part (`gcd`), forget the symmetric difference; observable = resistance of what was forgotten.
- **reset-erasure** `norm(a)` — forget a meaning entirely; observable = its resistance.

## 2. Results

1. **Meet-erasure is squared distance in meaning-space.** With feature vectors `uₐ[p] = √(ln p)·𝟙[p|a]`, the resistance of the symmetric difference satisfies `E(a,b) = ‖uₐ − u_b‖²` exactly. The erasures *are* the meaning-geometry, as pairwise distances. *(Fact, verified.)*
2. **Shared meaning recovered to machine precision.** `Ω(gcd(a,b)) = (norm_a + norm_b − E(a,b))/2`, exact to `10⁻¹⁶`. The crux — can the overlap structure be read from the erasure trace? — is yes. *(Fact.)*
3. **Primitive count recovered exactly.** Classical MDS on the meet-erasures returns embedding dimension 5 (the true number of hidden primes); five positive eigenvalues `[8.49, 5.00, 2.77, 1.85, 0.31]`, then zero. *(Fact.)*
4. **Meaning-geometry recovered up to isometry = the gauge.** After the single best rotation, reconstructed meaning-vectors match the true ones to `10⁻¹⁵`. The geometry is exact; the choice of axes within it — which direction is which meaning — is undetermined, because rotating the configuration leaves every distance unchanged. The prime *labels* are not in the trace, in principle. *(Fact.)*

## 3. Reading

The **syntax/semantics filter** is confirmed in a working model. The *meaning* — geometry, overlap (`gcd`) lattice, primitive count — crosses the barrier intact and reconstructs exactly. The *syntax* — the assignment of meanings to specific primes — does not cross, because it is the rotational gauge that distances cannot see. Erasure is the channel through which meaning, not syntax, reaches us; the labels are **surrogate keys**, free. *(Reading, strongly grounded in the result.)*

## 4. The frontier (what the clean case hides)

- **Noise.** The weakest primitive came in at eigenvalue `0.31` against the strongest's `8.5`; under noise the rarest, lowest-resistance meanings wash out first — the faint corners of the language go before the bold ones.
- **Partial and unlabelled observation.** The test was given exact erasures, every pair, *and* the operation type of each event (meet vs reset). Real reconstruction faces noise, missing pairs, and undifferentiated events — sorting "relate" from "forget" is itself an inference layer.
- **Surrogate vs natural key (the sharp form of §5.2).** MDS returns the geometry up to rotation; the true prime axes are one special set inside it — the sparsest, most orthogonal (each meaning a single 0/1 indicator). Whether those axes can be singled out from the geometry — whether the configuration has a uniquely natural basis — is now a concrete **sparse-axis-recovery problem** on the MDS output, not a philosophical one. This test recovered the room; whether the room has preferred walls is the next question. *(Lead.)*

## 5. Grading and honesty boundary

- **Fact** — meet-erasure = squared distance; `Ω(gcd)` recovered to machine precision; primitive count = MDS dimension recovered exactly; meaning-geometry recovered to machine precision up to isometry.
- **Reading** — the syntax/semantics filter (meaning crosses, syntax does not); labels as surrogate keys.
- **Lead** — robustness under noise and partial/unlabelled observation; whether a natural key is recoverable as a sparse basis.

Classical content: the symmetric-difference metric on weighted sets, classical multidimensional scaling, and Procrustes alignment — all standard. The contribution is the identification of meet-erasure with meaning-space distance, the demonstration that the meaning-geometry reconstructs exactly from erasure while the labels remain gauge, and the reframing of the forced-embedding question as sparse-axis recovery. This is the clean, fully-observed case; no claim is made about noisy or partial reconstruction, and the genesis system's mechanism is not asserted.

---

*Originating direction (the epistemic-barrier reconstruction question; primes as surrogate vs natural keys; the toy-language test as the first concrete step) is Alexander Pisani's; the experiment, the syntax/semantics-filter reading, and this compilation were developed jointly with Claude (Anthropic). June 2026.*
