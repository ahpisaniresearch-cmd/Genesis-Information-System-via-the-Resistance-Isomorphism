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

# Hidden Nesting, the Fluctuation Probe & Indeterminate Forms
## Convergent resistance series, quantized erasure, and the cumulant ladder as a probe into hidden depth

**Alexander Pisani & Claude (Anthropic)** · July 2026 · companion note to the Genesis Information Project (draft, in progress)

**Status.** Draft complete — sections 1–8 with a verbatim appendix. Two Leads resolved: both parked (§6 the cumulant ladder, §7 the primordial indeterminate). Nothing here is promoted to the project spine; findings remain in this companion note unless later judged load-bearing to the core narrative.

---

## 1. Scope and boundaries

**What this note does.** This note follows a single thread through four rooms.

- *Hidden nesting.* An infinite cascade of conditional erasures can carry exactly the same expected heat as a single hard erasure, so an ensemble mean can conceal unbounded machinery.
- *Quantization.* A hard erasure event comes in integer multiples of the genesis bit `ln 2`, so a single-run heat reading bounds the number of erasure events — *actual* erasures cannot hide.
- *The fluctuation probe.* Where the mean is blind, the variance is not, and each higher cumulant is a further handle on the hidden depth — a ladder.
- *Indeterminate forms.* The classical indeterminate forms of analysis are the same shadow-underdetermination surfacing inside the calculus — a value that fails to fix its process.

The organizing claim: **convergent resistance series are the barrier's hiding mechanism**, and the probe's route into what they hide is the cumulant ladder. **[Reading]**

**Regime 1 and Regime 2 — this note is the distinction at work.** The project separates two stances. *Regime 1* runs forward from genesis: a quantized unfolding, structure arriving one genesis bit at a time, events discrete and integer. *Regime 2* works backward from probe interception: realized states assumed, ensembles formed, averages taken — and the continuum appears only here, as a construct of averaging. This note stages the two directly against each other: the hiding experiment's cascade is a stream of discrete, integer-cost events (the Regime-1 face), while every heat *reading* — mean, variance, higher cumulants — is a Regime-2 ensemble quantity. The banked one-liner, following the framework: *the continuum is probe-manufactured; the system's own ledger is integer multiples of the genesis bit.* Everything measured in this note is Regime 2; the "machines" are shadow-facing models of erasure processes, not a view behind the barrier.

**Exact identities are not the content.** Several results here are exact arithmetic facts — `ln 2 = Σ_{n≥1} 1/(n·2^n)`, the cascade variance `(2/3)·ln²2`, the eight indeterminate forms. These are true by computation, not discoveries; as in the companion note, where a ledger closes the closure is the entropy chain rule and is guaranteed. The empirical content is always what these quantities *reveal* — that a mean cannot separate one erasure from an infinite cascade, that a variance can, that path-dependence picks out exactly the classical indeterminates. The identities are the instruments, not the findings.

**Boundaries.**

1. **No open-problem leverage.** Nothing here bears on any open problem — no Riemann Hypothesis, Goldbach, or P-versus-NP relevance, and no proof-discovery mechanism. The convergent series that emblematises the hiding mechanism — `Ω = Σ 2^{−|p|}`, finite-looking magnitude over unbounded depth — is cited, not leveraged.
2. **The machines are illustrative.** The two-machine constructions are toy models chosen to make a conceptual point exactly computable; they are not physical claims, and no thermodynamic measurement is asserted.
3. **Precision convention.** A reported `0.000e+00` means agreement to within double-precision arithmetic, not a proof of exact equality; genuinely exact identities are flagged as such and checked symbolically or in exact rationals where it matters.
4. **Cartography, not evidence (as in the companion note).** Everything is Regime-2 and shadow-side; the pole arithmetic of {0, 1, ∞} and the erasure machines say nothing about whether the genesis system holds beyond the axioms that posit it.

**Grading.** Every claim carries an inline grade — **[Fact]**, **[Reading]**, **[Lead]** — as throughout the project. This note carries two Leads: the *cumulant ladder* (whether matching `d` cumulants is what depth-`d` hiding costs) and the *primordial indeterminate* (whether the pre-distinction state admits a formal residue in the pole-arithmetic frame). Both are resolved — promoted, killed, or explicitly parked — before the note closes.

---

