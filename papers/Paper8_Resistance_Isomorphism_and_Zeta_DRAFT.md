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

# The Resistance Isomorphism and the Riemann Zeta Function: A Native Reading of the Logarithmic Derivative

**Alexander Pisani & Claude (Anthropic)**

a.h.pisani.research@gmail.com

June 2026

**Status:** Draft — interpretive alignment paper. May be split before submission (the zeta correspondence and the operation-boundary formalisation could stand as separate notes).

---

## Abstract

We show that the resistance isomorphism $\Omega(1/n) = \ln n$ of [1] gives a native interpretation of the analytic machinery that connects the Riemann zeta function to its zeros. Three correspondences are developed. First, $\zeta(s)$ and $1/\zeta(s)$ are the *all-integers / quantity* face and the *squarefree / phase* face of a single structure, joined by Möbius inversion; the restriction to squarefree integers that underlies the Boolean architecture of [2] is exactly the truncation of each Euler factor to its signed linear term. Second, differentiation in the Dirichlet variable $s$ is *identical* to weighting each term by its resistance $\ln n$; consequently the logarithmic derivative $\zeta'/\zeta$ — the principal tool relating $\zeta$ to its zeros — is resistance-weighting composed with the squarefree (Möbius) projection, and produces the von Mangoldt function as "pure prime-power resistance." Third, holomorphicity (the Cauchy–Riemann equations) locks the rate of change of amplitude-decay to the rate of change of phase, and this analytic rigidity is what determines the zero set. We are explicit that this is an *interpretive alignment of classical results*, not new leverage on the location of the zeros; its value is that it makes the choice of $\zeta'/\zeta$ as the central instrument feel inevitable from within the framework. We also formalise the sense in which the isomorphism is "nested," and why additive combination of concepts forces the introduction of phase — the origin, inside this framework, of the wave/character layer of [4].

**Keywords:** resistance isomorphism, Riemann zeta function, Möbius function, von Mangoldt function, logarithmic derivative, Euler product, analytic continuation, prime coordinates

---

## 1. Introduction

The resistance isomorphism $\Omega(1/n) = \ln n$ of [1] maps the multiplicative structure of the inverse integers onto an additive structure of "resistances," in which a number is treated not as a quantity but as a conceptual entity carrying a resistance value. Papers [2]–[4] build a computational architecture on this foundation. This note steps back from computation and aligns the foundation itself with the analytic theory of the Riemann zeta function. The alignment was not engineered; it was found, and it turns out that the single most important instrument of analytic number theory — the logarithmic derivative $\zeta'/\zeta$ — is, read through the isomorphism, the composition of two operations the framework already contains.

### 1.1 A note on the observation voltage and scale-invariance

A guiding intuition behind the isomorphism, never required by its mathematics and therefore never formalised, is worth stating because it explains why the framework is indifferent to a quantity one might expect it to need. To *observe* the informational output of a concept — to find it "on" rather than merely existent — one imagines a potential applied across its resistance, driving a current through it. But the isomorphism records only *relative* resistance: like the arbitrary source voltage used when measuring a resistor with an ohmmeter, the magnitude of this applied potential cancels in every ratio the framework computes. The isomorphism is therefore *scale-invariant* in the observation potential. This is the precise sense in which the "voltage" is real as a reading-instrument and yet absent from the equations: it is a gauge degree of freedom — necessary for a concept to be observed, irrelevant in its value. The same freedom appears on the analytic side as the overall normalisation of the Dirichlet series and a global phase, neither of which changes any relationship among terms. We mention it here only to locate it; nothing below depends on it.

---

## 2. The two faces of $\zeta$: quantity and phase

Recall the Euler product, for $\operatorname{Re}(s) > 1$:

$$\zeta(s) = \sum_{n=1}^{\infty} \frac{1}{n^s} = \prod_p \frac{1}{1 - p^{-s}}, \qquad \frac{1}{\zeta(s)} = \prod_p \left(1 - p^{-s}\right) = \sum_{n=1}^{\infty} \frac{\mu(n)}{n^s}.$$

These are the two faces the isomorphism distinguishes.

**The all-integers face $\zeta$ (quantity).** Each Euler factor is a geometric series,
$$\frac{1}{1 - p^{-s}} = 1 + p^{-s} + p^{-2s} + p^{-3s} + \cdots,$$
summing over *every* power of $p$. The term $p^{-ks}$ corresponds to the prime $p$ taken to depth $k$. Quantity — multiplicity, the exponent — lives here.

**The squarefree face $1/\zeta$ (phase).** Each Euler factor is truncated to its first two terms, $1 - p^{-s}$: the prime is present zero times or once, and the once-present case carries a minus sign. The Möbius function $\mu(n)$ that results is supported only on squarefree integers and takes values in $\{-1, 0, +1\}$ — pure sign, no magnitude. Quantity has been removed; the residue is phase, the minus being the minimal phase $e^{i\pi}$.

