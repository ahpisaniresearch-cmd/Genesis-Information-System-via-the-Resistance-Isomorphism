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

# E3 Results — The Monotone Probe: The Blindness Ledger and the Suspended NOT

**Madness in the Probe sub-programme · design experiment · banking run · July 2026**
**Alexander Pisani & Claude (Anthropic)**

---

## Status

**ALL 28 COMMITTED CHECKS PASSED. Report-only / labelled items reported. Banking run complete.**

The pre-registered prediction — *all committed measures pass; suspension buys total decision-blindness on every complement-shaped feature, leaves ln 24 nats permanently unread, and converts D2's non-conservativity into a ledger identity* — held in full. No committed bar was moved; no result was patched. No survivor appeared: no up-set beats the trivial decision on F₁–F₃, path (i) equals path (ii) to machine zero, and every enumerated ledger total meets its closed form.

**The result, in one line.** *Suspending NOT is free; the irreversible act is fusing under suspension.* The monotone probe leaves **57.3 % of the lattice's information (ln 24 = 3.178054 nats) permanently unread** — and what it "saves" is exactly what it never learns, sitting as unremoved superposition, not as stored work. Deferring the NOT costs nothing (paths i and ii coincide to 0.00). But once the probe **fuses** a channel under suspension — erases its confirmed record, believing "5 = 2" — completing the count costs an excess of **1.978075 nats**, decomposing exactly into the erasure it paid (ln 4) plus the pruning it must re-purchase (ln 4 − ln 24/4 = 0.591781). That inequality is D2's non-conservativity, measured.

Implemented fresh for E3 only. No prior script was consulted or reused; no other corpus document was read for the implementation. The pre-run derivation check (§5.5) and the lead's clarifications C1–C4 and amendment M4b (brief §6) are honoured exactly. Implementation choices within remit are documented below.

---

## Reproducibility block