## 2. Indeterminate forms as the discontinuity set of pole arithmetic

**The setup.** Take three distinguished points — the poles `{0, 1, ∞}` — and the four operations `{−, ×, ÷, ^}`. The poles are the framework's own distinguished points: the lattice bottom and top, `0` and `∞` reciprocal images of one another, `1` the unit between them; as Möbius points `{0, 1, ∞}` is the orbit of the anharmonic (S₃) group generated by `z ↦ 1/z` and `z ↦ 1−z`. **[Reading** for the framework identification; the S₃ orbit is classical.**]**

**The test.** For each ordered triple (pole, op, pole), approach the pole values along several path families — polynomial rates (`t`, `t²`, …) and exponential rates (`e^{−1/t}`, `e^{1/t}`) — and take exact symbolic limits. A combination is **path-dependent** exactly when distinct paths give distinct limits: the endpoint value fails to determine the process. The exponential families are essential — without them `0^0` and `∞^0` each collapse to the single limit `1` and would read as determinate. Everything here is Regime-2 and shadow-side: limits of realised paths, nothing at the genesis layer.

**Result. [Fact]** The path-dependent set is exactly the eight classical indeterminate forms — `∞−∞`, `0·∞`, `∞·0`, `0/0`, `∞/∞`, `0^0`, `1^∞`, `∞^0` — and nothing else (`Exact match: True`). Every one of the other 28 combinations returns a single value along every path. Path-dependence, defined with no prior notion of "indeterminate," reproduces the classical list on the nose.

**Two archetypes (by hand). [Fact]** Treating multiplication as commutative leaves seven distinct forms, and these reduce to two. Division by a pole is multiplication by its reciprocal, so `0/0 = 0·∞` and `∞/∞ = ∞·0`; and each exponential form has an exponent that is itself a `0·∞` product, since `a^b = e^{b·ln a}` gives exponents `0·ln 0` (for `0^0`), `∞·ln 1` (for `1^∞`), and `0·ln ∞` (for `∞^0`). Every multiplicative and exponential indeterminate therefore reduces to the single archetype **`0·∞`**, leaving **`∞−∞`** as the one irreducibly additive archetype. Two archetypes, not eight.

**Under the resistance map. [Fact, by hand → Reading]** Send each value to its resistance, `r = −ln v`. The three poles become `0 ↦ +∞`, `1 ↦ 0`, `∞ ↦ −∞`, and multiplication of values becomes addition of resistances. The multiplicative archetype `0·∞` then reads, in resistance coordinates, as `(+∞) + (−∞) = ∞−∞` — the difference of two infinite forgetting-costs; and the additive archetype `∞−∞` already wears that shape. So in resistance coordinates the two archetypes are one **[Fact, by hand]**, and the reading follows: **an indeterminate form is a contest between two infinite resistances that the value alone cannot settle.** What settles it is the *rate* at which each side approaches — and l'Hôpital's rule resolves the form by consulting exactly those rates, which is to say it reads the ledger. (Orders of infinity: du Bois-Reymond, Hardy.) **[Reading]**

**The shadow point.** The value is the shadow; the path is the process. An indeterminate form is a place where the shadow underdetermines the process — where the endpoint (`0`, `1`, or `∞`) leaves the outcome open and only the rate structure behind it decides. This is the same underdetermination the project reads at the barrier, now surfacing *inside* classical analysis rather than behind it. **[Reading]**

---

## 3. Quantization of hard erasure

**The claim.** A hard erasure event is the collapse of at least two distinguishable states onto one — fan-in ≥ 2 — so its cost is at least `ln 2`, one genesis bit. Erasure is therefore quantized: in the genesis-bit machines below, any run deposits heat in integer multiples of `ln 2`, and `ln 2` (fan-in 2) is the minimum quantum in general, since a fan-in-`k` erasure costs `ln k ≥ ln 2`. **[Fact]**

**The consequence.** Because heat comes in whole genesis bits, a single-run heat reading `H` bounds the number of hard-erasure events on that run: at most `⌊H / ln 2⌋` of them. An infinite cascade of *actual* erasures cannot hide behind a finite reading — each event costs a full bit, and the bits add up. **[Fact]**

**Verification.** On the support of the cascade machine's exact distribution, every outcome's heat is an integer multiple of `ln 2` (support check: `True`). The point is conceptual; the check is the one line that secures it. **[Fact]**

