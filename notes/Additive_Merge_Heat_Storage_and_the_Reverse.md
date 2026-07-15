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

# The Additive Merge: Heat, Storage, and the Reverse

## Stage 1 continued — the system's first irreversible operation on proto-integers

**Alexander Pisani & Claude (Anthropic)** · June 2026 · companion note

**Framing.** Under this programme we treat *erasure* as the only trace of the genesis information system that reaches our universe, so the work is cartography: map erasure values, and note where they coincide with known structure, without asserting the genesis system's mechanism and without taking its physical or numerical interpretation as load-bearing. We are looking for a correspondence richer than the resistance isomorphism. Because erasure is always *the log of a multiplicity* (Landauer), `ln(·)` appears everywhere; the discriminating content is never the log but the **multiplicity inside it**. Claims are graded Fact / Reading / Lead. Verified by `stage1_additive_merge.py`, `stage1_build_paths.py`, `reverse_merge_weyl.py`.

**Reading order.** Spine, then *Erasure at the Genesis Layer*, then *The Succession-Channel and the Two-Legged Ledger*, then this note.

---

## 1. The merge, and its erasure law

Proto-integers are unary tallies (length only, no multiplicity). The system's first **irreversible** operation merges two tallies of lengths `a` and `b` into one of length `n = a + b`, forgetting the split. The forward map is many-to-one, so it carries a Landauer cost.

A merge whose output has length `m` forgets which ordered split `(a,b)` with `a+b=m` produced it; with `a,b ≥ 0` there are `m+1` such splits, uniform under maximum ignorance, so

$$\varepsilon(m) = H(\text{uniform over } m{+}1 \text{ splits}) = \ln(m+1).$$

The processing erasure grows logarithmically with the proto-integer built. *(The split-count and its log: Fact. Reading it as the processing-erasure law: Reading.)*

**Hygiene on the correspondence.** `ε(m) = ln(m+1)` equals the resistance *value* of the real-world inverse integer `1/(m+1)` — but these are two different things sharing one number. The merged multiplicity is `m+1`, not `m`; the off-by-one is the marker that the proto-layer quantity is the *split count*, not the proto-integer wearing a resistance hat. Same `ln` hinge, different object.

**Temperature-independence and the gas test.** Under both a bounded-uniform and a geometric input prior, the splits given a fixed sum come out uniform (the prior weights cancel in the conditional), so `ε(m) = ln(m+1)` depends only on the output size, never on the prior. The realisation factor `R = m+1 = e^{ε(m)}` reproduces the gas test's `R = Q+1` (Circuits §4.5) on bare tallies rather than prime-encoded registers — the check flagged in advance, and it lands. *(Both: Fact.)*

**The two-legged ledger.** Over one merge-read-reset cycle the system's merge-erasure plus the demon's read-reset on the output sum to the whole input information:

$$\underbrace{H(\text{split}\mid\text{sum})}_{\text{system, merge}} \;+\; \underbrace{H(\text{sum})}_{\text{demon, reset}} \;=\; H(a,b) = H(a)+H(b),$$

confirmed exactly (`4.3944` for uniform `{0..8}`, `5.0040` for geometric mean 4). This is the chain rule `H(a,b)=H(n)+H(\text{split}\mid n)` realised as the ledger — the same two-legged shape the stream had, now for the system's own irreversible step. *(Chain rule: Fact. The reading: Reading.)*

## 2. Storage: build paths, and a path function

Storing a merged tally and reusing it makes addition repeatable. A stored intermediate is a *bare* proto-integer — it remembers its length, not its composition — so the next merge re-forgets a split. A build through merge-outputs `m₁,…,m_k` costs

$$E = \sum_i \ln(m_i+1) = \ln\prod_i (m_i+1).$$

Building the same `N` different ways gives very different totals (`N=8`: from `2.20` for one merge to `12.11` for eight ones in a line), so **build-erasure is a path function, not a state function** — heat, not energy. *(The sums: Fact. Path-function reading: well-grounded Reading.)*

Three trends, all reading off the product form:

- **Floor = single merge = `ln(N+1)`.** One 2-way merge is the cheapest route to `N`; every finer build costs strictly more. So `build-erasure = ln(N+1)` (state-function floor) `+` path-excess. That excess *is* the thermodynamic price of storing-and-reusing intermediates. *(Fact.)*
- **More merges, and bigger intermediates, cost more.** Each piece beyond the first multiplies in a factor `(m_i+1)>1`, and the cost is the product of the partial sums (plus one). *(Fact.)*
- **Smallest-first / balanced is the minimiser.** Combining the smallest pieces first keeps every intermediate smallest — the product-minimising (Huffman) shape. Balanced beats linear at every size (`N=8`, eight ones: `9.81` vs `12.11`). *(Ordering: Fact. Huffman link: Reading.)*

