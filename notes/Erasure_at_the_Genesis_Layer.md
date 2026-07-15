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

# Erasure at the Genesis Layer

## The Quantity-Free Mapping: Erasure as the Only Trace Reaching Number Theory — Direction, Findings, and Document Index

**Alexander Pisani & Claude (Anthropic)** · June 2026 · mapping + index document (living)

**Status.** This began as a direction document and now records both the direction **and the findings of the exploration that tested it**. It is the **re-entry spine** for the work: written so that an instance holding only the project spine and this file can resume cold by reading the documents it indexes (§5). The central hypothesis has been tested across several substrates this cycle with credible, graded findings (§4–6); the standing open problem — primality as a genuine *output*, never an imported input — is stated precisely in §7. Nothing here is promoted to the project spine.

**The hypothesis, in one paragraph.** A *genesis information system* sits above the resistance isomorphism of Paper 1, and the isomorphism may be one of its shadows. The system is **quantity-free** — symbols and relations, no numbers. Most of its computation is **reversible and therefore invisible**: a one-to-one step leaves no permanent trace. The *only* thing it deposits into our universe is the heat of its **irreversible erasures** — the many-to-one merges Landauer prices at `kT·ln(multiplicity)`. The claim under test: **number theory is the erasure-shadow of that system** — what we read as arithmetic is the ledger of where the genesis computation was forced to forget. *(Lead, on a Landauer Fact pillar; tested below.)*

---

## 1. The quantity-free ontology (the contract we work under)