**The point (forward pointer).** This is the wall the next sections press against. Actual erasure events are rigidly countable from a single run. What *can* hide — as §4 shows — is not an actual erasure but a *conditional* one, whose expected cost can be made arbitrarily small; and what exposes the hiding — as §5 shows — is not the mean but the variance. **[Reading]**

---

## 4. The series anchor and amortized hiding

**The series anchor. [Fact]** The genesis bit is itself an infinite sum of vanishing pieces:
`ln 2 = Σ_{n≥1} 1/(n · 2^n)`,
verified to `|diff| = 0.000e+00` over 200 terms. This is the Mercator series `−ln(1−x) = Σ x^n/n` at `x = 1/2` — a convergent *resistance* series, a finite resistance assembled from unboundedly many terms. It is the hiding mechanism of §1 in its barest arithmetic form: finite magnitude over unbounded depth.

**Two machines, one mean. [Fact]** Put the mechanism to work.

- *Machine A* performs a single hard erasure of the genesis bit: heat `= ln 2` on every run, variance 0.
- *Machine B* runs an infinite cascade of *conditional* erasures: stage `k` fires — erasing one genesis bit — with probability `2^{−k}`, independently. Its expected number of firings is `Σ 2^{−k} = 1`, so its expected heat is `ln 2` as well.

Their means coincide: `E[H_B] → ln 2 = E[H_A]`, converging to deviation `0.000e+00` by 64 stages. A probe that reads only average heat cannot tell the one hard erasure from the infinite cascade.

**How the amortization works. [Fact]** The equality of means is not because the machines behave alike. On Machine B a full `P(0 erasures) → Π_{k≥1}(1 − 2^{−k}) ≈ 0.2888` of runs fire *nothing at all* — over a quarter deposit zero heat — while rare runs fire several stages. The finite mean `ln 2` is amortised out of many do-nothing runs and a thin tail of do-a-lot runs. The infinite machinery is real on any given run; it is the *averaging* that folds it into a single finite number.

**Reading.** This is how a barrier hides depth from a mean-probe. The convergent resistance series is the mechanism, and the ensemble mean is the blind instrument: reading only the average, a probe sees a finite genesis bit and cannot distinguish a single erasure from an unbounded conditional cascade behind it. The nesting is not destroyed — it is amortised. **[Reading]**

---

## 5. The fluctuation probe

**The mean was blind; the variance is not. [Fact]** The two machines of §4 share a mean but not a variance.

- Machine A (one hard erasure) is deterministic: `Var[H_A] = 0` exactly.
- Machine B (the infinite conditional cascade) fluctuates: `Var[H_B] → (2/3)·ln²2 ≈ 0.3203`, computed exactly by dynamic programming over the cascade's distribution — no sampling.

The first cumulant, the mean, cannot separate the machines — both are `ln 2`. The second cumulant, the variance, separates them cleanly — `0` against `(2/3)·ln²2`. The probe that was blind at first order sees at second order.

**Where the number comes from. [Fact]** Heat is `m · ln 2` for an integer firing-count `m`, so `Var[H] = ln²2 · Var[m]`. For independent stages with `P(fire at k) = 2^{−k}`, `Var[m] = Σ_{k≥1} 2^{−k}(1 − 2^{−k}) = Σ 2^{−k} − Σ 4^{−k} = 1 − 1/3 = 2/3`. Hence `Var[H_B] = (2/3)·ln²2`, matching the DP to the printed precision.

**Reading — the fluctuation is the granularity showing through.** A nonzero variance is the discreteness of §3 made visible. A single deterministic erasure has no spread; the cascade's spread is exactly the ensemble's uncertainty about *how many* integer bits fired. So the second cumulant does two things at once: it exposes the hidden nesting the mean amortised away, and it does so precisely because erasure is quantized — there is an integer count to be uncertain about. The mean sees the total; the variance sees that the total was assembled from discrete, countable events. **[Reading]**

**Forward pointer (to §6).** If the first cumulant is blind and the second sees, it is natural to ask whether each further cumulant is a further rung — whether matching `d` cumulants is what it costs to hide depth `d`. That is the cumulant-ladder Lead, tested next. **[Lead — stated, resolved in §6]**

---

## 6. A parked Lead: the cumulant ladder

