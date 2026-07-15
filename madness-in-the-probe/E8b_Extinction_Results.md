# E8b — Results: Hunting the Extinction Constant λ

**Madness in the Probe sub-programme · identification experiment · implementing instance, July 2026**
**Attribution:** Alexander Pisani & Claude (Anthropic). Alex originated the object, the phenomenon, and the pre-registered design; the implementing instance executed against the fixed bars.

---

## 0. Status

**Outcome: the pre-registered prediction is borne out — λ is measured, gauge-robust in the natural neighbourhood, and *parked* (not identified in closed form), with the identification obstruction stated precisely.** Two results exceed the brief:

1. **The register's λ = 0.7225535(60) is revised.** The true asymptotic constant is **λ = 0.7224793(2)**. The old figure is the *local* ratio r(n+1)/r(n) read at **n ≈ 273**, mistaken for the limit; the local ratio descends monotonically past it to the asymptote. The correction is confirmed independently three ways (log-domain fit, an independent magnitude route, and mpmath).
2. **M3 (the gauge audit) does not cleanly kill the phenomenon, but it does not leave "gauge-robust" unqualified either.** Decay is robust across the whole natural neighbourhood a ∈ [−0.5, 0.5] with large margins, strengthens to a maximal-extinction weighting near a ≈ +0.25, and **crosses over to growth at the extremes a = ±1**. Per the literal M3b bar this is a partial trigger; per the brief's own statement that the reweighting *genuinely changes the object*, the honest reading is neighbourhood-robustness, not global gauge-invariance. **This is flagged for lead adjudication (refine vs. kill); it is reported, not patched (§4 escalation).**

All Bessel/annealed/linearisation pins pass. No result approaches the §1 boundary.

**Grades.** Bessel identification of μ, the per-node annealed identity, the linearisation chain, the exact collision census — **Fact** (elementary / classical-adjacent; no novelty claimed). The extinction as a deterministic, neighbourhood-robust, faster-than-typical-chance destructive phenomenon with constant λ = 0.7224793(2) — **Reading: measured and parked**, obstruction stated (M4a route (a) obstructed by non-separability; M4b route (b) exhaustive negative).

---

## 1. Reproducibility block

| item | value |
|---|---|
| Script | `529_e8b_lambda.py` (PID-prefixed) |
| Raw output | `529_e8b_raw.json` |
| Seed | `20260710` (fixed; used only by the Monte-Carlo ensembles — pins, census, and the deterministic recursions are seed-independent and exact) |
| Libraries | numpy 2.4.4, mpmath 1.3.0 (dps 40–50 for checks), sympy 1.14.0, `fractions` (exact census) |
| Precision method | per-step log-renormalisation with tracked log-magnitudes (supersedes global rescale); complex F-leg summed in the linear domain after max-subtraction so phase cancellation is preserved; exact zeros masked |
| Extent | clock recursion to **n = 8000**; gauge scan to n = 4000; μ pin to n = 4000; census exact for n = 6…10; shared-DP 500 seeds to n = 200; per-node MC 12k–200k samples |
| Test-run | exits 0 |

The recursion validated against mpmath (dps 50) to **7×10⁻¹⁵ and 2×10⁻¹⁴** relative at n = 100, 200 — r(n) itself is exact to float64; only the n→∞ extrapolation carries model uncertainty.

---

## 2. Bars vs. actuals

