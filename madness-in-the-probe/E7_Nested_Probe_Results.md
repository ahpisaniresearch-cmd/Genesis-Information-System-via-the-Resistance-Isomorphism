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

# E7 Results — The Nested Probe and the Insight Ledger: Conversion, Never Transfer

**Madness in the Probe sub-programme · design experiment · banking run · July 2026**
**Alexander Pisani & Claude (Anthropic)**

---

## Status

**ALL 33 COMMITTED CHECKS PASSED. Report-only / labelled items reported. Banking run complete.**

The pre-registered prediction — *all committed measures pass; insight is real conversion at zero outer queries and never exceeds the record ceiling; the leak is caught; premature compression forecloses* — held in full. No committed bar was moved; no result was patched. **No survivor appeared:** across the full DPI battery on both S₁ and S₂ — deterministic coarsenings, compositions, and randomized maps with independent noise — not one post-processing exceeded its bound; the largest within-battery information exactly *equals* the bound (appending independent noise), never beats it. A within-battery gain above a DPI bound at closed interface would have struck the tower's spine; none did.

**The result, in one line.** *Insight is conversion, and the record ceiling is where it stops.* The inner probe, reading its own closed record store, converts **0.259 nats** of real knowledge about the generator (S₁→S₂) with **zero outer queries** — but it can never exceed the records' own content, and here that content **saturates at the minimal sufficient statistic**: bigram counts (S₂) read everything about θ that the raw record (S₃) holds, so **I(S₂;θ) = I(R;θ) to 3×10⁻¹⁶**, with **H(R|S₂) = 2.237 nats** of further record structure carrying exactly **zero** θ-content. Forgetting below sufficiency **forecloses** — discard to S₁ and the S₂ insight is unreachable forever, no re-purchase possible (unlike E3's path (iii)); forgetting *down to* sufficiency is **insight-safe** — discard to S₂ loses no generator-information at all. The leaky oracle (5 fresh symbols disguised as inner noise) was **caught**: it lifts the information **0.202 nats above** the ceiling, and above-ceiling is communication, not insight.

Implemented fresh for E7 only. No prior script was consulted or reused; no other corpus document was read for the implementation. The §6 pre-run correction (C1/C2 M1 rewrite, the new H(R|S₂) ≥ 0.5 floor, the M4b amendment, C3 floors) and the §5.5 derivation check are honoured exactly. Implementation choices within remit are documented below.

---

## Reproducibility block

| Item | Value |
|---|---|
| Script | `535_e7_nested.py` (fresh; PID-prefixed) |
| Recorded seed | `20260710` (form only; **no sampling occurs** — the experiment is exact enumeration) |
| Runtime PID (this run) | `534` |
| Wall-clock runtime | ~2.1 s |
| Exit code | `0` (all committed checks passed) |
| Python | 3.12.3 |
| mpmath | 1.3.0 (dps=50 cross-check of sufficiency and the S₂ ledger identity) |
| Precision | float64 + `math.fsum` throughout; one **mpmath dps=50** recomputation of the two tightest identities |
| Enumeration | full 8×2¹⁰ joint (records) and 8×2¹⁵ joint (records + oracle), exact; **no Monte Carlo anywhere** |
| Generator | 4 i.i.d. Bernoulli p∈{.2,.4,.6,.8}; 4 symmetric order-1 Markov, stay-prob s∈{.2,.35,.65,.8}, started at stationarity |
| Records length | T = 10 (all four committed floors met at T=10; T not tuned up) |

**Precision justification (why float64 suffices here — the E3 convention, carried).** Every quantity is an entropy or mutual information in nats of magnitude ≤ ~6.6 (the largest is H(R) = 6.5579). float64 carries ~15–16 significant digits, so absolute error is ≲10⁻¹⁴ at this scale; `fsum` removes accumulation error. The tightest bars (sufficiency and the ledger identity at 10⁻¹²) clear by ~100–1000×. Confirmed independently by an **mpmath dps=50** recomputation: the sufficiency residual |I(S₂;θ)−I(R;θ)| is **4.0×10⁻⁵⁰** (float64 gave 3.3×10⁻¹⁶) and the S₂ ledger residual is **6.2×10⁻⁴⁹** (float64 gave 0.0) — honest float artifacts, not masked violations. E4's ≥800-digit regime was continued-fraction-specific and does not transfer to this combinatorial setting (E3 ratification, carried).