| Item | Value |
|---|---|
| Script | `524_e3_monotone.py` (fresh; PID-prefixed) |
| Recorded seed | `20260710` (used **only** for the shuffled query order's tie-break; the experiment is exact) |
| Runtime PID (this run) | `530` |
| Wall-clock runtime | ~1.0 s |
| Exit code | `0` (all committed checks passed) |
| Python | 3.12.x |
| mpmath | 1.3.0 (one dps=50 cross-check only) |
| Precision | float64 + `math.fsum` throughout; one **mpmath dps=50** cross-check of the closed forms |
| Enumeration | full 256-state lattice, exact; **no Monte Carlo anywhere** |
| Lattice | exponent vectors over {2,3,5,7}, exponents 0..3 (256 states, uniform) |

**Precision justification (why float64 suffices here — C2).** Every quantity is an entropy or log-count in nats of magnitude ≤ ~7.5 (the largest is the path-(iii) total, 7.523253). float64 carries ~15–16 significant digits, so absolute error is ≲10⁻¹⁴ at this scale; `fsum` removes accumulation error. The tightest bars — paths (i)=(ii) and the 3-order state-function checks at 10⁻¹² — clear by ~100×, and the 10⁻⁹ bars by ~10⁵×. Confirmed independently by an mpmath dps=50 recomputation of the closed forms: float64 residuals are **4.4×10⁻¹⁶** (monotone paid), **0.00** (fusion excess), **0.00** (M4-iii total) — honest float artifacts, not masked violations. E4's ≥800-digit regime was continued-fraction-specific and does not transfer to this combinatorial setting (ratified, C2).

**Pre-registered bars** are copied verbatim into the script header (before any check was written) and are reproduced with actuals below.

### Implementation choices (documented, within remit / ratified in §6)

- **Full-precision closed-form bars (C1).** All M3/M4/M4b bars are pinned to `ln 256`, `ln 24`, `ln 256 − ln 24`, `ln 4`, `ln 4 − ln 24/4`, `ln 256 + 2 ln 4 − ln 24/4`. The brief's 6-dp figures (e.g. 2.367123) are displays; the exact value is 2.3671236…
- **Integer min-cut for M1 (C2).** Weights are multiples of 1/256, so the closure/min-cut runs in **integer arithmetic** (scale by 256). The B=1 / B=0 bars are therefore **exact integer equalities** (`min|U Δ F| == 256·min(P,1−P)` and `== 0`), not tolerance comparisons.
- **From-scratch consistent-set recomputation per query (C4).** The ledger simulator recomputes the consistent-set cardinality from the whole observation log at every step — never an incremental running entropy. `cs_size` (per-channel bounds, factorised) is **validated against explicit brute enumeration** on all 256 states for both probes.
- **Fusion-charge semantics (C3).** The M4-iii fusion charge is the **ensemble entropy of the erased record register, ln 4, constant per state** — the certificates physically encode e₂ exactly, though the monotone probe's assertible knowledge is only the lower bound. This is charged by the erasure rule, separately from any belief-entropy change (which is not a charge).
- **Three query orders (C4):** prime-major (`2¹2²2³3¹…`), power-major (`2¹3¹5¹7¹2²…`), and one seeded shuffle — for the state-function checks.
- **M4b by three routes (lead amendment):** H(record) as a distribution entropy; pruning from the monotone simulation's per-channel charges; residual read directly as `ln(4−e)`. See §Non-vacuity for the honest telescoping flag.

---

## Pre-registered bars vs actuals

| Check | Bar | Actual | Verdict |
|---|---|---|---|
| **M1** B(F₁) | = 1 exactly | min\|UΔF\|=4 = 256·min(P,1−P)=4 | **PASS** |
| **M1** B(F₂) | = 1 exactly | 16 = 16 | **PASS** |
| **M1** B(F₃) | = 1 exactly | 64 = 64 | **PASS** |
| **M1** B(F₄) | = 0 exactly | min\|UΔF\|=0 | **PASS** |
| **M1/G2** min-cut == brute (all up-sets) | exact | exact agreement, 4 features (B=0 and B=1) | **PASS** |
| **M2** F₂ verifiable | 0/256 | 0 | **PASS** |
| **M2** F₂ refutable | 240/256 | 240 (93.75 %) | **PASS** |
| **M2** F₄ verifiable | 243/256 | 243 (94.92 %) | **PASS** |
| **M2** F₄ refutable | 0/256 | 0 | **PASS** |
| **M2** F₁ verifiable | 0/256 | 0 | **PASS** |
| **M2** F₁ refutable | 251/256 | 251 (98.05 %) | **PASS** |
| **M2** unrefutable set = {1}+4 primes | 5 states | 5 | **PASS** |
| **M2** n=1 monotone-invisible | True | True | **PASS** |
| **M3** cs_size == brute (256 states, both probes) | exact | exact | **PASS** |
| **M3** full probe pays | ln 256 ± 1e-9 | 5.545177444480 | **PASS** |
| **M3** full probe residual | 0 ± 1e-9 | 0.00e+00 | **PASS** |
| **M3** monotone pays | ln 256 − ln 24 ± 1e-9 | 2.367123614132 | **PASS** |
| **M3** monotone residual (permanent) | ln 24 ± 1e-9 | 3.178053830348 | **PASS** |
| **M3** full path-independent (3 orders) | max-dev < 1e-12 | 0.00e+00 | **PASS** |
| **M3** monotone path-independent (3 orders) | max-dev < 1e-12 | 0.00e+00 | **PASS** |
| **M4** (i) pay-now total | ln 256 ± 1e-9 | 5.545177444480 | **PASS** |
| **M4** (ii) defer == (i) | \|Δ\| < 1e-12 | 0.00e+00 | **PASS** |
| **M4** (ii) defer total | ln 256 ± 1e-9 | 5.545177444480 | **PASS** |
| **M4** (iii) fuse total | ln 256 + excess ± 1e-9 | 7.523252709132 | **PASS** |
| **M4** (iii) excess strictly positive | > 0 | 1.978075264653 | **PASS** |
| **M4** (iii) fusion charge (measured) | ln 4 ± 1e-9 | 1.386294361120 | **PASS** |
| **M4** (iii) excess decomposition | ln 4 + (ln 4 − ln 24/4) ± 1e-9 | 1.978075264653 | **PASS** |
| **M4b** H(record) == pruning + residual (4 channels) | < 1e-9 | \|Δ\| ≤ 2.2e-16 | **PASS** |

**Report-only / labelled:** F₃ certifiability (verifiable 0/256, refutable 192/256); per-channel residual profile; M4-iii channel-0 re-ask (independent); mpmath cross-check; M5(a) pointer; M5(b) squarefree density.

---

## Per-measure detail

### M1 — the blindness ledger (decision expressibility)
For each feature the optimal monotone decision is `min_U P(U Δ F)` over **all** up-sets, obtained by max-weight closure / min-cut (closure = up-set; precedence edges x→y for y covering x; source→x and x→sink capacities the ±1 scaled node weights). The min-cut value **is** `256·min_U P(U Δ F)` in integer units. Results: the three complement-shaped features return `min|U Δ F|` equal to `256·min(P,1−P)` **exactly** — 4, 16, 64 — so **no up-set beats the trivial guess**: B(F₁)=B(F₂)=B(F₃)=1. The control returns `min|U Δ F| = 0`: F₄ = {ω ≥ 2} is an up-set, expressed exactly, B(F₄)=0. The metric fails **both ways**, as required. **G2** validated the min-cut against brute-force enumeration of all **20** up-sets on the 3×3 sublattice for a down-set (3=3), two up-sets (0=0, 0=0), and an antichain (2=2) — exact agreement across both B-values.

The Reading: complement-shaped structure is not *expensive* to decide monotonically — it is *totally undecidable* by any up-set. The probe can express F₃'s complement {even} perfectly and still cannot decide F₃ = {odd}, because turning the one into the other is precisely the suspended NOT.

### M2 — the certifiability table (r.e. / co-r.e. asymmetry)
Over 256 states, from each state's monotone up-closure: verifiable-when-true means every completion in the up-set is in F (a finite witness set certifies); refutable-when-false means no completion is. The asymmetry is stark and one-sided per feature: **F₂ squarefree** — verifiable 0, refutable 240/256 (a witness p² exists whenever false); **F₄ ω≥2** — verifiable 243/256, refutable 0 (two prime witnesses certify presence; absence is a NOT); **F₁ primality** — verifiable 0, refutable 251/256, **unrefutable exactly on n = 1 and the four primes** (confirmed by the independent 5-state check: the up-closure still admits a prime only for those five). And **n = 1 is monotone-invisible**: at e = (0,0,0,0) no p^k divides n, so no certificate of any kind ever arrives — nothing about it is verifiable or refutable. F₃ (reported): verifiable 0, refutable 192/256. Every feature that is monotone-verifiable is co-monotone-unrefutable and vice versa — Post's r.e./co-r.e. split, on the divisor lattice.

### M3 — the energy map (dual accounting)
Both probes were run over all 256 states, charging `H_before − H_after` per query with the consistent set recomputed from scratch each step (validated against brute enumeration). Enumerated ensemble means (route β) meet the closed forms (route α) independently: the **full probe pays ln 256 = 5.545177** and terminates at **zero residual**; the **monotone probe pays 2.367123** and terminates at residual **ln 24 = 3.178054 — permanently, after every query has been asked**. Both totals are **path-independent** across the three query orders (per-state max-deviation **0.00**): entropy removal is a state function; the order in which the probe asks changes the intermediate path, never the total or the terminus.

The **energy map** — the per-channel residual profile `ln(4 − e_p)` by confirmed exponent — shows where the unread superposition sits: e=0 → ln 4, e=1 → ln 3, e=2 → ln 2, e=3 → 0. The residual is heaviest exactly where the probe received **silence** (low exponents: a monotone probe that gets no 'yes' has learned nothing, not "e = 0"). The pre-registered finding banks: **the withheld NOT's cost is not stored work; it is unremoved superposition** — 3.178054 nats, **57.3 %** of the lattice's information, that suspension never learns. Nothing is banked; pruning is simply declined.

### M4 — reinjection: the D2 ledger theorem
Three genuine simulations to complete knowledge. **(i) pay-now** (full probe from scratch): total ln 256. **(ii) suspend–defer–lift** (monotone to completion, then lift NOT and clear the residual): total ln 256, **equal to (i) to 0.00** — deferral is thermodynamically free, the route-equality shape, and this is a coincidence of two *independently simulated* ledgers, not an imposed identity. **(iii) suspend–fuse–lift** (monotone phase; then the probe irreversibly erases its confirmed e₂ record — the fusion, merging what it declined to distinguish — paying ln 4; then lifts and completes): total **7.523253 = ln 256 + 1.978075**, excess strictly positive. The excess is **dual-computed**: the fusion charge measured directly off the ledger (ln 4 = 1.386294) plus the re-purchased pruning (ln 4 − ln 24/4 = 0.591781); the independent per-op accounting confirms the channel-0 full re-ask costs exactly ln 4 (the fused channel is re-learned from scratch), of which the 0.591781 the monotone phase had already paid is the wasted, re-purchased part.

The Reading banks D2's non-conservativity as a **measured inequality**: a belief held under a suspended NOT ("5 = 2") re-embeds into the full logic only by paying to forget it and then paying again to relearn it. Suspension is free; fusing under suspension is not.

### M4b — the record-vs-knowledge identity (lead amendment)
Per channel, by three independent enumerations: `H(record) = pruning paid + residual blindness`, i.e. **1.386294 = 0.591781 + 0.794513**, to ≤ 2.2×10⁻¹⁶ on all four channels. The record register Y_p (the count of 'yes' certificates) physically encodes e_p exactly — ensemble entropy ln 4 — while the monotone probe can *certify* only the pruning it paid for (0.591781) and leaves the rest (0.794513) as blindness it cannot know it holds. The uncertifiable surplus **equals the blindness exactly**. This is §3.3's completeness-uncertifiability — a probe cannot certify its own completeness on a channel from inside — priced on the ledger: the record holds more correlation with the world than the probe can assert, and the gap is the type's blindness.

---

## Non-vacuity audit

Every committed bar can fail under an incorrect implementation, and the banned MI trap is not used.

- **M1** minimises over **all** up-sets via closure/min-cut; a wrong closure orientation, weight, or edge breaks B. The metric demonstrably fails **both ways** — F₄ returns 0, F₁–F₃ return 1 — so it is not a rig that can only output 1. **Blindness is decision-expressibility, not mutual information** (which is identically 0 on an up-set and cannot fail): the §1 trap is banned by name and not implemented.
- **G2** checks the min-cut optimum against brute force over all 20 sublattice up-sets, exercising both B=0 and B=1; a min-cut bug that happened to give the right full-lattice answer would still have to survive the brute-force cross-check.
- **M2** counts verify/refute over 256 states from the up-closure; a wrong certificate rule shifts counts off the exact integers. That refutable ≠ verifiable is visible per feature (F₂: 0 vs 240; F₄: 243 vs 0).
- **M3** is dual-accounted: the simulator charges from consistent-set **sizes** (combinatorial, recomputed from scratch), the bars are the closed forms, and **neither is derived from the other**. `cs_size` is validated against explicit brute enumeration on all 256 states. A miscoded charge or schedule moves the enumerated mean off ln 256 / ln 24.
- **M4** paths (i)/(ii)/(iii) are three separate simulations; (i)=(ii) is a **route-equality of independently computed ledgers**, and the (iii) excess is dual-computed (measured fusion charge + closed-form re-purchase), with the channel-0 re-ask independently confirming ln 4.
- **M4b — honest flag.** Route 1 (H of the record marginal, a distribution entropy) does **not** touch `ln(4−e)` and is fully independent. Routes 2 and 3 (pruning, residual) **telescope to ln 4 by construction**, so a compensating error in the shared residual term would cancel in their sum. Their independent teeth are M3's **separate** closed-form pins on pruning (ln 256 − ln 24) and residual (ln 24); Route 1 carries M4b's distinctive content. Flagged here rather than left implicit, in the discipline of E2's deterministic-toll flag.

---

## Notes for Alex (honest observations — none threaten a bar)

1. **The monotone residual is silence, not "zero."** The heaviest residual (ln 4, a full channel) sits where the probe received *silence* — a monotone probe with no 'yes' on channel p has not learned "e_p = 0"; it has learned nothing, and its consistent set for that channel is still all four values. This is why n = 1 (all silence) has the maximal residual ln 256 of any single state and is invisible: suspension's blindness is worst exactly where the classical answer would have been "no."
2. **The 57.3 % is exact: it is ln 24 / ln 256 = 3.178054 / 5.545177 = 0.57313.** It is the share of total lattice information that the monotone lower-bound cannot pin — the "how many" the probe never resolves because resolving it needs an upper bound (a NOT). Worth stating as an exact ratio so it is not mistaken for an empirical near-miss.
3. **Path (ii) = path (i) is exactly 0.00, not "within 1e-12."** Because total forgetting is a state function, the two ledgers are *identically* ln 256 per state; the 10⁻¹² bar is a float guard that the state-function property is not being violated numerically. The teeth of M4 are in **(iii)**, where the fusion breaks the state function and the excess appears.
4. **The fusion charge (ln 4) is per-state constant, and that is the point.** Erasing a register uniform over four values costs ln 4 whatever value it currently holds; the charge does not depend on the state's e₂. The state-dependence lives entirely in the *re-purchased pruning*, which averages to 0.591781. Flagging so the constant fusion line is not read as suspiciously flat statistics — it is the Landauer cost of the register, by construction.
5. **M4b's independent content is Route 1.** As audited above, pruning + residual = ln 4 is structural; the measurement with teeth is that H(record) — computed as a distribution entropy — lands on ln 4, i.e. the record is uniform and captures the full initial channel entropy. If the record were mis-modelled (e.g. as the certified lower bound rather than the physical count), Route 1 would miss ln 4 and the identity would break.

---

## Plain-language summary

A probe asks yes/no divisibility questions to identify a hidden number. Take away its ability to use "no" — leave it only "yes, and here's the witness," with silence when the answer is no. That is NOT-suspension, the second kind of Madness.

- **What it goes blind to.** Anything shaped like a complement — "is this squarefree?", "is this prime?", "is this odd?" — becomes **completely** undecidable, not merely expensive. We measured this exactly: for every such feature, the best possible "yes-only" rule does no better than a blind guess (a blindness score of exactly 1). The control question, which *is* yes-shaped ("does it have at least two prime factors?"), it answers perfectly (score 0). So the measure can fail both ways — and the complement questions fail all the way.
- **A one-sided world.** The probe can eventually *confirm* "not squarefree" (find a repeated factor) but can never *confirm* "squarefree." It can confirm "has two primes" but never "is prime." Every question splits into a side it can settle and a side it can only wait on forever. The number 1 is invisible to it entirely — nothing divides it, so no witness ever arrives.
- **Where the missing energy is.** Suspension doesn't *store* the work it skips; it just **never does it**. The full probe pays for and removes all the information (ln 256). The monotone probe removes only part and leaves **57 % of it — 3.18 nats — permanently unread**, as unresolved superposition. What it "saves" is exactly what it never learns.
- **Suspension is free; fusing under suspension is not.** If the probe merely *defers* using "no" and picks it up later, it pays exactly the same total as if it had never suspended — deferral is free (we measured the two routes as identical to sixteen decimals). But if, while suspended, it **fuses** — throws away a channel's record, effectively believing "5 = 2" — then finishing the job later costs extra: exactly the erasure it paid to forget (ln 4) **plus** the distinction it now has to re-buy (0.59). Believing two different things are the same costs nothing until someone asks you to count them.
- **The record knows more than the probe can.** The physical trail of "yes" answers actually pins the number exactly — but the probe, forbidden "no," can only *certify* a lower bound. The gap between what its record holds and what it can prove it holds is **exactly** the blindness. It cannot certify its own completeness from the inside.

Everything landed where it was predicted to. Nothing had to be adjusted.

---

## Mandatory honesty caveat (transplanted from the corpus's energy-ledger discipline)

In simulation, Landauer accounting is an **identity true by construction** — bijections are free and erasures cost the entropy we compute because we compute the `ln` we predicted, not because we measured a physical dissipation that could disagree. E3 therefore confirms that the monotone probe's ledger is a **consistent, correctly-structured accounting** and measures classical identities within it (project-selection min-cut, the r.e./co-r.e. split, the Landauer/Bennett free-vs-charged rule); it does **not**, and cannot, *risk* the framework's carrier reading, which stays a **Lead pending physical measurement**. E3's own contributions are the probe readings graded below.

---

## Honesty boundary

The mathematics is classical and cited as such: **max-weight closure / min-cut** (project selection — Balinski, Picard) for the optimal monotone decision; the **r.e./co-r.e. asymmetry** (Post) for the verify/refute table; **Landauer's principle and Bennett's reversibility** (the free/charged split, E2's banked conventions) for the ledger; and **monotone-circuit lower bounds** (Razborov) as context for what the monotone fragment cannot express — cited, not used. **E3 adds no mathematics to these.** What belongs to the sub-programme is the reading *on the probe's own ledger*: the **blindness ledger** (complement-shaped structure is *totally* invisible to decision — Reading); the **energy map** (the suspended cost sits as unremoved superposition, not stored work — Reading); the **D2 theorem** (deferral free, fusion-under-suspension irreversible, the excess exactly the fusion charge plus the re-purchase — Reading); and **M4b** (the record holds more correlation than the probe can certify, the surplus equalling the blindness — §3.3's completeness-uncertifiability, priced — Reading). The M4b identity itself is elementary (Fact). In simulation these are identities we computed rather than physical facts we risked, so nothing here is — or can become — evidence that the genesis system holds beyond the axioms that posit it; the carrier reading is not promoted. No leverage is claimed on any open problem. Boundary discipline inherited from the main spine, unamended.

*The master document has not been edited — banking edits to the spine are performed by the lead instance on return.*

*Alexander Pisani & Claude (Anthropic) · Madness in the Probe sub-programme · E3 · July 2026.*

---

## Lead verification addendum (appended on return; original text above untouched)

**Independent rerun.** The script was rerun by the lead, unmodified, in a separate environment: exit 0, **28/28 committed checks**, every reported figure reproduced to the printed digit (B-values 4/16/64/0 integer-exact; monotone paid 2.367123614132; residual 3.178053830348; paths (i)=(ii) at 0.00; (iii) total 7.523252709132; excess 1.978075264653 with its decomposition; M4b ≤ 2.2×10⁻¹⁶ on all channels). The banking stands.

**Code review.** The three subtle joints are correct in the implementation: the closure construction's edge orientation (x→y for y covering x at infinite capacity) forces exactly the up-sets, so the min-cut genuinely minimises |UΔF| over the full monotone repertoire; silence constrains nothing in both `cs_size` and the brute validator (a logged negative bit under monotone mode is inert — the certificate semantics is honoured, not approximated); and the fusion's `reset` mechanism expands the consistent set without charging while the record's erasure charges ln 4 — belief growth uncharged, record destruction priced, exactly C3.

**On the M4b telescoping flag.** The implementing instance identified that Routes 2 and 3 of the lead's own amendment telescope to ln 4 by construction, so their sum could mask a compensating error, and correctly located M4b's independent teeth in Route 1 (the record-marginal entropy landing on ln 4) with M3's separate pins guarding the parts. This was a weakness in the lead's amendment as issued, caught by the implementer — the correction now flows in both directions across the handoff, which is the discipline working as intended. Noted with approval, and the flag's analysis is adopted as the authoritative reading of what M4b measures.

**One observation elevated.** The note's sharpest line is its first Note for Alex: *the monotone residual is silence, not "zero"* — the blindness is heaviest exactly where the classical answer would have been "no," and n = 1, being all silence, is the maximally-unread state on the lattice. This is the cleanest single sentence the programme owns on what NOT is *for*, and it is carried into the master's M₂ section.

*Lead instance, July 2026.*