| Bar | Target | Actual | Verdict |
|---|---|---|---|
| **Pin a** | −x(ln w)′ series = G(n) exactly, n ≤ 20 | exact match; c₁(w) = **−1** (the flagged coefficient, from −2x/2!) | **PASS** |
| **Pin b** | g(x) vs J₁(√8x)/√(2x) to 1e-12, 5 pts | max rel err **3.9×10⁻¹⁷** | **PASS** |
| **Pin c** | G(n+1)/G(n) → μ = 8/j₁₁² to ≥6 digits | late-window fit agrees to **15.2 digits** | **PASS** |
| **M1a** | λ to ≥8 sig figs + band | **λ = 0.72247931(19)** — 7 figures solid, 8th within band | **MET (7 solid + banded 8th)** |
| **M1b** | two windows agree within band | W1[1000,4000] = 0.72247947, W2[4000,8000] = 0.72247928; agree to 7th figure, **spread 1.9×10⁻⁷** at the 8th | **PASS at 7 figs**; spread reported as the honest systematic |
| **M1c** | float64 vs mpmath to 1e-10 | 7×10⁻¹⁵, 2×10⁻¹⁴ | **PASS** |
| **M1d** | β measured + band + honest caveat | **β = 2.3755680**, std 6×10⁻⁸ — a *single* dominant complex ζ; converges cleanly (no conjugate-pair ambiguity) | **PASS** |
| **M2a** | per-node mean = G(n) within CI; sharing must fail | ratios 0.9987 / 1.0017 / 1.0079 / 0.9995 at n = 4/6/8/10, all within CI; shared-DP at n=6 gives 1.076 (outside per-node CI) → **non-vacuity demonstrated** | **PASS** |
| **M2b-i** | shared-DP median rate reported vs clock λ | median rate **0.901**, geomean **0.892**; both ≫ clock 0.7225 | **PASS** |
| **M2b-ii** | exact census; single collision at n=6; pin 71/66 | **1 collision group at n=6, E[r(6)] = 71/66 exactly**; census G matches recursion for n=6…10 | **PASS** |
| **M2b-iii** | shared-DP MC means match census within CI | 1.082/1.355/1.737 vs census 1.076/1.292/1.673 — within CI (heavy-tailed; sample mean noisy-high as expected) | **PASS** |
| **M3a** | report λ(a) each a | tabulated §3 | **reported** |
| **M3b** | kill if any a → no decay; else robust | central a∈[−0.5,0.5] all decay (large margins); **extremes a=±1 grow** | **NOT universal — flagged for lead** |
| **M4a** | derivation attempt + outcome | non-separability obstruction stated (§3) | **PARK (obstructed, precise)** |
| **M4b** | exhaustive committed sweep; negatives reported | no meaningful lead; nearest Bessel candidate j₀₁²/8 agrees only **3.2 digits** | **PASS (clean negative)** |
| **M5** | report-only | sign rate 1.111 (grows; + odd-n zeros); flat 3.636 (grows); I₁ no positive zero; split central-peaked | **reported** |

---

## 3. Per-measure detail

### M1 — λ, β, and the register revision

**The constant.** F(n) has a clean single-exponential asymptotic F(n) ~ C·ζⁿ with a **single dominant complex growth constant**

$$\zeta \;=\; |\zeta|\,e^{i\beta}\;=\;0.6274304\;e^{\,2.3755680\,i}\;=\;-0.452172 + 0.434982\,i,\qquad \lambda \;=\; \frac{|\zeta|^2}{\mu}\;=\;0.7224793(2).$$

Two independent routes agree: the direct Δ(n) = ln r(n+1) − ln r(n) fit (with 1/n, 1/n², log n /n corrections) gives λ = 0.72247931; the **independent magnitude route** measures |ζ| = 0.6274307 directly from the decay of |F(n)| and compares to √(λμ) = 0.6274304 — agreement to six digits. β is sharply defined (std 6×10⁻⁸), which is *why* r(n) decays smoothly: there is no conjugate partner of equal modulus, so |F(n)|² = |ζ|²ⁿ(1+o(1)) with no leading oscillation, and the M1d caveat (real/conjugate-pair ambiguity) does not bite here — β simply converges.

**The register revision (the headline).** The local ratio r(n+1)/r(n) **crosses 0.7225535 at n ≈ 273** and continues descending: 0.7224797 at n = 8000, extrapolating to 0.7224793. The register's 0.7225535(60) was therefore a finite-n reading of a slowly-converging ratio, not the asymptote; its stated (60) band did not cover the ~7.5×10⁻⁵ gap because the true uncertainty was the unmodelled convergence, not statistical scatter. Since r(n) is exact to 10⁻¹⁴ at the checkpoints, the revision is secure. The residual 1.9×10⁻⁷ spread between the two late windows is a subdominant (smaller-modulus) singularity's decaying contribution — it limits the honest precision to 7 solid figures with a banded 8th.

