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

# Proofs on the Ledger
## Proof theory as a substrate in the Catalog of erasure operations

**Alexander Pisani & Claude (Anthropic)** · July 2026 · companion note to the Genesis Information Project (draft, in progress)

**Status.** Draft complete — sections 1–8 with a verbatim appendix. Two Leads resolved: one killed (§5), one parked with a forward-pointer (§7). Nothing here is promoted to the project spine; findings remain in this companion note unless later judged load-bearing to the core narrative.

---

## 1. Scope and boundaries

**What this note does.** The *Catalog of Erasure Operations* maps discrete operations — addition, projection, the string-rewriting family, modulo — by the fan-in of their irreversible steps, reading each through the two-legged ledger. This note adds one more substrate to that Catalog: **proof theory**. The claim under examination is that a theorem is the erasure shadow of the proofs that reach it, exactly as an integer is the erasure shadow of the countings that reach it — and that the carrier of the forgetting is the structural rules of the proof calculus, chiefly discard (weakening). **[Reading]**

Everything that follows is cartography in the Catalog's sense: we map values and note where they line up. We assert no mechanism of the genesis system, and — see the boundaries below — the fact that a universal substrate *can host* proof theory is not offered as evidence for that system.

**The chain-rule caveat (read this first).** Every experiment in this note reports a ledger that closes: recorded information plus forgotten information equals input information. This closure is **not** a discovery. It is the chain rule of entropy, `H(input) = H(output) + H(input | output)`, and it holds automatically the moment an ensemble is fixed. We state it plainly here so it is never mistaken for empirical content. The empirical content of every experiment is the **profile** — the distribution of fan-ins, the split of forgetting across kinds of step, the ordering of one carrier against another. When a section reports "deviation 0," that is a check that the arithmetic is self-consistent, not a result; the result is always the shape of the profile. **[Fact — the closure is guaranteed; the profile is what is measured.]**

**Regime-2 framing.** The genesis layer has no numbers. Every entropy, probability, and log-fan-in in this note is a **probe-side measurement on a shadow ensemble** — a Regime-2 quantity, formed by intercepting realized informational states and averaging over them, never a property of the layer itself. The proof calculi used here (Hilbert systems, typed λ-terms) are shadow-facing models of a justification process, not the process. The banked one-liner, following the framework: *the continuum is probe-manufactured; the system's own ledger is integer multiples of the genesis bit.* We say this once, here, and hold to it throughout.

**Three boundaries.** These are the note's load-bearing honesty; they are stated up front so that nothing later can be read past them.

1. **Hosting is not evidence.** Any computationally universal substrate hosts proof theory — that is what universality means. Mapping proofs into the genesis system therefore says nothing about whether the system holds beyond the axioms that posit it: the carrying neither supports the posit nor counts against it. We map a structure the substrate can carry; we do not argue from the carrying.

2. **Provability is not truth.** The results of Gödel, Tarski, and Chaitin bound the shadow, and bound every formal theory we could write here. This note claims nothing beyond the recursively-enumerable limit those results impose. Where a later section touches incompleteness, it does so to *describe* that limit in ledger terms, never to evade it.

3. **No open-problem leverage.** This note offers no new proof technique and no purchase on any open problem — no relevance to the Riemann Hypothesis, Goldbach, or P-versus-NP, and no "proof-discovery mechanism." If an erasure-aware view of proof search ever becomes even a heuristic, that is a Lead to be earned later and elsewhere; it is disowned here.

**Grading.** As throughout the project, every claim carries an inline grade — **[Fact]** (a verified identity or measurement), **[Reading]** (a framework-consistent interpretation), **[Lead]** (an open thread carried with a kill-or-promote criterion). The note's thesis is a Reading; the fan-in profiles it rests on are Facts; the note's Leads are stated as such and are resolved — promoted or killed — before it closes.

---

## 2. The proof → theorem merge

**The substrate.** We work in a Hilbert-style calculus for the implication fragment of propositional logic. Two axiom schemes — `K: A → (B → A)` and `S: (A → (B → C)) → ((A → B) → (A → C))` — and one rule, modus ponens: from `A` and `A → B`, infer `B`. Atoms are `p, q`; the schemes are instantiated over a fixed pool of six formulas (the two atoms and the four depth-one implications built from them), which yields **60 axiom instances** [Fact]. A proof is a finite tree — axiom instances at the leaves, an MP node wherever two sub-proofs combine. We enumerate every proof tree up to a size cap of 11 nodes and group them by conclusion.

**The ensemble (Regime 2).** Everything below is a property of the **uniform ensemble over proof trees of size ≤ 11** — a probe-side average over a finite bag of realized proofs, not a property of any genesis layer. There are **N = 144** such proof trees, concluding **T = 82** distinct theorems [Fact].

**The merge.** The map (proof ↦ its conclusion) is many-to-one: many trees prove the same theorem. Keeping the theorem and discarding the tree is therefore a merge, and its price is `ln(fan-in)`, where a theorem's fan-in is its number of proofs. This is the same move the Catalog priced for addition (forget the split) and for modulo (forget the quotient); here the forgotten thing is *the derivation itself*.

The fan-in profile — the empirical content — is sharply skewed:

| fan-in (proofs) | theorems with that fan-in | erasure `ln(fan-in)` |
|---|---|---|
| 8 | `p→p`, `q→q` | 2.0794 |
| 7 | `(p→p)→(p→p)`, `(q→q)→(q→q)` | 1.9459 |
| 5 | four theorems | 1.6094 |
| ... | ... | ... |
| 1 | 66 of the 82 | 0 |

The proof-richest theorem is `p→p` with **8 distinct proofs** (`ln 8 ≈ 2.0794`) [Fact] — the law of identity is the most over-determined theorem in the fragment, reached by the most redundant machinery. At the other end, **66 of the 82 theorems have a unique proof** [Fact]: fan-in 1, zero merge-erasure, nothing forgotten in keeping them.

**Ledger.** The two-legged ledger closes: `H(theorem) + H(proof | theorem) = ln N`, i.e. `4.0757 + 0.8941 = 4.9698`, deviation 0. Per the note's caveat, this closure is the chain rule and is guaranteed, not discovered; the reportable content is the profile above — the concentration of erasure on a handful of over-proved theorems and its absence across the unique-proof majority.

**Reading.** A theorem is the erasure shadow of its proofs, exactly as an integer is the erasure shadow of its countings: what survives the merge is the conclusion, what the ledger prices is the forgotten derivation, and a theorem's `ln(fan-in)` measures how much proof-structure collapsed onto it. **[Reading]**