**The Lead.** §5 gave the first rung — the mean is blind, the variance sees. The ladder Lead generalises: for each depth `d`, do erasure machines exist that agree on cumulants `κ₁…κ_d` and first differ at `κ_{d+1}`, so an order-`d` probe (one reading the first `d` cumulants) is fooled and the `(d+1)`-th cumulant is the rung that exposes it — and does climbing to depth `d` carry a cost that grows with `d`? Promotion was reserved for the case where the erasure-cascade structure adds something moment theory does not; anything explicable by classical moment theory parks. Expectation, disclosed in advance: park.

**Closed-form cascade cumulants. [Fact]** The genesis-bit cascade — independent stages `k`, stage `k` firing with probability `2^{−k}` — has exact cumulants, from `κ_j = Σ_k κ_j(Bernoulli(2^{−k}))` and `Σ_k 2^{−jk} = 1/(2^j − 1)`:

`κ₁ = 1,  κ₂ = 2/3,  κ₃ = 2/7,  κ₄ = −2/105,  κ₅ = −18/217,  κ₆ = 58/651`,

with denominators products of `(2^j − 1)`. The second cumulant recovers §5 exactly: `κ₂·ln²2 = (2/3)·ln²2`, the heat variance. This clean sequence is worth banking on its own.

**The ladder exists. [Fact, classical]** For `d = 1…4` there are distribution pairs — built exactly in rationals by the finite-difference perturbation `w_i = (−1)^i C(d+1, i)` on `{0…d+1}`, whose moments `0…d` vanish and whose `(d+1)`-th does not — that agree on `κ₁…κ_d` and differ at `κ_{d+1}`. An order-`d` probe cannot separate them; the `(d+1)`-th cumulant does. This is standard moment theory: cumulants and moments are interconvertible, and moment-matched distributions differing beyond a fixed order are classical.

**The cost, in two currencies. [Fact]** To hide depth `d` — to exhibit a distinct pair matching `κ₁…κ_d` — costs:

| currency | minimal size | source |
|---|---|---|
| free distribution (support points) | `⌈d/2⌉ + 1` | Gauss quadrature (`s` points fix `2s − 1` moments) |
| genesis-bit cascade (stages) | `d + 1` | Newton's identities (a size-`s` multiset is fixed by its first `s` power sums) |

The two coincide at `d = 1` (both 2) and **diverge for `d ≥ 2`**: the cascade costs `d + 1` stages against the free distribution's `⌈d/2⌉ + 1` support points. Hiding depth `d` in genuine independent stages is strictly more expensive than in a free distribution, because the cascade stages are rigid — a sum of independent Bernoullis (a Poisson binomial) carries fewer degrees of freedom than an arbitrary distribution on the same support.

**Verdict — parked.** The ladder is real, and the cascade cost is a clean, framework-native law: `depth d ↦ d + 1 genesis-bit stages`. But by the pre-registered criterion this parks rather than promotes. Both cost bounds are consequences of classical theory — Gauss quadrature and Newton's identities — and the cascade-vs-free divergence, clean as it is, is itself classical: the rigidity of Poisson-binomial sums, not a law beyond moment theory. What the ladder shows is the framework's arithmetic mapping cleanly onto the classical moment problem; it does not add to it. Newton's identities in cascade dress. **[Lead — parked]**

**Follow-up (F2): the heat-currency cost also parks.** §6 priced hiding in *stages* and left the framework-native heat currency unmeasured. One route was closed in advance — expected heat is `κ₁·ln 2`, equal by construction, so it cannot be the price — leaving the **concealed leg** `H(pattern | heat)`: how much of a hider's internal firing pattern stays hidden behind its heat reading. (Patterns determine heat, so this is the chain rule, not a finding; the content is how it scales.) Across matched `(d+1)`-stage machines for `d = 1…5` (κ₁…κ_d matched, κ_{d+1} differing) and two canonical cascades computed exactly, the concealed leg `C = H(pattern) − H(heat)` is dominated by `H(pattern) = Σ_k h(q_k)`, while `H(heat)` grows only logarithmically. Normalising against the configuration count (`C / (s·ln 2)`) returns nothing but the stages' own entropy budget: it climbs toward 1 for fair-coin stages (`q_k = ½`) and *falls toward 0* for the genesis-bit cascade (`q_k = 2^{−k}`), whose deep stages fire too rarely to carry entropy; the concealed fraction `C / H(pattern)` tells the same story. **[Fact]** The heat-currency cost of hiding reduces to stage-entropy bookkeeping — not a law beyond the stage count — so §6's park stands unimproved.

