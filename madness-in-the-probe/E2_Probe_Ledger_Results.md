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

# E2 Results — The Probe's Own Ledger: Balanced, or Net Stored?

**Madness in the Probe sub-programme · design experiment · banking run · July 2026**
**Alexander Pisani & Claude (Anthropic)**

---

## Status

**ALL 22 COMMITTED CHECKS PASSED. 6 report-only / labelled items reported. Banking run complete.**

The pre-registered prediction — *all committed measures pass; the identities are classical
and the deliverable is the resolution plus the three priced quantities* — held in full. No
committed bar was moved; no result was patched. The originating question is answered.

**The resolution.** *Balanced, or net stored?* resolves as a **conservation frontier**. On
the probe's own ledger the ingested information of a stream is split, with no residue,
between what the probe **pays to erase** and what it **retains in storage** — and the split
is the free parameter. There is no regime in which the ledger fails to close and no regime in
which it stores "net energy" beyond the information it took in: storage is exactly memory
growth, payment is exactly memory bound, and the two poles are the **summarizer** (erase
everything, pay the full rate, store nothing) and the **hoarder** (keep everything reversibly,
pay nothing, store the full rate). What knowledge changes is not *whether* it balances but the
*rate*: a learned model is a discount on the price of forgetting worth exactly the redundancy
it captures, and a wrong model is a surcharge of exactly the KL divergence.

Implemented fresh for E2 only. No prior script was consulted or reused; no other corpus
document was read. The pre-run pins C1–C4 (brief §6) are honoured exactly. Implementation
choices within the implementing instance's remit are documented in §Reproducibility and §Notes.

---

## Reproducibility block

| Item | Value |
|---|---|
| Script | `521_e2_ledger.py` (fresh; PID-prefixed) |
| Recorded seed | `20260710` |
| Runtime PID (this run) | `565` |
| Wall-clock runtime | ~1.4 s |
| Exit code | `0` (all committed checks passed) |
| Python | 3.12.3 |
| numpy | 2.4.4 |
| mpmath | 1.3.0 |
| Precision | float64 `math.lgamma` + `math.fsum` throughout; one **mpmath dps=50** cross-check of the M1 identity at n=100 |
| Stream length `T` | 100,000 (i.i.d. from `p`, one seeded stream shared by M1-realized / M2 / M3 / M4) |
| Markov stream (M6) | 100,000 from a separate seed (`SEED+1`) |
| M2 memory bound | 16 count records (end-of-run inventory reported as an explicit storage line) |

**Precision justification (why float64 suffices here).** Every quantity is an entropy or a
log-count in nats, magnitude ≤ ~10⁴ (largest is `n·H` at n=6400 ≈ 7763). float64 carries
~15–16 significant digits, so absolute error is ≲10⁻¹¹ even at the largest scale; `fsum`
removes accumulation error. The tightest bar (M1 at 10⁻⁹) therefore clears by ≥4 orders. This
is confirmed independently: recomputing the M1 identity at n=100 in mpmath (dps=50) gives
residual **−1.09×10⁻⁴⁷**, i.e. the float64 residual (~10⁻¹²) is an honest float artifact, not
a masked violation. Charges use the same `lgamma`-based coefficient wherever `op-F` and
`op-D` must cancel, so the route-equality (A1) closes to machine epsilon.

**Pre-registered bars** are copied verbatim into the script header (before any check was
written) and are reproduced with actuals below.

### Implementation choices (documented, within remit / ratified in §6)

- **Learned model = pinned dyadic `p`** everywhere (C2); tolls are averages of `−ln p(x)`
  over the realized stream, never an empirical re-fit.
- **op-D on a stored count record** charges `−ln P_multinomial(c)` under `p` (C1) — the
  self-information of what is still held.
- **M4** is op-R (reversible, free) + archive-or-discard of whole blocks; **op-F does not
  enter M4** (C3). Archiving = first ⌊fB⌋ blocks (representative for i.i.d.).