**Pre-registered bars** are copied verbatim into the script header (before any check was written) and are reproduced with actuals below.

### Implementation choices (documented, within remit)

- **T = 10, not tuned up (C3).** The §5.5 derivation-check enumeration confirmed all four floors at T=10 with comfortable margins (F1 dI = 0.259 ≥ 0.05; F2 I(R;θ) = 0.695 ≤ 2.029; F3 oracle = 0.202 ≥ 0.05; F4 H(R|S₂) = 2.237 ≥ 0.5). T=12 was checked as a fallback (all floors also pass) but not needed; T=10 is reported.
- **S₀/S₁/S₂ as partitions of R (C-honesty).** I(S₂;θ) is computed from the S₂-partition and I(R;θ) from the full R-partition — **two independent partitions**, so their equality is a measured coincidence of sufficiency, not an assumed identity. I(S₀;θ) is computed as the MI of the constant map (structural 0; float residual 5.9×10⁻¹⁴ ≤ 10⁻¹²).
- **Oracle Z = fresh independent draw (convention pinned).** "5 fresh symbols drawn from the same θ" is implemented as an *independent* draw from θ (Markov restarted at stationarity), so R ⟂ Z | θ and P(R,Z|θ) = P(R|θ)·P(Z|θ). This makes Z a clean "outer channel disguised as inner noise": it carries fresh generator-evidence, hence lifts the information above the ceiling.
- **DPI battery built by honest enumeration (non-vacuity).** Each post-processing — deterministic coarsening, composition, or randomized channel — is applied by constructing the joint P(θ, output) directly from the enumerated joint; **DPI is never invoked** to obtain any bound. Randomized channels use independent noise only (an appended fair bit; an ε=0.3 erasure coin; ε=0.25 symmetric relabel; a ±1 count-shift for S₁).
- **M5 three routes independent; M4/M4b charge dual-computed.** In M5 each of H(R), H(S_k), H(R|S_k) is a direct enumeration (marginal entropy, marginal entropy, within-class entropy sum) — **no term by subtraction**. The M4/M4b *charge* H(R|S_k) is separately cross-checked route-1 (direct within-class) against route-2 (H(R)−H(S_k)); the non-vacuous independent form is M5's identity (see §Non-vacuity).

---

## Pre-registered bars vs actuals

| Check | Bar | Actual | Verdict |
|---|---|---|---|
| **M1.1** I(S₀;θ)=0 | ≤ 1e-12 (constant statistic) | **5.879e-14** | **PASS** |
| **M1.2** I(S₁;θ)>0, ≤ I(S₂;θ) | 0 < I(S₁) ≤ I(S₂) | **0.435845569** | **PASS** |
| **M1.3** insight gap dI(S₁→S₂) | ≥ 0.05 | **0.259278932** | **PASS** |
| **M1.4** sufficiency I(S₂;θ)=I(R;θ) | \|·\| ≤ 1e-12 (independent partitions) | **3.331e-16** | **PASS** |
| **M1.5** ceiling I(R;θ) | ≤ ln8 − 0.05 = 2.029442 | **0.695124502** | **PASS** |
| **M1.6** surplus floor H(R\|S₂) | ≥ 0.5 | **2.236710818** | **PASS** |
| **M2.1** insight gain, zero outer queries | ≥ 0.05 | **0.259278932** | **PASS** |
| **M2.2** dual accounting A=B | \|A−B\| ≤ 1e-12 | **1.110e-16** | **PASS** |
| **M3a.1–8** DPI battery on S₂ (8 maps) | each I(f;θ) ≤ I(S₂;θ)+1e-12 | max attained **0.695124502** (= bound) | **PASS** ×8 |
| **M3b** leaky oracle caught | I((R,Z);θ)−I(R;θ) ≥ 0.05 | **0.201690585** (I(R,Z)=0.896815) | **PASS** |
| **M4.1–8** foreclosure battery on S₁ (8 maps) | each I(f;θ) ≤ I(S₁;θ)+1e-12 | max attained **0.435845569** (= bound) | **PASS** ×8 |
| **M4.charge** H(R\|S₁) dual-computed | \|r1−r2\| ≤ 1e-12 | **8.882e-16** (r=4.330307581) | **PASS** |
| **M4b.1** discard-to-S₂ loses no θ-info | \|I(S₂;θ)−I(R;θ)\| ≤ 1e-12 | **3.331e-16** | **PASS** |
| **M4b.2** H(R\|S₂) dual-computed | \|r1−r2\| ≤ 1e-12 | **0.000e+00** (r=2.236710818) | **PASS** |
| **M4b.3** S₁ forecloses / S₂ safe contrast | I(S₁;θ) < I(R;θ), gap ≥ 0.05 | gap **0.259278932** | **PASS** |
| **M5.S₀** ledger three routes | \|resid\| ≤ 1e-12 | **8.882e-16** | **PASS** |
| **M5.S₁** ledger three routes | \|resid\| ≤ 1e-12 | **8.882e-16** | **PASS** |
| **M5.S₂** ledger three routes | \|resid\| ≤ 1e-12 | **0.000e+00** | **PASS** |
| **M5.S₃=R** ledger three routes | \|resid\| ≤ 1e-12 | **0.000e+00** | **PASS** |