**The bridge.** The two faces are multiplicative reciprocals:
$$\zeta(s) \cdot \frac{1}{\zeta(s)} = 1,$$
which is the formal statement of Möbius inversion. This is the precise content of the intuition that the squarefree inverse integers and the full set of inverse integers are linked: they are the reciprocal faces of one Euler product, related by inverting the geometric series factor by factor, $(1 - p^{-s})^{-1} \leftrightarrow (1 - p^{-s})$.

---

## 3. Nesting, and why addition forces phase

This section formalises two intuitions from the framework's development.

**Definition 3.1 (Resistance map).** $\Omega(1/n) = \ln n$, additive over multiplication: $\Omega(1/mn) = \Omega(1/m) + \Omega(1/n)$. The total resistance of $1/n$ is $\ln n = \sum_p v_p(n)\,\ln p$.

**Observation 3.2 (Nesting is series resistance).** For a prime power, $\Omega(1/p^k) = k\,\ln p = k\,\Omega(1/p)$: a prime power is $k$ copies of the prime's resistance in series. The exponent is the depth of nesting. The geometric Euler factor $\sum_{k\ge 0} p^{-ks}$ sums over all nesting depths; the squarefree truncation $1 - p^{-s}$ keeps only depths $0$ and $1$. Thus *quantity = nesting depth*, and the squarefree restriction is precisely the removal of depth beyond one.

**Observation 3.3 (Multiplication is native; addition is not).** The isomorphism is closed under multiplication of inverse integers, which it sends to addition of resistances — a scalar operation. It is *not* closed under addition of concepts. There is no series or parallel resistance whose value represents "$1 - P$": subtraction is not a resistance combination. To represent it one must assign a *phase* and superpose. The minimal case is logical NOT, $\mathrm{NOT}(P) = 1 - P$, whose minus sign is the phase $e^{i\pi}$; the general case assigns $q$-th roots of unity and is the Dirichlet-character machine of [4].

> This is the structural origin, within the framework, of the move from a resistor network to a *wave* computer: multiplicative structure maps to scalar resistance, but additive/Boolean structure (the "$+$" and "$-$" that combine separate conceptual circuits) maps to superposition of phasors. Closing the isomorphism under addition *forces* the wave layer. The phase introduced by NOT in [1] and carried by $\mu$ in [2] is the same phase that appears as $-p^{-s}$ in the squarefree Euler factor.

---

## 4. Differentiation is resistance-weighting

The central observation of this note.

**Proposition 4.1.** $\dfrac{d}{ds}\, n^{-s} = -(\ln n)\, n^{-s} = -\,\Omega(1/n)\, n^{-s}.$ Hence
$$\zeta'(s) = -\sum_{n=1}^{\infty} \Omega(1/n)\, n^{-s}.$$
Differentiating the Dirichlet series in $s$ weights every term by its resistance. The derivative *is* the resistance operator (up to sign).