- **M2** memory bound = 16 records; the 16 records still held at the end are reported as an
  explicit **retained-storage line** so the conservation statement closes (C4, lead's addition).
- **H(counts)** is computed by an independent chain-rule route (binomial entropies of partial
  sums, O(n²)), **not** by subtracting `E[ln C]` from `nH` (anti-tautology, §5.3), and is
  validated against brute-force simplex enumeration at n=50 and n=100.
- **Three labelled additions**, graded separately — A1 route-equality, the enumeration
  validation, and the capacity/blank harvest — see §Implementer additions.

---

## Pre-registered bars vs actuals

| Check | Bar | Actual | Verdict |
|---|---|---|---|
| **M1** conservation n=50 | \|nH − (H(counts) + E[ln C])\| ≤ 1e-9 | resid **+1.82e-12** | **PASS** |
| **M1** conservation n=100 | ″ | resid **−3.82e-12** | **PASS** |
| **M1** conservation n=200 | ″ | resid **−3.00e-11** | **PASS** |
| **M1** realized n=50 | \|mean op-F − E[ln C]\|/SE ≤ 3 | z = **0.86** (B=2000) | **PASS** |
| **M1** realized n=100 | ″ | z = **0.93** (B=1000) | **PASS** |
| **M1** realized n=200 | ″ | z = **0.91** (B=500) | **PASS** |
| **M2** perpetual toll | paid erasure/sym ∈ H ± 0.02 | **1.21317** (H=1.21301, \|d\|=1.7e-4) | **PASS** |
| **M3** ignorant → ln4 | ln4 ± 0.02 | **1.38629** (exact, see note) | **PASS** |
| **M3** learned → H | H ± 0.02 | **1.21441** (\|d\|=1.4e-3) | **PASS** |
| **M3** mismatched → H+KL | H+KL ± 0.02 | **1.64699** (\|d\|=7.7e-4) | **PASS** |
| **M3** ordering | learned < ignorant < mismatched | 1.2144 < 1.3863 < 1.6470 | **PASS** |
| **M4** frontier f=0 | storage+erasure = H ± 0.02 | **1.21441** | **PASS** |
| **M4** frontier f=¼,½,¾,1 | ″ | **1.21441** at every f | **PASS** |
| **M4** storage f=0 | storage = f·H ± 0.02 | **0.00000** | **PASS** |
| **M4** storage f=¼ | ″ | **0.30459** (f·H=0.30325) | **PASS** |
| **M4** storage f=½ | ″ | **0.60716** (f·H=0.60650) | **PASS** |
| **M4** storage f=¾ | ″ | **0.91021** (f·H=0.90976) | **PASS** |
| **M4** storage f=1 | ″ | **1.21441** (f·H=1.21301) | **PASS** |
| **M5** MDL slope | slope = −1.5 ± 0.05 | **−1.5038** (intercept −1.108) | **PASS** |

**Report-only / labelled additions:** M1 chain-vs-enumeration validation; M1 mpmath cross-check;
A1 route-equality; M4 capacity/blank harvest; M6 order-0-vs-order-1 gap. (Below.)

---

## Per-measure detail

### M1 — dual-accounting conservation (the non-circularity core)
The identity `nH = H(counts) + E[ln C(n;c)]` is the chain rule `H(Xⁿ) = H(counts) +
H(Xⁿ|counts)`, with the conditional equal to `E[ln (multinomial coefficient)]` because, given
counts, the block is uniform over its class (exchangeability). All three terms are computed by
**genuinely different routes**: `nH` from the closed form; `E[ln C]` from per-coordinate
binomial sums (`ln n! − Σᵢ E[ln cᵢ!]`, each `cᵢ ~ Binom(n, pᵢ)`); `H(counts)` from a chain-rule
over binomial entropies of partial sums. None is obtained by subtracting the others. The
identity held to **1.8×10⁻¹²** (n=50), **3.8×10⁻¹²** (n=100), **3.0×10⁻¹¹** (n=200) — four to
seven orders inside the 10⁻⁹ bar. The chain-rule `H(counts)` matched brute-force simplex
enumeration to **1.4×10⁻¹⁴** (n=50) and **6.4×10⁻¹⁴** (n=100), and the two independent `E[ln C]`
routes agreed to ~**4×10⁻¹²**. The mpmath (dps=50) recomputation put the identity residual at
**10⁻⁴⁷**. On the realized leg, the mean per-block op-F charge over the T-stream matched the
exact `E[ln C]` at **z = 0.86 / 0.93 / 0.91** — comfortably inside 3 SE at all three block
sizes.

### M2 — the perpetual toll (bounded probe)
The bounded probe forgets order within n=100 blocks (op-F, paying `ln C`) and discards count
records under the learned model when memory exceeds 16 records (op-D, paying `−ln P(c)`). The
**paid** erasure came to **1.21317 nats/symbol**, within **1.7×10⁻⁴** of H — inside the ±0.02
bar. The full ledger closes exactly:

> paid erasure (1.21317) + retained storage (0.00123) = **ingested rate 1.21441** = the direct
> per-symbol op-D(raw) codelength to **7×10⁻¹⁶**.

The 16 records still held at the end carry the 0.00123 nats/symbol of retained storage; the
paid toll sits below the ingested rate by exactly that inventory. The ingested rate is H up to
Monte Carlo (here +1.4×10⁻³ above H on this stream), which is why the paid toll lands a hair
*above* H rather than below — the ledger identity is exact, the relation to the theoretical
floor carries the stream's fluctuation. The universal floor (no lossless-forgetting policy pays
less than H/symbol in expectation) is **Shannon's**, cited as classical; this run measures a
policy's realized toll against it, and does **not** present the measurement as a proof of the
floor.