**33/33 committed checks passed.** Report-only: M5 inner-erasure ratios; M6(a) filling-in identity; the mpmath cross-check.

---

## Per-measure detail

### M1 — the ceiling and the chain (corrected per §6 C2)

By exact enumeration the chain is `0 = I(S₀;θ) ≤ I(S₁;θ) < I(S₂;θ) = I(S₃;θ) = I(R;θ) < ln8`:

```
I(S₀;θ) = 5.879e-14   (structural 0)
I(S₁;θ) = 0.435845569   (count of 1s)
I(S₂;θ) = 0.695124502   (first symbol + bigram counts)
I(R ;θ) = 0.695124502   (full record)   |I(S₂)−I(R)| = 3.3e-16
H(θ|R)  = 1.384317040   (records leave this much uncertainty — the ceiling headroom)
```

The insight gap S₁→S₂ is **0.259 nats** and the sufficiency equality is **exact to float zero, computed on two independent partitions**. The adopted finding (C2) is confirmed as measured: **the insight ladder saturates at the minimal sufficient statistic, not at the raw record.** The records conserve strictly more structure than the generator-information they carry — H(R|S₂) = 2.237 nats of record detail with exactly zero θ-content — the crisp separation of "structure the records conserve" from "information about the generator," on M3's conversion/transfer line. *(Sufficiency: Fact, Fisher–Neyman. Saturation: Reading, E7's.)*

### M2 — insight with the interface closed

The upgrade S₁→S₂ on the same closed record store gains **0.259278932 nats** about θ with **zero outer queries**. The dual accounting agrees to **1.1×10⁻¹⁶**: the ensemble MI gain (route A: I(S₂;θ)−I(S₁;θ), computed from the coarsened S-partitions) equals the mean per-record posterior log-improvement (route B: E over the full (θ,R) grid of ln P(θ|S₂)−ln P(θ|S₁)). The two aggregate at different resolutions (per-class vs per-record) from the same joint, so the agreement is a genuine check *of the implementation*, exactly as pre-registered. This is real knowledge of the world, from nowhere but the records — because it was always in the records.

### M3 — conversion, never transfer

**(a) The DPI battery on S₂** (bound I(S₂;θ) = 0.695124502):

| post-processing | I(f;θ) |
|---|---|
| → constant | 0.000000000 |
| ⊕ independent fair bit | **0.695124502** (= bound; noise adds nothing) |
| erasure(0.3), independent coin | 0.486587151 |
| symmetric-noise(0.25), independent | 0.377100472 |
| → S₁ (count) | 0.435845569 |
| → a (stays) | 0.409693644 |
| → x₁ (first symbol) | 0.053220068 |
| composition → S₁ → parity | 0.000760756 |

Every map lands at or below the bound; the appended-independent-noise case lands *exactly on* it. No coarsening, composition, or independent randomization of S₂ manufactures information about θ.