### M2 — the two ignorances of the benchmark, made exact

**Per-node identity (M2a), re-derived and measured.** With an independent phase on every merge of every tree, cross terms vanish in expectation (each tree carries ≥1 fresh uniform phase, E[eⁱᶿ]=0), so E|F(n)|² = Σ_P|A(P)|² = G(n) exactly. Monte Carlo confirms it at n = 4,6,8,10. **Non-vacuity is live and demonstrated:** a phase-*sharing* sampler (shared-DP) gives the census value 1.076 at n=6 — outside the per-node CI around 1 — so a sampler that accidentally shares would fail this bar.

**Shared-DP and the exact collision census (M2b).** The register's benchmark reuses one phase per (n,k) slot through the memoised recursion, which breaks the per-node identity. The mechanism is exact: two distinct trees can share an identical (m,k)-slot multiset, forcing identical amplitudes and a surviving cross term. The census enumerates all trees, groups by slot multiset, and computes E[r(n)] = (Σ_g |g|² w_g)/(Σ_g |g| w_g) in rationals:

| n | E[r(n)] exact | float | collision groups | trees |
|---|---|---|---|---|
| 6 | **71/66** | 1.07576 | **1** | 42 |
| 7 | 1465/1294 | 1.13215 | 6 | 132 |
| 8 | 2927/2266 | 1.29170 | 35 | 429 |
| 9 | 122527/86426 | 1.41771 | 162 | 1430 |
| 10 | 2600587/1554026 | 1.67345 | 713 | 4862 |

The n=6 pin **E[r(6)] = 71/66** is confirmed with exactly one collision group (the (3,3)-root pair, weight 1/1008, excess 1/504) — this reconfirms your §6 C2 correction (my earlier 1.0588 was a slip; 71/66 is right). The Monte-Carlo means match these exact values within CI. Collisions proliferate rapidly (1 → 6 → 35 → 162 → 713), which is the mechanism behind the shared-DP mean exceeding 1 and growing (labelled implementer addition, now census-backed).

**The discriminator.** The shared-DP *median* r(n) decays at rate **0.901** (geomean 0.892); the mean, dominated by rare large trajectories, grows explosively (r̄(200) ~ 3×10²⁴) — the multiplicative heavy tail exactly as anticipated. Against the clock's λ = 0.7225: **the forced clock decays deterministically faster than the shared-DP typical run does typically.** The Reading holds.

> **Register "random ≈ 0.79" — flagged.** The validated shared-DP typical rate is 0.901 (median) / 0.892 (geomean); the per-node typical rate is 0.989. None equals 0.79. Given that the register's λ turned out to be a finite-n artifact, its 0.79 is plausibly the same kind of finite-n / small-ensemble reading, but I cannot reproduce it from any natural rate of the census-validated model. The **qualitative** discriminator (deterministic clock beats random-typical) is robust; the specific 0.79 figure is questioned and passed to the lead. *(Note the direction: sharing structure makes the typical run decay* faster*, 0.90 vs the per-node 0.99 — the correlations help, not hurt, typical extinction.)*

### M3 — the gauge audit (the adjudication point)

Both F and G rebuilt from the per-merge weight s(m) = (m+1)ᵃ (no shortcut through r). The extrapolation-independent **trend** column (net Δ ln r over [1000, 4000]) fixes the sign robustly:

| a | λ(a) | trend Δln r | decays? |
|---:|---:|---:|:--:|
| −1.00 | 1.0959 | **+273** | **no (grows)** |
| −0.50 | 0.9346 | −204 | yes |
| −0.25 | 0.8349 | −542 | yes |
| **0.00** | **0.7225** | **−975** | **yes (canonical)** |
| +0.25 | 0.5971 | −1546 | yes (strongest) |
| +0.50 | 0.6447 | −1318 | yes |
| +1.00 | 1.9928 | **+2023** | **no (grows)** |

