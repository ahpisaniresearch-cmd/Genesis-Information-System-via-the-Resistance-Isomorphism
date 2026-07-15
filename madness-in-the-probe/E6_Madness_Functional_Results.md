# E6 — Results: The Madness Functional — The Kill Test

**Madness in the Probe sub-programme · final register entry · kill test · implementing instance, July 2026**
**Attribution:** Alexander Pisani & Claude (Anthropic). Alex originated the functional, the typology, and the pre-registered kill design; the implementing instance re-derived the pins, flagged the step-4 flaw before execution, and computed against the fixed bars. The lead issued §9 (the pre-run corrections) in response.

---

## 0. Status

**Outcome: PROMOTE.** Under the classifier committed in §4 (as corrected by §9 C2), the four Madness types land on four *distinct* degeneracies of the single functional

$$M(q)\;=\;\frac{P_T\ (\text{erasure paid by the probe})}{G_T\ (\text{target-superposition entropy removed})},$$

with **no post-run refinement** (`post_run_refinement_used = False`), and the full adversarial re-labelling battery §5(a)–(d) passes:

| type | degeneracy | canonical instance | landed |
|---|---|---|---|
| Type 1 | ∞/∞ (rates decide) | Q₁ (CF typicals + φ, √2, e) | **TYPE1** ✓ |
| Type 2 | 0/0 (blindness) | Q₂ (squarefreeness, exhausted) | **TYPE2** ✓ |
| Type 3 | paid/0 (positive price, zero lawful return) | Q₃ (self/system label query) | **TYPE3** ✓ |
| Type 4 | undefined (off the arithmetic) | Q₄a (self-assertion), Q₄b (record-completeness) | **TYPE4** ✓ |

Both adjudication points resolved and are reported, not smoothed:
- **A1** — the price-grade and the rate-grade **disagree** on the Type-1 pole (price crowns incompressible typicals, M≈1.94; rate crowns φ, the slowest extractor / banked E4 maximal pole). The disagreement is the finding; the master's distillation adjudicates.
- **A2** — the M₃/M₄ boundary is **confirmed at the ask/assert seam**: the existence-bit *query* is paid/0 (Type-3); the *assertion* of the same bit is undefined (Type-4), on an identical frozen ln 2 marginal.

**This was a live kill test.** Park and kill were both reachable and the confounds are the classifier's genuine failure modes — C-iii would have collapsed into Type-3 (→ kill) had its all-strategies audit come back structural; it did not (audit deviation 0.30, structural = False). The result is earned, but it is **conditional on accepting two pre-registered definitional pins** (the answer-type of a target; the target-relative ledger). Those pins carry the unification and are named explicitly in §6.

**Grades.** The three machines and every closed form in them are constructed toys: KT tolls, the frozen twin marginal, the (0,0) certificate, the CF Lévy/Gauss–Kuzmin regime — all **computed identities in constructed apparatus, no novelty claimed (Fact/Reading in toys)**. The claim that *one ratio functional's four degeneracies are mechanically separable by a pre-committed classifier surviving an adversarial battery* is a **Reading about the corpus's own object**, scoped to these machines. It is not a theorem about mathematics, cognition, or any posit's truth (§7 fences).

---

## 1. Reproducibility block