### M3 — the knowledge discount and the error surcharge (the experiment's teeth)
Three erasers, op-D on raw blocks of the same realized stream:

- **ignorant** (uniform protocol) → **1.38629** = ln4 (the cell capacity);
- **learned** (protocol p) → **1.21441** ≈ H;
- **mismatched** (protocol q) → **1.64699** ≈ H+KL,

with the strict ordering **learned < ignorant < mismatched** holding. The **discount** of
knowing the distribution is `ignorant − learned = 0.17189`, matching the redundancy `ln4 − H =
0.17329`. The **surcharge** of the wrong model is `mismatched − learned = 0.43258`, matching
`KL(p‖q) = 0.43322`. The teachable lands sharply: the surcharge (**0.4332**) exceeds the
redundancy (**0.1733**), so the confident wrong model costs **more than pure ignorance** —
`1.647 > 1.386`. Knowing the wrong thing is worse than knowing nothing.

### M4 — balanced-or-stored: the frontier
Whole blocks are reversibly compressed (op-R, free) and then either archived (storage) or
discarded under the learned model (op-D). Across `f ∈ {0, ¼, ½, ¾, 1}`:

| f | storage/sym | erasure/sym | sum | f·H |
|---|---|---|---|---|
| 0.00 | 0.00000 | 1.21441 | **1.21441** | 0.00000 |
| 0.25 | 0.30459 | 0.90982 | **1.21441** | 0.30325 |
| 0.50 | 0.60716 | 0.60725 | **1.21441** | 0.60650 |
| 0.75 | 0.91021 | 0.30419 | **1.21441** | 0.90976 |
| 1.00 | 1.21441 | 0.00000 | **1.21441** | 1.21301 |

The frontier `storage + erasure` is the ingested rate at **every** f — conservation is
f-independent, which *is* the content: no matter how the probe splits keep-vs-discard, the
ledger sums to what it took in. Storage tracks `f·H` (within 1.3×10⁻³) and the two poles are
realized cleanly — summarizer at f=0 (pays H, stores 0) and hoarder at f=1 (stores H, pays 0).

### M5 — the model's residue (the MDL term)
The exact `E[ln C(n;c)] − nH` was computed for n from 50 to 6400 and fit against `ln n`:
slope **−1.5038**, dead on the pinned `−(|A|−1)/2 = −1.5` and inside ±0.05. The per-doubling
decrements converge monotonically to `−1.5·ln2 = −1.0397` (−1.0516 → −1.0451 → −1.0423 →
−1.0410 → −1.0404 → −1.0400 → −1.0399), the clean signature of the Rissanen/MDL parametric term.
What op-F retains — the counts — is exactly what its charge falls short of `nH` by, and that
permanent residue of n symbols grows as `(k−1)/2 · ln n`. What survives forgetting the details
is the model, logarithmically.