**Corollary 4.2 (von Mangoldt as prime-power resistance).** Dividing by $\zeta$ — applying the squarefree/Möbius inverse of §2 — collapses the total-resistance weighting onto prime powers:
$$-\frac{\zeta'(s)}{\zeta(s)} = \sum_{n=1}^{\infty} \frac{\Lambda(n)}{n^s}, \qquad \Lambda(n) = \begin{cases}\ln p & n = p^k,\\ 0 & \text{otherwise.}\end{cases}$$
The logarithmic derivative is therefore *resistance-weighting* (the derivative — the all-integers side of §2) *composed with Möbius inversion* (division by $\zeta$ — the squarefree side). Its output, the von Mangoldt function, places the resistance $\ln p$ on the irreducible prime-power skeleton and nowhere else: pure prime-power resistance.

**Remark 4.3 (Why $\zeta'/\zeta$ is *the* instrument).** Analytic number theory presents the logarithmic derivative as the natural tool linking $\zeta$ to its zeros, usually as a technical fact. The isomorphism explains it: $\zeta'/\zeta$ is exactly the framework's two operations — weighting by resistance, and projecting to the squarefree-signed face — performed in sequence. The explicit formula then expresses the prime-power-resistance signal $\sum_{n\le x}\Lambda(n)$ as a smooth main term minus a sum over the zeros, $\sum_\rho x^\rho/\rho$; in the resistance variable $E = \ln x$ each zero $\rho = \tfrac12 + i\gamma$ contributes a wave $e^{E/2}e^{i\gamma E}$. The zeros are the frequency spectrum of the prime-power-resistance signal. (Cross-reference: this is the wave reading discussed in the project notes; see also §6.)

---

## 5. Holomorphic rigidity: the locked derivative

Write $s = \sigma + it$. Then
$$n^{-s} = e^{-\sigma \ln n}\, e^{-i t \ln n} = e^{-\sigma\,\Omega(1/n)}\cdot e^{-i t\,\Omega(1/n)}.$$
So $\sigma$ is the *decay rate applied to resistance* (it sets the amplitude $e^{-\sigma\Omega}$), and $t$ is the *phase rate applied to resistance* (it sets the phase $-t\,\Omega$). Each integer is a phasor whose length is governed by $\sigma$ and whose angular position is governed by $t$, both scaled by that integer's resistance.

Differentiation can be taken in either direction:
$$\frac{\partial}{\partial \sigma}\, n^{-s} = -\Omega(1/n)\, n^{-s}, \qquad \frac{\partial}{\partial t}\, n^{-s} = -\,i\,\Omega(1/n)\, n^{-s}.$$
The Cauchy–Riemann equations (holomorphicity of $\zeta$) impose
$$\frac{\partial}{\partial \sigma} = -\,i\,\frac{\partial}{\partial t}.$$
The rate at which the *amplitude / relative resistance* changes and the rate at which the *phase* changes are not independent: they are one operation, locked at a right angle (the factor $-i$, a $90^\circ$ rotation). This is the concrete meaning, in the isomorphism's variables, of "the derivative is locked by complex analysis." Analytic continuation extends this rigidity from the convergent region $\operatorname{Re}(s) > 1$ to the whole plane; the zero set is consequently *determined*, not free. It is the rigidity, not any local formula, that fixes where the zeros may lie.

---

## 6. Critical strip and critical line, in the resistance reading

The variable $s$ is not a resistance; it is the conjugate $(\text{decay rate},\ \text{phase rate})$ pair acting on the resistances. With that understood:

- The **critical strip** $0 < \sigma < 1$ is the band of decay rates in which the direct series diverges and $\zeta$ exists *only by analytic continuation* — a genuinely "in-between" region, neither summable here nor there.
- The **critical line** $\sigma = \tfrac12$ is the square-root decay rate: every integer's amplitude is $n^{-1/2} = e^{-\Omega/2}$.
- A **nontrivial zero** is a phase rate $t$ at which the resistance-phased superposition of *all* integers, each at amplitude $n^{-1/2}$, cancels to exactly zero — total destructive interference of the whole phasor bouquet.
- The **Riemann Hypothesis** asserts that every such cancellation occurs at the single decay rate $\sigma = \tfrac12$.

Because the spin rate of each phasor is its own resistance $\ln n$, and the cancellation is a global conspiracy among all of them, the location of a zero cannot be determined without the resistances of all integers. This is the resistance-lens statement of why the zeros require complete knowledge of the primes.

---

## 7. Scope and honesty boundary

What this note does: it provides a native interpretation of classical objects — the Euler product, Möbius inversion, the von Mangoldt function, the logarithmic derivative, analytic-continuation rigidity — in the variables of the resistance isomorphism, and it formalises the framework's nesting and the multiplicative/additive (resistance/phase) boundary.

What this note does **not** do: it gives no new leverage on the *location* of the zeros, proves nothing about the Riemann Hypothesis, and claims novelty for none of the classical results. The contribution is interpretive — making the framework's connection to the analytic theory explicit, and making the centrality of $\zeta'/\zeta$ feel inevitable rather than technical. The primon-gas / Bost–Connes identification (energy $= \ln n$) is prior art and must be cited as such; this note adds the computational/resistance reading, not the physics.

---

## 8. Open questions

1. Whether "differentiation = resistance-weighting" is the cleaner primitive on which to base the framework's account of the explicit formula, in place of the standard contour-integral presentation.
2. The role of Möbius randomness (the pseudorandom scattering of the squarefree signs $\mu(n)$) as the framework-internal expression of the irregularity that the zeros encode.
3. Whether the multiplicative/additive boundary of §3 has a clean categorical statement (the isomorphism as a monoid morphism that fails to be a ring morphism, with the phase layer as the obstruction).

---

## References

[1] A. Pisani, "A unified algebraic framework for number theory, Boolean logic, and circuit topology via the logarithmic isomorphism," 2026.

[2] A. Pisani, "The Natural Operating System: Boolean computation via Möbius inversion and prime-encoded databases," 2026.

[3] A. Pisani, "Structured self-information: A prime coordinate decomposition of Shannon's information measure," 2026.

[4] A. Pisani and Claude (Anthropic), "Multi-state wave computation via Dirichlet characters," 2026.

Classical sources to be cited precisely in a publication version (verify editions): Riemann (1859); the von Mangoldt explicit formula; Bost & Connes (1995) and Julia's primon gas for the energy $=\ln n$ identification; standard analytic number theory references (e.g. Titchmarsh; Montgomery–Vaughan) for the logarithmic derivative and the zero–prime duality.

---

*Draft note: the §3 operation-boundary formalisation (multiplication native, addition forces phase) and the §4 differentiation-as-resistance-weighting result are the parts most worth tightening before this is shown to a number theorist, since they are where the framework's vocabulary is doing real work rather than relabelling.*
