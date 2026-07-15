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

# The Zeta Circuit
## ζ(s) as a composite of resistances, and the two companion notes as its first two logarithmic derivatives

**Alexander Pisani & Claude (Anthropic)** · July 2026 · companion note to the Genesis Information Project (draft, in progress)

**Status.** Companion note under construction, section by section. This is the opening scope and the foundational verification (§§1–2) only; a later section pursues the one open question — whether the primon cumulants carry arithmetic structure beyond generic moment theory — under criteria committed in advance. Nothing here is promoted to the project spine.

---

## 1. Scope and boundaries

**What this note does.** The companion notes read discrete operations through the two-legged ledger and price their erasures. This note turns the same reading on the Riemann zeta function — not as an object to be interrogated for its zeros, but as a **circuit** assembled from the framework's primitives: prime resistances, a composition rule, and the ledger. The organizing claim, verified in §2 and developed after: **ζ(s) is the partition function of a gas of erasure-priced integers, and the two companion notes are its first two logarithmic derivatives** — Note A (innovation) at the first, Note B (fluctuation) at the second. **[Reading]**

**The primon reading (known physics, with the framework's one turn).** Via the Euler product `ζ(s) = Σ_n n^{-s} = Π_p (1 − p^{-s})^{-1}`, the statistical theory of numbers treats each integer `n` as a state of energy `ln n`, each prime `p` as a fundamental mode of energy `ln p`, and `s` as an inverse temperature, with `ζ(s)` its partition function (Julia; Spector; and, in its operator form, the Bost–Connes system). This much is established. **[Fact, known]** The framework adds one identification: by the resistance isomorphism `Ω(1/n) = ln n`, the energy `ln n` **is** the Landauer erasure cost of the integer. So the primon gas is a gas of integers weighted by their erasure cost, and `ζ(s) = Σ_n e^{−s·(erasure cost of n)}`. **[Reading]**

**Regime framing.** The per-integer erasure cost `ln n` is a Regime-1 quantity — a discrete, quantized cost carried by an individual integer. Every *cumulant* computed in this note is a Regime-2 quantity: an average over the primon Gibbs ensemble at temperature `s`, a probe-side statistic, never a property of the genesis layer. The banked one-liner holds — the ensemble is probe-manufactured; the integers' own costs are the quantized ledger.

**Standard identities are not the content.** The relations used here — that the cumulants of the energy are the logarithmic derivatives of the partition function — are textbook statistical mechanics, exact and standard. As in the companion notes, we say this plainly so it is never mistaken for a discovery. The content is the **erasure reading**: that the first log-derivative is an innovation spectrum, the second a fluctuation, and that the circuit's steps sort into reversible and dissipative on the ledger.

**Boundaries.**

1. **No leverage on the Riemann Hypothesis.** This is the load-bearing boundary, stated as firmly as the corpus states it elsewhere. Nothing here bears on the location of ζ's zeros or the critical line. The dissection lives entirely in the **convergent regime `s > 1`**, in the analytic structure of the logarithmic derivatives; it reads ζ's thermodynamic and erasure structure, not its zeros. The Weyl-clock / phasor-bouquet correspondence already in the corpus carries an explicit no-leverage flag, and that flag stays up here.
2. **The physics is borrowed; the reading is the contribution.** The primon gas is an established model; this note does not claim it. What it claims is the erasure interpretation of the model's quantities and their assembly into a circuit.
3. **Cartography, not evidence.** As throughout, the circuit is a reading; that ζ hosts an erasure interpretation says nothing about whether the genesis system holds beyond the axioms that posit it.

**Grading.** Every claim carries an inline grade — **[Fact]** (a verified identity or established result), **[Reading]** (a framework-consistent interpretation), **[Lead]** (an open thread with a kill-or-promote criterion). §2's identities are Facts, verified against high-precision ground truth; the erasure readings are Readings; the one genuinely open question — arithmetic structure in the cumulants — is carried as a Lead and resolved, under pre-registered criteria, in a later section.

---

## 2. The primon circuit and its first two cumulants

**The circuit.** The components are the framework's own. Each prime `p` is a resistance of value `ln p`. The composition rule is the Euler product: the primes combine multiplicatively, `ζ(s) = Π_p (1 − p^{-s})^{-1}`, which is the same object as the Dirichlet sum `Σ_n n^{-s}` by unique factorization. The reading is `ζ(s) = Σ_n e^{−s·ln n}` — the partition function over integer erasure costs.

**The reversible seam. [Fact → Reading]** The Euler product and the Dirichlet sum are equal because every integer factors uniquely into primes. We verified this directly: the product over primes `p ≤ P` equals the sum over `P`-smooth integers (those with no prime factor above `P`), agreeing to 10⁻⁸–10⁻¹¹ across `P = 2, 3, 5, 7, 13`, both climbing toward `ζ(s)` as `P` grows. **[Fact]** On the ledger this seam is *reversible*: factoring and re-multiplying is a lossless re-encoding of the same number, and reversible operations are free. The circuit's compositional wiring costs nothing; the price, when it comes, is elsewhere. **[Reading]**

**The first cumulant: mean erasure cost is the innovation spectrum. [Fact]** Under the Gibbs measure `P_s(n) = n^{-s}/ζ(s)`, the mean energy is the mean erasure cost, and it is the first logarithmic derivative of ζ:

`κ₁ = ⟨ln n⟩ = −ζ′(s)/ζ(s) = Σ_n Λ(n) n^{-s}`,

the von Mangoldt Dirichlet series. We computed all three expressions independently at `s = 2` and `s = 3`: the Gibbs mean, the von Mangoldt series, and a high-precision evaluation of `−ζ′/ζ` agree — to ten–twelve digits at `s = 3` (where the truncation converges fast), to five–seven at `s = 2`. **[Fact]** The reading writes itself: the von Mangoldt function is exactly Note A's channel-innovation spectrum, so **the mean energy of the primon gas is the innovation spectrum**, and taking the first derivative of ζ is the irreversible act that extracts it — `Λ` is where the ledger is finally charged. **[Reading]**

**The second cumulant: fluctuation, Fisher, heat. [Fact]** The variance of the erasure cost is the second logarithmic derivative:

`κ₂ = Var(ln n) = (log ζ)″(s) = ζ″/ζ − (ζ′/ζ)²`,

which is at once the primon gas's heat capacity and the **Fisher information** the ensemble carries about the temperature `s` — the score of the Gibbs family in `s` is `−(ln n − ⟨ln n⟩)`, whose variance is `κ₂`. We confirmed the primon variance against `(log ζ)″` at both temperatures: matching to ten digits at `s = 3`, to five at `s = 2`. **[Fact]** This is Note B's fluctuation probe made analytic: where the mean `κ₁` fixes the innovation spectrum, the variance `κ₂` is the second-cumulant handle Note B built by hand, here delivered as a concrete number-theoretic function. **[Reading]**

**The ladder, and the two notes as two derivatives.** The pattern continues: `κ_j = (−1)^j (log ζ)^{(j)}` is the whole cumulant ladder of Note B §6, now indexed by derivatives of ζ. So the two companion notes attach to one object at successive derivatives — Note A at the first log-derivative (innovation, von Mangoldt), Note B at the second and beyond (fluctuation, the ladder). The circuit is: prime resistances `ln p` → Euler-product composition (reversible) → ζ → differentiate once for the innovation spectrum, again for the fluctuation. **[Reading]** What remains open — taken up next under committed criteria — is whether these primon cumulants carry structure specific to the primes, beyond the generic moment relations any energy spectrum would satisfy. **[Lead — open]**

---

## 3. Independent prime modes, and where the arithmetic lives

Z1 established that the primon cumulants are the logarithmic derivatives of ζ. The question §1 flagged as open: do those cumulants carry structure *specific to the primes*, beyond the generic moment relations any energy spectrum satisfies? This section answers it — for the convergent regime — and the answer sharpens the picture rather than promoting it.

**The primon gas is a system of independent prime modes. [Fact]** Because `log ζ(s) = Σ_p −log(1 − p^{−s})`, the gas factors into one independent mode per prime: prime `p` is a geometric (bosonic) oscillator of quantum energy `ln p`, occupied `n_p` times with probability `∝ (p^{−s})^{n_p}`, and the total erasure cost is `E = Σ_p n_p ln p`. Every cumulant is therefore additive over primes,

`κ_j(s) = Σ_p (ln p)^j · g_j(p^{−s})`,

with `g_j` the `j`-th cumulant of a geometric distribution. We verified this against the ground truth `(−1)^j (log ζ)^{(j)}` at `s = 2` and `s = 3`, matching to ten–thirteen digits where the truncation converges. **[Fact]** The first cumulant is the cleanest case: `κ₁ = Σ_p ln p · p^{−s}/(1 − p^{−s}) = Σ_n Λ(n) n^{−s}`, so the von Mangoldt series is exactly the summed mean occupation energy of the prime modes. This is the arithmetic realisation of the picture Note A §7 and the F1 follow-up circled — the primes as the independent generators of a free commutative monoid, here the independent oscillators of the primon gas. **[Reading]**

**The cumulant-generating function is a shift of `log ζ`. [Fact]** The same independence gives `K(t) = log⟨e^{tE}⟩ = log ζ(s − t) − log ζ(s)`, so the entire ladder is the local Taylor expansion of `log ζ` at `s`; the Taylor coefficients reproduce the cumulants to ten digits for `j = 1…4`.

**The leading singularity is universal. [Fact]** From ζ's simple pole at `s = 1` with residue 1, `κ_j(s) · (s − 1)^j → (j − 1)!` as `s → 1⁺` — verified at `s = 1.1, 1.01, 1.001` (`0.999, 1.000, 2.0, 6.0` for `j = 1…4` at `s = 1.001`). This leading behaviour reflects only that the integers have density 1; it is shared by any independent-mode system whose zeta has a simple pole of residue 1, and is therefore *not* arithmetic-specific.

**Where the arithmetic does live: the spectrum and the subleading constants. [Fact]** The prime content shows up not in the cumulant *algebra* but in the *values* it is fed. The subleading term of `κ₁` at the pole is the Euler–Mascheroni constant — `κ₁(s) − 1/(s − 1) → −γ` (verified: `−0.57720` against `−γ = −0.57722`); deeper terms carry prime-zeta constants. These are genuine arithmetic quantities, but they are constants set by the spectrum `{ln p}`, not relations among the cumulants.

**The algebra is generic. [Fact]** To confirm the cumulant algebra carries no prime-specific relation, we recomputed the standardised cumulants (skewness, excess kurtosis) at `s = 2` for two null mode systems of the same form — fake primes `q_k ~ k ln k` (density-matched) and all integers `m ≥ 2`. The primon values (skew 2.344, exkurt 7.627) sit *between* the fake-prime (2.458, 8.349) and integer (2.015, 5.374) values: all three are generic geometric-mode shapes, and nothing singles the primes out. **[Fact]**

**Verdict — parked, and §6's park extended.** No cumulant-level relation distinguishes the primon gas from a generic independent-geometric-mode gas: the mode decomposition, the CGF-as-shift, the universal pole, and the standardised-cumulant character are all matched by the nulls. The arithmetic lives entirely in the spectrum `{ln p}` and in subleading analytic constants (`γ`, prime-zeta values), never in the ladder algebra. Note B §6 parked the cumulant ladder as classical moment theory on content-free cascades; Z2 shows that carrying *real primes* in the cumulants does not change the verdict — the algebra is generic even here. **[Lead — parked]**

**The one place not looked. [boundary]** There is exactly one place where non-generic prime structure genuinely resides: the *analytic continuation*. The function `κ₁(s) = −ζ′/ζ(s)`, continued past `s = 1`, has poles at the nontrivial zeros of ζ — this is the content of the classical explicit formula, and it is where the primes' fine structure lives. That structure is real, and it is entirely classical (Riemann; von Mangoldt). It is also precisely the critical-strip territory this note's boundary places out of scope: the location of those zeros is the Riemann Hypothesis, on which the framework offers descriptive correspondence (the corpus's Weyl-clock / phasor-bouquet bridge) and no leverage. We name the structure to be honest about where it lives, and we do not cross into it here. **[Fact, classical]** that the continuation's poles are the zeros; **[boundary]** that this yields no purchase on their location.

---

## Appendix — verbatim script outputs

*Built incrementally, one block per experimental step; every number in the prose above appears here.*

### Z1 · `z1_primon_circuit.py` (self-authored, PID-named)

Three independent routes to `κ₁` (Gibbs mean, von Mangoldt series, mpmath `−ζ′/ζ`) agree; `κ₂` matches mpmath `(log ζ)″`; the Euler product equals the `P`-smooth sum.

```
truncation N = 2000000;  mpmath ground truth: True

--- Cumulants of the primon energy (E = ln n) under Gibbs measure n^-s/zeta ---

  s = 2.0
    zeta_N(s)                         = 1.6449335668
    kappa_1  mean energy  (-zeta'/zeta) = 0.5699564523
    kappa_1  via  sum Lambda(n) n^-s    = 0.5699604931   |diff| = 4.04e-06
    kappa_2  variance = Fisher = C_heat = 0.8844139649
    kappa_3                             = 1.9491208924
    mpmath truth: -zeta'/zeta = 0.5699609931,  (log zeta)'' = 0.884481834
    |mean - truth| = 4.54e-6;  |var - truth| = 6.79e-5

  s = 3.0
    zeta_N(s)                         = 1.2020569032
    kappa_1  mean energy  (-zeta'/zeta) = 0.1648226822
    kappa_1  via  sum Lambda(n) n^-s    = 0.1648226822   |diff| = 3.14e-12
    kappa_2  variance = Fisher = C_heat = 0.1722807115
    kappa_3                             = 0.2215047317
    mpmath truth: -zeta'/zeta = 0.1648226822,  (log zeta)'' = 0.1722807115
    |mean - truth| = 3.54e-12;  |var - truth| = 2.13e-11

--- Reversible re-encoding: Euler product over p<=P  vs  sum over P-smooth n<=N ---
    P= 2: Euler product = 1.3333333333   P-smooth sum = 1.3333333333   |diff| = 1.94e-11
    P= 3: Euler product = 1.5000000000   P-smooth sum = 1.4999999998   |diff| = 2.14e-10
    P= 5: Euler product = 1.5625000000   P-smooth sum = 1.5624999990   |diff| = 1.02e-09
    P= 7: Euler product = 1.5950520833   P-smooth sum = 1.5950520802   |diff| = 3.13e-09
    P=13: Euler product = 1.6179176613   P-smooth sum = 1.6179176490   |diff| = 1.23e-08
```

*Note: an earlier run used `mp.zeta(s, 1)` for the cross-check — the Hurwitz zeta, not the derivative — which printed an absurd `−ζ′/ζ = −1.0`; the script was corrected to `mp.diff`, and the corrected ground truth (shown above) confirms the primon computation, which was independently self-consistent throughout.*

### Z2 · `z2_primon_arithmetic.py` (self-authored, PID-named; **parked Lead**)

Decomposition matches ground truth; CGF = shift of `log ζ`; universal pole `(j−1)!/(s−1)^j`; subleading constant `−γ`; standardised cumulants generic across primon / fake-prime / integer mode systems.

```
(1) Independent-prime-mode decomposition  kappa_j = sum_p (ln p)^j g_j(p^-s)
    s=2.0
      kappa_1: mode-sum=0.5699604932  truth=0.5699609931  |diff|=5.00e-07
      kappa_2: mode-sum=0.8844740819  truth=0.8844818340  |diff|=7.75e-06
      kappa_3: mode-sum=1.9500151080  truth=1.9501358327  |diff|=1.21e-04
      kappa_4: mode-sum=5.9668314706  truth=5.9687202695  |diff|=1.89e-03
    s=3.0
      kappa_1: mode-sum=0.1648226822  truth=0.1648226822  |diff|=4.02e-13
      kappa_2: mode-sum=0.1722807115  truth=0.1722807115  |diff|=1.93e-12
      kappa_3: mode-sum=0.2215047320  truth=0.2215047321  |diff|=2.82e-11
      kappa_4: mode-sum=0.3606578108  truth=0.3606578112  |diff|=4.24e-10

(2) CGF = shift:  kappa_j = j! * [t^j]( log zeta(s-t) - log zeta(s) )   at s=2
      kappa_1 via CGF = 0.5699609931   truth = 0.5699609931
      kappa_2 via CGF = 0.884481834   truth = 0.884481834
      kappa_3 via CGF = 1.950135833   truth = 1.950135833
      kappa_4 via CGF = 5.968720269   truth = 5.968720269

(3) Universal pole:  kappa_j(s) * (s-1)^j  ->  (j-1)!   as s->1+
    s=    1.1:  j=1:0.94410364(target 1)   j=2:0.99822366(target 1)   j=3:1.999905(target 2)   j=4:5.9999922(target 6)
    s=   1.01:  j=1:0.99424655(target 1)   j=2:0.99998135(target 1)   j=3:1.9999999(target 2)   j=4:6.0(target 6)
    s=  1.001:  j=1:0.99942297(target 1)   j=2:0.99999981(target 1)   j=3:2.0(target 2)   j=4:6.0(target 6)

(4a) Subleading constant:  kappa_1(s) - 1/(s-1)  ->  -gamma
    s=    1.01:  kappa_1 - 1/(s-1) = -0.5753453567   (-gamma = -0.5772156649)
    s=   1.001:  kappa_1 - 1/(s-1) = -0.5770281702   (-gamma = -0.5772156649)
    s=  1.0001:  kappa_1 - 1/(s-1) = -0.5771969097   (-gamma = -0.5772156649)

(4b) Null comparison — standardized cumulants at s=2 (skew=k3/k2^1.5, exkurt=k4/k2^2)
    primon (primes)        k2=0.88447  skew=2.34428  exkurt=7.62735
    fake-primes k ln k     k2=0.87622  skew=2.45808  exkurt=8.34879
    all-integers m>=2      k2=2.16096  skew=2.01502  exkurt=5.37412
```

---

*End of current draft of The Zeta Circuit. Sections 1–3 complete with a verbatim appendix (Z1, Z2). One Lead parked (§3, the cumulant algebra is generic). The analytic-continuation structure is named and placed out of scope by the no-leverage boundary. Nothing here is promoted to the project spine.*