**(b) The detector.** The leaky oracle — Z = 5 fresh symbols correlated with θ — is caught: **I((R,Z);θ) = 0.896815 ≥ I(R;θ) + 0.05**, a margin of **0.202 nats above the ceiling**. This is the both-ways non-vacuity, and it pairs with M3a's independent-noise cases to make the signature sharp: *independent* noise (M3a: appended bit) leaves the information exactly at the ceiling, while a *correlated* channel (M3b: the oracle) lifts it above — so "conversion, never transfer" is a signature the audit can enforce, not a tautology. The banked Reading: **the record ceiling is an operational criterion — within-ceiling gains are always conversion; above-ceiling gains are always communication.**

### M4 — the foreclosure theorem (fusion echo, interface closed)

The inner probe discards R down to S₁, charging the inner ledger **H(R|S₁) = 4.330307581 nats** (dual-computed; routes agree to 8.9×10⁻¹⁶). It then attempts the S₂ upgrade via the full battery (bound I(S₁;θ) = 0.435845569):

| post-processing of S₁ | I(f;θ) |
|---|---|
| → constant | 0.000000000 |
| ⊕ independent fair bit | **0.435845569** (= bound) |
| erasure(0.3) | 0.305091899 |
| symmetric-noise(0.25) | 0.199287760 |
| → parity | 0.000760756 |
| → (k mod 3) | 0.006181666 |
| composition → (k mod 3) → parity | 0.001858455 |
| noisy count-shift ±1, independent | 0.365658296 |