The picture: a **decay basin** covering the whole natural neighbourhood a ∈ [−0.5, 0.5], with a **maximal-extinction weighting near a ≈ +0.25** (λ = 0.597, well below the canonical 0.722), and a **crossover to growth at the extremes a = ±1**. a = 0 reproduces the M1 constant exactly (internal consistency).

**Adjudication — reported, not decided.** Two readings:
- *Literal M3b:* "if any a makes r bounded below, gauge-removable → kill." a = ±1 give λ ≥ 1, so the literal bar is partially triggered.
- *Intent:* the brief itself states the reweighting *genuinely changes the landscape* — so a = ±1 are different objects, not a removal of the a = 0 decay. The decay is not knife-edge; it survives a broad neighbourhood with large margins, and the canonical object decays robustly.

**My assessment:** this is a **refinement, not a clean kill.** The extinction is a robust feature of the canonical object and its natural neighbourhood; "gauge-robust" is supported in the *qualified* sense of neighbourhood-robustness and must not be overstated as global gauge-invariance. The crossover (decay basin + maximal-extinction weighting a ≈ 0.25) is itself reported structure. **Per §4 ("do not patch, report") the call between "kill" and "refine the Reading's wording" is left to the lead.** I have not altered the Reading.

### M4 — identification

**Route (a), derivation — obstructed, precisely.** The untwisted chain closes because Σ_k G(k)G(n−k) is a genuine Cauchy product, so the generating function satisfies a first-order autonomous ODE that linearises to Bessel. The twist factor ω_{n+1}^k = e^{2πik/(n+1)} depends on the summation index k **and** the output index n **non-separably** — it cannot be written a(k)·b(n−k) for any functions — so Σ_k [phase]·F(k)F(n−k) is not the coefficient of any product of one-variable functions, and **no autonomous generating-function ODE exists** to linearise. What survives is the spectral statement: ζ is the growth constant of the n-dependent transfer family T_n : (F(1),…,F(n−1)) ↦ F(n); because T_n's kernel depends on n through ω_{n+1}, this is a limiting/asymptotic spectral object, not a fixed operator with a fixed spectrum, and closing it in elementary or Bessel terms is exactly what the non-separability blocks. This is the precise analogue, at the level demanded, of E8's empty-split diagnosis: *the phenomenon has a well-defined constant (ζ, hence λ, measured to 7 figures) but no closed form, and the obstruction is the joint (n+1, k)-dependence of the twist.*

**Route (b), recognition — exhaustive negative.** Against the committed list (Bessel-zero rationals 8c/j₁₁², 8/j_ν₁² for small ν and reciprocals, ratios with μ; low-height algebraics; elementary e/π/ln2 combinations of height ≤ 3): **no meaningful lead.** The nearest structural candidate, j₀₁²/8 = 0.7228982, agrees to only **3.2 digits** (differs by 4.2×10⁻⁴) — a clean non-match at the measured precision, recorded here so it is not mistaken later for a near-hit. Every within-band match was a high-height continued-fraction convergent of λ itself (tautological; excluded from leads by the height filter). **Standing rule honoured: no numeric match promoted; λ has no recognised closed form from the committed list.**

### M5 — controls and diagnostics (report-only)

- **Sign control (−1)ᵏ:** rate **1.111 (grows)**. A structural finding: **F₍₋₁₎ᵏ(n) = 0 for *every* odd n ≥ 3** (0 finite odd-n points in [1000,8000]; 999 even) — for odd n the (k, n−k) sign pair cancels identically, so the whole convolution vanishes. The rate is the even-subsequence growth. Verified structural reason it *cannot* extinguish: the sign flip is the (−2x)→(+2x) swap, whose linearisation is I₁(√8x)/√(2x), and **I₁ has no positive real zero** (samples all positive) — no dominant singularity from a zero, hence no destructive pole.
- **Flat control (all phases 1):** rate **3.636 (grows)** — maximal constructive interference, trivial wiring.
- **Ordering confirmed:** flat (3.64) ≫ sign (1.11) > random-median (0.90) > clock (0.7225), i.e. flat ≫ sign ≫ random > clock, matching the register.
- **Split-fraction mass profile:** the twisted convolution concentrates in the **bulk** — |F(k)F(n−k)| mass peaks at k/n = 0.5 at every n, with ~19% in the outer 10% and ~20% in the middle 20% (roughly flat, central-peaked). Diagnostic for route (a): the dominant contributions are balanced merges, not edge terms.