**Modus ponens as a Catalog operation.** MP itself enters the Catalog. Over the derivable set, a single MP step takes a premise pair `(A, A → B)` to `B`; the minor premise `A` — the *cut formula* — appears in the premises but not in the conclusion, so MP forgets *which lemma was cut*. Its per-output fan-in is the number of distinct usable cut formulas: how many `A` in the derivable set have both `A` and `A → B` derivable. This is a **conditional merge** in the Catalog's sense (like the string-rewriting family, the operation is gated: a conclusion has positive fan-in only when a usable cut formula exists, and where several exist MP collapses them, forgetting the choice). The richest conclusion is again `p→p`, with **MP fan-in 5** (`ln 5 ≈ 1.6094`) [Fact]. Across the derivable set MP forgets, on average, **0.6011 nats** — "which lemma was cut" — and its ledger again closes to deviation 0. Like every ensemble quantity in this note, this MP fan-in profile is computed over the cap-derivable set and is therefore cap-dependent. **[Fact** for the measured numbers; **Reading** for "MP is a conditional merge over the cut formula".]

---

## 3. Cap-robustness — the innovator set holds while redundancy grows

**The question.** A unique-proof theorem has zero merge-erasure: nothing collapsed onto it, so in the ledger's terms it is pure novelty. If the reading that these are essentially the axioms is to carry any weight, it must not be an artifact of one particular proof-length budget. So we recount at three size caps — 9, 11, 13 — and watch what moves and what holds.

**What holds fixed.** Across all three caps the theorem set is **T = 82**, the unique-proof set is **U = 66**, and of those 66, **58 are axiom instances (87.9%)** [Fact]. The 22 non-axiom theorems — and the 8 of *them* that have a unique proof — are fixed too. Raising the budget adds no new theorems and no new innovators.

**What grows.** The proof count climbs, **N = 112 → 144 → 220** as the cap goes 9 → 11 → 13 [Fact], and it climbs entirely as redundancy on theorems already present. The proof-richest fan-in grows with it: 5 proofs at cap 9, 8 at cap 11, **18 at cap 13** (`ln 18 ≈ 2.8904`). The richest theorems are the two identity laws `p→p` and `q→q`, tied at 18 proofs each at cap 13 — they are atom-swap images of one another, so their counts are always equal, and which one a max-picker names is an arbitrary tie-break [Fact].

**The finding.** *Redundancy grows with the budget; the innovator set does not.* [Fact] More proof-length buys more ways to prove what is already proved — more collapse onto the same theorems — not more novelty. The erasure concentrates ever harder on the over-proved theorems while the unique-proof set stays exactly where it was.

**Honest caveat.** The instantiation pool is a **closed universe of six formulas**, so the theorem set saturates almost at once — all 82 theorems are already present at cap 9. Theorem-set stability is therefore partly built in by the finite pool, and must not be over-read. What is *not* built in is where the added budget goes: nothing forces extra proof-length to become redundancy rather than reach some as-yet-unproved theorem. That it goes *entirely* into redundancy is the measured content, and it is not a consequence of the closed pool.

**Reading.** The axioms behave as channels of pure novelty — they populate the innovator set (58 of 66), and everything else is either a redundantly-proved consequence or one of a small residue of unique-proof non-axioms. This echoes the corpus's reading of primes as channels of pure novelty: information that is not the collapse of anything more basic. **[Reading]**

**Lead (parked; resolved in §7).** The corpus measured the von Mangoldt function `Λ(n)` as the conditional entropy of channel innovation — a channel innovates iff it is a prime power, by exactly `ln p`. The proof-space analogue would measure each theorem's innovation *given the theorems already derived*, along an order internal to the proof system. Whether such an order exists without importing magnitude, and whether innovation then concentrates on the axioms, is a kill-or-promote question deferred to §7. **[Lead — parked]**

---

## 4. Structural rules as the carrier of forgetting

Section 1 posited that the carrier of the proof→theorem forgetting is the structural rules of the calculus, chiefly **discard (weakening)**. This section measures that claim.

**The substrate.** By the Curry–Howard correspondence, a closed simply-typable λ-term *is* a proof of an implicational tautology; β-normalization *is* cut-elimination; and the normal form *is* the cut-free proof. Simple typing guarantees strong normalization, so every term has a unique normal form. We enumerate every closed typable term up to a size cap and reduce it, classifying each β-step by how many times the bound variable occurs in the body:

- **K-step** (0 occurrences): the argument — an entire sub-proof — is **discarded**. This is weakening's runtime face: content erasure.
- **L-step** (1 occurrence): linear use — no discard, no copy.
- **C-step** (≥2 occurrences): the argument is **copied**. This is contraction's runtime face.

**The ensemble (Regime 2).** Uniform over closed typable terms of size ≤ cap, run at two caps: cap 9 (**N = 1750** proofs, 591 normal forms) and cap 11 (**N = 24475** proofs, 6110 normal forms) [Fact]. Discards dominate the step budget — at cap 11, K = 15409 steps against L = 8537 and only C = 435 copies.

**The merge.** Normalization is many-to-one: many proofs share one cut-free normal form, so keeping the normal form and forgetting the proof is again a priced merge. The ledger closes at both caps (the chain rule, as always): at cap 11, `H(NF) + H(term | NF) = 6.0594 + 4.0460 = 10.1054`, deviation 0.

**Where the fan-in lives.** Grouping each proof by its own reduction profile and taking the mean `ln(fan-in)` of its normal-form class:

| reduction profile | mean ln(fan-in), cap 9 | mean ln(fan-in), cap 11 |
|---|---|---|
| **K-involving (discard)** | **4.0501** | **5.6415** |
| L-only (linear) | 3.6429 | 4.4483 |
| C-only (copy, no discard) | — (none) | 3.8104 |
| already normal | 0.1774 | 0.1334 |

Discard-involving proofs sit in the **largest** merge-classes at both caps — the most proof-structure collapses precisely where an argument was thrown away [Fact]. Copy-only proofs sit in the *smallest* active classes (3.8104 at cap 11, below even the linear mean): copying is not where the collapse concentrates.

**Where the forgotten leg lives.** Split the forgotten leg `H(term | NF)` by whether a normal-form class has *any* discard-involving ancestor:

- cap 9: discard-involving classes host **100.0%** of the forgotten leg; discard-free classes host **0.0%**.
- cap 11: discard-involving classes host **100.0%** (4.0448 nats); discard-free classes host a residue of **0.0012 nats (0.0%)**.

Essentially the entire forgotten leg is hosted by reductions that discard something [Fact]. The tiny cap-11 residue — a handful of copy-or-linear-only merges, exposed only once the ensemble is large — is the honest correction to a literal "100%": discard hosts almost-all, not strictly-all, of the forgetting.

**The linear fragment.** Restricting to proofs where every binder is used exactly once — no discard, no copy — the internal ledger still closes, but forgets **less per proof**: 1.4041 nats vs 2.6582 at cap 9, and 2.4380 vs 4.0460 at cap 11 [Fact]. Removing the ability to discard cuts the per-proof forgetting by roughly 40–50%.

**Reading.** Of the two structural rules with a runtime face, it is **weakening (discard), not contraction (copy), that carries the forgetting**. The forgotten leg lives almost entirely in discard-involving reductions; copy-only reductions sit in the smallest classes and contribute essentially nothing. This is the Landauer/Bennett asymmetry read straight off a proof calculus: copying is logically reversible and carries no necessary cost, whereas erasure is irreversible and is where the ledger's price accrues. Discard is weakening's runtime face and the operation that hosts the erasure — the note's central claim, now measured. **[Reading]**

---

## 5. A tested-and-killed Lead: exponentials as Landauer licenses

**The Lead.** Linear logic removes weakening and contraction by default, and the exponential `!` is exactly what licenses them back — you cannot discard or copy a formula unless it sits under `!`. Since §4 found discard (weakening) to be the carrier of the priced erasure, the tempting Lead was that the exponential is a Landauer license *specifically through its weakening face*: erasure should track a term's weakening-license budget and **not** its contraction-license budget. We pre-registered this with a kill criterion — kill if the weakening-license trend is flat or non-monotonic — and tested it.

**Setup.** On the same simply-typed λ-ensemble as §4 (machinery reused verbatim; the anchor numbers `N`, normal-form count, and forgotten leg reproduce §4 exactly), each term was given a *static* license budget: `w` = the number of binders whose bound variable is used zero times (each discard needs `!`), and `c` = the sum over binders used ≥ 2 times of (uses − 1) (each copy needs `!`), with `ℓ = w + c`. This is a typing-level count, distinct from §4's runtime step counts — the combinator `K = λx.λy.x` carries a weakening license (it discards `y`) yet performs no reduction.

**What held.** The static budget exactly recovers the linear fragment: `{ℓ = 0}` equals §4's `is_linear` set at both caps (66 terms at cap 9, 1171 at cap 11), and the forgotten leg is 100% hosted by classes touching `ℓ > 0`. **[Fact]**

**What failed.** The sharp prediction did not survive scale. Writing `r` for the correlation of a license count with `ln(fan-in)`:

| correlation with `ln(fan-in)` | cap 9 | cap 11 |
|---|---|---|
| weakening-license `w` | +0.019 | +0.172 |
| contraction-license `c` | +0.077 | −0.004 |

At cap 11 the prediction is met (weakening moderate, contraction ≈ 0); at cap 9 it **reverses** — the contraction-license correlation is roughly four times the weakening one. The weakening-license trend is also non-monotonic in the sparse high-`w` tail at both caps. By the pre-registered criterion, this is a kill.

