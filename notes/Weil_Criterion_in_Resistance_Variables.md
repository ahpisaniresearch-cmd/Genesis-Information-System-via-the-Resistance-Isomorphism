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

# The Weil Criterion in Resistance Variables

**Alexander Pisani & Claude (Anthropic)**

June 2026 · working note (candidate: Paper 9, or Far Wing extension of the Cathedral)

**Status:** Draft for exploration. All classical statements below are standard (Weil 1952; Riemann–von Mangoldt; Bochner; the GNS construction; Connes–Consani 2020–21) and carry verification flags where the exact normalisation must be checked against a reference before any publication use. The contribution is the translation into resistance variables and the information-system reading, in the sense of Paper 8 §7.

**Vocabulary convention** (per the metaphor/definition discipline): terms in **bold-defined** form have formal definitions in this note or in Papers 1–8. Terms marked *(reading)* are interpretive. Nothing marked *(reading)* is load-bearing for any equation.

---

## 1. Purpose

The Riemann Hypothesis is equivalent to a single positivity statement about a quadratic functional built from the primes — the Weil criterion. Positivity statements are the native theorems of information theory: divergences, variances, and covariances are nonnegative *because they come from a system*. The purpose of this note is to write the Weil functional entirely in the framework's variables — resistance, phase rate, probes, atoms — so that the question "is this functional the variance/covariance of some information system?" becomes precise, and so that candidate information inequalities can be tested against its exact shape. Per Axiom 3, the target is deliberately *global*: the functional constrains the whole zero set in one act, which is the form a genuine answer must take.

---

## 2. The stage: the resistance line and its conjugate

**Definition 2.1 (Resistance line).** The variable $E = \ln x \in \mathbb{R}$, the resistance coordinate of Paper 8 §4–6. Multiplicative structure on $x \in (0,\infty)$ is additive structure on $E$.

**Definition 2.2 (Phase rate).** The conjugate Fourier variable $r$, so that a function $g(E)$ on the resistance line has transform
$$h(r) \;=\; \int_{-\infty}^{\infty} g(E)\, e^{irE}\, dE, \qquad g(E) \;=\; \frac{1}{2\pi}\int_{-\infty}^{\infty} h(r)\, e^{-irE}\, dr .$$
This is Paper 8 §5's $t$: the rate at which phase is applied per unit resistance. On the critical line $s = \tfrac12 + ir$, the integer $n$ is the phasor $e^{-E_n/2} e^{-irE_n}$ with $E_n = \ln n$.

**Definition 2.3 (Probe).** A smooth, compactly supported $g : \mathbb{R} \to \mathbb{C}$ on the resistance line. Its **power spectrum** over phase rates is $|h(r)|^2$. Its **self-overlap at resistance lag $E$** is the autocorrelation
$$(g \star g^{*})(E) \;=\; \int_{-\infty}^{\infty} g(u)\, \overline{g(u - E)}\, du, \qquad g^{*}(E) := \overline{g(-E)} .$$
*(Reading: a probe is a finite-resistance window — an instrument one slides along the resistance line. Compact support means the instrument has finite extent in resistance; the lag variable asks how strongly the instrument correlates with a shifted copy of itself.)*