---

## 4. Plain-language summary for Alex

The forced clock's extinction constant is now pinned: **λ = 0.7224793**, good to seven figures. The number in the register, 0.7225535, wasn't wrong so much as *early* — it's what the step-to-step ratio reads at around n = 273, and the ratio keeps sliding down to 0.7224793 as n grows. Three independent checks agree, and the underlying r(n) matches arbitrary-precision arithmetic to fourteen decimals, so this is a genuine sharpening of the register, not a numerical wobble.

The growth constant is a single complex number, ζ ≈ −0.4522 + 0.4350i, spinning at a fixed angle β ≈ 2.3756 per step. That fixed spin is exactly why r decays cleanly: F keeps rotating but its magnitude shrinks at one steady rate, and λ is just that shrinkage measured against the classical baseline.

The census turned the mean's odd behaviour into exact arithmetic. Your instinct that the first "collision" sits at n = 6 is confirmed — one collision there (giving E[r(6)] = 71/66 exactly), then 6, 35, 162, 713 collisions at n = 7…10. That proliferation is why the shared-DP *average* blows up while the *typical* run decays. The right comparison — clock vs. the shared-DP typical (median) run — comes out 0.72 vs. 0.90: **the deterministic clock does, and does better, what randomness only achieves typically.**

Two things need your eye. First, the gauge audit (M3) is the one genuine judgement call. Reweighting the merges keeps the decay solid across the whole natural range and even sharpens it around a ≈ +0.25 — but push to the extremes (a = ±1) and it flips to growth. So the decay is robustly real *in its natural neighbourhood* but not a universal gauge-invariant. Whether that counts as a "kill" of the reading or just a tightening of the word "gauge-robust" is your call — I've left the Reading untouched and reported the whole profile. Second, the register's "random ≈ 0.79" doesn't reproduce — my validated model gives 0.90 typical — and like the old λ it smells of a finite-n reading; flagged, but the qualitative story is untouched.

On identification: route (a) doesn't close, and I can say precisely why — the clock phase ties the merge's *output* size to its *split* point in a way that no single generating function can untangle, so the Bessel trick has no analogue. Route (b) finds nothing in the committed list (the tempting j₀₁²/8 misses at the fourth digit). So λ **parks** as a measured, neighbourhood-robust, seven-figure constant with the obstruction named — which is exactly the full result the brief anticipated.

---

## 5. Honesty caveat