### M6 — Markov extension (report-only, no bar, no grade)
Sticky doubly-stochastic chain (`P_stay=0.7`, else `0.1`; stationary π uniform, verified). The
**order-0** learned toll (marginal π) was **1.38629** = ln4; the **order-1** learned toll
(transition) was **0.93641**, estimating the entropy rate `H(0.7,0.1,0.1,0.1) = 0.94045`. The
gap **0.44989** reproduces the adjacent-symbol mutual information `ln4 − H(row) = 0.445846`
(the ~4×10⁻³ excess is Monte Carlo on the order-1 estimate). The discount of M3 extends to
temporal structure: a higher-order model lowers the toll by exactly the mutual information it
captures.

---

## Grades on pass (per §4 of the brief)

- **Fact** (classical) — the conservation identity `nH = H(counts) + E[ln C]` (Shannon's source
  coding; the chain rule and exchangeability); the toll values ln4, H, H+KL (Shannon's
  source-coding theorem and the mismatched-code / Kraft identity: erasing p-data under model m
  costs the cross-entropy `H(p) + KL(p‖m)` per symbol); the KL surcharge; and the MDL slope
  `−(k−1)/2` (Rissanen). The reversible-free / erasure-positive accounting is Landauer and
  Bennett. Attributions carried; the thermodynamics-of-prediction literature is adjacent and
  may be cited as such.
- **Reading** (E2's own, on top of those facts, on the probe's own ledger):
  1. **The resolution** — *"balanced or stored?" is answered by a conservation frontier:*
     *storage is exactly memory growth (f·H), payment is exactly memory bound ((1−f)·H), the*
     *ledger closes to the ingested information at every f, and the poles are the summarizer*
     *and the hoarder.*
  2. **Knowledge is a discount on the price of forgetting**, worth exactly the redundancy the
     model captures (`ln4 − H`).
  3. **Model error is a surcharge of exactly `KL(p‖q)`** — the probe's model quality is
     measurable on its own ledger — with the sharp corollary that a confident wrong model costs
     *more* than ignorance whenever `KL > redundancy`.
  4. **Learning's permanent residue grows as the MDL term** — what op-F keeps (the counts) is
     the model, and it grows as `(k−1)/2 · ln n`.