Two facts and a reading fall out. **Free-support machines have no concealed leg at all**: their outcome *is* the count *is* the heat, so `C ≡ 0`; concealment is a cascade-specific phenomenon, and the currency matters. **[Fact]** Matching more cumulants **squeezes the hider toward the reference**: the total-variation distance between their heat distributions falls geometrically with `d` (`0.020, 0.040, 0.008, 0.0016, 0.00032` across `d = 1…5`). **[Fact]** And, tying back to §§4–5: the genesis-bit cascade — Machine B itself — has a **bounded** concealed leg even at infinite depth. Its deep stages fire so rarely that its total *concealable* information saturates; Machine B hides its depth from the mean, but there is only a finite amount it can ever hide. **[Reading]** (Appendix F2.)

---

## 7. A parked Lead: the primordial indeterminate

**The Lead.** §2 read every indeterminate form as a contest between two infinite resistances that the value cannot settle. This Lead asks whether the genesis event itself — the first distinction emerging from non-distinction — carries such a form: does the pre-distinction state admit a formal residue in the pole-arithmetic frame?

**The formal residue. [Reading]** Under the resistance map `r = −ln v` the reciprocal poles `0` and `∞` sit at `+∞` and `−∞`, and `1` — the unit, zero resistance — sits between them. Non-distinction is the absence of any resistance difference: the state in which the two infinite poles have not yet separated into a determinate relation. That is exactly the archetype §2 isolated — `0·∞`, equivalently `∞−∞` in resistance coordinates. So the structure of §2 extends, of its own accord, to a *form of the genesis event*: the first distinction is the resolution of a primordial `0·∞` into a determinate value, and the rate that resolves it — l'Hôpital reading the ledger — is that first distinction being recorded. The indeterminate form is the "before"; the recorded value is the "after"; the ledger entry is the resolution.

**Why this is a residue and not a result.** Two things keep this a Reading, held inside the axioms.

- *The pre-distinction state is behind the barrier.* By the probe axiom, the genesis layer lies beyond any probe, and the pre-distinction state is the least probeable thing in the framework. To *assert* that it wears the form `0·∞` — that this is its structure, verifiable — would be a claim about what lies behind the barrier beyond the axioms that posit it, which the note's boundaries forbid. What we have is a structural extension of the shadow-side indeterminate-forms picture, offered as an analogy the frame supports, not a fact established about the layer.
- *An indeterminate form is, by definition, unresolved.* The primordial form's whole content is that it does not fix its own value; naming it does not resolve it, and could not, without supplying the very rate-structure — the ledger — whose arrival *is* genesis. The residue names the shape of the question, not an answer.

**Verdict — parked, within the axioms.** The formal residue is real as a structural reading: the pole-arithmetic frame of §2 reaches naturally to a form for the genesis event, `0·∞`, resolved into a value by the first ledger entry. It is held as a **[Reading]** and parked — consistent with the framework's posit and claiming nothing about the layer beyond it. It is the frame's own account of where the indeterminate-forms story points when extended inward to genesis, not a probe of what cannot be probed. **[Lead — parked]**

---

## 8. Regimes, honest tensions, and what the note establishes

**The regime distinction, as the note ran it.** This note was the Regime-1/Regime-2 distinction at work. Forward from genesis (Regime 1): erasure events are discrete and integer, one genesis bit at a time — §3's quantization is that face, and it makes actual erasures rigidly countable from a single run. Backward from the probe (Regime 2): every heat *reading* is an ensemble average, and it is at this level that the hiding (§4) and its undoing (§5) live. The mean, a Regime-2 quantity, cannot see the Regime-1 granularity; the variance, also Regime-2, can — because the granularity is integer, there is a whole number to be uncertain about. The continuum is probe-manufactured; the system's own ledger is integer multiples of the genesis bit.

**The tensions, collected.**