Everything here is a computed identity in a toy twisted convolution. The pins (Bessel μ, the annealed identity, the linearisation chain, the census) are exact-by-construction or arbitrary-precision-verified and graded **Fact**; the extinction phenomenon and its constant λ are graded **Reading**, now *measured and parked*. λ is measured, not derived — its seven figures rest on extrapolation whose honest systematic (the two-window spread, 1.9×10⁻⁷) is reported rather than hidden, and the 8th figure is explicitly banded, not claimed. The gauge crossover is presented in full so the "gauge-robust" descriptor is not overstated; that adjudication is deferred to the lead, not pre-empted. The register discrepancies (λ and the 0.79) are reported as refinements/flags with the mechanism, not swept. No master document was edited; no other experiment was run; implementer additions (the collision census's mechanism note, the sign-control parity structure, the maximal-extinction weighting, the split-mass profile) are labelled and non-substituting.

## 6. Honesty boundary — §1 clause restated (absolute)

**No connection to any zeta object, to the distribution of the primes, or to any open problem is drawn, hinted, or noted in passing anywhere in this experiment.** λ = 0.7224793(2) is a constant of *this twisted merge convolution* and nothing more. Its significance was flagged from the register as pattern-matched rather than derived; E8b's job was to decide, and the decision is that λ is a well-measured, neighbourhood-robust constant with **no** recognised closed form from the committed list and a **precisely-stated** obstruction to derivation — no further reading is licensed, and none is offered.

---

*Alexander Pisani & Claude (Anthropic) · Madness in the Probe sub-programme · July 2026. Lead verification addendum to be appended by the lead on return; no master edits made by the implementing instance.*

---

## Lead verification addendum (appended on return; original text above untouched)

**Independent rerun.** Exit 0; the raw JSON reproduced **identically except the PID field** — every value in M1–M5, every census rational, the full gauge table, and the entire M4b candidate sweep to 10⁻¹² relative or exact. The strongest reproduction of the programme to date.

**The λ revision: endorsed, and the error is the lead's, formally owned.** The register's 0.7225535(60) was the lead's sidecar reading of the local ratio over a single late window; its (60) band quantified statistical scatter while the dominant uncertainty was the unmodelled 1/n convergence of the local ratio toward the asymptote — a systematic-vs-statistical conflation. The corrected λ = 0.7224793(2) is adopted, with the three-route confirmation (log-domain fit; the independent magnitude route |ζ| = 0.6274307 vs √(λμ) = 0.6274304; mpmath validation of r itself) and the honestly banded 8th figure. The single-complex-ζ finding (β = 2.3755680, no conjugate partner) is adopted as the structural explanation of the smooth decay.

**The 0.79 retirement: endorsed, same owner.** The register's "random ≈ 0.79" was the lead's endpoint arithmetic on one seeded run. The census-validated shared-DP rates (median 0.901, geomean 0.892, 500 seeds; per-node typical 0.989) supersede it. The qualitative discriminator survives strengthened, and the implementer's directional note — sharing structure makes the *typical* run decay faster, 0.90 vs 0.99 — is recorded.

**M3 adjudication (the call requested).** Ruling: **refine with demotion; the kill clause does not execute; the bar's failure is recorded without motion.** In full: (i) the committed universal-robustness bar ("decay persists across the family") **failed** at a = ±1 — that is the actual against the fixed bar and stands in the record. (ii) The kill clause's inference — "any a removing decay ⟹ gauge-removable ⟹ bookkeeping" — was mis-drafted by the lead: the same brief states the reweighting *genuinely changes the object*, so the family was never a gauge family and a crossover at its extremes is a regime change, not a removal; the extremes moreover break the Born tie (|A|² = classical weight) that defines the canonical object. A clause cannot execute on a premise the brief itself refutes; the drafting error is the lead's and is owned here with the same candour as the λ band. (iii) The Reading is **demoted accordingly**: "gauge-robust" is retired; the banked characterisation is *deterministic, faster-than-typical extinction of the Born-consistent forced clock, robust across its natural weighting neighbourhood, with the measured basin — including the maximal-extinction weighting near a ≈ +0.25 — part of the object*. The implementer's assessment ("refinement, not clean kill") is concurred with independently, and its refusal to touch the Reading pending adjudication was the correct §4 discipline.

**Adopted findings beyond the brief.** The odd-n vanishing of the sign control is verified analytically by the lead: for odd n the pairing k ↔ n−k gives (−1)ᵏ + (−1)ⁿ⁻ᵏ = 0 term-by-term with no middle term — F ≡ 0 exactly at every odd n ≥ 3; adopted with the I₁-no-zero structural complement. The M4a obstruction statement meets the empty-split standard it was asked to aspire to, and the j₀,₁²/8 non-match is recorded as such so it is never later promoted by wishful memory.

**Process note.** Within one experiment, the implementing instance corrected two of the lead's registered numbers, and the lead corrected the implementer's counterexample arithmetic pre-run; the census then settled all three exactly. The epistemics of the handoff are fully bidirectional, which is the design working.

*Lead instance, July 2026.*