*Note forward (one line, per §4):* M3's "erasure paid per nat" machinery supplies the numerator
and denominator vocabulary for the register's **E6** candidate `M(q) = erasure paid /
entropy removed`.

---

## Implementer additions (labelled; separate grade; do not substitute for any committed measure)

**A1 — route-equality (the exact per-block ledger split).** For every one of the 1000 blocks
in the M2 run, `op-F(c) + op-D(counts)(c) = op-D(raw block)` held to a max deviation of
**2.8×10⁻¹⁴** (machine epsilon). This is the exact-per-realization identity behind C1: the two
forgetting routes — forget-order-then-discard-the-summary versus discard-the-raw-block — cost
**identically**, and differ only in *where* the payment is located on the ledger (op-F pays the
order information `ln C`; op-D(counts) pays the count information `−ln P(c)`; their sum is the
block's self-information `−Σ ln p(xᵢ)`). It is the demonstration that M2's accounting is a real
split, not a circular restatement. *(Grade: Fact — it is algebra. Its role is non-vacuity.)*

**Enumeration validation of H(counts).** The chain-rule `H(counts)` used in M1 was checked
against brute-force enumeration of the full count simplex at n=50 (23,426 vectors) and n=100
(176,851 vectors): agreement to **1.4×10⁻¹⁴** and **6.4×10⁻¹⁴**, with the multinomial
normalisation `Σ P(c)` recovering 1 to ~10⁻¹⁴. *(Grade: internal validation; no claim.)*

**Capacity/blank harvest (C3, unbarred).** Each cell has capacity ln4 but the source spends only
H; the gap `ln4 − H = 0.173287 nats/symbol` is the redundancy a learned model can harvest —
the same quantity as M3's knowledge discount, viewed from the cell rather than the eraser.
Reported alongside, unbarred, per C3. *(Grade: Reading, and it is the same Reading as M3.ii.)*

---

## Non-vacuity audit (per §5.3; performed before running)

Every committed bar is capable of failing under an incorrect implementation, and no check
compares a quantity to itself or restates a definition:

- **M1** computes its three terms by three independent routes; a bug in any (a mis-enumerated
  simplex, a wrong multinomial coefficient, a normalisation error) breaks the identity. The
  specific trap — deriving a conservation term by subtraction — is avoided: `H(counts)` is a
  chain-rule computation, not `nH − E[ln C]`. The realized leg is a genuine Monte Carlo test.
- **M2** simulates the bounded-memory policy on the realized stream; a wrong charge or wrong
  discard rule shifts the toll off H. The independent cross-check (paid + retained = direct
  op-D(raw), to 7×10⁻¹⁶) confirms the split closes rather than assuming it.
- **M3** compares three realized tolls to three fixed closed forms. **Honest flag:** the
  *ignorant* toll (and M6's order-0 toll) is `−ln(¼) = ln4` for every symbol, so it is exact by
  construction, not statistical — it tests the op-D wiring, not a fluctuating mean. The
  genuinely statistical tolls are *learned* and *mismatched*, and those are where the discount
  and surcharge are measured.
- **M4** simulates archive-or-discard; the frontier and the `f·H` storage law both move under a
  miscoded storage/erasure account.
- **M5** is an exact computation whose slope fit fails if `E[ln C]` is wrong.

---

## Notes for Alex (honest observations — none threaten a bar)

1. **The ignorant toll is deterministic, not measured.** Under the uniform protocol every symbol
   costs exactly `ln4`, so `M3-ignorant` and `M6-order0` land on ln4 to machine precision rather
   than "within 0.02." This is worth knowing so the two exact values aren't mistaken for
   suspiciously-good statistics — they are the capacity, by construction. The statistical teeth
   of M3 are the *learned* (1.21441) and *mismatched* (1.64699) tolls.
2. **M2's paid toll sits just above H, not below.** The exact ledger identity is `paid +
   retained = ingested`, and it closes to 7×10⁻¹⁶. Its relation to the *theoretical* floor H
   carries the stream's Monte Carlo fluctuation: here the ingested rate ran +1.4×10⁻³ above H,
   more than the retained inventory (1.2×10⁻³) pulls down, so the paid toll is +1.7×10⁻⁴ from H.
   Flagging so the *sign* of the deviation isn't a surprise. Reporting the retained inventory as
   an explicit storage line (your addition) is what makes this legible rather than mysterious.
3. **The M4 frontier is f-independent — that is the resolution in one number.** `storage +
   erasure = 1.21441` at every f. The dichotomy "balanced or stored" dissolves: it is always
   balanced *against the ingested information*, and "stored vs paid" is the free parameter f, not
   an alternative to conservation.
4. **The MDL slope is −1.5038, just off dead-centre.** Well inside ±0.05; the per-doubling
   decrements show a clean monotone approach to −1.5·ln2, so the small excess is the finite-n
   endpoint (n=50) transient in the log-linear fit. Noting it in case the n-range is ever changed.
5. **M6's gap exceeds MI by ~4×10⁻³** — Monte Carlo on the order-1 entropy-rate estimate;
   report-only and unbarred, as pre-registered.

---

## Plain-language summary

A probe reads a stream, tidies its memory, and throws things away. The question was whether that
tidying **balances** — every nat paid for — or whether the probe somehow ends up storing "net
energy." The answer is a clean frontier.

- Everything the probe takes in has to go **somewhere**: either it is **paid off** (erased, at a
  Landauer cost) or it is **kept** (stored, still occupying memory). Add the two and you get back
  exactly what came in — every time, at every setting. There is no leak and no free lunch. We
  measured this directly: paid + stored = ingested, to sixteen decimal places.
- The **only** free choice is *how much to keep*. Keep nothing and you are a **summarizer**: you
  pay the full information rate and your memory stays flat. Keep everything and you are a
  **hoarder**: you pay nothing (reversible compression is free) and your memory grows at the full
  rate. Every mix in between sits on a straight line between those two.
- **Knowing the source is worth money.** An ignorant eraser pays the full cell capacity; an
  eraser that has learned the distribution pays less, and the saving is *exactly* the redundancy
  it learned. Knowledge is a discount on the price of forgetting.
- **Being confidently wrong is worse than knowing nothing.** An eraser using a wrong model pays a
  surcharge equal exactly to how wrong it is (the KL divergence) — and here that surcharge
  (0.43) is bigger than the whole redundancy (0.17), so the wrong model costs more than pure
  ignorance. The probe's model quality is readable straight off its own energy bill.
- **What survives forgetting is the model.** When the probe forgets the order of a block and
  keeps only the counts, the little that it keeps grows very slowly — like `1.5 · ln n`, the
  textbook "model description length." Forget the details and what is left, permanently, is the
  summary.

Everything landed where it was predicted to. Nothing had to be adjusted.

---

## Mandatory honesty caveat (transplanted from the corpus's energy-ledger discipline; §1)

In simulation, Landauer accounting is an **identity true by construction** — bijections are free
and merges cost the entropy drop *because we compute the `ln` we predicted*, not because we
measured a physical dissipation that could disagree. E2 therefore confirms that the probe's
ledger is a **consistent, correctly-structured accounting** and measures classical identities
within it; it does **not**, and cannot, *risk* the framework's carrier reading, which stays a
**Lead pending physical measurement**. E2's own contributions are the probe readings graded
above.

---

## Honesty boundary

The mathematics is classical and cited as such: Landauer's principle and Bennett's reversibility
(the free/charged split), Shannon's source-coding theorem and the mismatched-code identity (the
floor H and the cross-entropy tolls ln4, H, H+KL), and Rissanen's MDL (the `(k−1)/2 · ln n`
residue). **E2 adds no mathematics to these.** What belongs to the sub-programme is the reading
*on the probe's own ledger*: the frontier resolution of "balanced or stored," and the discount /
surcharge / residue as measurements of a probe's knowledge, error, and permanent residue against
its own erasure bill. In simulation these are identities we computed rather than physical facts
we risked, so nothing here is — or can become — evidence that the genesis system holds beyond the
axioms that posit it; the carrier reading is not promoted. No leverage is claimed on any open
problem. Boundary discipline inherited from the main spine, unamended.

*The master document has not been edited — banking edits to the spine are performed by the lead
instance on return.*

*Alexander Pisani & Claude (Anthropic) · Madness in the Probe sub-programme · E2 · July 2026.*

---

## Lead verification addendum (appended on return; original text above untouched)

**Independent rerun.** The script was rerun by the lead, unmodified, in a separate environment: exit 0, **22/22 committed checks**, and the full run log **byte-identical to the submitted log** modulo the runtime PID line. The banking stands.

**Code review of the non-circularity claims.** The three M1 routes are genuinely independent *in code*, not merely in description: nH from the pinned closed form; E[ln C] as ln n! − Σ E[ln cᵢ!] via per-coordinate binomial sums; H(counts) via a chain rule whose conditionals are correctly derived (c₁|c₀ ~ Binom(n−c₀, p₁/(1−p₀)); c₂|c₀,c₁ collapsing to Binom(n−s, p₂/(p₂+p₃)) with s ~ Binom(n, p₀+p₁)); plus brute simplex enumeration as validation. The anti-tautology clause of brief §5.3 is honoured in the implementation.

**One relation noted for the record.** M2's conservation cross-check (paid + retained = direct op-D(raw), 7×10⁻¹⁶) is algebraically entailed by A1's per-block route-equality plus the bookkeeping; as an implementation check it remains non-vacuous (two independently computed sums meeting), the same status the note itself assigns to A1. Recorded so the 10⁻¹⁶ agreement is read as the split closing, not as a separate statistical result.

**On the implementer's self-flags.** The deterministic ignorant toll (and M6's order-0 toll) was identified by the implementing instance itself, in its own non-vacuity audit, before the lead's review — the correct call, correctly reasoned (it tests op-D wiring, not a fluctuating mean; M3's statistical teeth are the learned and mismatched tolls). Two experiments ago this class of observation had to come from the lead's addendum; the discipline is now being applied by implementers to their own work unprompted. Noted with approval.

*Lead instance, July 2026.*