- *Exact identities are instruments, not findings.* `ln 2 = Σ 1/(n·2^n)`, `(2/3)·ln²2`, the eight indeterminate forms, the cumulant sequence — all exact by computation. The content is what they reveal — a mean cannot separate one erasure from an infinite cascade, a variance can, path-dependence picks out the classical indeterminates — never the identities themselves.
- *The machines are toy constructions.* Machines A and B are chosen to make a conceptual point exactly computable; no physical or thermodynamic measurement is asserted.
- *Precision.* A reported `0.000e+00` means double-precision agreement; the genuinely exact results are the ones checked in rationals or symbolically — the cumulants, the ladder, and the indeterminate-forms match.
- *§6 parked.* The cumulant ladder is classical moment theory — Newton's identities and Gauss quadrature; the cascade cost law is clean but adds nothing beyond them.
- *§7 parked, within the axioms.* The primordial `0·∞` is a structural reading the frame offers, not a claim about the pre-distinction state, which sits behind the barrier by the probe axiom.
- *Cartography, not evidence.* Everything is Regime-2 and shadow-side; the pole arithmetic and the erasure machines say nothing about whether the genesis system holds beyond the axioms that posit it.

**What the note establishes.** The note's Facts are exact and modest. Erasure is quantized in genesis bits, so actual events are countable from a single run (§3); an infinite conditional cascade shares its mean with a single erasure (§4); the variance separates them, exactly `(2/3)·ln²2` (§5); the cascade has closed-form cumulants (§6); and — the result that stands most on its own — path-dependence over the poles `{0, 1, ∞}`, defined with no prior notion of indeterminacy, reproduces exactly the eight classical indeterminate forms, which collapse under the resistance map to a single archetype: a contest between two infinite forgetting-costs (§2). The Readings that frame these — convergent resistance series as the barrier's hiding mechanism, the cumulant ladder as the probe's route in, the indeterminate form as shadow-underdetermination surfacing inside analysis, the primordial `0·∞` as the frame's form for genesis — are held as Readings; the two Leads are parked; and no claim is made for or against the genesis system beyond the axioms that posit it. The same discipline, and the same limits, as the rest of the project.

**Citations.**

- *Thermodynamics of computation.* The erasure cost is Landauer (1961); the cost-free status of copying is Bennett (1973); the fluctuation relation connecting nonequilibrium work to free-energy differences is Jarzynski (1997), the project's grounding for reading fluctuations physically.
- *Information theory and the moment problem.* Entropy and conditional entropy are Shannon (1948); cumulants, the moment problem, Gauss quadrature, and Newton's identities on power sums and elementary symmetric functions are classical.
- *Orders of infinity.* The rates that resolve indeterminate forms trace to du Bois-Reymond and to Hardy, *Orders of Infinity* (1910); l'Hôpital's rule is classical.
- *The convergent-series emblem.* Chaitin's Ω (the halting probability) is the emblem of finite magnitude over unbounded depth; `ln 2 = Σ 1/(n·2^n)` is the Mercator series at `x = 1/2`.
- *Framework.* The resistance isomorphism `Ω(1/n) = ln n`, the genesis bit `ln 2`, the Regime-1/Regime-2 distinction, and the two-legged ledger are developed in the project's Papers 1–9 and companion notes, including the companion "Proofs on the Ledger."

---

## Appendix — verbatim script outputs

*Built incrementally, one block per experimental step; every number in the prose above appears here.*

### B2 · `indeterminate_poles.py`

