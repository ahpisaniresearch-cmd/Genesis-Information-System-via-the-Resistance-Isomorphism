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

# E4 Handoff Brief — The Type-1 Madness Grade: Extraction Rates of Rational Probing

**Madness in the Probe sub-programme · banking run · issued by the lead instance, July 2026**

You are the implementing instance for experiment E4 only. This brief is self-contained; do not request or assume other corpus documents. Implement fresh — do not consult, reconstruct, or reuse any prior sweep script.

---

## 1. Context (all you need)

The sub-programme studies **Madness**: structure or queries for which a probe cannot extract lawful answers at bounded cost. **Type 1 ($M_1$) is unbounded rationalisation cost**: objects that yield information forever, but at a floor-limited rate — resistance without terminus, not lawlessness.

The probe model: learning a real number $x$ by rational approximation. The continued-fraction (CF) algorithm is the optimal rational prober (its convergents $p_k/q_k$ are the best approximations, $|x - p_k/q_k| \asymp 1/(q_k q_{k+1})$), so $\ln q_k$ tracks the nats-about-$x$ extracted after $k$ questions. **The $M_1$ grade is the per-question information rate:**

$$\text{rate}(x) \;=\; \lim_k \tfrac{1}{k}\ln q_k, \qquad \text{rate}_k(x) := \tfrac{1}{k}\ln q_k.$$

A lead preview found the classical structure lands cleanly on the grade; this run re-establishes it fresh and banks it. Stakes: the originator conjectured the golden ratio $\varphi$ as maximal Type-1 Madness; the floor theorem makes that exact.

**Convention pin (mandatory — bars below are indexed to it).** CF $x = [a_0; a_1, a_2, \ldots]$ with $a_0 = \lfloor x \rfloor$; denominators $q_0 = 1$, $q_1 = a_1$, $q_k = a_k q_{k-1} + q_{k-2}$. Internal check: for $\varphi = [1;1,1,\ldots]$, $q_4$ **must equal 5** ($q_k = F_{k+1}$). Compute $q_k$ in exact integer arithmetic from extracted CF terms; only term extraction uses arbitrary-precision floats.

---

## 2. The precision trap (mandatory guards)

A preview run fed 53-bit machine doubles into a high-precision CF: the CF of an exact dyadic rational terminates, and rounding near termination produced astronomical spurious quotients (rates $\approx 15$, i.e. $q_{60} \sim e^{900}$). Guards, all committed:

- **G1.** Random reals must carry entropy matching working precision: generate $\ge 800$ random decimal digits per sample from a seeded generator. Never use float `random()` output as a real.
- **G2.** Working precision `mp.dps ≥ 800` for $k_{\max} = 200$ (a typical real consumes $\approx 1.03$ digits of precision per CF term).
- **G3.** Round-trip: on a $\ge 10\%$ subsample, reconstruct $x$ from its extracted terms and confirm agreement to $10^{-0.9 \cdot \text{dps}}$.
- **G4.** Double-precision control: recompute a $\ge 10\%$ subsample at $2\times$ dps; rates must agree to $10^{-6}$.
- **G5.** Sanity: every extracted $a_i \ge 1$ for $i \ge 1$; for the known quadratics the periodic terms must match theory **exactly** ($\varphi$: all 1s; silver $1{+}\sqrt2$: all 2s; $\sqrt2$: $[1;2,2,2,\ldots]$); for $e = [2;1,2,1,1,4,1,1,6,\ldots]$ the first 30 terms must match the pattern $a_{3m-1} = 2m$, others 1.

---

## 3. Pre-registered measures and bars

Copy this section into the script header before any check is written; report actuals against these fixed bars; **do not move bars** (standing ruling from E1). Checkpoints: $k \in \{30, 60, 120, 200\}$.

**M1 — The universal floor (exact at finite $k$).** Since $a_i \ge 1$ forces $q_k \ge F_{k+1}$, the floor holds at every $k$, not just in the limit: for **every** sampled or named $x$ and every checkpoint, $\text{rate}_k(x) \ge \text{rate}_k(\varphi) - 10^{-12}$. Additionally $\varphi$'s own convergence: $|\text{rate}_{200}(\varphi) - 0.479594| \le 10^{-4}$ (the $k$-corrected value: $\text{rate}_k(\varphi) \approx \ln\varphi + (\ln\varphi - \ln\sqrt5)/k$, with $\ln\varphi = 0.4812118\ldots$), and a fit of $\text{rate}_k(\varphi)$ against $1/k$ over $k \in [20, 200]$ recovering drift coefficient $-0.3235 \pm 0.01$.