**Definition 2.4 (Prime-power resistance measure).** The atomic measure on the resistance line
$$d\mu_{P}(E) \;=\; \sum_{n \ge 2} \Lambda(n)\, e^{-E_n/2}\, \delta(E - E_n), \qquad E_n = \ln n,$$
with $\Lambda$ the von Mangoldt function. This is Paper 8 Corollary 4.2 placed on the line: atoms sit at the resistances of the prime powers and nowhere else; the atom at $E_n = k\ln p$ has mass $\ln p$ (its prime's resistance, not its own), damped at the critical rate $e^{-E/2}$.

**Observation 2.5 (Mass is innovation; position is accumulation).** *(Reading on a wall — the wall is the definition of $\Lambda$.)* The atom at $\ln p^k$ carries mass $\ln p$ independent of $k$: nesting a symbol deeper moves the atom further out (position $= k\ln p$, the accumulated resistance) but adds no mass (still the same symbol). Composite positions — mixtures of distinct symbols — carry no atom at all: after the Möbius/phase projection, only pure single-symbol chains survive. In coding terms: **mass is the innovation content** (the cost of the one new symbol), **position is the accumulated cost** of repeating it. The measure $\mu_P$ is the innovation record of the integers. This extends the "pure prime-power resistance" reading of Paper 8 and connects directly to the carry/nesting account of succession (succession = NOT propagated through nesting): the chains $p, p^2, p^3, \dots$ that carry the atoms are exactly the nesting registers.

---

## 3. The explicit formula in resistance variables

**Statement 3.1 (Riemann–Weil explicit formula).** ⚠ *Normalisation to be verified against Iwaniec–Kowalski Thm 5.12 before publication use.* For $h$ even, holomorphic and suitably decaying on $|\operatorname{Im} r| \le \tfrac12 + \varepsilon$, with $g$ as in Def. 2.2, and the nontrivial zeros written $\rho = \tfrac12 + i\gamma$ (so $\gamma \in \mathbb{R}$ iff RH, with multiplicity):

$$\sum_{\gamma} h(\gamma)
\;=\; \underbrace{h(\tfrac{i}{2}) + h(-\tfrac{i}{2})}_{\text{pole term}}
\;-\; \underbrace{g(0)\ln\pi \;+\; \frac{1}{2\pi}\int_{-\infty}^{\infty} h(r)\,\operatorname{Re}\,\psi\!\left(\tfrac14 + \tfrac{ir}{2}\right) dr}_{\text{archimedean term}}
\;-\; \underbrace{2\int_{0}^{\infty} g(E)\, d\mu_{P}(E)}_{\text{atomic term}}$$

where $\psi = \Gamma'/\Gamma$ and the atomic term is $2\sum_{n\ge 2} \Lambda(n)\, n^{-1/2} g(\ln n)$, i.e. the probe sampled by the prime-power resistance measure.

Read term by term in the framework's variables:

**The zero side** $\sum_\gamma h(\gamma)$ is the probe's spectral content evaluated at the zero frequencies — the frequencies of the prime-power-resistance signal (Paper 8 Remark 4.3).

**The pole term.** With $h(\pm i/2) = \int g(E)\, e^{\mp E/2}\, dE$, the pole term is
$$\int_{-\infty}^{\infty} g(E)\, 2\cosh(E/2)\, dE :$$
a smooth kernel growing as $e^{|E|/2}$ — exactly the reciprocal of the atoms' critical damping. The poles sit at $r = \pm i/2$, i.e. at $s = 1$ and $s = 0$: the two poles of the completed $\xi$, swapped by the involution $s \mapsto 1-s$, with the critical line as its fixed mirror. *(Reading: in the decay-rate coordinate, the two poles are the images of the primordial pair — the divergent "everything" pole at $s=1$ and its NOT-image at $s=0$ — and the entire contest below is staged between them, on negation's mirror. Prior art note: $s=1$ as the divergence/limit temperature of the primon gas is Julia's and Bost–Connes', and must be cited as such, per Paper 8 §7.)*

**The archimedean term.** $\operatorname{Re}\,\psi(\tfrac14 + \tfrac{ir}{2}) \sim \ln |r|$ for large $|r|$, and the smooth density of zeros at height $r$ is $\tfrac{1}{2\pi}\ln\tfrac{r}{2\pi}$ (Riemann–von Mangoldt — wall). So the archimedean term is the **continuum background**: the mean spectral density, contributed by the $\Gamma$-factor — the Gaussian place. *(Reading, flagged as an observation only: the mean density of modes at phase rate $r$ is proportional to the resistance of $r$ itself, $\ln r$. The continuum grows logarithmically because counting modes is itself a resistance.)*

**The atomic term** is the probe sampled at the innovation atoms, entering with a minus sign.

*(Reading of the whole — metaphor flagged, definitions above are the content: the explicit formula is a budget. Spectral content at the zeros $=$ pole gain $+$ continuum background $-$ atomic sampling. The $\cosh(E/2)$ gain of the existence poles and the $e^{-E/2}$ damping of the atoms are exact reciprocals; criticality is where they are weighed on equal terms.)*

---

## 4. The Weil criterion