```
   a op     b   limits along paths
------------------------------------------------------------
   0  -     0   determinate    ['0']
   0  -     1   determinate    ['-1']
   0  -   inf   determinate    ['-oo']
   0  *     0   determinate    ['0']
   0  *     1   determinate    ['0']
   0  *   inf   INDETERMINATE  ['0', '1', 'oo']
   0  /     0   INDETERMINATE  ['0', '1', 'oo']
   0  /     1   determinate    ['0']
   0  /   inf   determinate    ['0']
   0  ^     0   INDETERMINATE  ['1', 'exp(-1)']
   0  ^     1   determinate    ['0']
   0  ^   inf   determinate    ['0']
   1  -     0   determinate    ['1']
   1  -     1   determinate    ['0']
   1  -   inf   determinate    ['-oo']
   1  *     0   determinate    ['0']
   1  *     1   determinate    ['1']
   1  *   inf   determinate    ['oo']
   1  /     0   determinate    ['oo']
   1  /     1   determinate    ['1']
   1  /   inf   determinate    ['0']
   1  ^     0   determinate    ['1']
   1  ^     1   determinate    ['1']
   1  ^   inf   INDETERMINATE  ['0', 'E', 'exp(-1)', 'oo']
 inf  -     0   determinate    ['oo']
 inf  -     1   determinate    ['oo']
 inf  -   inf   INDETERMINATE  ['-oo', '0', 'oo']
 inf  *     0   INDETERMINATE  ['0', '1', 'oo']
 inf  *     1   determinate    ['oo']
 inf  *   inf   determinate    ['oo']
 inf  /     0   determinate    ['oo']
 inf  /     1   determinate    ['oo']
 inf  /   inf   INDETERMINATE  ['0', '1', 'oo']
 inf  ^     0   INDETERMINATE  ['1', 'E']
 inf  ^     1   determinate    ['oo']
 inf  ^   inf   determinate    ['oo']

Path-dependent set found: [('0', '*', 'inf'), ('0', '/', '0'), ('0', '^', '0'), ('1', '^', 'inf'), ('inf', '*', '0'), ('inf', '-', 'inf'), ('inf', '/', 'inf'), ('inf', '^', '0')]
Classical indeterminate:  [('0', '*', 'inf'), ('0', '/', '0'), ('0', '^', '0'), ('1', '^', 'inf'), ('inf', '*', '0'), ('inf', '-', 'inf'), ('inf', '/', 'inf'), ('inf', '^', '0')]
Exact match: True
```

### B3–B5 · `heat_hiding_fluctuations.py` (single run; sliced across §§3–5)

This one run supplies the quantization support check (§3), the series anchor and cascade means (§4), and the fluctuation/variance results (§5).

```
(1) sum 1/(n 2^n) = 0.693147180559945;  ln 2 = 0.693147180559945;  |diff| = 0.000e+00

(2)+(4) Machine B cascade, exact (heat = m * ln2 per run):
 stages K         E[H]     E[H]-ln2       Var[H]   P(0 erasures)
        2  0.519860385   -1.733e-01  0.210198194     0.375000000
        4  0.649825482   -4.332e-02  0.290899286     0.307617188
        8  0.690439574   -2.708e-03  0.318427683     0.289919118
       16  0.693136604   -1.058e-05  0.320294678     0.288792502
       32  0.693147180   -1.614e-10  0.320302009     0.288788095
       64  0.693147181    0.000e+00  0.320302009     0.288788095

Predicted Var limit = ln2^2 * (1 - 1/3) = 0.320302009  (= (2/3) ln2^2 = 0.320302009)
Machine A:  E[H] = 0.693147181,  Var[H] = 0 exactly

(3) Every run's heat is an integer multiple of ln2 (support check): True
    => a single-run heat reading H bounds the hard-erasure count by floor(H/ln2);
       only the ENSEMBLE MEAN is blind to the nesting; the variance is not.
```

### B6 · cumulant ladder (self-authored, PID-named; **parked Lead**)

`κ₂` cross-check (`κ₂·ln²2 = 0.320302009`) reproduces §5's heat variance, tying the cumulant computation to the fluctuation result.

```
(1) EXACT cascade cumulants  (kappa_j, from sum_k Bernoulli(2^-k)):
    kappa_1 =        1  = +1.000000000
    kappa_2 =      2/3  = +0.666666667
    kappa_3 =      2/7  = +0.285714286
    kappa_4 =   -2/105  = -0.019047619
    kappa_5 =  -18/217  = -0.082949309
    kappa_6 =   58/651  = +0.089093702
    cross-check: kappa_1=1.000000 (=1), kappa_2*ln2^2 = 0.320302009  (heat variance (2/3)ln2^2)

(2) Ladder exists (EXACT, general distributions on {0..d+1}):
    d=1: kappa_1..kappa_1 match: True;  kappa_2 differs: True  (kP[2]=    3/4, kQ[2]=    1/4)
    d=2: kappa_1..kappa_2 match: True;  kappa_3 differs: True  (kP[3]=   -3/8, kQ[3]=    3/8)
    d=3: kappa_1..kappa_3 match: True;  kappa_4 differs: True  (kP[4]=    1/4, kQ[4]=   -5/4)
    d=4: kappa_1..kappa_4 match: True;  kappa_5 differs: True  (kP[5]=  -15/8, kQ[5]=   15/8)

(3) Cost of hiding depth d:  free-support bound  vs  cascade-stage bound
     d s_free=ceil(d/2)+1  s_cascade=d+1     distinct (d+1)-stage pair matches k1..kd?
     1                  2              2        True   (d-stage pair exists: False)
     2                  2              3        True   (d-stage pair exists: False)
     3                  3              4        True   (d-stage pair exists: False)
     4                  3              5        True   (d-stage pair exists: False)
    minimality of s_cascade=d+1 is Newton's identities (size-s multiset fixed by P_1..P_s);
    s_free=ceil(d/2)+1 is Gauss quadrature (s points fix 2s-1 moments). Both are classical.
```

