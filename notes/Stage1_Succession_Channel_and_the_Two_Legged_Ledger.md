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

# The Succession-Channel and the Two-Legged Ledger

## Stage 1 of the Quantity-Free Programme: the erasure ledger of a clock, and the bitstream it emits

**Alexander Pisani & Claude (Anthropic)** · June 2026 · companion note · Stage 1 findings

**Status.** Records the first experimental stage under *Erasure at the Genesis Layer*. The erasure accounting here is solid and quantity-free: it depends only on the size of a superposition and on a destructive binary probe, never on any factorization, so it is **Fact** where marked. One earlier claim — "primality as an output" — is **corrected** to a relabel and graded down; the correction is recorded in §3. The connections to the central hypothesis (resistance is erasure-dominated; the genesis bit is the lossless anchor) are **Readings** with quantitative shape. Verified by `stage1_erasure_channels.py` and `stage1_stream.py`. Resumable cold by an instance holding the direction note.

**Reading order.** *The Genesis Information Project* (spine), then *Erasure as the Carrier of Mathematics* and *Erasure at the Genesis Layer* (the direction this stage executes), then this note.

---

## 1. The model (quantity-free)

The only finite structure succession can build alone is a **cycle**: NOT-propagated-through-nesting, run until it returns to its origin after some number of steps `g`, the channel's **girth**. The girth is a structural return-time, not a number we impose — it is the stride-skeleton, the strides-analogue of the unary dot-count that precedes a symbol in Paper 6 (*The Geometry of Knowing* / the hypergrid). What we *keep* is not the integer `g` but the resistance `ln g` and the erasure-decomposition that rides on it: the **inverse-integer resistance constructed from erasure**.

- **Superposition** = the maximum-entropy belief state over the channel's `g` internal states (Axiom 3, state form): uniform, entropy `ln g`.
- **The probe** is the destructive meet-atom: the binary test "is the state the origin?" On a single channel this *is* the divisibility atom. Being destructive (Probe §5), it records the partition and erases the rest.

We do **not** claim the genesis substrate houses the integers. The integer girth is scaffolding; primality, where it appears, is read off the scaffolding, not derived (§3).

## 2. One channel: the chain rule, and one budget with two faces

The resistance of a channel splits, with no slack, by the **chain rule of entropy** on the meet-atom:

$$\ln g = \underbrace{H(1/g)}_{\text{kept / recorded}} + \underbrace{(1-\tfrac1g)\ln(g-1)}_{\text{erased / coarsened}}.$$

The uniform residue carries `ln g`; the binary partition keeps `H(1/g)`; the "origin" class is a singleton (hides nothing); the "non-origin" class hides `g−1` equiprobable strides, entropy `ln(g−1)`, weighted `(1−1/g)` — the *which-stride* information the destructive probe coarsens away. *(Fact — chain rule.)*