**Every attempt lands ≤ I(S₁;θ) = 0.436 < I(S₂;θ) = 0.695.** The insight is unreachable forever. No re-purchase exists here, unlike E3's path (iii): the interface is closed, so premature compression does not incur a re-payable debt — it **forecloses**. The Reading: *forgetting lowers the insight ceiling irreversibly; the hoarder's memory bill buys the right to insights it cannot yet name; the summarizer forecloses them.* (E2's frontier, reappearing in the tower.)

### M4b — insight-safe compression (lead amendment, §6)

The inner probe discards R down to S₂, charging **H(R|S₂) = 2.236710818 nats** (dual-computed; routes agree to 0.0). Post-discard the information **reaches I(R;θ) exactly** (|I(S₂;θ)−I(R;θ)| = 3.3×10⁻¹⁶) — **no foreclosure at the sufficient rung** — and the battery on S₂ (M3a above) confirms nothing exceeds it. Against M4's discard-to-S₁ (which forecloses the 0.259-nat gap), this banks the paired Reading: **compression is insight-safe exactly down to minimal sufficiency, and forecloses below it** — E2's hoarder–summarizer frontier acquires its safe floor, and the floor has a classical name (the minimal sufficient statistic).

### M5 — the inner ledger identity (three independent routes)

`H(R) = H(S_k) + H(R|S_k)` holds at every ladder level, each term by a direct enumeration (no subtraction):

| level | H(R) | H(S_k) | H(R\|S_k) | residual |
|---|---|---|---|---|
| S₀ | 6.557893709 | 0.000000000 | 6.557893709 | 8.9e-16 |
| S₁ | 6.557893709 | 2.227586128 | 4.330307581 | 8.9e-16 |
| S₂ | 6.557893709 | 4.321182891 | 2.236710818 | 0.0 |
| S₃=R | 6.557893709 | 6.557893709 | 0.000000000 | 0.0 |

**Report-only — information actualised per nat paid inwardly (E6 vocabulary):**

| upgrade step | dI (θ-info gained) | d(inner erasure) | ratio |
|---|---|---|---|
| S₀→S₁ | +0.435845569 | 2.227586128 | 0.195658 |
| S₁→S₂ | +0.259278932 | 2.093596762 | 0.123844 |
| **S₂→S₃** | **0** (sufficiency) | 2.236710818 | **0** |

The last row is the finding made vivid: reading the full record beyond its bigram counts costs the inner probe **2.237 nats** of erasure and actualises **zero** additional information about the generator. Below sufficiency, inner erasure buys θ-knowledge; at and above it, inner erasure buys only generator-irrelevant record detail.

### M6 — report-only

**(a) Filling in the blanks = conditioning.** The inner probe's max-ent-inward completion for an unread symbol (uniform over records consistent with its statistic) is compared to the record store's own conditional P(x_T | S_k). At the **sufficient rung S₂ the two coincide to 0.0** — sufficiency makes the ignorance-maximizing completion equal the true weighting, so max-ent-inward *is* conditioning. At **S₁ they diverge by 0.029** — and that gap is precisely the (count, stay)-structure S₁ cannot read: the non-sufficiency signature, not a failed identity.

**(b) The P4 boundary (per the fence).** The record ceiling gives P4's boundary an operational statement: within-ceiling gains (I ≤ I(R;θ)) need **no host** — they are the inner repertoire reading what the records already held; above-ceiling gains are **communication**, not insight. Whether any host exists is unfalsifiable by construction and owned; E7 bears on it not at all.

**(c) The dreaming scaffold, caged.** Inner-phase activity with the outer interface closed is the whole of E7's setting — the scaffolding term earns its cage: it names the arena and nothing more.

---

## Non-vacuity (audit; honest flags)

Every committed bar can fail under an incorrect implementation, and no check compares a quantity to itself or restates a definition:

- **M1.4 / M4b.1 sufficiency.** I(S₂;θ) and I(R;θ) are computed from **two different partitions** of the same joint; a bug in the S₂-map (a mis-tallied bigram, a wrong count-recovery) would break the equality, which is why it is a measured coincidence, not an identity assumed. The equality is *predicted* by Fisher–Neyman but *verified* by enumeration.
- **M2.2 dual accounting.** Routes A and B share the joint but aggregate at different resolutions (per-class MI vs per-record posterior average). A mistake in the R→S map, or in the per-record weighting, breaks B without touching A. Agreement (1.1×10⁻¹⁶) is therefore a check of the implementation, as the brief specifies.
- **M3a / M4 battery.** Each joint P(θ, f-output) is built by honest enumeration of the channel; **DPI is never invoked** to obtain a bound. A miscoded channel (mass not summing to 1, a leaked θ-dependence in the "independent" noise) would raise I(f;θ) above the bound and fail loudly — the appended-independent-bit case sitting *exactly* at the bound (not below) is the tightest demonstration that the battery measures rather than assumes.
- **M3b detector — the both-ways teeth.** The audit is shown to fire when it should: the oracle, correlated with θ, is caught above the ceiling. Paired with M3a's independent-noise cases (which do *not* breach the ceiling), this is the demonstration that "conversion, never transfer" is a signature and not a tautology — an audit that could not catch a disguised channel would be vacuous; this one does.
- **M5 three routes.** H(R), H(S_k), H(R|S_k) are three independent direct enumerations; the identity fails under any single-route bug. **Honest flag (carried from E3/E2):** the M4/M4b *charge* H(R|S_k) is additionally cross-checked by route-2 = H(R)−H(S_k), which *is* a subtraction and telescopes by construction — so it cannot, alone, catch a compensating error. Its independent teeth are M5's three-route identity, which computes H(R|S_k) directly and pins H(R) and H(S_k) separately. The charge's subtraction route is a consistency cross-check, not the non-vacuous measurement; flagged here rather than left implicit.
- **I(S₀;θ) is structurally zero, not measured.** A constant statistic carries no information by construction; the 5.9×10⁻¹⁴ residual tests the MI wiring (that a point-mass partition returns 0), not a fluctuating quantity. Flagged so the near-zero is not mistaken for a tight statistical result.

---

## Notes for Alex (honest observations — none threaten a bar)

1. **The sufficiency collapse, now measured, is the note's centre — and it strengthens the fence.** The pre-run correction turned a broken strict inequality into a cleaner true one. What lands is sharper than three strict rungs would have been: **the records hold 2.237 nats of structure that is provably irrelevant to the generator** (H(R|S₂), zero θ-content). "Structure the records conserve" and "information about the generator" are not the same set, and the tower now exhibits the gap between them exactly. This is the single cleanest thing E7 owns.

2. **Independent noise sits *exactly* on the ceiling; that is the point.** In both batteries the appended-independent-bit map returns I(f;θ) equal to I(S;θ) to the printed digit — not a hair below. This is not a suspicious coincidence; it is the DPI equality case (post-processing by independent randomness is information-lossless in the MI sense), and it is what makes M3b's *above*-ceiling oracle unambiguous. Flagging so the equality is read as the tight boundary, not as a near-miss.

3. **The S₂→S₃ ratio is 0, and it is the finding in one number.** Paying 2.237 nats of inner erasure to read the raw record beyond its bigrams actualises zero θ-information. Below sufficiency, inner erasure is insight; at and above it, inner erasure only forgets generator-irrelevant detail. The E6 vocabulary ("information actualised per nat paid inwardly") makes the saturation legible as a rate that hits zero exactly at the sufficient rung.

4. **The oracle margin (0.202) is bounded by the ceiling headroom, not by Z's strength.** With I(R;θ) = 0.695 and I((R,Z);θ) = 0.897, the oracle recovers a healthy share of the 1.384 nats of headroom H(θ|R). It clears the 0.05 floor by ~4×; the margin would grow with more oracle symbols and shrink toward the floor if the records were richer. Noting the dependence in case the toy is ever re-tuned.

5. **Foreclosure vs E3's path (iii) is the substantive contrast, and it is clean.** In E3, fusing under an *open* interface incurred a re-payable debt (1.978 nats). Here the interface is closed, so there is nothing to re-purchase against — discard below sufficiency and the gap is gone, full stop. M4b's addition makes the pair complete: safe exactly down to minimal sufficiency, foreclosing below it. The frontier E2 found (summarizer↔hoarder) now has a named safe floor.

---

## Plain-language summary

Picture a mind as a notebook plus a reader. The notebook holds a record; the reader can only take in *summaries* of it. "Insight" here means the reader upgrading its summary — noticing structure that was on the page all along — with no new look at the outside world.

- **Insight is real, and it comes from nowhere but the page.** Our reader starts by counting the 1s in a 10-symbol record. That count tells it something about which of eight hidden processes wrote the record — but it is blind to *which* of the four "streaky" processes it was, because they all produce the same number of 1s on average. Upgrade the reader to also see the *pairs* of adjacent symbols, and it suddenly distinguishes them: a real gain of **0.26 nats** of knowledge about the world, bought with **zero** new observations. It was always in the record; the reader just learned to read it.

- **But insight cannot exceed what the record holds — and here the record runs out early.** Once the reader can see the adjacent pairs, it has extracted **everything** the record says about the hidden process. Reading the raw record symbol-by-symbol adds **nothing** — we measured the extra information as exactly zero. The record still contains more *detail* (which exact string, out of many that share the same pair-counts), but that detail says nothing about the world: **2.24 nats of structure with zero bearing on the generator.** What the record conserves and what it tells you about the world are two different things, and we can see the gap.

- **Forgetting too much is permanent.** If the reader throws away the record and keeps only the count, it can never recover the pair-structure — no amount of clever reprocessing, no added noise, gets the 0.26 nats back. At a closed notebook there is no "buy it back later" (that existed in an earlier experiment where the notebook stayed open); here, forgetting below the useful summary **forecloses** the insight for good. Forgetting down *to* the useful summary, though, is completely safe — it loses no knowledge of the world at all.

- **A disguised outside line gets caught.** We slipped the reader five *fresh* symbols from the same hidden process, dressed up to look like more of its own notebook. Because they carry genuinely new evidence, they push its knowledge **0.20 nats above** the record's ceiling — and that is the tell. Anything that lifts you above what your records could contain is not insight; it is a message from outside. The audit catches it every time, which is exactly what stops "insight is never transfer" from being an empty slogan.

Everything landed where it was predicted to. Nothing had to be adjusted (the one pre-run correction was made *before* the run, with the run then confirming it).

---

## The fence (§1, mandatory)

E7 prices the **definitions** of the nested tower inside a toy. It makes **no claim about human insight, cognition, or psychology** — "insight" and "dreaming" here are the corpus's deflationary terms (inner conversion of record-virtual to record-actual structure; inner-phase activity with the interface closed) and nothing more. And it neither tests nor touches the owned posit **P4** (the host probe): the record ceiling gives P4's *boundary* an operational statement — within-ceiling gains need no host, above-ceiling gains are communication, not insight — but whether any host exists is unfalsifiable by construction and owned, and E7 bears on it not at all.

---

## Mandatory honesty caveat (transplanted from the corpus's energy-ledger discipline)

In simulation, Landauer accounting is an **identity true by construction** — bijections are free and erasures cost the entropy we compute because we compute the `ln` we predicted, not because we measured a physical dissipation that could disagree. E7 therefore confirms that the nested probe's ledger is a **consistent, correctly-structured accounting** and measures classical identities within it (the data-processing inequality, sufficiency/coarsening monotonicity, the entropy chain rule); it does **not**, and cannot, *risk* the framework's carrier reading, which stays a **Lead pending physical measurement**. E7's own contributions are the probe readings graded below.

---

## Honesty boundary

The mathematics is classical and cited as such: the **data-processing inequality** in its standard information-theoretic form; **sufficiency and the Fisher–Neyman factorisation** (the minimal sufficient statistic (count, stay-count) for the i.i.d.⊕symmetric-Markov family, and the resulting I(S₂;θ) = I(R;θ)); and the **entropy chain rule** (Shannon) for the ledger identity. **E7 adds no mathematics to these.** What belongs to the sub-programme is the reading *on the probe's own ledger*: **insight priced as conversion** (real gain at zero outer queries, always within the ceiling — Reading); **the ceiling as insight-capacity** and as the operational conversion/communication criterion (the P4 boundary, fence intact — Reading); **the saturation finding** (the ladder saturates at minimal sufficiency, the record conserving strictly more structure than its θ-content — Reading); **the foreclosure theorem** (forgetting below sufficiency lowers the insight ceiling irreversibly once the interface closes — Reading); **insight-safe compression** (safe exactly down to minimal sufficiency — Reading, M4b); and **the E2-frontier echo** (the summarizer↔hoarder frontier acquiring its safe floor in the tower — Reading). In simulation these are identities we computed rather than physical facts we risked, so nothing here is — or can become — evidence that the genesis system holds beyond the axioms that posit it; the carrier reading is not promoted, P4 is not promoted, and nothing here touches human cognition. No leverage is claimed on any open problem. Boundary discipline inherited from the main spine, unamended.

*The master document has not been edited — banking edits to the spine are performed by the lead instance on return.*

*Alexander Pisani & Claude (Anthropic) · Madness in the Probe sub-programme · E7 · July 2026.*

---

## Lead verification addendum (appended on return; original text above untouched)

**Independent rerun.** The script was rerun by the lead, unmodified, in a separate environment: exit 0, **33/33 committed checks**, every figure reproduced to the printed digit (the 0.259278932 gap; the 0.695124502 ceiling met exactly by the independent-noise case in both batteries; the 0.201690585 oracle margin; the ledger table including H(R|S₁) = 4.330307581 and H(R|S₂) = 2.236710818; the mpmath dps=50 residuals). The banking stands.

**Code review.** The load-bearing joints are as claimed: sufficiency (M1.4) is measured across two independently constructed partitions — the S₂-map with its own count/stay recovery functions versus the raw-record partition — so the 3.3×10⁻¹⁶ equality is a verified coincidence of Fisher–Neyman, not an assumed identity; every battery joint P(θ, output) is built by direct channel enumeration with DPI nowhere invoked; the three ledger routes are three separate direct enumerations.

**Ruling on the mid-run correction (M6a).** Endorsed, with the mathematics verified by the lead: the max-ent-inward completion (uniform over the statistic's class) equals the true conditional **exactly when the statistic is sufficient** — within an S₂-class every record is equiprobable under each θ, by the same factorisation that drove the §6 correction — and diverges below sufficiency by precisely the unread structure (the 0.029 at S₁ is the bigram-weighting S₁ cannot see). The first-pass reading ("identity failing") was wrong and the corrected reading is right; the item is report-only, no bar was involved, and the correction was disclosed with both numbers shown. This is the legitimate case for a mid-run correction, handled correctly — and the corrected item upgrades the master's own §4 sentence: *max-ent-inwardly is conditioning at sufficiency, biased below it*, with the bias itself a measurable non-sufficiency signature.

**On the honest flags.** The telescoping route-2 flag (the charge's subtraction cross-check cannot alone catch compensating error; M5's three-route identity carries the teeth) and the structural-zero flag on I(S₀;θ) are both correct and both self-identified — the fourth consecutive experiment in which the implementing instance has applied the non-vacuity discipline to its own work unprompted. The equality-case observation (independent noise sitting *exactly on* the ceiling as the DPI equality, making the oracle's *above*-ceiling unambiguous) is adopted as the authoritative reading of why the detector pair has teeth.

*Lead instance, July 2026.*