### F2 · concealed-leg / heat-currency cost (self-authored, PID-named; **parked, refines §6**)

Concealed leg `C = H(pattern) − H(heat)`, in nats. Distributions exact-rational where probabilities are rational (Part 1); matched pairs numerical (Part 2). Normalised concealed leg reduces to stage-entropy bookkeeping; free-support machines have `C = 0`; the hider–reference TV distance falls with `d`.

```
==========================================================================
PART 1  Canonical cascades, exact rational distributions
==========================================================================
family           s  H(pattern)   H(heat)         C  C/(s ln2) phi=C/Hpat
genesis 2^-k     2     1.25548   0.97431   0.28117    0.20282    0.22395
genesis 2^-k     3     1.63225   1.08442   0.54783    0.26345    0.33563
genesis 2^-k     4     1.86604   1.13286   0.73318    0.26444    0.39291
genesis 2^-k     5     2.00510   1.15584   0.84926    0.24505    0.42355
genesis 2^-k     6     2.08559   1.16707   0.91852    0.22086    0.44041
fair-coin 1/2    2     1.38629   1.03972   0.34657    0.25000    0.25000
fair-coin 1/2    3     2.07944   1.25548   0.82396    0.39624    0.39624
fair-coin 1/2    4     2.77259   1.40753   1.36506    0.49234    0.49234
fair-coin 1/2    5     3.46574   1.52367   1.94207    0.56036    0.56036
fair-coin 1/2    6     4.15888   1.61736   2.54152    0.61111    0.61111

==========================================================================
PART 2  B6 matched pairs: (d+1)-stage reference vs hider matching kappa_1..kappa_d
==========================================================================
 d stages kmatch kdiff    C_ref    C_hid Cref/(s ln2)  phi_ref TV(ref,hid)
 1      2   True  True   0.1521   0.1699       0.1097   0.1520    0.020000
 2      3   True  True   0.5611   0.5633       0.2698   0.3313    0.040000
 3      4   True  True   1.0433   1.0501       0.3763   0.4446    0.008000
 4      5   True  True   1.5602   1.5602       0.4502   0.5220    0.001600
 5      6   True  True   2.0985   2.0986       0.5046   0.5787    0.000320

==========================================================================
PART 3  Free-support hider contrast
==========================================================================
  d=1: free-support machine needs ceil(d/2)+1 = 2 points;  outcome = count = heat  ->  H(pattern|heat) = 0  (no concealed leg)
  d=2: free-support machine needs ceil(d/2)+1 = 2 points;  outcome = count = heat  ->  H(pattern|heat) = 0  (no concealed leg)
  d=3: free-support machine needs ceil(d/2)+1 = 3 points;  outcome = count = heat  ->  H(pattern|heat) = 0  (no concealed leg)
  d=4: free-support machine needs ceil(d/2)+1 = 3 points;  outcome = count = heat  ->  H(pattern|heat) = 0  (no concealed leg)
  d=5: free-support machine needs ceil(d/2)+1 = 4 points;  outcome = count = heat  ->  H(pattern|heat) = 0  (no concealed leg)

==========================================================================
READINGS
==========================================================================
  C is dominated by H(pattern)=sum h(q_k); H(heat)<=log(s+1) grows only logarithmically.
  C/(s ln2) -> the average stage entropy / ln2 (fair-coin -> ~1; genesis -> ->0 as it saturates).
  => normalized concealed leg reduces to stage-count bookkeeping. Free-support C=0.
```

---

*End of Note B (draft). Sections 1–8 complete, with follow-up test F2 (appendix) refining the §6 park in the heat currency. The appendix carries every number quoted in the prose. Two Leads parked — §6 (F2-refined) and §7. Nothing here is promoted to the project spine.*