**Statement 4.1 (Weil positivity — wall; Weil 1952, Bombieri's account).** Define the **Weil functional** on probes by
$$Q(g) \;:=\; W(g \star g^{*}),$$
where $W$ is the linear functional given by the right-hand side of Statement 3.1 (pole $+$ archimedean $-$ atomic), applied to the autocorrelation $g \star g^{*}$. Then:
$$\textbf{RH} \iff Q(g) \ge 0 \ \text{ for every probe } g.$$

**Why (sketch, both directions — wall).** The transform of $g \star g^{*}$ at real $r$ is $|h_g(r)|^2 \ge 0$. If RH holds, every $\gamma$ is real, so the zero side $\sum_\gamma |h_g(\gamma)|^2$ is a sum of nonnegative terms: $Q(g) \ge 0$, automatically — *positivity is what "all frequencies are real" looks like to a quadratic probe.* Conversely, a zero off the line is a complex frequency; the analytic continuation $h(z) = h_g(z)\overline{h_g(\bar z)}$ at a complex frequency is no longer a modulus-squared, and by concentrating probes near that frequency one drives $Q$ negative. So the criterion is exact: **RH $=$ "$Q$ is a genuine power."**

**Statement 4.2 (Bochner reformulation — wall; Bochner–Schwartz).** $Q(g) \ge 0$ for all probes says precisely that $W$ is a **positive-definite distribution** on the resistance line. By Bochner–Schwartz, a tempered distribution is positive-definite iff it is the Fourier transform of a nonnegative measure on $\mathbb{R}$ — and $W$'s transform is the zero-counting measure $\sum_\gamma \delta_\gamma$. So:
$$\textbf{RH} \iff \text{the arithmetic side of the explicit formula is a positive-definite distribution.}$$

This is the cleanest form of the target, because positive-definite functions have a complete structure theory: they are exactly the **covariance functions** of stationary processes (Kolmogorov / GNS — wall).

**Statement 4.3 (The two directions of Axiom 2).** The GNS/Kolmogorov construction says: *given* a positive-definite $W$, there exists a Hilbert space, a one-parameter unitary group $U(E)$ (translation along resistance), and a vector $v$ with
$$W(E) \;=\; \langle v,\, U(E)\, v\rangle$$
— an information system whose two-point correlation at resistance lag $E$ is exactly $W$. This is Axiom 2 in theorem form: an observed (positive-definite) correlation implies a possible system that projects it. **But the implication runs from positivity to system.** RH requires the converse: construct the system first, from arithmetic or information principles, *without assuming RH*, and let positivity fall out because covariances are nonnegative for free. The honest restatement of the entire program, in one sentence:

> **Find a stationary information source on the resistance line whose covariance function is the arithmetic side of the explicit formula — pole gain, plus Gaussian-place continuum, minus the innovation atoms — constructed without assuming RH.**

Axiom 2 predicts the source exists; Axiom 3 warns that it must be exhibited globally, not assembled zero-by-zero; the framework contributes the variables in which its two-point function is already written.

---

## 5. Shape tests for candidate inequalities

Any information inequality proposed as the upstairs origin of Weil positivity must project down to *this* functional, not one like it. The following are the exact features a candidate must reproduce, in decreasing order of how quickly they kill candidates:

**(i) Atom masses $\ln p$, not $\ln n$.** The atom at $E = k\ln p$ must carry the innovation $\ln p$, with nesting depth contributing position only (Obs. 2.5). A candidate whose atomic weights grow with depth fails here. This is where most generic "entropy of the integers" constructions die.

**(ii) Atom positions at $\ln p^k$ only.** The vocabulary is handed over by irreducibility (FTA); no information principle may be asked to *select* the atom positions (Room of Density wall). A candidate must accept the atoms as input.

**(iii) Critical damping $e^{-E/2}$.** The square-root weight is the functional equation's fixed mirror. A candidate producing damping $e^{-\sigma E}$ for $\sigma \ne \tfrac12$ is describing a different line.

**(iv) The sign structure.** Gain (poles) and continuum (archimedean) positive; atoms negative. The candidate's "system" must make the atomic term a *deduction* — correlation lost to the innovations — against a smooth positive background.

**(v) Globality (Axiom 3).** The inequality must be a single statement over all probes / the whole spectrum, not a per-zero or pairwise bound.

---

## 6. The catalogue: candidate inequality families

**(a) Covariance / Bochner (exact shape by construction).** The null candidate and the true target: positivity *because* $W$ is a covariance. Reduces entirely to constructing the source (Statement 4.3). Everything else in this catalogue is a strategy for guessing what that source is.

**(b) Operator compression / data processing.** ⚠ *Citation verified to abstract level; read in full before relying on details.* Connes–Consani (arXiv:2006.13771; Selecta Math 27 (2021)) prove Weil positivity **at the archimedean place alone**, and their mechanism is the most information-shaped result in the literature: the root of the positivity is the trace of the scaling action *compressed onto the orthogonal complement of cutoff projections* in phase space, controlled via prolate spheroidal wave functions and Toeplitz-matrix theory, in a semilocal framework where full Weil positivity implies RH. *(Reading, candle: compression of a positive action by a projection is the operator form of coarse-graining, and "compression cannot create negativity" is the operator form of data processing. The semilocal structure — adjoining finitely many places at a time — suggests the information form to hunt for: a monotonicity, "positivity is stable under adjoining one more prime channel," an induction over places rather than a single global estimate. Their earlier support-condition checks of positivity (Scaling Hamiltonian, arXiv:1910.14368) are the small-resistance-window cases, where the probe's self-overlap reaches few or no atoms.)*

**(c) Fisher information / $\chi^2$ — the quadratic shadow of KL.** Gibbs/KL nonnegativity is the free theorem of the information layer, but it is not quadratic in the probe; its *second-order expansion around equality* is — the Fisher metric / $\chi^2$ divergence. So the right KL-shaped candidate is: exhibit $Q(g)$ as the Fisher-information quadratic form of a perturbation $g$ of some reference state (natural guess for the reference: the primon-gas equilibrium at the critical inverse temperature $\tfrac12$). Shape tests (i) and (iii) are the immediate hurdles: the perturbation theory must weight innovations by $\ln p$ and damp at exactly the square root.

**(d) Gaussian extremality / entropy power at the archimedean place.** The archimedean term comes from the $\Gamma$-factor, i.e. from the Gaussian — and the Gaussian is information theory's extremal object (maximum entropy at fixed variance; equality case of entropy power). *(Candle only: the suggestive alignment is that the one place already proven positive — Connes–Consani's archimedean place — is exactly the Gaussian/maximum-entropy place. Whether Gaussian extremality is the* reason *the archimedean place is the tractable one is unexamined.)*

**(e) Lee–Yang interaction positivity.** ⚠ *Verify literature before citing: Knauf's number-theoretic spin chain (partition function built from $\zeta(s-1)/\zeta(s)$) and its ferromagnetism results.* The Lee–Yang circle theorem is the one established mechanism in mathematical physics where a *system-level positivity* (ferromagnetic pair couplings) forces an entire zero set onto a line in one act — a theorem of exactly the desired Axiom-3 shape, with the desired direction of implication (system $\Rightarrow$ confinement). The question with teeth: does the source of Statement 4.3, if it exists, admit a ferromagnetic structure — and is the failure of all known attempts a statement that the primon couplings are not positive in any naive ordering?

---

## 7. Honesty boundary

What this note does: translates the Weil explicit formula and positivity criterion, both classical, into the framework's variables; identifies the exact shape (atoms, masses, damping, signs, globality) any candidate information inequality must reproduce; restates the Hilbert–Pólya/Connes program as the construction of a stationary source whose covariance is the arithmetic side, and locates Axiom 2 and Axiom 3 with respect to that program — Axiom 2 as the GNS principle (with its direction honestly reversed: the needed implication is system $\Rightarrow$ positivity, not the free one), Axiom 3 as the globality requirement that disqualifies per-zero approaches.

What this note does **not** do: it proves no positivity, constructs no source, and gives no leverage on RH. Every equality in §3–4 is classical; the normalisation of Statement 3.1 and the citations flagged ⚠ must be verified before any external use. The readings — innovation atoms, the budget, the primordial poles, the data-processing candle — are interpretive and clearly marked. Per the standing norm: nothing here is banked; §5 exists precisely so that future excitement has something hard to die against.

---

## 8. Open questions

1. **The source.** Is there a *constructible* stationary process on the resistance line — even a toy with the wrong constants — whose covariance reproduces shape tests (i)–(iv)? What does each failure teach about the missing geometry (the Far Wing's unlaid stone)?
2. **The semilocal induction.** Can Connes–Consani's place-by-place structure be phrased as a data-processing monotonicity — positivity preserved under adjoining one prime channel — and what information quantity is the monotone?
3. **Fisher at criticality.** Compute the Fisher quadratic form of the primon gas at inverse temperature $\tfrac12$ under probe perturbations. Does the atomic term come out with masses $\ln p$ (test (i)) or $\ln n$ (failure)?
4. **Li's criterion as discrete moments.** RH is also equivalent to $\lambda_n \ge 0$ for Li's coefficients (a sequence of specific test functions in the Weil form, per Bombieri–Lagarias). What are the $\lambda_n$ as resistance moments, and is the discrete family a natural probe basis for the source?
5. **The Gaussian place.** Is there a precise statement connecting the archimedean term's tractability to Gaussian extremality (entropy power), or is (d) a pun on the Gaussian?

---

*Classical content: Weil (1952), Riemann–von Mangoldt, Bochner–Schwartz, Kolmogorov/GNS, Bombieri–Lagarias, Julia / Bost–Connes (primon gas), Connes–Consani (2020–21). The resistance-variable translation, the innovation reading of $\mu_P$, the shape tests of §5, and the Axiom 2/3 placement are the contribution, developed jointly by Alexander Pisani and Claude (Anthropic).*