**M2 — Metallic fixed points.** For $x_a = [a; a, a, \ldots] = \tfrac{a + \sqrt{a^2+4}}{2}$: $\text{rate}(x_a) = \ln x_a$ — the number is learned at exactly its own log. Bars: $|\text{rate}_{200}(x_a) - \ln x_a| \le 4\times10^{-3}$ for $a = 1..5$ (targets: $0.481212$, $0.881374$, $1.194763$, $1.443635$, $1.647231$), with $|\text{rate}_k - \ln x_a|$ shrinking across checkpoints.

**M3 — The tail control (the experiment's conceptual pin).** $\sqrt2 = [1; 2,2,2,\ldots]$ shares the silver tail, so its rate must converge to $\ln(1{+}\sqrt2) = 0.881374$, **not** $\ln\sqrt2 = 0.346574$: bars $|\text{rate}_{200}(\sqrt2) - \ln(1{+}\sqrt2)| \le 5\times10^{-3}$ and $|\text{rate}_{200}(\sqrt2) - \ln\sqrt2| \ge 0.5$. This pins the Reading that the grade reads the *probing process* (the tail), never the number's size. If $\sqrt2$ tracked $\ln\sqrt2$ the design itself would be wrong — report and stop, do not patch.

**M4 — Typicality (Lévy).** $n = 100$ random reals per G1, $k = 200$: sample mean of $\text{rate}_{200}$ within $1.18657 \pm 0.02$ (Lévy's constant $\pi^2/(12\ln2)$); every sample obeys M1's floor; report the standard deviation and extremes.

**M5 — The $e$ anomaly.** $e$'s partial quotients are unbounded (Euler), so its rate grows without bound — $e$ is **anti-Mad**: more learnable per question than a typical real. Bars: $\text{rate}_k(e)$ strictly increasing across all four checkpoints; $\text{rate}_{200}(e) > 1.25$ (clear of Lévy). Report-only, no bar: a fit of $\text{rate}_k(e)$ against $\ln k$ over $k \in [50,200]$, slope reported against the heuristic $1/3$. Companion, report-only: $\pi$ (no known pattern; expect Lévy-ish).

**M6 — Self-priced census (report-only, no bar, no grade).** Count any sampled random real landing within $10^{-3}$ of its own $\ln x$ at $k = 200$ (i.e. $|\text{rate}_{200}(x) - \ln x| \le 10^{-3}$). Feeds an open thread ("self-priced numbers"); strictly observational.

---

## 4. Prediction, grades on pass, escalation

**Pre-registered prediction: all measures pass.** This is a banking run of previewed classical structure. Any deviation is an implementation bug until proven otherwise; a **verified surviving** violation of the M1 floor or failure of the M3 tail control must not be patched — report it and return it to the register, since it would strike at the grade's definition.

Grades on pass: floor, Lévy typicality, $e$-growth — **Fact** (classical: Hurwitz/Fibonacci bound, Lévy's theorem, Euler's CF of $e$; carry these attributions). Metallic fixed-point identity — **Fact** (elementary). Tail control — **Fact**, pinning the process-not-value **Reading**. $\varphi$ as the maximal-Madness pole of Type 1, and $e$ as anti-Mad — **Reading**. M6 — report-only.

---

## 5. Protocol (carried from E1, with two additions)

1. Fresh implementation; PID-prefixed filename (`{PID}_e4_rates.py`); fixed recorded seed; pre-registered bars in the script header before checks are written; test-run to exit 0; report actuals against fixed bars.
2. Deliverable: a results note `E4_Extraction_Rate_Results.md` mirroring E1's format — status; reproducibility block (script, seed, versions, bars); per-measure results with actuals; a plain-language summary for Alex; an honesty-boundary paragraph (all asymptotics are classical; the grade $M_1$, the tail-control design, and the Mad-pole/anti-Mad readings are the sub-programme's; no leverage on any open problem). Do not edit the master document; do not stray into other experiments.
3. **Non-vacuity clause (new, from E1's addendum):** no check may compare a quantity to itself or restate a definition as a test; every committed bar must be capable of failing under an incorrect implementation. Audit your own checks against this before running.
4. **Implementer-additions clause (new, from E1):** additions beyond the pre-registered set are welcome — label them explicitly as implementer additions, grade them separately, and never let them substitute for a committed measure.

---

*Alexander Pisani & Claude (Anthropic) · Madness in the Probe sub-programme · July 2026.*