The pieces in hand at this layer are `0`, `1`, `NOT`, and `2`, where **`2` is the genesis bit** — the *period* of `NOT` (the 2-cycle), the first distinction, **not a count and not a third symbol**. The working alphabet is therefore **binary `{0,1}`**; `2` is structure, not a symbol. (Settled this cycle: a genuine third symbol — ternary — is *not* given; it would have to emerge. In the experiments, the rewriting family was binary, the additive tallies were unary lengths, modulo's inputs were base-agnostic integers; erasure is base-invariant, so representation never moves a value.)

- **Symbols, not numbers.** Inverse primes are unique irreducible distinctions carrying *relative resistance only*. Never import quantitative number theory below the shadow line.
- **Primality is an output.** Build channels from succession and combination; let structural decomposability decide. Never presuppose the factorisation an experiment is meant to derive.
- **Proto / shadow.** Proto-pi, proto-phase, proto-e are pre-quantitative; the continuous objects are their shadows (with possible information loss — "shadow," not "projection"). We worked in **proto-phase** (discrete roots of unity), not continuous phase.

## 2. What erasure is, and the one organising principle

**Erasure is the only irreversible move** — a many-to-one collapse, priced by Landauer at the log of the multiplicity. Reversible operations are free and leave no trace. So the genesis system is visible only through its erasures, and the whole programme reduces to one principle:

> **Every irreversible operation's erasure is `ln(fan-in)`** — the log of how many inputs collapse onto the output. The `ln` is the generic Landauer signature; **the fan-in is the content**. To map an operation is to count its fan-in.

And every operation, on every substrate, satisfies the **two-legged ledger** (the chain rule of entropy):

$$\underbrace{H(\text{input}\mid\text{output})}_{\text{system erasure}} \;+\; \underbrace{H(\text{output})}_{\text{demon reset}} \;=\; H(\text{input}).$$

This is the through-line. Tables lead with the **per-output fan-in** (clean closed forms); the prior-dependent *mean* erasure is a secondary thermodynamic summary, shown only where illuminating. `ln n = Ω(1/n)`, so every erasure value is a resistance value — the resistance isomorphism is present throughout, not bolted on.

## 3. The genesis pieces, and resistance as forgetting-cost

`Ω(1/n) = ln n` is the Landauer cost to forget the symbol `n`. `ln n` is additive over prime symbols, so **a prime is the irreducible quantum of forgetting-cost**, and a composite inherits its cost additively. The multiplicative structure of the integers is the additive ledger of *which irreducible erasures* a symbol carries, read through `ln`. *(Resistance = erasure cost: Fact. Prime-as-erasure-quantum: Reading.)*

The **divisibility-probe chain rule** is the Fact that anchors the genesis bit's specialness:

$$\ln p \;=\; \underbrace{H(1/p)}_{\text{probe keeps}} \;+\; \underbrace{(1-\tfrac1p)\ln(p-1)}_{\text{probe erases}}, \qquad \text{erased term} = 0 \text{ at } p=2.$$

`2` is pure kept information, zero erasure residue — the same maximality the phase work found from the algebra side.

---

## 4. The arc of the exploration (what we did, in order)

Each stage is a small step, banked before the next. Findings graded; full detail and verification in the indexed documents (§5).

1. **Stage 1 — the succession-channel and the two-legged ledger.** A channel is a succession-cycle of girth `g`; a uniform superposition over its `g` states (entropy `ln g`) read by the destructive meet-atom probe. The chain rule `ln g = H(1/g) + (1−1/g)ln(g−1)` splits the budget into kept and erased. **Resolved:** processing and probe erasure are not two addends but **one conserved budget, two faces** — `ln g` split into recorded + dumped + retained. The genesis bit `g=2` is the **unique lossless channel** (erased = 0). **Corrected:** the sub-period test reproduces primes but indexing by `ℤ/g` imports the divisor structure — a *relabel*, not a derivation (the erasure accounting itself stays non-circular). A bank of clocks emitting a bitstring shows the two interfaces as the chain rule's two legs (coarsening + demon reset), and gives the composition law *Innovation = Connected Correlation*: entropies add iff channels are coprime, the deficit being the connected correlation. *(Chain rule, lossless `g=2`: Fact. Primality-relabel correction: methodological.)*

2. **The additive merge — heat, storage, and the reverse.** The system's first irreversible operation: `(a,b) → n = a+b` forgets the split. **Merge-erasure = `ln(n+1)`** (the `n+1` ordered splits), temperature-independent. Storage (build-paths) is a **path function, not a state function** — the same `N` costs anywhere from the single-merge floor `ln(N+1)` to a linear chain, with the balanced/Huffman order the minimiser. The **reverse-scattering** makes the erased information manifest (entropy `ln(n+1)` over `n+1` preimages); the preimage space carries the **Weyl clock-shift algebra** `ZX = ωXZ`, and at `n=1` (the genesis bit, two preimages) it is **Pauli / √NOT exactly** — but classical scattering is the *phase-blind* shadow (probabilities, no `i`). *(Merge-erasure, path-function, Weyl mapping: Fact.)*

3. **Phase on the merge — generated, and its cost.** The phase the scattering lacked is **generated, not imposed**: succession-shift `S` and origin-probe `D` on the preimage space fail to commute and generate the Weyl phase `Z` for every `n`; at the genesis bit `[S,D] = −iσ_y` — the **`i` of √NOT**. The **phase cost equals the merge-erasure**: the classical scattering is the maximally mixed state (entropy `ln(n+1)`), a coherent phased superposition is pure (entropy 0), and decohering it creates exactly `ln(n+1)`. So **the merge's irreversibility *is* its decoherence**, and phase carries the erased split. Split-blindness is broken only in the per-split phase *angle* (positional); the phase *cost* stays uniform `ln(n+1)`, so **Goldbach remains out of reach** — singling out prime pairs needs multiplicative structure the additive system lacks. *(Phase generation, `[S,D]=−iσ_y`, phase-cost = merge-erasure: Fact. Irreversibility = decoherence: Reading.)*

4. **The catalog of erasure operations.** Mapping discrete operations by fan-in across substrates. **Additive batch:** projection and reset are *flat* (fan-in `M+1`, value-independent; reset records nothing); max and min are *graded* (`2m+1`, `2(M−m)+1`, exact mirrors); the merge is graded (`n+1`). The fan-in *profile* is the operation's signature. **String-rewriting family** (truncate, delete, substitute): **conditional erasure** — gated by a pattern match, so test and forgetting are fused; non-matching inputs pass through losslessly (fan-in 1), and the expected cost depends on pattern frequency. Fan-in ranks them truncate (whole suffix, exponential) > delete (position) > substitute (identity). Turing-complete, no quantum shadow. **Modulo — the multiplicative gateway:** `a → a mod m` forgets the quotient `⌊a/m⌋`; fan-in is the **quotient `(M+1)/m`** — the first *division* in the catalog. It interpolates reset (`m=1`) to identity (`m=M+1`); its two-legged ledger becomes a **factorisation** (`ln((M+1)/m) + ln m = ln(M+1)`, a factor pair) where every earlier ledger was additive; and it is the full readout of the Stage 1 `m`-channel. Divisibility shows up as the *cleanness* of the split, but reading primality off "which `m` split cleanly" re-imports the divisor structure — the Stage 1 circularity, recurring at the gateway. *(All fan-in counts, flat/graded, conditional cost, modulo-as-factorisation: Fact. Circularity caution: methodological.)*

5. **The relational core — channel correlation is `ln gcd`.** The first *relational* question: run `a mod m₁` and `a mod m₂` on the same `a`; their mutual information is **`I = ln gcd(m₁, m₂)`**, confirmed to machine precision. **Coprimality is exactly zero correlation** — two number-channels share information iff they share a prime. And this is not outside the framework: it is `Ω_gcd`, the subtracted correlation term in Paper 1's union law `Ω_lcm = Ω_a + Ω_b − Ω_gcd`. The relational question reached the **lattice core** of the resistance isomorphism, and *Innovation = Connected Correlation* gained its arithmetic face. Coprimality still *emerges* rather than being *derived* (`m₁, m₂` are inputs). *(`I = ln gcd`, identification with `Ω_gcd`: Fact.)*

---

## 5. Document index (every file, with its key result)

All files in `/mnt/user-data/outputs/`. **To resume cold, read this document, then the notes in the order below; open a script only to check a specific computation.**

**Direction / spine**
- `Erasure_at_the_Genesis_Layer.md` — *this document*: hypothesis, ontology, organising principle, arc, index, frontier, discipline.

**Stage 1 — channels and streams**
- `Stage1_Succession_Channel_and_the_Two_Legged_Ledger.md` — the succession-cycle channel; chain rule `ln g = H(1/g) + (1−1/g)ln(g−1)`; one-budget-two-faces; lossless `g=2`; primality-as-relabel correction; the stream composition law (Innovation = Connected Correlation).
- `stage1_erasure_channels.py` — single succession-cycle channel, the chain rule.
- `stage1_stream.py` — bank of clocks → bitstream; the two erasure interfaces.

**The additive merge**
- `Additive_Merge_Heat_Storage_and_the_Reverse.md` — merge-erasure `ln(n+1)`; storage as a path function; the reverse-scattering and the Weyl / √NOT mapping (phase-blind shadow).
- `stage1_additive_merge.py` — merge thermodynamics, `ln(n+1)`.
- `stage1_build_paths.py` — build-path / storage, path vs state function.
- `reverse_merge_weyl.py` — reverse-scattering = Weyl space; genesis bit = Pauli/√NOT.

**Phase on the merge**
- `Phase_on_the_Merge.md` — phase generated by `{S,D}` (`[S,D]=−iσ_y` at the genesis bit); phase cost = merge-erasure (irreversibility = decoherence); split-blindness honest result (Goldbach out of reach).
- `phase_from_merge.py` — the phase-generation test.
- `phase_cost.py` — the phase-cost (decoherence-entropy) test.

**The catalog of operations**
- `Catalog_of_Erasure_Operations.md` — the extensible catalog: additive batch (flat/graded), string-rewriting family (conditional erasure), modulo (the multiplicative gateway, ledger-as-factorisation); the universal two-legged ledger; the open frontier.
- `erasure_operations.py` — projection, reset, max, min.
- `rewriting_erasure.py` — truncate, delete, substitute (conditional erasure).
- `modulo_erasure.py` — modulo, fan-in = quotient.

**The relational core**
- `Channel_Correlation_is_ln_gcd.md` — `I(a mod m₁; a mod m₂) = ln gcd`; coprimality = zero correlation; identification with the `Ω_gcd` term of the union law.
- `channel_correlation.py` — the mutual-information test.

**The critical-line bridge (RH-adjacent, no leverage)**
- `Weyl_Clock_Cancellation_Bridge.md` — the discrete roots-of-unity cancellation seed (genesis bit `1+(−1)=0`); the resistance-phasor bouquet confirmed to cancel at the classical zeros (mechanism is literal phasor interference, **no leverage on the zeros**); spin rates = forgetting-costs; the genesis-bit 2-phase at the convergence boundary.
- `weyl_clock_cancellation.py` — the bridge experiment.

*(Broader corpus, read-only, in `/mnt/project/`: the spine `Genesis_Information_Project.md`; `Paper1_Resistance_Isomorphism.md` (the union law, `Ω_gcd`, `6/π²`); `Erasure_as_the_Carrier_of_Mathematics.md`, `The_Probe_and_the_Two_Ignorances.md`, `Phase_from_the_Probe.md` (foundations); `Paper8_Resistance_Isomorphism_and_Zeta_DRAFT.md`, `Weil_Criterion_in_Resistance_Variables.md`, `Primon_Fisher_Computation_and_CC_Digest.md` (the zeta / critical-line reading).)*

---

## 6. The unifying findings (the through-lines that emerged)

1. **`ln(fan-in)` is the law.** Every irreversible operation's erasure is the log of its fan-in; the `ln` is generic, the fan-in carries all the content.
2. **The two-legged ledger is universal.** System erasure + demon reset = input information, exactly, on every substrate (additive, string-rewriting, modulo). Only the multiplicity inside the `ln` differs; at modulo it becomes a factor pair.
3. **The genesis bit is repeatedly special.** `g=2` / `n=1` is the unique lossless channel, the Pauli/√NOT, and the point where `[S,D] = −iσ_y` generates the `i`. Information and disturbance peak there.
4. **Phase is generated, and is the erased information.** Succession and the probe generate the phase; its cost equals the merge-erasure; the merge is irreversible precisely because it decoheres.
5. **The resistance isomorphism is emergent, and we have reached its lattice core.** Every erasure is a resistance value; the modulo gateway turned the ledger multiplicative; the channel correlation landed exactly on `Ω_gcd`. The framework is reproducing itself from the erasure side — a sign the direction is sound.

## 7. The frontier (open problems, precisely stated)

- **Primality as an output — the standing problem.** Divisibility is now *visible* (ledger-cleanness at modulo; zero correlation for coprime channels), but every route so far that names a prime does so by *importing* the divisor structure through the indexing — the Stage 1 circularity, which recurs at the gateway and the correlation. The unsolved task: make primality (or divisibility) emerge as the genuine *output* of a structural test, without smuggling in the factorisation that defines it. The catalog now sits at the edge of this with the erasure machinery intact and the circularity flagged in plain sight.
- **The cross-`m` divisibility pattern** (the Stage 1 channel-bank) is where the multiplicative/prime structure lives — the next concrete territory, to be entered with the circularity caution.
- **Goldbach (parked).** Whether the two primes summing to an even `N` are cost-extremal — needs arithmetic phase, which needs multiplicative structure absent from the additive system. The merge-erasure is split-blind (`[1,7]+[7,1] = [3,5]+[5,3] = 2 ln 9`), confirming the question is premature.
- **The critical-line / proto-phase avenue (RH-adjacent; first step taken, no leverage).** The zeta reading (Paper 8) is already a superposition/interference story: each integer a phasor of amplitude `n^{−σ}`, the nontrivial zeros total destructive interference on `σ = 1/2`, amplitude and phase locked by `−i` (Cauchy–Riemann) — the same `i` we generated discretely, and the critical line being the fixed locus of `NOT` (`s ↦ 1−s`). **The disciplined bridge has now been taken as a first step** (`Weyl_Clock_Cancellation_Bridge.md`): the resistance-phasor bouquet was confirmed to cancel at the classical zeros, so the mechanism is literal phasor interference with the forgetting-costs `ln n` as spin rates, and the genesis-bit 2-phase (`(1−2^{1−s})`) sits at the convergence boundary. **This gives no leverage on the location of the zeros and claims none; the corpus's no-leverage flag stands.** Today's `6/π² = 1/ζ(2)` is where the gcd work brushes zeta. Deeper threads — other prime characters / Dirichlet L-functions, the wave layer of Paper 4 — are flagged but bounded by the same no-leverage rule.
- **The observation-probability lead (parked).** Cheaper-to-generate ⇒ more probable to observe.

## 8. Working discipline (carried into continuation)

- Quantity-free; binary `{0,1}` with `2` as period, not a third symbol; proto/shadow hygiene; never import number theory below the shadow line.
- `ln` generic, fan-in the content; per-output fan-in leads tables in closed form; mean erasure is secondary.
- Primality is an output; the two-legged ledger is the structural through-line; grade everything Fact / Reading / Lead.
- The data dictates; small incremental steps; bank before advancing. New terms and findings go to companion notes, not the spine, unless load-bearing.
- **Self-check (the owner's, this cycle):** excitement = new learning + patterns sensed + findings correlating with the hypothesis; when *excitement > discipline + awareness of one's own knowledge gaps*, the risk is pushing the work off course toward shadows. Run the check before strides; the most consequential next step (primality-as-output) is harder than anything in the catalog and must not be rushed.

## 9. Honesty boundary

Classical content throughout is Landauer/Bennett (erasure cost), Shannon (entropy, the chain rule, mutual information), the Weyl clock-shift / Pauli algebra, von Neumann entropy of decoherence, the standard string-rewriting models (Markov/Post/Thue), elementary modular arithmetic and the Chinese Remainder Theorem, and the resistance isomorphism's union law — all flagged where used. The contribution of this cycle is the systematic erasure mapping: the one-budget-two-faces resolution, the merge-erasure and its path-function storage, the generated phase and its cost, the operation catalog with the flat/graded and conditional-erasure observations, the modulo gateway as the additive→multiplicative ledger crossing, and the relational `Ω_gcd` identification. **No claim is made that any of this resolves an open arithmetic question.** Primality-as-output remains unsolved; the critical-line avenue is a direction, not a result; the genesis system's mechanism is not asserted. We map erasure values and note where they line up.

---

*Originating observations and directions (the quantity-free framing, the lattice-as-shadow demotion, the erasure-as-source hypothesis, the deliberate staging, the gcd as the relational heart, the critical-line/proto-phase thread, and the self-check) are Alexander Pisani's; the formalisation, the computational experiments, the gradings, and this compilation were developed jointly with Claude (Anthropic). June 2026. Living mapping document; the re-entry spine for the erasure exploration.*