**The refinement is resolved: one budget, two faces, not two addends.** `ln g` is the single conserved quantity (the channel's state-information). Any process partitions it into recorded + dumped-to-heat + retained-reversibly:

| process | recorded | dumped | retained | total |
|---|---|---|---|---|
| reversible succession (tick) | 0 | 0 | ln g | ln g |
| destructive meet-atom read | H(1/g) | (1−1/g)ln(g−1) | 0 | ln g |
| overwrite (reset the clock) | 0 | ln g | 0 | ln g |

So "processing erasure" and "probe erasure" are not two independent `ln g` costs; they are different fates of the *same* `ln g`. *(Conservation: Fact. The resolution of the processing/probe relation: well-grounded Reading.)*

**The genesis bit is the unique lossless channel.** At `g = 2` the erased term is `(1−½)ln 1 = 0`: pure recorded signal, zero coarsening — the same maximality *Phase from the Probe* found from the algebra side. The extraction efficiency `H(1/g)/ln g` falls from `1` at `g = 2` (1.00, 0.58, 0.41, 0.31, …), and the erased fraction `→ 1`: under the genesis probe, a larger channel's resistance is increasingly *erased*, not recorded. This is the first quantitative texture under the central hypothesis — resistance is erasure-dominated, anchored at the genesis bit. *(Fractions: Fact. The erasure-domination reading: Reading.)* The "erased" leg is genuine heat only because the probe is destructive; a non-destructive probe would retain the residue (hidden), not erase it.

## 3. Primality came out — but as a relabel, not a derivation (correction)

The structural test "does the cycle have a proper sub-period?", run by stepping succession at every stride and watching for an early return, returns exactly the primes (`2, 3, 5, 7, 11, 13, …`) with no arithmetic factoring. It is faithful. But it is **circular as a derivation**: indexing channels by ℤ/g puts the integer's divisor structure in at the door — "no proper sub-cycle" *is* "no proper divisor." The uniqueness was moved across to a unique channel, not produced. *(Corrected: relabel, not output. Graded down from the earlier "primality as output" claim.)*

What is **not** circular is the erasure accounting of §2 and §4: it holds for any `g`, prime or composite, and presupposes no factorization. So the discipline going forward: accept the stride-skeleton, study the erasure. Deriving the integers from erasure — making elements *earn* their existence through the ledger (the generative inversion sketched in the direction note) — remains the open, harder target, not something Stage 1 achieved.

## 4. The stream: both erasure interfaces, and the composition law

Let a bank of clocks `{g₁,…,g_N}` tick off one shared succession; the probe reads one bit per clock, `bitᵢ(t) = [gᵢ | t]`, and the readout `B(t)` is the bitstring the system emits from its current state. Over a period `L = lcm`, the demon reads repeatedly — and reading repeatedly forces a **record reset** between readouts.

**Both erasure interfaces now appear, as the two legs of the chain rule.** Per read-reset cycle:

$$\underbrace{(\ln L - H(B))}_{\text{coarsening — observation}} + \underbrace{H(B)}_{\text{reset — Maxwell's-demon}} = \ln L.$$

The coarsening leg is the destructive measurement discarding what it cannot resolve; the reset leg is the recorded bitstring cleared so the demon can read again. The *kept* leg of the snapshot is thereby revealed as **deferred erasure**: free-looking when recorded, paid back as heat at the reset. Over a full operating cycle the demon dumps the whole `ln L`. The snapshot saw only the coarsening leg; the stream forces both. *(Total = ln L: Fact. The two legs = the direction note's two interfaces: Reading.)* (Assumes the demon records the full bitstring it reads; a coarser record clears for less.)

**The composition law — Innovation is Connected Correlation, in the ledger.** The recorded information `H(B)` (= the reset cost) is the sum of the per-channel marginals minus the redundancy:

| bank | L | ln L | Σ Hᵢ | H(B) | redundancy | coarsen | reset | independent? |
|---|---|---|---|---|---|---|---|---|
| (2,3) | 6 | 1.792 | 1.330 | 1.330 | 0.000 | 0.462 | 1.330 | yes |
| (2,4) | 4 | 1.386 | 1.255 | 1.040 | 0.216 | 0.347 | 1.040 | no |
| (2,3,5) | 30 | 3.401 | 1.830 | 1.830 | 0.000 | 1.571 | 1.830 | yes |
| (2,4,8) | 8 | 2.079 | 1.632 | 1.213 | 0.419 | 0.866 | 1.213 | no |
| (2,3,4) | 12 | 2.485 | 1.892 | 1.676 | 0.216 | 0.809 | 1.676 | no |
| (3,5,7) | 105 | 4.654 | 1.547 | 1.547 | 0.000 | 3.107 | 1.547 | yes |

For coprime banks the redundancy is exactly zero — `H(B) = Σ Hᵢ`, the channels record independent information, the reset cost is fully additive. For banks sharing structure the redundancy is positive — correlated bits, so the demon records *less* and its reset is *cheaper*, the saving equal to the connected correlation. Sharing structure buys a discount on the Maxwell's-demon bill at the cost of carrying less information. *(Additivity iff coprime, redundancy = connected correlation: Fact, from CRT + entropy. The discount reading: Reading.)*

**The genesis bit is the cheapest source.** Any bank containing `2` gets `H(1/2) = 0.693` of recorded signal and *zero* coarsening from that channel. Drop it for larger primes and the cost inverts: `(3,5,7)` records *less* than `(2,3,5)` (1.547 vs 1.830) yet costs far *more* (4.654 vs 3.401), almost all coarsening. Information is cheapest to generate at the genesis bit — which is why a single bit *should* be the easiest thing the system emits. *(Fact on the numbers; the "cheapest source" reading connects to a parked lead, §6.)*

## 5. Honest boundary

The *system* here is still reversible — the clocks only tick. The processing erasure added in §4 is the **demon's record reset** (the Maxwell's-demon form), not the system's own dynamics. Making the underlying system irreversible — clocks that *merge*, adder-style, so the system pays alongside the demon — is the next distinct thing to build, and is not yet tested.

## 6. Grading and parked leads

- **Fact** — the chain rule and its `g=2` vanishing; the one-budget conservation; reversible-tick `= 0`, overwrite `= ln g`; the stream's per-cycle total `= ln L` split into coarsening + reset; `H(B)` additive iff coprime, redundancy = connected correlation. (⚠ Landauer/Bennett, Shannon, CRT carried throughout.)
- **Reading** — resistance is erasure-dominated with the genesis bit as lossless anchor; the two stream legs are the direction note's two interfaces; the Maxwell's-demon discount for shared structure; the genesis bit as cheapest source.
- **Corrected** — "primality as output" → a faithful *relabel*, not a derivation (§3); the integers enter through the channel family ℤ/g.
- **Parked leads** — (i) *cheaper-to-generate ⇒ more probable to observe* (Alex's, deferred): the observation that a single bit is the cheapest emission may connect erasure cost to observation probability; not yet explored. (ii) the system-irreversibility knob (§5), the immediate next target. (iii) the demon that *accumulates* across reads — synchronising to the phase over time rather than resetting each tick — an alternative stream mode left unbuilt.

## 7. Honesty boundary

The classical content is Landauer/Bennett (erasure cost, the demon's reset), Shannon (entropy, the chain rule, mutual information / connected correlation), Jaynes (maximum entropy over the superposition), and the Chinese Remainder Theorem (independence of coprime clocks) — all flagged where used. The contribution is the quantity-free channel model, the one-budget resolution of the processing/probe refinement, the honest correction of the primality claim, and the two-legged stream ledger with its composition law. No open arithmetic question is claimed resolved. Stage 1: foundational, graded throughout.

---

*Originating direction (quantity-free framing, erasure-as-source, the stride/unary connection, the parked observation-probability lead) is Alexander Pisani's; the model, the erasure accounting, the primality correction, the stream design, and this compilation were developed jointly with Claude (Anthropic). June 2026.*