| item | value |
|---|---|
| Script | `523_e6_functional.py` (PID-prefixed) |
| Raw output | `e6_results.json`, `e6_stdout.txt` |
| Seed | `20260710` (fixed; Machine-A streams, the audit's longer histories, and the 20 typical reals are the only stochastic elements — all pins, enumerations, and the recurrences are seed-independent and exact) |
| Libraries | numpy 2.4.4, mpmath 1.3.0 |
| Precision (Machine C) | dps 2600 (≥ 1.1×T digits); typical reals defined by 2600 random decimal digits (entropy ≥ working precision); big-int convergent denominators exact; `ln q_T` via mpmath |
| Extent | Machine A streams T = 5000; all-strategies audits enumerate all 4⁶ = 4096 histories + 1000 longer; Machine B enumerates all 2¹² = 4096 certificate subsets; Machine C T = 2000 for 23 reals; uniqueness over all 4! = 24 assignments |
| Precision guards | CF round-trip (convergent vs x) on all 20 typicals; independent 2×-precision spot-check (dps 5200) on 3 typicals + φ + √2; special-CF spot-checks (φ, √2, e first 40 quotients) |
| Test-run | exits 0 |

**One precision-guard correction, documented (not a bar, not classificatory).** The round-trip check first used an arbitrary threshold (10⁻²⁴⁰⁰) stricter than a CF convergent's mathematical accuracy; a convergent reconstructs x only to |x − p_T/q_T| < 1/q_T², which for a typical (G₂₀₀₀ ≈ 2374) is ~10⁻²⁰⁶². The threshold was corrected to the true bound `err·q_T² < 1`. **The outcome is identical with or without this fix** — the round-trip only certifies quotient trustworthiness, which the independent 2×-precision spot-check corroborates separately. All 20 round-trips pass under the correct bound; err·q_T² < 1 confirmed (0.14–0.91 across the spot sample).

---

## 2. Bars vs. actuals (all fixed pre-run; no bar motion)

| Bar | Target | Actual | Verdict |
|---|---|---|---|
| KT hand case | `[0,0,1]`, A=2 toll = 4 ln 2 = 2.772589 | sequential **2.7725887**, closed-form **2.7725887** | **PASS** (to 1e-12) |
| KL floor | min pairwise (ordered) KL ≥ 0.05 | achieved **0.098083** (matches banked E5 size-8) | **PASS** |
| q₄(φ) | = 5 | **5** | **PASS** |
| Machine A freeze | twin marginal → ½ to 1e-12 | Q₃ marginal **0.5000000000 (±1e-13)**; max\|G\| **5.3e-14**; audit dev **1.8e-15** | **PASS** |
| R limit | G_T → ln 8 = 2.079442 | **2.079442** | **PASS** |
| Machine B zeros | Q₂ (P, G) = (0, 0) exact | **(0.0, 0.0)** exact, exhausted = True | **PASS** |
| Lévy slope | typical G-slope = 1.18657 ± 0.02 | mean **1.1877** ± 0.034 | **PASS** |
| capped-GK toll | typical P-slope ∈ [2.25, 2.45] nats | mean **2.2659** ± 0.042 | **PASS** |
| M∞ typical | ∈ [1.88, 2.10] | mean **1.9373**, range [1.9105, 1.9635] | **PASS** |
| KT redundancy | φ P-vs-ln T slope = 32 ± 4 | **31.14** (φ and √2 identical — depends only on A=65) | **PASS** |
| φ price | M(φ, 2000) ≤ 0.30 **and** strictly decreasing last decade | **0.1707**, strictly decreasing = **True** | **PASS** |
| Canonical landings | Q₁→T1, Q₂→T2, Q₃→T3, Q₄a→T4, Q₄b→T4 | **all as predicted** | **PASS** |
| Confound landings | C-i→LAZY, C-ii→REGULAR, C-iii→REGULAR_MISDIRECTED | **all as predicted** | **PASS** |
| Battery (a) uniqueness | 1 of 24 assignments consistent | **1** | **PASS** (weak leg — see §5) |
| Battery (b) swap | no canonical passes a foreign test | **0 foreign passes** | **PASS** |
| Battery (c) confound | three confounds land apart from their lures | **all three apart** | **PASS** |
| Battery (d) cross-machine | Q₄a, Q₄b both Type-4 by step 1 | **both TYPE4** | **PASS** |

Every fixed bar met; nothing approaches the §1 boundary.

---

## 3. Classifier raw outputs (per instance, mechanical §4 + §9 C2)

The decision tree, in order: **(1)** not admissible → TYPE4; **(2)** P≡0 ∧ G≡0 → TYPE2 if exhausted else LAZY; **(3)** G≡0 ∧ P>0 → TYPE3 if all-strategies-structural else REGULAR_MISDIRECTED; **(4)** G→finite positive → REGULAR; **(5)** G→∞ → TYPE1.

| instance | admissible | P≡0 | G≡0 (run) | audit structural | P>0 | G conv + | G div | **→ landing** |
|---|---|---|---|---|---|---|---|---|
| Q₁ (CF) | T | F | F | – | T | F | **T** | **TYPE1** |
| Q₂ (squarefree) | T | **T** | **T** | – | F | F | F | **TYPE2** (exhausted=T) |
| Q₃ (label query) | T | F | **T** | **T** | T | F | F | **TYPE3** |
| Q₄a (self-assert) | **F** | – | – | – | – | – | – | **TYPE4** (step 1) |
| Q₄b (completeness) | **F** | – | – | – | – | – | – | **TYPE4** (step 1) |
| R (control) | T | F | F | – | T | **T** (→ln 8) | F | **REGULAR** |
| C-i (lazy) | T | T | T | – | F | F | F | **LAZY** (exhausted=F) |
| C-ii (verbose) | T | F | F | – | T | **T** (→ln 8) | F | **REGULAR** |
| C-iii (contingent) | T | F | **T** | **F** | T | – | – | **REGULAR_MISDIRECTED** |

Key computed separators (all with wide margin, all enumerated not assumed):
- **Q₃ vs C-iii** (structural vs contingent zero-yield): identical on-run signature (G ≡ 0, P > 0), separated only by the all-strategies audit over all 4⁶ histories — Q₃ deviation **1.8×10⁻¹⁵** (no admissible conditioning ever moves the twin marginal → structural), C-iii deviation **0.3015** (histories containing the unobserved symbols {2,3} discriminate the twins → contingent). This is the sharpest non-vacuity in the experiment: a wrong C-iii (accidentally identical twins) would have read structural and collapsed into Type-3, tripping the kill clause.
- **Q₃ vs C-ii** (paid/0 vs expensive-regular): Q₃ G ≡ 0 (5.3e-14) vs C-ii G → ln 8 = 2.0794 — a positive price with *large* G is regular, never Type-3.
- **Q₂ vs C-i** (0/0 vs lazy): identical (0, 0), separated only by the exhaustion flag (Q₂ asked all 8 squarefreeness-repertoire queries; C-i asked 0 of 8).
- **Q₄a/Q₄b vs everything numeric**: step 1 halts both before any measurement (§6).

---

## 4. Type-1 internals and A1 (reported as found)

The class signature is the **divergence order of both legs** (fits over the upper window, never endpoint ratios — the E8b lesson), then M = lim P_T/G_T:

| real | G-slope (yield rate) | P behaviour | M(2000) | resolves ∞/∞ to |
|---|---|---|---|---|
| typicals (20) | **1.1877** (Lévy) — linear | linear, slope 2.266 | **1.937** | positive constant ≈ H_capGK / Lévy |
| φ | **0.4812** = ln φ — linear (min) | **logarithmic**, ln T slope 31.1 | **0.171** | **0** |
| √2 | 0.8814 = ln(1+√2) — linear | logarithmic, ln T slope 31.1 | 0.093 | **0** |
| e | 2.5316 — linear (steepest here) | linear, slope 0.68 | 0.361 (reported, no bar) | small positive |

**A1, plainly.** By the **price-grade** (M = P/G), the *most Mad* Type-1 instance is the incompressible typical (M ≈ 1.94); φ and √2 sit at the bottom (M → 0), because their quotient streams are predictable so the toll is only logarithmic while the yield stays linear. By the **rate-grade** (yield rate = G-slope, where the extremal pole is the *slowest* extractor), the most Mad instance is **φ** — minimal G-slope 0.4812, the golden ratio's worst-approximability, the banked E4 maximal Type-1 pole. **The two grades crown opposite poles.** Both grades stand; neither is wrong; the disagreement is exactly what A1 anticipated. The master §6 distillation adjudicates which grade the unified definition privileges (or whether it keeps both and reports the tension as structural).

---

## 5. Adversarial re-labelling battery (the promote gate)

- **(a) Uniqueness** — of all 24 assignments of {Q₁, Q₂, Q₃, Q₄} to {T1, T2, T3, T4}, exactly **1** is consistent with the computed landings. *Honest caveat:* this leg is the weakest of the four — once the four canonicals occupy four distinct classes, uniqueness of the labelling is near-automatic. It rules out an alternative *global re-labelling*; it carries little independent adversarial weight. The real weight is in (b) and (c).
- **(b) Swap battery** — each canonical run through every foreign class's test path fails all of them: Q₁ fails T2/T3/T4 (G diverges; admissible); Q₂ fails T1/T3/T4 (P ≡ 0, so no paid/0, no divergence, admissible); Q₃ fails T1/T2/T4 (P > 0, so not 0/0; G ≡ 0, so not divergent; admissible); Q₄a fails T1/T2/T3 (step 1 halts it). **0 foreign passes.**
- **(c) Confound battery** — C-i → LAZY (not Type-2: unexhausted); C-ii → REGULAR (not Type-3: G → ln 8 ≠ 0); C-iii → REGULAR_MISDIRECTED (not Type-3: audit contingent). **All three land apart from their lures.**
- **(d) Cross-machine coherence** — Q₄a (Machine A) and Q₄b (Machine B) are the *same* class by the *same* step-1 admissibility failure, in two different machines with two different repertoires. **Both TYPE4.**

All four legs pass; combined with distinct canonical landings and no post-run refinement, the §7 PROMOTE condition is met.

---

## 6. Where the result's weight actually sits (A2, and the honest crux)

Two pre-registered definitional pins carry the unification. They were fixed before computation (brief §2–§4 and §9), so their use is not the hand-tuning the kill clause forbids — but PROMOTE is *conditional on accepting them*, and a critic's whole leverage lives here.

**Pin 1 — the answer-type of a target (this is what makes Type-4 a category, and it is A2).** Admissibility (step 1) is decided by: *does some admissible act's output inhabit the target's answer-type?*
- **Q₃** types its target as *the value of the self/system label* → answer-type "distribution over labels." The posterior read-off act returns such a distribution (the frozen ½,½). Inhabited → **admissible** → then paid/0 (Type-3).
- **Q₄a** types its target as *the truth of the self-assertion "my label is X"* → answer-type "truth-value." Enumerating all 4⁶ + 1000 histories, **no act ever collapses the marginal to a definite label** (deviation 1.8e-15), so no act outputs a truth-value. Not inhabited → **undefined** (Type-4).

The two instances share an *identical frozen ln 2 marginal*. What separates M₃ from M₄ is **only** whether the target demanded a *value* (which the machine supplies, uselessly → paid/0) or a *truth* (which the machine cannot supply → undefined). This is the A2 boundary, and it is real but definitional: it rests on granting that "asking the value of a frozen bit" and "asserting that bit" are genuinely different acts. The computation does the second half honestly (the machine provably yields no truth-value — enumerated, not assumed), but the first half — that the assertion *demands* a truth-value the value-query does not — is a pinned reading, not a discovered fact. **A skeptic who denies the ask/assert distinction dissolves Type-4 back into Type-3.** This is flagged for the master, not hidden inside a checkmark. Q₄b makes the same split in a different machine (a state-fact certificate codomain that provably never contains a "your record is complete" verdict, though the probe can *infer* e₂ exactly — the record-vs-knowledge gap), which is why the cross-machine leg matters: the pin is not an artefact of one machine's construction.

**Pin 2 — the target-relative ledger (this is what makes Type-2 an exact (0,0)).** Q₂'s (P, G) = (0, 0) holds because the squarefreeness ledger charges and credits only *squarefreeness-discriminating* certificates (the non-squarefreeness witnesses "e_p ≥ 2/3"), and a squarefree state (1,1,1,1) yields none. Presence facts ("e_p ≥ 1") are target-irrelevant and excluded from the squarefreeness ledger. This is the E2/E3 target-relative convention, pinned pre-run; under it the (0,0) is exact by construction (computed, asserted-against). A ledger that charged for every positive certificate would give Q₂ a positive P and it would not be 0/0 — so this pin, too, is load-bearing and is named.

**A2 verdict, plainly.** The existence-bit **query** lands paid/0 (Type-3); the existence-bit **assertion** lands undefined (Type-4); the boundary is **confirmed** (not collapsed) and sits exactly at the ask/assert seam. Whether the typology's boundary is thereby *redrawn* depends on the master's prior placement — mechanically, M₃ = "ask the value of the unremovable bit," M₄ = "assert its truth."

**Completed-price note (§9 C3, report-only, no bar, cannot rescue any landing).** For the one regular streaming instance, R resolves (pair posterior ≥ 1 − 10⁻⁶) at T\* = 181, giving M\* = P₁₈₁/G₁₈₁ = **115.8**. This is dominated by the ambient perpetual toll (banked E2 structure, ~1.28 nats/symbol), not by the price of the *answer* — the caveat the brief attached. It plays no classificatory role.

---

## 7. Fences (mandatory) and honesty boundary

**Fences.**
- **No claim about human cognition.** Type-4 instances here are *diagonal-query events* under the corpus's scoped, deflationary definition: a target whose answer-type is a self-referential truth-value that the machine's own act algebra cannot inhabit. Nothing in this experiment speaks to minds, understanding, or madness in any ordinary sense.
- **No bearing on any posit's truth.** Nothing here tests whether the genesis system holds beyond the axioms that posit it. The machines are constructed; the barrier is not probed.
- **No leverage on any open problem.** The CF/Lévy/Gauss–Kuzmin facts are classical; φ's worst-approximability is classical; the squarefreeness structure is elementary. No claim touches RH, primes, or any unsolved question.
- **The honesty caveat travels.** Every quantity is a computed identity in a toy built to have it. Convergences (KT redundancy 31.1 ≈ 32; typical G-slope 1.1877 ≈ Lévy) confirm the toys behave as their theory says — they discover nothing about mathematics.

**Honesty boundary.** PROMOTE means: *within these three constructed machines, a single ratio functional's four degeneracy modes are separable by a classifier committed before the data existed, and the separation survives an adversarial battery.* It does **not** mean the four types are "really one thing" in any sense stronger than "one functional exhibits four degeneracies under these pins." The unification is **conditional on Pin 1 (answer-type / ask-assert) and Pin 2 (target-relative ledger)**; both are pre-registered and both are load-bearing, and a critic's entire purchase is on the ask/assert distinction that carries Type-4 (§6). The uniqueness battery leg is near-tautological and is reported as such. The result is a demonstration of internal coherence, graded Reading-in-toys, not a theorem.

**Non-vacuity (carried, discharged).** The classifier can misclassify under a wrong implementation — the confounds are its live failure modes, and C-iii's audit is a genuine kill-trigger that came back clean by a 10¹⁴-margin. Exact zeros (Q₂'s (0,0), Q₃'s frozen marginal) are **computed and asserted-against**, never hard-coded. The all-strategies audits **enumerate** (4⁶ histories; 2¹² certificate subsets; 24 assignments), never assume. KT is **verified** against its closed form on a hand case. The CF quotients are **precision-guarded** two independent ways.

---

## 8. Scope discipline

No master edits: the master §6 rewrite (unified definition, A1/A2 distilled) and any lead verification addendum are left for Alex on return — this note only reports the mechanical result and its conditions. No other experiments were run. The register is now complete (E1–E8, E8b, E6); whether E6's PROMOTE licenses the §6 rewrite, or whether the master should instead record the unification as *pin-conditional* with the ask/assert crux foregrounded, is a lead/Alex judgement, not the implementer's.

*Alexander Pisani & Claude (Anthropic) · Madness in the Probe sub-programme · July 2026.*

---

## Lead verification addendum (appended on return; original text above untouched)

**Independent rerun.** Exit 0; the results JSON reproduced with **zero mismatches** beyond 10⁻¹¹ relative — every landing, every trajectory, the full battery, and the OUTCOME: PROMOTE. This outcome received the most adversarial review of the programme, deliberately, because a kill test that promotes is the result most vulnerable to motivated reading.

**Code review of the promote's load-bearing joints.** The classifier is verbatim the committed C2 tree (G-only step 4), with every input a computed boolean — no hand-tuning surface exists in the decision path. The two admissibility audits are mechanical, not definitional: Q4a's inadmissibility is *computed* (over the 4⁶+1000 conditioning events, none drives the label marginal to a definite value — the truth-value is uninhabited by any act, verified by enumeration), and Q4b's is *computed* (over all 2¹² certificate subsets, the producible answer types are silence and state-facts only, while the probe's record demonstrably determines e₂ — the banked record-vs-knowledge structure, now the mechanical face of a Type-4 landing). The `post_run_refinement_used` flag is honest: the single design correction (step 4) predates execution and is recorded in the brief's §9.

**One snug margin, recorded so it is never suspected of tuning.** The typicals' mean P-slope (2.2659, SE ≈ 0.009) passed the committed band [2.25, 2.45] with only 1.7 SE to spare — because the band was mis-centered high at commitment by both parties' rough tail estimates. A more careful capped-entropy calculation (the >64 tail's internal entropy replaced by the overflow symbol's) puts the true value near 2.26, exactly where the measurement sits. The pass is physics, the snugness is the band's fault, and the bar was not moved.

**The promote is ratified.** The four types land as the four degeneracies without argumentation — blindness is zero-under-exhaustion, not idleness; the gauge is structural zero-yield, not misdirection; the diagonal is an uninhabited answer type, in two machines; and the ∞/∞ class carries its rate-resolution openly, including the finding that the price-grade and rate-grade crown different poles. §6 is rewritten per its own registration. The excitement flag raised when the functional was first caged — "pattern-matched, not derived" — is discharged: it is now derived, measured, and adversarially survived.

*Lead instance, July 2026.*