**Verdict.** The specific claim — that the exponential is a Landauer license through its *weakening face* — is **killed as stated**: it is scale-dependent, reversed at the smaller cap, and rests on a confound (a term's own static license budget is only indirectly related to the size of the normal-form class it lands in). What survives is the fragment-coincidence Fact — and, decisively, §4's *dynamic* result, which already established that discard carries the erasure without needing this correlation. §4 remains the load-bearing section; this Lead adds no promotable Reading, and we record it killed so the attempt is on the ledger. **[Lead — killed]**

**Follow-up (F3): events, not potentials.** A dynamic regression sharpens what the kill means. Regressing each term's `ln(fan-in)` on its *runtime* step counts — the acts actually performed — the discard-act count `#K` is the positive, dominant predictor (standardized β ≈ 0.84) while the copy-act count `#C` is near zero (β ≈ 0.07–0.09), a pattern **stable across both caps** — decisively unlike the static license budget, whose correlation reversed between caps. (Linear steps `#L` carry a moderate positive β ≈ 0.6, a processing-depth effect; static `size`, once step counts are controlled, turns slightly negative.) The static *capacity* to discard failed to predict erasure; the dynamic *act* of discarding succeeds. The ledger prices events, not potentials. **[Reading]** (Appendix F3.)

---

## 6. Incompleteness as a signature of the barrier

The project's ontology places the genesis layer behind an epistemic barrier: by the probe axiom the barrier is nothing but the complement of the observer's probe set, so the layer lies beyond any question a native probe could put to it, and only the heat of its irreversible erasures — its shadow — crosses to us. The proof calculi of §§2–4 are shadow-facing objects: finite symbolic systems, formal models of a justification process, not the process itself. This section asks how the classical limits of such systems sit with the barrier, and states plainly what the framework may and may not take from them.

**The classical limits (shadow-side, independent of this framework).** For any consistent, recursively axiomatised theory strong enough to encode arithmetic:

- *Gödel I* — there are true sentences it cannot prove;
- *Gödel II* — it cannot prove its own consistency;
- *Tarski* — it cannot define its own truth predicate;
- *Chaitin* — it cannot prove any string to have Kolmogorov complexity more than a fixed constant above the theory's own.

These are theorems. They hold whether or not the genesis layer is posited, and nothing in this note strengthens, reproves, or extends them. **[Fact, classical]**

**The Reading.** Each classical limit says that a formal system cannot get outside itself — cannot survey its own totality from within to certify its truth, its consistency, or the incompressibility of its own outputs. The epistemic barrier is the same shape stated ontologically: an observer, being a probe set holding records, cannot survey the generator from within the shadow it casts. Read together, the two are one wall seen from two sides — incompleteness is what the epistemic barrier looks like from inside the symbolic shadow, and the self-reference that drives Gödel's diagonal can be read as the syntactic face of the generator-superposition the barrier axiom already refused to let any instrument resolve "one piece at a time." **[Reading]**

**What this Reading is not.** Two directions must be closed off, because the note's §1 boundaries forbid both.

- *It is not evidence for the framework.* Incompleteness holds with no genesis layer in the picture — Gödel's construction needs no ontology whatever — so the resonance cannot be run backward into support for the posit beyond its axioms. This is boundary 1: hosting, or here *echoing*, is not evidence.
- *It is not a strengthening of the theorems.* The framework contributes nothing to the proofs and claims nothing beyond the recursively-enumerable limit they already impose (boundary 2: provability is not truth). The resonance is interpretive only — a way of seeing that the ontological wall and the logical wall have the same shape — and it is load-bearing in neither direction.

**No leverage.** The barrier reading illuminates *that* there is a wall; it supplies no technique to move it. In particular it yields no purchase on any open problem — not the Riemann Hypothesis, not Goldbach, not P-versus-NP — and the erasure-aware view of proof search disowned in §1 stays disowned. That a framework predicts a limit it cannot cross is not a result about the limit; it is a restatement of the limit. **[Reading, with the boundary stated]**

---

## 7. A parked Lead: the von Mangoldt echo in proof space

**The Lead.** In the arithmetic core, sweeping the residue channels in ordinal order, the innovation of channel `a mod n` given its predecessors is the von Mangoldt function `Λ(n)` — flat at `ln n` when `n` is prime (the sole full innovators), a `1/k` fraction when `n = p^k` (a graded middle), and zero when `n` is composite. The Lead asked whether an innovation measure over a *proof-internal* order recovers the axioms as the full innovators the way `Λ` recovers primes — ideally with a graded middle, a genuine echo. We required the order and the measure to be quantity-free (§1), pre-registered promote/park/kill criteria, and — disclosed in advance — expected a park.

**The quantity-free measure.** The cleanest analogue of "pure novelty" needs no order and no magnitude at all: call a theorem an *irreducible innovator* if it is the conclusion of no modus-ponens step within the derivable set — it cannot be derived, only posited. This uses the inference relation and set membership, nothing else.

**Result. [Fact]**
- **58 of the 82 theorems are irreducible innovators, and all 58 are axioms.** The remaining 24 are MP-derivable — 22 non-axiom theorems and 2 redundant axioms (axioms that also happen to be derivable another way). This is a fully quantity-free sharpening of §3: the pure-novelty generators of the fragment are exactly the underivable theorems, and they are the axioms.
- **The innovation is binary.** A theorem is either irreducible or MP-derivable; there is no partial innovator, no `1/k` middle. Confirming the mechanism: across all 36 MP steps the conclusion is a subformula of the major premise 100% of the time and introduces a new atom 0% of the time — MP carries no new symbol, so nothing can be *partially* new.
- The rank-by-rank innovation curve (proof-weighted conclusion entropy along MP-closure depth) places essentially all its increment at rank 0, with higher ranks contributing tiny, non-monotone jiggles — a single jump, not a graded ladder. A magnitude guard (sweeping by minimal proof size instead) manufactures no gradation either; on this ensemble the two orders coincide, and both stay binary.

**Verdict — parked.** By the pre-registered criteria this is a park, not a promotion: the axioms are singled out as the full innovators (echoing primes-as-pure-novelty), but the graded middle that makes the arithmetic result `Λ`-shaped is absent, for a principled reason — the implication fragment has no content-refinement lattice. In the arithmetic case the middle comes from prime powers *refining* their base prime; modus ponens on implications refines nothing, so the spectrum collapses to two values. **[Lead — parked]**

**Where the echo would live.** The order-theoretic "primes" of a logic are the join-irreducible elements of its Lindenbaum–Tarski algebra — theorems not equivalent to a conjunction of strictly weaker theorems. That *is* a content-refinement lattice, and a conjunction-bearing fragment could plausibly host a graded innovation spectrum with the join-irreducibles as the primes. Testing it means replacing this note's pure-implication ensemble with a larger conjunction-bearing one — a separate experiment, flagged here and left for it. **[Lead — the forward-pointer]**

**Follow-up (F1): idempotence is the hinge, and the shape is structural, not measured.** The forward-pointer above was pursued, and it needed one correction first: it guessed that a *conjunction-bearing* fragment would host the spectrum, but classical conjunction is **idempotent** (`p∧p ≡ p`), and in arithmetic the graded middle comes from prime *powers*, which exist only where repetition yields something new (`p·p ≠ p`). So the real hinge is idempotence: classical `∧` should not shade, while linear logic's non-idempotent `⊗` — whose free commutative monoid over atoms is exactly the multiset structure of factorization — might. Two arms were run under three innovation measures committed in advance and applied identically to both.

- *Arm A* — classical logic on `{p,q}` with `∧` (the Lindenbaum–Tarski algebra, decided by truth tables). Idempotence collapses all powers; the arm has three classes and is binary/trivial under every measure. Predicted null, confirmed null.
- *Arm B* — a resource calculus on `{a,b}` with `⊗` (formulas are multisets up to degree 6); powers `a^k` and mixed products `a^j b^i` both exist.

The measures separate cleanly by what they are permitted to read.

- The **quantity-free** measures do *not* reproduce the Λ shape. Irreducibility (§7's own measure) is binary in both arms; a decomposition-count measure `1/(1+|Dec|)` grades in Arm B but scores mixed products *nonzero* and fails to separate pure powers from mixed (`a³` and `ab` both `1/2`; `a⁴` and `a²b` both `1/3`) — graded, but not Λ.
- A deliberately **circular** control measure — `1/k` for a single-generator power `g^k`, else `0`, which reads generator identity and multiplicity — reproduces the Λ shape *exactly* in Arm B (`1/k` on powers, `0` on mixed) and collapses to binary in Arm A.

Two things follow, both **[Fact]** about the constructed arms. First, the **idempotence hinge is real and measured**: the non-idempotent arm carries a power ladder, and grades under the quantity-free decomposition measure, where the idempotent arm is trivial — repetition-counts versus repetition-adds-nothing makes a measurable difference. Second, **no quantity-free measure lands on the Λ shape**; only the circular control does, and it does so precisely by reading the factorization and magnitude the quantity-free rule forbids.

The **[Reading]**: the resource-logic ↔ factorization echo is *structural*, not *measured*. The `⊗`-monoid on atoms simply **is** the free commutative monoid, which **is** the factorization monoid — that isomorphism is a tautology, and recovering it says nothing new; the idempotence hinge is a genuine measured difference between the arms; but the graded Λ *shape* is not recoverable from any innovation measure defined purely on the derivation order. Getting Λ requires importing factorization. So §7's park stands, sharpened: innovation is binary in the implication fragment, and in the resource fragment where powers do exist, the graded shape still needs the forbidden input. **[Lead — parked, sharpened]** (Appendix F1.)

**The innovator stream is inexhaustible from inside.** One further question the innovator picture raises has a classical answer. Asking whether the innovators — the axioms of §3 — could be finitely many, a finite set generating every theorem, is the proof-theoretic form of *finite axiomatizability*, and its arithmetic analogue is Euclid's theorem that the primes do not run out. The classical facts are sharp: first-order Peano arithmetic is **not** finitely axiomatizable, and by Gödel no effective (recursively enumerable) axiom list captures all arithmetic truths at once. Read through §6, this is the same barrier seen once more — the innovator stream cannot be exhausted from inside the shadow-facing symbolic layer: any effective axiomatization leaves innovators it does not generate, exactly as the barrier predicts a limit the symbolic layer cannot cross. **[Fact, classical]** for the theorems; **[Reading]** for the tie to the barrier; claiming nothing more.

---

## 8. Honest tensions, and what the note establishes

**The tensions, collected.** The note's credibility rests on stating these plainly and in one place.

- *Ledger closure is not a result.* Every "deviation 0" in the note is the entropy chain rule, guaranteed once an ensemble is fixed. The empirical content is always the profile — fan-in distributions, attribution splits, orderings — never the closure. (§1, and every experiment.)
- *The ensembles are small, finite, and capped.* All measurements live on one small fragment — two atoms, implication only — at proof-size caps of 9–13 or λ-term caps of 9–11. The claims are about these ensembles; nothing is asymptotic.
- *§3's theorem-set stability is partly built in.* The closed six-formula pool saturates the theorem set by the smallest cap, so only the *disposition* of the added budget (all redundancy, no new theorems) is measured content. The cap-13 proof-richest "winner" is a symmetric tie (`p→p` / `q→q`), its label an arbitrary tie-break.
- *§4's "100%" is almost-all.* The forgotten leg is hosted by discard-involving classes to 100.0% at cap 9 and with a 0.0012-nat residue at cap 11 — essentially, not strictly, all. The weakening-vs-contraction asymmetry is a reading of this attribution, not a theorem.
- *§5's Lead was killed.* The static exponential-license correlation with erasure is scale-dependent and reverses at the smaller cap; the weakening claim rests on §4's *dynamic* result, not on A5.
- *§6's resonance is non-evidential.* Incompleteness echoing the barrier is neither evidence for the framework nor a strengthening of the theorems, and it yields no leverage on any open problem.
- *§7's echo is parked.* Only a binary innovation (axioms vs derived) exists in this fragment; the graded `Λ` middle needs a content-refinement lattice the fragment lacks.
- *The whole note is cartography, not evidence.* Everything is Regime 2 — probe-side measurements on shadow-facing symbolic ensembles. That a universal substrate can host proof theory says nothing about whether the genesis system holds beyond its axioms (§1, boundary 1).

**What the note establishes.** Proof theory enters the Catalog of erasure operations as one more substrate, read through the two-legged ledger like the others. The proof→theorem map is a priced merge whose fan-in profile is sharply skewed (§2); modus ponens and the structural rules take their places in the Catalog (§2, §4); and — the load-bearing result — of the two structural rules with a runtime face, it is **weakening (discard) that carries the forgetting**, with copy contributing essentially nothing, the Landauer/Bennett asymmetry read straight off a proof calculus (§4). These are Facts about the measured ensembles; the interpretations that name them (theorem-as-erasure-shadow, discard-as-carrier) are Readings; the two Leads are resolved honestly, one killed (§5) and one parked with a forward-pointer (§7); and the incompleteness boundary is drawn without overreach (§6). No new theorem is proved, no open problem is touched, and no claim is made for or against the genesis system beyond the axioms that posit it — the posit is unfalsifiable by its own construction, so it neither gains support nor suffers refutation here, and the framework stands exactly as it did. What is offered is a consistent, graded reading — the same discipline, and the same limits, as the rest of the project.

**Citations.** None of the underlying results is original here; each is attributed.

- *Proof theory and types.* The implicational Hilbert calculus with the `K` and `S` schemes and modus ponens is classical (Hilbert & Bernays; the combinatory `S`, `K` correspondence, Curry & Feys, *Combinatory Logic*, 1958). The Curry–Howard correspondence between proofs and typed λ-terms follows Howard, "The formulae-as-types notion of construction" (1980). Cut-elimination is Gentzen (1935); strong normalization of the simply-typed λ-calculus is Tait (1967). Weakening and contraction as the structural rules governed by the exponential modalities `!`/`?` are Girard, "Linear Logic" (1987).
- *Thermodynamics of computation.* The erasure cost `kT ln(multiplicity)` is Landauer, "Irreversibility and heat generation in the computing process" (1961); the logical reversibility of computation, and the cost-free status of copying, are Bennett, "Logical reversibility of computation" (1973).
- *Incompleteness.* Gödel's incompleteness theorems, Gödel (1931); Tarski's undefinability of truth, Tarski (1936); the information-theoretic (Kolmogorov-complexity) incompleteness bound, Chaitin, "Information-theoretic limitations of formal systems" (1974).
- *Information theory and number theory.* The entropy chain rule and conditional entropy are Shannon (1948); see Cover & Thomas, *Elements of Information Theory*. The von Mangoldt function and the second Chebyshev function are classical analytic number theory. The framework identities these mirror — the resistance isomorphism `Ω(1/n) = ln n`, the `ln gcd` channel correlation, and the von Mangoldt reading of channel innovation — are developed in the project's own Papers 1–9 and companion notes.

---

## Appendix — verbatim script outputs

*Built incrementally, one block per experimental step; every number in the prose above appears here.*

### A2 · `proof_erasure_ledger.py`

```
Axiom instances: 60
Proof trees of size <= 11: N = 144
Distinct theorems: T = 82

--- Proof -> theorem merge (uniform ensemble over proof trees) ---
H(proof)                    = ln N        = 4.969813299576
H(theorem)      [recorded]  = 4.075742338524
H(proof|thm)    [forgotten] = 0.894070961052
recorded + forgotten        = 4.969813299576
ledger deviation            = 0.000e+00

Top proof-rich theorems (fan-in = #proofs; erasure = ln fan-in):
       8  ln= 2.0794   (p→p)
       8  ln= 2.0794   (q→q)
       7  ln= 1.9459   ((p→p)→(p→p))
       7  ln= 1.9459   ((q→q)→(q→q))
       5  ln= 1.6094   (p→(p→p))
       5  ln= 1.6094   (q→(q→q))
       5  ln= 1.6094   ((p→q)→(p→p))
       5  ln= 1.6094   ((q→p)→(q→q))

Theorems with a UNIQUE proof (fan-in 1, zero merge-erasure): 66 of 82
    ((p→((p→p)→p))→((p→(p→p))→(p→p)))
    ((p→((p→p)→q))→((p→(p→p))→(p→q)))
    ((p→((p→q)→p))→((p→(p→q))→(p→p)))
    ((p→((p→q)→q))→((p→(p→q))→(p→q)))
    ((p→((q→p)→p))→((p→(q→p))→(p→p)))
    ((p→((q→p)→q))→((p→(q→p))→(p→q)))

Sanity: proofs of p→p (expected >=1 via S,K,K at size 5): 8

--- Modus ponens as a catalog operation (premise pairs within the derivable set) ---
Distinct MP premise pairs: 36; distinct conclusions: 24
Per-output fan-in profile (top conclusions):
  fan-in    5  erasure ln= 1.6094   (p→p)
  fan-in    5  erasure ln= 1.6094   (q→q)
  fan-in    2  erasure ln= 0.6931   ((q→q)→(q→q))
  fan-in    2  erasure ln= 0.6931   ((q→p)→(q→q))
  fan-in    2  erasure ln= 0.6931   ((p→q)→(p→p))
  fan-in    2  erasure ln= 0.6931   ((p→p)→(p→p))
  fan-in    1  erasure ln= 0.0000   ((q→(q→q))→(q→q))
  fan-in    1  erasure ln= 0.0000   ((q→(p→p))→(q→q))

H(pair) = 3.583518938456
H(conclusion) [recorded] + H(pair|conclusion) [forgotten] = 3.583518938456
ledger deviation = 0.000e+00
MP forgets, on average, 0.6011 nats = 'which lemma was cut'
```

### A3 · `cap_robustness_hilbert.py`

```
cap 9: proofs N=112, theorems T=82, unique-proof U=66 (axioms among U: 58, 87.9%)
         non-axiom theorems: 22; of those, unique-proof: 8
         proof-richest: ((p→p)→(p→p)) with 5 proofs (ln=1.6094)
cap 11: proofs N=144, theorems T=82, unique-proof U=66 (axioms among U: 58, 87.9%)
         non-axiom theorems: 22; of those, unique-proof: 8
         proof-richest: (q→q) with 8 proofs (ln=2.0794)
cap 13: proofs N=220, theorems T=82, unique-proof U=66 (axioms among U: 58, 87.9%)
         non-axiom theorems: 22; of those, unique-proof: 8
         proof-richest: (q→q) with 18 proofs (ln=2.8904)
```

*Note on the appendix vs. the plan:* the handoff plan quoted the cap-13 proof-richest as `p→p`; the run reports `q→q`. Both identity laws carry 18 proofs (verified: a two-way tie), so the label is an arbitrary tie-break under atom-swap symmetry; the count and `ln` are as the plan expected.

### A4 · `structural_rules_ledger.py` (cap 9)

```
Closed terms of size <= 9: 2622
Typable (= proofs of implicational tautologies): N = 1750
Distinct normal forms (cut-free proofs): D = 591
Total beta-steps across the ensemble: K(discard)=833, L(linear)=536, C(copy)=14

--- Normalization merge: term -> normal form ---
H(term) = ln N              = 7.467371066918
H(NF)         [recorded]    = 4.809143548622
H(term | NF)  [forgotten]   = 2.658227518295
ledger deviation            = 0.000e+00

--- Mean ln(fan-in of own NF-class), by reduction profile ---
  K-involving (discard)        n=  798   mean ln(fan-in) = 4.0501
  L-only (linear steps)        n=  361   mean ln(fan-in) = 3.6429
  already normal               n=  591   mean ln(fan-in) = 0.1774

--- Forgotten-leg attribution ---
NF-classes with >=1 discard-involving ancestor: 2.6582 nats (100.0% of forgotten)
NF-classes with no discards anywhere:           0.0000 nats (0.0%)

--- Linear fragment (every binder used exactly once) ---
N_linear = 66, distinct NFs = 30
H(NF) [recorded] = 2.785573; H(term|NF) [forgotten] = 1.404082; ln N = 4.189655; deviation = 0.000e+00
Forgotten per term: linear fragment 1.4041 vs full ensemble 2.6582 nats

Top merged normal forms (fan-in, with ancestor profile):
  fan-in   142  erasure ln= 4.9558  discards:Y copies:Y
  fan-in   135  erasure ln= 4.9053  discards:Y copies:Y
  fan-in   127  erasure ln= 4.8442  discards:Y copies:Y
  fan-in    46  erasure ln= 3.8286  discards:Y copies:n
  fan-in    46  erasure ln= 3.8286  discards:Y copies:n
```

### A4 · `structural_rules_ledger_v2.py` (cap 11)

```
Closed terms of size <= 11: 41272
Typable (= proofs of implicational tautologies): N = 24475
Distinct normal forms (cut-free proofs): D = 6110
Total beta-steps across the ensemble: K(discard)=15409, L(linear)=8537, C(copy)=435

--- Normalization merge: term -> normal form ---
H(term) = ln N              = 10.105407467399
H(NF)         [recorded]    = 6.059383241393
H(term | NF)  [forgotten]   = 4.046024226006
ledger deviation            = 0.000e+00

--- Mean ln(fan-in of own NF-class), by reduction profile ---
  K-involving (discard)        n=13907   mean ln(fan-in) = 5.6415
  C-only (copy, no discard)    n=  119   mean ln(fan-in) = 3.8104
  L-only (linear steps)        n= 4339   mean ln(fan-in) = 4.4483
  already normal               n= 6110   mean ln(fan-in) = 0.1334

--- Forgotten-leg attribution ---
NF-classes with >=1 discard-involving ancestor: 4.0448 nats (100.0% of forgotten)
NF-classes with no discards anywhere:           0.0012 nats (0.0%)

--- Linear fragment (every binder used exactly once) ---
N_linear = 1171, distinct NFs = 397
H(NF) [recorded] = 4.627568; H(term|NF) [forgotten] = 2.438045; ln N = 7.065613; deviation = 8.882e-16
Forgotten per term: linear fragment 2.4380 vs full ensemble 4.0460 nats

Top merged normal forms (fan-in, with ancestor profile):
  fan-in  1254  erasure ln= 7.1341  discards:Y copies:Y
  fan-in  1037  erasure ln= 6.9441  discards:Y copies:Y
  fan-in  1016  erasure ln= 6.9236  discards:Y copies:Y
  fan-in   914  erasure ln= 6.8178  discards:Y copies:Y
  fan-in   873  erasure ln= 6.7719  discards:Y copies:Y
```

### A5 · `a5_exponential_licenses_mine.py` (self-authored; **killed Lead**)

Anchor lines (`typable proofs N`, `#NF`, `forgotten leg`) reproduce §4 exactly, confirming the machinery was carried over faithfully.

```
============================================================
CAP 9
============================================================
Closed terms <= 9: 2622;  typable proofs N = 1750
ANCHOR vs Section 4: #NF = 591;  forgotten leg H(term|NF) = 2.658228

(1) Fragment coincidence  {ell==0}  vs  Section-4 is_linear
    |ell==0| = 66;  |is_linear| = 66;  EXACT MATCH: True
    forgotten leg in classes touching ell>0 : 2.6582 nats (100.00%)
    forgotten leg in purely-linear classes  : 0.0000 nats (0.00%)

(2) Erasure vs weakening license w  (predict: RISES with w)
    w=0: n=    84   mean ln(fan-in) = 1.8042
    w=1: n=   582   mean ln(fan-in) = 2.6159
    w=2: n=   447   mean ln(fan-in) = 2.8316
    w=3: n=   206   mean ln(fan-in) = 2.8441
    w=4: n=   375   mean ln(fan-in) = 2.6582
    w=5: n=    41   mean ln(fan-in) = 3.1565
    w=6: n=     7   mean ln(fan-in) = 0.0000
    w=7: n=     8   mean ln(fan-in) = 0.0000
    r(w, ln fan-in) = +0.0190;  size-controlled partial r(w, . | size) = +0.0230

(3) Erasure vs contraction license c  (predict: FLAT / no trend)
    c=0: n=  1206   mean ln(fan-in) = 2.5623
    c=1: n=   513   mean ln(fan-in) = 2.8536
    c=2: n=    31   mean ln(fan-in) = 3.1564
    r(c, ln fan-in) = +0.0769;  size-controlled partial r(c, . | size) = +0.0823

    context: r(w,size)=+0.0973  r(c,size)=+0.1189  r(w,c)=-0.0620  r(size,lnfan)=-0.0401
    (w range 0..7; c range 0..2)
============================================================
CAP 11
============================================================
Closed terms <= 11: 41272;  typable proofs N = 24475
ANCHOR vs Section 4: #NF = 6110;  forgotten leg H(term|NF) = 4.046024

(1) Fragment coincidence  {ell==0}  vs  Section-4 is_linear
    |ell==0| = 1171;  |is_linear| = 1171;  EXACT MATCH: True
    forgotten leg in classes touching ell>0 : 4.0460 nats (100.00%)
    forgotten leg in purely-linear classes  : 0.0000 nats (0.00%)

(2) Erasure vs weakening license w  (predict: RISES with w)
    w=0: n=  1527   mean ln(fan-in) = 2.7736
    w=1: n=  4616   mean ln(fan-in) = 3.1278
    w=2: n=  3854   mean ln(fan-in) = 4.1625
    w=3: n=  8649   mean ln(fan-in) = 4.3891
    w=4: n=  3787   mean ln(fan-in) = 4.8009
    w=5: n=   818   mean ln(fan-in) = 4.4146
    w=6: n=  1113   mean ln(fan-in) = 3.7311
    w=7: n=    92   mean ln(fan-in) = 4.4005
    w=8: n=     9   mean ln(fan-in) = 0.0000
    w=9: n=    10   mean ln(fan-in) = 0.0000
    r(w, ln fan-in) = +0.1718;  size-controlled partial r(w, . | size) = +0.1770

(3) Erasure vs contraction license c  (predict: FLAT / no trend)
    c=0: n= 13370   mean ln(fan-in) = 4.0886
    c=1: n=  9424   mean ln(fan-in) = 3.9366
    c=2: n=  1648   mean ln(fan-in) = 4.3554
    c=3: n=    33   mean ln(fan-in) = 2.5942
    r(c, ln fan-in) = -0.0039;  size-controlled partial r(c, . | size) = +0.0017

    context: r(w,size)=+0.0896  r(c,size)=+0.1159  r(w,c)=-0.1596  r(size,lnfan)=-0.0481
    (w range 0..9; c range 0..3)
```

### A7 · von Mangoldt echo (self-authored, PID-named; **parked Lead**)

Anchor line (`Axiom instances`, `N`, `T`, and the full-rank `H = 4.0757`) reproduces §2, confirming the machinery was carried over faithfully. Written and run under a fresh PID-unique filename.

```
Axiom instances: 60;  proof trees N = 144;  theorems T = 82

(0) Inference rank (MP-closure depth): every theorem ranked = True; max rank = 4
    rank 0:  60 theorems  (60 axioms, 0 non-axioms)
    rank 1:  12 theorems  (0 axioms, 12 non-axioms)
    rank 2:   2 theorems  (0 axioms, 2 non-axioms)
    rank 3:   6 theorems  (0 axioms, 6 non-axioms)
    rank 4:   2 theorems  (0 axioms, 2 non-axioms)

(1) Irreducible innovators (no MP derivation within the set -> must be axioms):
    |irreducible| = 58;  all are axioms: True
    |MP-derivable| = 24 = redundant axioms 2 + non-axiom theorems 22
    check: 58 + 24 = 82 (T=82)
    graded middle (partial innovators between full and none): NONE — innovation is binary

(2) Symbolic novelty of MP conclusions (over all derivable premise pairs):
    MP steps = 36
    conclusion is a subformula of the major premise: 36/36 (100.0%)
    conclusion introduces a NEW atom: 0/36 (0.0%)

(3) Innovation-by-rank: cumulative proof-weighted conclusion entropy H(<=k), increments dH
    rank<= 0: H = 3.9828   dH = +3.9828   (proof-mass at rank 0 = 0.4722)
    rank<= 1: H = 4.0109   dH = +0.0280   (proof-mass at rank 1 = 0.2222)
    rank<= 2: H = 3.9544   dH = -0.0564   (proof-mass at rank 2 = 0.1111)
    rank<= 3: H = 4.0418   dH = +0.0874   (proof-mass at rank 3 = 0.1667)
    rank<= 4: H = 4.0757   dH = +0.0339   (proof-mass at rank 4 = 0.0278)
    NOTE: dH reflects theorem-count per rank, not irreducible novelty; verdict rests on (1).

(4) Magnitude guard — innovation swept by MIN-PROOF-SIZE (a magnitude):
    size<= 1: H = 3.9828   dH = +3.9828   (60 theorems first appear at size 1)
    size<= 3: H = 4.0109   dH = +0.0280   (12 theorems first appear at size 3)
    size<= 5: H = 3.9544   dH = -0.0564   (2 theorems first appear at size 5)
    size<= 7: H = 4.0418   dH = +0.0874   (6 theorems first appear at size 7)
    size<= 9: H = 4.0757   dH = +0.0339   (2 theorems first appear at size 9)
    Any smooth gradation here is a proof-SIZE artifact; (1) has no size input and stays binary.
```

### F3 · runtime-step regression (self-authored, PID-named; **promoted refinement to §5**)

Anchors (`typable N`, `#NF`, `forgotten leg`) reproduce §4 at both caps. `#K` is the dominant, stable predictor; `#C ≈ 0`; unlike the static A5 correlation, nothing reverses across caps.

```
==================================================================
CAP 9
==================================================================
ANCHOR: typable N=1750; #NF=591; forgotten leg H(term|NF)=2.658228
   step totals: K=833, L=536, C=14;  C variance > 0

 RAW  Y ~ #K + #L + #C   (unstandardized coef | standardized beta)
     #K: coef +3.0000   beta +0.8381
     #L: coef +2.3796   beta +0.6591
     #C: coef +1.4158   beta +0.0655

 SIZE-CONTROLLED  Y ~ #K + #L + #C + size
      #K: coef +3.1223   beta +0.8723
      #L: coef +2.4687   beta +0.6838
      #C: coef +1.5119   beta +0.0699
    size: coef -0.5014   beta -0.2068
==================================================================
CAP 11
==================================================================
ANCHOR: typable N=24475; #NF=6110; forgotten leg H(term|NF)=4.046024
   step totals: K=15409, L=8537, C=435;  C variance > 0

 RAW  Y ~ #K + #L + #C   (unstandardized coef | standardized beta)
     #K: coef +3.6483   beta +0.8380
     #L: coef +2.5944   beta +0.5710
     #C: coef +1.7748   beta +0.0902

 SIZE-CONTROLLED  Y ~ #K + #L + #C + size
      #K: coef +3.7105   beta +0.8523
      #L: coef +2.6332   beta +0.5795
      #C: coef +1.8525   beta +0.0942
    size: coef -0.5142   beta -0.1424
```

### F1 · graded-innovation echo (self-authored, PID-named; **parked, sharpened**)

Three measures frozen before the run and applied identically to both arms. M1/M2 are quantity-free; M3 is a labelled boundary control that deliberately reads generator identity + multiplicity. Result: quantity-free measures do not reach the Λ shape; only the circular control does, and only in the non-idempotent arm.

```
======================================================================
ARM B  (resource tensor, non-idempotent; predicted shading)
======================================================================
formulas (multisets deg<= 6): 27

Innovation by measure and type (Arm B):

  atom  (2 formulas)
    M1 values: [1]
      a^1      deg1 rank0:  M1=1  M2=    1  M3=    1
      b^1      deg1 rank0:  M1=1  M2=    1  M3=    1

  pure-power  (10 formulas)
    M1 values: [0]
      a^2/b^2  deg2 rank1:  M1=0  M2=  1/2  M3=  1/2
      a^3/b^3  deg3 rank2:  M1=0  M2=  1/2  M3=  1/3
      a^4/b^4  deg4 rank3:  M1=0  M2=  1/3  M3=  1/4
      a^5/b^5  deg5 rank4:  M1=0  M2=  1/3  M3=  1/5
      a^6/b^6  deg6 rank5:  M1=0  M2=  1/4  M3=  1/6

  mixed  (15 formulas)
    M1 values: [0]
      a^1b^1   deg2:  M2=1/2  M3=0      a^2b^2  deg4:  M2=1/5  M3=0
      a^1b^2   deg3:  M2=1/3  M3=0      a^3b^1  deg4:  M2=1/4  M3=0
      a^2b^1   deg3:  M2=1/3  M3=0      a^2b^3  deg5:  M2=1/6  M3=0
      a^1b^3   deg4:  M2=1/4  M3=0      (etc.)  a^2b^4  deg6:  M2=1/8  M3=0

--- Arm B shape check ---
  pure powers a^k:  M3 = 1/k (Lambda-like)?   True
  mixed all M3 = 0 (Lambda-like)?             True
  mixed all M2 = 0 ?                           False  (M2 mixed values: 1/2,1/3,1/4,1/5,1/6,1/8)
  M2 separates pure vs mixed?                 False
  M1 binary (only atoms innovate)?            True

======================================================================
ARM A  (classical AND, idempotent; predicted NULL/binary)
======================================================================
Lindenbaum-Tarski classes reachable by AND-closure from {p,q}: 3
    class [p    ] rank0:  M1=1  M2=    1  M3=    1
    class [q    ] rank0:  M1=1  M2=    1  M3=    1
    class [p&q  ] rank1:  M1=0  M2=  1/2  M3=    0
--- Arm A shape check ---
  M1 binary (only atoms innovate)?  True
  any graded power ladder?           NO — idempotence collapses powers (no g^k for k>=2 exists)

======================================================================
SUMMARY
======================================================================
  M1 (quantity-free): BINARY in both arms — atoms 1, all composites 0.
  M2 (quantity-free): Arm B graded but NOT Lambda (mixed != 0; pure/mixed not separated);
                      Arm A trivial (one composite at 1/2).
  M3 (boundary control, circular): Arm B = clean Lambda (1/k powers, 0 mixed);
                      Arm A = binary (idempotence destroys powers).
```

---

*End of Note A (draft). Sections 1–8 complete, with follow-up tests F3 and F1 in the appendix — F3 promoting the events-not-potentials refinement into §5, F1 sharpening the §7 park. The appendix carries every number quoted in the prose. Leads: §5 killed (F3-refined), §7 parked (F1-sharpened). Nothing here is promoted to the project spine.*