**Repeated-same is not special.** At three pieces building `6`, the all-equal `2+2+2` (`3.56`) costs *more* than mixed `1+2+3` small-first (`3.33`) and `1+1+4` small-first (`3.04`). What sets the cost is the profile of partial sums, not whether the pieces are equal. *(Fact.)*

## 3. The reverse, and the Weyl/√NOT shadow

Forward, `(a,b) → n` forgets the split. **Force-reversing is one-to-many**: `n` maps back to all `n+1` ordered splits, and with no energy supplied the system spreads uniformly over them — a scattering whose entropy is exactly `ln(n+1)`, the erased amount. So the reverse-scattering *is* the erased information made manifest as a distribution over configurations; collapsing it to the original split requires injecting that `ln(n+1)` back. *(Scattering entropy = erased: Fact.)*

**The configuration space carries the Weyl algebra.** The `(n+1)`-dimensional preimage space, equipped with the clock-shift operators `X` (shift the split) and `Z` (phase the split, `ω = e^{2πi/(n+1)}`), satisfies `ZX = ω XZ` — verified for `n = 1..5`. At `n = 1` — the genesis bit, two preimages, `ln 2` erased — it is exactly the Pauli algebra (`X = σ_x = NOT`, `Z = σ_z`), and `√NOT` exists with its characteristic `i` (`√NOT² = NOT`). So three things line up at `2`: the genesis bit, the merge-to-length-1's two preimages, and the Pauli/`√NOT` that *Phase from the Probe* found independently. *(The Weyl relation and the `n=1`→Pauli/`√NOT` identification: Fact. That these are "the same 2": noted lining-up, Reading.)*

**But the scattering is not the √NOT/Weyl structure — it is its phase-blind shadow.** `|+⟩` and `|−⟩` carry *identical* classical probabilities yet are orthogonal, and superposing them cancels an outcome to zero amplitude — interference no mixture of probabilities can produce. The scattering supplies the probabilities (`|amplitude|²`); `√NOT` carries the *phase* (the `i`), which the scattering lacks. The lining-up is real and precise — erased multiplicity `n+1` = Weyl dimension; genesis bit = Pauli/`√NOT` — but **phase is the one missing ingredient**, and phase is what enables interference. *(Phase as the missing ingredient: Fact.)*

This is also where the order-dependence of §2 points. The build cost is non-associative (grouping matters) even though the sum is associative — a real path-structure, and the kind of order-sensitivity that, laid over amplitudes, *becomes* interference. Whether the genesis dynamics supplies the phases (the Phase note derives them from succession and the probe failing to commute) is the open lead; coupling proto-phase into the merge is what would promote the scattering to the full Weyl structure and turn the order-dependence into genuine cancellation.

## 4. Grading and parked leads

- **Fact** — `ε(m) = ln(m+1)` and its temperature-independence; `R = m+1` reproducing the gas test on tallies; the two-legged chain-rule total; build-erasure as a path function with floor `ln(N+1)` and smallest-first minimiser; the reverse-scattering entropy equalling the erased `ln(n+1)`; the Weyl relation on the preimage space and the `n=1`→Pauli/`√NOT` identification; phase as a genuine addition enabling interference. (⚠ Landauer, Shannon, Weyl/Pauli carried throughout.)
- **Reading** — the erasure-as-processing-law reading; the Huffman link; the genesis bit / merge-to-1 / Pauli being "the same `2`."
- **Lead** — the genesis dynamics *supplying* the phase that would make the scattering the true Weyl/`√NOT` structure and the order-dependence true interference; this is the natural next experiment (couple proto-phase to the merge).
- **Parked (Alex's, deferred)** — *cheaper-to-generate ⇒ more probable to observe*; not explored here.

## 5. Honesty boundary

Classical content is Landauer (erasure = log multiplicity), Shannon (entropy, chain rule, mutual information), the Weyl/Pauli clock-shift algebra, and Huffman/optimal-merge order — all flagged where used. The contribution is the quantity-free additive-merge ledger on proto-integers, its two-legged and storage thermodynamics, and the demonstration that the reverse-merge's configuration space is the phase-blind shadow of the Weyl/`√NOT` structure with the genesis bit landing exactly on the Pauli case. No open arithmetic question is claimed resolved, and the genesis system's mechanism is not asserted — only erasure values, and where they line up.

---

*Originating direction (erasure-only cartography, the reverse-as-scattering intuition, the Paper 6 superposition framing, the parked observation-probability lead) is Alexander Pisani's; the merge ledger, the build-path and storage results, the reverse/Weyl test, and this compilation were developed jointly with Claude (Anthropic). June 2026.*
