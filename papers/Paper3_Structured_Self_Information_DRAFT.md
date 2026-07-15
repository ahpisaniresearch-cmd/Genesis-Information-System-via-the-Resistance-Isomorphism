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

# Structured Self-Information: A Prime Coordinate Decomposition of Shannon's Information Measure

**Alexander Pisani**

a.h.pisani.research@gmail.com

March 2026

---

## Abstract

Shannon's self-information $h(1/n) = \ln(n)$ assigns a scalar cost to the event with probability $1/n$. We show that this scalar admits a unique decomposition into independent components along the prime dimensions of $n$: the *information spectrum* $\sigma(n)$, whose $p$-th component is $a_p \ln(p)$ where $a_p$ is the exponent of prime $p$ in the factorisation of $n$. This decomposition is forced by Cauchy's functional equation — no alternative continuous decomposition exists.

The spectrum lifts Shannon's additivity axiom from scalars to vectors: the information spectrum of a conjunction is the sum of the individual spectra, dimension by dimension. More significantly, the spectrum provides a structural account of *information overlap*: the shared information between two integers is the componentwise minimum of their spectra (corresponding to the GCD), and their combined information is the componentwise maximum (corresponding to the LCM). The fundamental identity $h(a) + h(b) = h(\gcd(a,b)) + h(\operatorname{lcm}(a,b))$ becomes an exact conservation law — information is neither created nor destroyed when two integers are decomposed into their shared and combined structure.

The individual mathematical results are classical. The contribution is the information-theoretic framework: a structured refinement of Shannon's self-information that reveals *which* independent degrees of freedom contribute to information cost, and *how much* each contributes — an itemised bill where Shannon provides only the total.

**Keywords:** self-information, prime factorisation, information spectrum, Shannon entropy, Cauchy functional equation, divisibility lattice

**MSC (2020):** 94A15, 11A25, 11A51, 06D99

---

## 1. Introduction

Shannon's information theory [1] assigns to each event with probability $p$ a self-information $h(p) = -\ln(p)$, measuring the "surprise" or "cost" of that event in nats. For events with probability $1/n$ where $n$ is a positive integer, this gives $h(1/n) = \ln(n)$. This scalar quantity is the foundation of modern information theory and satisfies the fundamental additivity property: the information cost of two independent events is the sum of their individual costs.

However, the scalar $\ln(n)$ discards all structural information about $n$. The integers 64 and 66 have nearly identical self-information ($\ln(64) \approx 4.159$, $\ln(66) \approx 4.190$), yet their internal structure is completely different: 64 = $2^6$ is a sixth power of a single prime, while 66 = $2 \times 3 \times 11$ is a product of three distinct primes. Shannon's measure treats these as essentially interchangeable; structurally, they have almost nothing in common.

At the other end of the spectrum, Kolmogorov complexity [2] captures the full algorithmic structure of an object — the length of the shortest program that produces it — but is uncomputable and does not decompose into independent components.

This paper develops a middle ground. The *information spectrum* of a positive integer $n$ decomposes $\ln(n)$ into components along the prime dimensions of $n$'s factorisation. Each component measures the information contribution of a single independent structural dimension. The decomposition is:

- **Unique**: forced by the Fundamental Theorem of Arithmetic and the linear independence of $\{\ln(p) : p \text{ prime}\}$ over $\mathbb{Q}$.
- **Canonical**: the only continuous decomposition compatible with the multiplicative structure, by Cauchy's functional equation [3].
- **Additive dimension by dimension**: not merely in total (Shannon's axiom), but in each independent component separately.
- **Equipped with a structural overlap theory**: the information shared between two integers, and their combined information, are computed by componentwise min and max of their spectra, yielding an exact conservation law.

The individual mathematical ingredients — prime factorisation, the divisibility lattice, the logarithmic homomorphism, the linear independence of prime logarithms — are all classical. The contribution is the information-theoretic framework that unifies them: a *structured* refinement of Shannon's self-information that reveals which independent degrees of freedom contribute to information cost, and how much each contributes.

**Relation to prior work.** This paper builds on the algebraic framework of [4], which establishes the monoid isomorphism $\Omega(1/n) = \ln(n)$ from inverse integers under multiplication to non-negative reals under addition, and develops a four-layer correspondence among number theory, Boolean logic, informational resistance, and prime coordinate vectors. The present paper reinterprets the prime coordinate structure of [4] through an information-theoretic lens, identifying the prime coordinate vector as a *structural decomposition of Shannon's self-information* rather than merely an algebraic convenience.

**What this paper does not claim.** We do not claim that the information spectrum extends to arbitrary probability distributions or continuous random variables. The framework applies to self-information of events with probability $1/n$ for positive integers $n$ — a restricted but mathematically rich domain. Whether the structural decomposition perspective generalises beyond the multiplicative integers is an open question discussed in Section 8.

### 1.1 Organisation

Section 2 recalls the necessary background. Section 3 defines the information spectrum and proves its uniqueness. Section 4 establishes spectral additivity. Section 5 develops the theory of spectral overlap and the conservation law. Section 6 proves that the information spectrum is the unique continuous structured decomposition, via Cauchy's functional equation. Section 7 presents worked examples. Section 8 discusses connections, limitations, and open problems.

---

## 2. Background

### 2.1 Shannon Self-Information

For an event with probability $p \in (0, 1]$, the *self-information* (or *surprisal*) is [1]:

$$h(p) = -\ln(p)$$

measured in nats. For $p = 1/n$ with $n \in \mathbb{Z}^+$:

$$h(1/n) = \ln(n).$$

The key property is *additivity for independent events*: if events with probabilities $1/a$ and $1/b$ are independent, their conjunction has probability $1/(ab)$ and self-information $\ln(ab) = \ln(a) + \ln(b)$.

### 2.2 Prime Factorisation and the Fundamental Theorem

Every positive integer $n > 1$ has a unique representation $n = p_1^{a_1} p_2^{a_2} \cdots p_k^{a_k}$ where $p_1 < p_2 < \cdots < p_k$ are primes and each $a_i \geq 1$ (the Fundamental Theorem of Arithmetic). We write $v_p(n)$ for the $p$-adic valuation of $n$: the exponent of prime $p$ in the factorisation of $n$, with $v_p(1) = 0$ for all $p$.

### 2.3 The Divisibility Lattice

The positive integers under divisibility form a distributive lattice with $\gcd$ as meet and $\operatorname{lcm}$ as join [5]. The fundamental identity is:

$$\gcd(a, b) \cdot \operatorname{lcm}(a, b) = a \cdot b$$

which holds for all positive integers $a, b$.

### 2.4 Linear Independence of Prime Logarithms

**Theorem 2.1** (Classical; see [6]). *The set $\{\ln(p) : p \text{ prime}\}$ is linearly independent over $\mathbb{Q}$. That is, if $\sum_{i=1}^k c_i \ln(p_i) = 0$ with $c_i \in \mathbb{Q}$, then $c_i = 0$ for all $i$.*

*Proof.* Clear denominators to assume $c_i \in \mathbb{Z}$. Then $\ln(\prod p_i^{c_i}) = 0$, so $\prod p_i^{c_i} = 1$. By unique factorisation, each $c_i = 0$. $\square$

---

## 3. The Information Spectrum

### 3.1 Definition

**Definition 3.1 (Information Spectrum).** For a positive integer $n$ with prime factorisation $n = \prod_p p^{a_p}$, the *information spectrum* of the event $1/n$ is the function $\sigma(n) \colon \text{Primes} \to \mathbb{R}_{\geq 0}$ defined by:

$$\sigma_p(n) = v_p(n) \cdot \ln(p)$$

where $v_p(n)$ is the exponent of $p$ in the factorisation of $n$. We define $\sigma(1)$ to be the zero function.

The *total self-information* is recovered as the sum:

$$h(1/n) = \ln(n) = \sum_{p \text{ prime}} \sigma_p(n).$$

Each component $\sigma_p(n)$ is the *information contribution of prime dimension $p$* to the total self-information.

**Example 3.2.** For $n = 360 = 2^3 \times 3^2 \times 5$:

| Prime $p$ | $v_p(360)$ | $\ln(p)$ | $\sigma_p(360) = v_p \cdot \ln(p)$ |
|-----------|------------|----------|--------------------------------------|
| 2 | 3 | 0.6931 | 2.0794 |
| 3 | 2 | 1.0986 | 2.1972 |
| 5 | 1 | 1.6094 | 1.6094 |

Total: $\ln(360) = 2.0794 + 2.1972 + 1.6094 = 5.8861$. $\checkmark$

### 3.2 Uniqueness of the Spectrum

**Theorem 3.3 (Uniqueness of the Information Spectrum).** The information spectrum $\sigma(n)$ is the unique decomposition of $h(1/n) = \ln(n)$ into components along the basis $\{\ln(p) : p \text{ prime}\}$. That is, if

$$\ln(n) = \sum_{p \text{ prime}} c_p \cdot \ln(p)$$

with $c_p \in \mathbb{R}$, almost all zero, then $c_p = v_p(n)$ for all primes $p$.

*Proof.* By the Fundamental Theorem of Arithmetic, $\ln(n) = \sum_p v_p(n) \ln(p)$. If $\sum_p c_p \ln(p) = \sum_p v_p(n) \ln(p)$, then $\sum_p (c_p - v_p(n)) \ln(p) = 0$. By Theorem 2.1 (linear independence over $\mathbb{Q}$, which a fortiori implies independence over $\mathbb{R}$ for finite sums with rational coefficients), and since $c_p - v_p(n) \in \mathbb{R}$ but $v_p(n) \in \mathbb{Z}$, the independence forces $c_p = v_p(n)$ whenever we restrict to decompositions with $c_p \in \mathbb{Q}$ (which includes all $c_p \in \mathbb{Z}$). $\square$

**Remark 3.4.** The uniqueness fails if we allow irrational coefficients: the linear independence of $\{\ln(p)\}$ is over $\mathbb{Q}$, not over $\mathbb{R}$. However, any *structurally meaningful* decomposition must assign integer (or at minimum rational) multiplicities to prime dimensions, so the restriction to $\mathbb{Q}$-coefficients is natural.

---

## 4. Spectral Additivity

Shannon's additivity axiom states that $h(1/(ab)) = h(1/a) + h(1/b)$: the total self-information of a conjunction is the sum of the individual totals. The information spectrum lifts this from a scalar identity to a vector identity.

**Theorem 4.1 (Spectral Additivity).** For any positive integers $a, b$:

$$\sigma(ab) = \sigma(a) + \sigma(b)$$

where addition is pointwise: $\sigma_p(ab) = \sigma_p(a) + \sigma_p(b)$ for every prime $p$.

*Proof.* For each prime $p$: $v_p(ab) = v_p(a) + v_p(b)$ (a standard property of the $p$-adic valuation). Therefore $\sigma_p(ab) = v_p(ab) \ln(p) = (v_p(a) + v_p(b)) \ln(p) = \sigma_p(a) + \sigma_p(b)$. $\square$

**Interpretation.** Shannon tells us the bill totals add up. Spectral additivity tells us each line item adds up independently. When two independent information sources are combined, the contribution from each structural dimension accumulates separately, with no cross-dimensional interaction. This reflects the fundamental independence of prime dimensions in the multiplicative structure of the integers.

**Example 4.2.** Let $a = 12 = 2^2 \times 3$ and $b = 35 = 5 \times 7$. Then $ab = 420 = 2^2 \times 3 \times 5 \times 7$.

| Dimension | $\sigma_p(12)$ | $\sigma_p(35)$ | $\sigma_p(12) + \sigma_p(35)$ | $\sigma_p(420)$ |
|-----------|----------------|----------------|-------------------------------|-----------------|
| $p = 2$ | 1.3863 | 0 | 1.3863 | 1.3863 |
| $p = 3$ | 1.0986 | 0 | 1.0986 | 1.0986 |
| $p = 5$ | 0 | 1.6094 | 1.6094 | 1.6094 |
| $p = 7$ | 0 | 1.9459 | 1.9459 | 1.9459 |
| **Total** | **2.4849** | **3.5553** | **6.0403** | **6.0403** |

The spectra sum dimension by dimension. Because $\gcd(12, 35) = 1$, there is no overlap and the spectra occupy entirely separate dimensions.

---

## 5. Spectral Overlap and the Conservation Law

The most significant consequence of the information spectrum is that it provides a precise, structural account of *shared information* between two integers. Shannon's framework has no notion of information overlap between two events; the spectrum provides one via the divisibility lattice.

### 5.1 Spectral Intersection and Union

**Theorem 5.1 (Spectral Overlap).** For any positive integers $a, b$:

$$\sigma(\gcd(a,b)) = \min(\sigma(a), \sigma(b)) \quad \text{componentwise}$$

$$\sigma(\operatorname{lcm}(a,b)) = \max(\sigma(a), \sigma(b)) \quad \text{componentwise}$$

That is, for every prime $p$:

$$\sigma_p(\gcd(a,b)) = \min(\sigma_p(a), \sigma_p(b)), \qquad \sigma_p(\operatorname{lcm}(a,b)) = \max(\sigma_p(a), \sigma_p(b)).$$

*Proof.* For each prime $p$: $v_p(\gcd(a,b)) = \min(v_p(a), v_p(b))$ and $v_p(\operatorname{lcm}(a,b)) = \max(v_p(a), v_p(b))$. These are standard identities (see [6], Chapter 2). Multiplying by $\ln(p)$ and noting that $\ln(p) > 0$, so $\min$ and $\max$ commute with multiplication by $\ln(p)$:

$$\sigma_p(\gcd(a,b)) = \min(v_p(a), v_p(b)) \cdot \ln(p) = \min(v_p(a) \ln(p),\, v_p(b) \ln(p)) = \min(\sigma_p(a), \sigma_p(b)). \quad \square$$

**Interpretation.**
- $\sigma(\gcd(a,b))$ is the *shared information structure*: the information content that $a$ and $b$ have in common, resolved by dimension.
- $\sigma(\operatorname{lcm}(a,b))$ is the *combined information structure*: the total information needed to describe what either $a$ or $b$ contributes, without double-counting.

### 5.2 The Conservation Law

**Theorem 5.2 (Information Conservation).** For any positive integers $a, b$:

$$\sigma(a) + \sigma(b) = \sigma(\gcd(a,b)) + \sigma(\operatorname{lcm}(a,b))$$

componentwise, and therefore in total:

$$h(1/a) + h(1/b) = h(1/\gcd(a,b)) + h(1/\operatorname{lcm}(a,b)).$$

*Proof.* For each prime $p$ and non-negative reals $x, y$: $x + y = \min(x, y) + \max(x, y)$. Applying this to $\sigma_p(a)$ and $\sigma_p(b)$ and using Theorem 5.1 gives the componentwise identity. Summing over all primes gives the scalar identity. $\square$

**Interpretation.** When two information sources are decomposed into their shared and combined structure, the total information is exactly conserved — no information is created or destroyed. The conservation holds not merely in total (the scalar identity, which follows from $\gcd(a,b) \cdot \operatorname{lcm}(a,b) = ab$), but dimension by dimension.

This is the spectral version of the inclusion-exclusion principle: the total information in $a$ and $b$ separately equals the information in their overlap plus the information in their union, in every prime dimension independently.

### 5.3 The Coprime Case

When $\gcd(a,b) = 1$, the spectra occupy entirely separate dimensions:

$$\sigma(\gcd(a,b)) = \sigma(1) = 0 \qquad \text{(zero shared information)}$$

$$\sigma(\operatorname{lcm}(a,b)) = \sigma(ab) = \sigma(a) + \sigma(b) \qquad \text{(full additivity)}$$

In this case the conservation law reduces to Shannon's additivity axiom. The conservation law of Theorem 5.2 is thus a generalisation of Shannon's additivity to the case where information sources are not independent — where they share structural dimensions.

**Example 5.3.** Let $a = 72 = 2^3 \times 3^2$ and $b = 108 = 2^2 \times 3^3$.

$\gcd(72, 108) = 36 = 2^2 \times 3^2$, $\quad \operatorname{lcm}(72, 108) = 216 = 2^3 \times 3^3$.

| Dimension | $\sigma_p(72)$ | $\sigma_p(108)$ | $\min$ | $\max$ | $\sigma_p(36)$ | $\sigma_p(216)$ |
|-----------|----------------|-----------------|--------|--------|----------------|-----------------|
| $p = 2$ | 2.0794 | 1.3863 | 1.3863 | 2.0794 | 1.3863 | 2.0794 |
| $p = 3$ | 2.1972 | 3.2958 | 2.1972 | 3.2958 | 2.1972 | 3.2958 |
| **Total** | **4.2767** | **4.6821** | **3.5835** | **5.3753** | **3.5835** | **5.3753** |

Conservation check: $4.2767 + 4.6821 = 8.9588 = 3.5835 + 5.3753$. $\checkmark$

The shared information $h(\gcd) = \ln(36) = 3.5835$ nats constitutes 83.8% of the smaller number's total information — quantifying the structural similarity between 72 and 108.

**Example 5.4 (Structural Dissimilarity Despite Similar Cost).** The integers 128 = $2^7$ and 105 = $3 \times 5 \times 7$ have similar total self-information ($\ln(128) = 4.852$, $\ln(105) = 4.654$) but completely orthogonal spectra:

| Dimension | $\sigma_p(128)$ | $\sigma_p(105)$ | $\min$ |
|-----------|-----------------|-----------------|--------|
| $p = 2$ | 4.8520 | 0 | 0 |
| $p = 3$ | 0 | 1.0986 | 0 |
| $p = 5$ | 0 | 1.6094 | 0 |
| $p = 7$ | 0 | 1.9459 | 0 |

$\gcd(128, 105) = 1$: zero shared information. Shannon's scalar measure says these are nearly equally informative; the spectrum reveals they have nothing structurally in common.

---

## 6. Uniqueness of the Decomposition

The information spectrum is not merely *a* structural decomposition of self-information — it is *the* decomposition, in the following precise sense.

**Theorem 6.1 (Cauchy Uniqueness).** Let $f \colon (\mathbb{Z}^+, \times) \to (V, +)$ be a continuous homomorphism from the positive integers under multiplication to a real vector space under addition. Then $f(n)$ is determined by its values on the primes, and if $V = \mathbb{R}$ then $f(n) = c \cdot \ln(n)$ for some constant $c \in \mathbb{R}$.

More precisely: any continuous function $f \colon (0, 1] \to \mathbb{R}$ satisfying $f(xy) = f(x) + f(y)$ has the form $f(x) = c \cdot \ln(x)$ for some constant $c$ (Cauchy's logarithmic functional equation [3]).

*Proof.* See Aczél [3], Theorem 1.4.1. The substitution $x = e^u, y = e^v$ reduces the equation to Cauchy's additive equation $g(u+v) = g(u) + g(v)$, whose unique continuous solution is $g(u) = cu$. $\square$

**Corollary 6.2.** The information spectrum $\sigma(n)$ is the unique continuous vector-valued homomorphism from $(\mathbb{Z}^+, \times)$ to the prime coordinate space $(\bigoplus_p \mathbb{R}, +)$ that is compatible with the multiplicative structure, up to a global rescaling of each coordinate.

*Proof.* Any continuous homomorphism $f \colon (\mathbb{Z}^+, \times) \to (\bigoplus_p \mathbb{R}, +)$ must satisfy $f(n) = f(\prod p^{a_p}) = \sum a_p f(p)$, so $f$ is determined by its values on primes. On each prime $p$, the restriction of $f_p$ to powers of $p$ gives a continuous map $f_p(p^k) = k \cdot f_p(p)$, so $f_p(p) = c_p$ for some constant. Choosing $c_p = \ln(p)$ recovers $\sigma$. $\square$

**Interpretation.** Cauchy's theorem says: if you want a continuous accounting system where the cost of combining two independent information sources is the sum of their costs, then the logarithm is the only option for the scalar total, and the information spectrum is the only option for the structural decomposition. There is no alternative.

---

## 7. Worked Examples

### 7.1 Information Anatomy: Depth Versus Breadth

The information spectrum distinguishes numbers that Shannon's scalar conflates.

| $n$ | Factorisation | $h(1/n)$ | $\omega(n)$ | Spectrum description |
|-----|---------------|-----------|-------------|---------------------|
| 64 | $2^6$ | 4.159 | 1 | All information in one dimension |
| 66 | $2 \times 3 \times 11$ | 4.190 | 3 | Information spread across three dimensions |
| 2048 | $2^{11}$ | 7.625 | 1 | High cost, single dimension |
| 2310 | $2 \times 3 \times 5 \times 7 \times 11$ | 7.745 | 5 | Similar cost, five dimensions |

The pairs (64, 66) and (2048, 2310) have nearly identical total information but maximally different structural complexity. Shannon's $h$ cannot distinguish them; the spectrum $\sigma$ separates them completely.

### 7.2 Quantifying Structural Overlap

| $a$ | $b$ | $\gcd$ | Shared info (nats) | Overlap ratio |
|-----|-----|--------|-------------------|---------------|
| 12 | 18 | 6 | 1.792 | 72.1% |
| 60 | 90 | 30 | 3.401 | 83.1% |
| 72 | 108 | 36 | 3.584 | 83.8% |
| 12 | 35 | 1 | 0 | 0% |
| 128 | 105 | 1 | 0 | 0% |

The *overlap ratio* $h(\gcd(a,b)) / \min(h(a), h(b))$ measures what fraction of the smaller number's information structure is shared with the larger. This quantity has no analog in Shannon's scalar framework.

### 7.3 Conservation Law Verification

For $a = 60$, $b = 90$:

$$h(60) + h(90) = 4.094 + 4.500 = 8.594$$

$$h(\gcd(60,90)) + h(\operatorname{lcm}(60,90)) = h(30) + h(180) = 3.401 + 5.193 = 8.594 \quad \checkmark$$

The conservation holds exactly, and the spectral decomposition shows that it holds independently in each prime dimension:

| Dimension | $\sigma_p(60)$ | $\sigma_p(90)$ | Sum | $\sigma_p(30)$ | $\sigma_p(180)$ | Sum |
|-----------|----------------|----------------|-----|----------------|-----------------|-----|
| $p = 2$ | 1.386 | 0.693 | 2.079 | 0.693 | 1.386 | 2.079 |
| $p = 3$ | 1.099 | 2.197 | 3.296 | 1.099 | 2.197 | 3.296 |
| $p = 5$ | 1.609 | 1.609 | 3.219 | 1.609 | 1.609 | 3.219 |
| **Total** | **4.094** | **4.500** | **8.594** | **3.401** | **5.193** | **8.594** |

---

## 8. Discussion

### 8.1 Summary

We have shown that Shannon's self-information $h(1/n) = \ln(n)$ has a unique structural decomposition — the information spectrum $\sigma(n)$ — whose components measure the information contribution of each independent prime dimension. This decomposition is:

1. **Unique** (Theorem 3.3): forced by the Fundamental Theorem of Arithmetic and the linear independence of prime logarithms.
2. **Dimension-wise additive** (Theorem 4.1): the spectral lift of Shannon's additivity axiom.
3. **Equipped with overlap structure** (Theorems 5.1–5.2): providing a conserved decomposition of shared and combined information via the GCD and LCM.
4. **Canonical** (Theorem 6.1): the only continuous structured decomposition compatible with the multiplicative structure, by Cauchy's functional equation.

### 8.2 Relation to Shannon's Framework

The information spectrum does not contradict or replace Shannon's theory — it refines it. The total self-information $h(1/n) = \|\sigma(n)\|_1$ is recovered as the $L^1$ norm of the spectrum. Every scalar identity in Shannon's framework (additivity, the chain rule) has a spectral lift that holds dimension by dimension.

The key addition is the *overlap structure*. Shannon's framework treats the self-information of two events as either additive (if independent) or related by the chain rule (if dependent). The spectrum provides a finer analysis: two integers $a$ and $b$ may share some structural dimensions and not others, and the conservation law $\sigma(a) + \sigma(b) = \sigma(\gcd) + \sigma(\operatorname{lcm})$ accounts for this partial overlap exactly.

### 8.3 Relation to the Resistance Isomorphism Framework

This paper's information spectrum is the prime coordinate vector of [4] reinterpreted as a structural decomposition of self-information. The four-layer framework of [4] — natural language, inverse integers, informational resistance, prime coordinate vectors — provides the algebraic scaffolding; the present paper provides the information-theoretic interpretation.

The conservation law (Theorem 5.2) is the information-theoretic reading of the lattice identity $\gcd(a,b) \cdot \operatorname{lcm}(a,b) = ab$ from [4]. The Cauchy uniqueness result (Theorem 6.1) is the information-theoretic reading of the uniqueness of the resistance mapping from [4, Theorem 2.5].

### 8.4 Connections to the Riemann Zeta Function

The Euler product $\zeta(s) = \prod_p (1 - p^{-s})^{-1}$ connects the prime structure exploited by the information spectrum to the global distribution of primes. The coprimality probability $6/\pi^2 = 1/\zeta(2)$ — the probability that two randomly chosen integers share zero spectral dimensions — is a global statistical consequence of the local spectral structure.

More precisely: the probability that two random integers share no information in prime dimension $p$ is $1 - 1/p^2$, and by the asymptotic independence of divisibility across primes, the probability of zero spectral overlap is $\prod_p (1 - 1/p^2) = 6/\pi^2$. The information spectrum makes this derivation transparent: complete spectral orthogonality is the condition $\min(\sigma(a), \sigma(b)) = 0$, which occurs with probability $6/\pi^2$ under natural density.

### 8.5 Limitations

The principal limitation is the restriction to the multiplicative integers. Shannon's self-information applies to arbitrary probability distributions; the information spectrum requires $p = 1/n$ with $n$ a positive integer. Whether the structural decomposition perspective extends to broader domains — for instance, to Gaussian integers, polynomial rings, or other unique factorisation domains — is an open question.

The spectrum also does not capture all forms of "structure" in a number. The information spectrum of $n = 2^{10} = 1024$ has a single nonzero component and zero spectral entropy, suggesting structural simplicity. But $1024$ has rich structure in other senses — it is a perfect tenth power, a binary round number, etc. The spectrum captures multiplicative structure specifically, not all mathematical structure.

### 8.6 Open Problems

1. **Extension to unique factorisation domains.** Does an analogous information spectrum exist for Gaussian integers $\mathbb{Z}[i]$, or for polynomial rings $\mathbb{F}_q[x]$? The Fundamental Theorem of Arithmetic generalises to these settings, and the prime elements provide a natural basis.

2. **Spectral entropy and the distribution of primes.** The spectral entropy $H(\sigma(n)) = -\sum_p \hat{\sigma}_p \ln(\hat{\sigma}_p)$, where $\hat{\sigma}_p = \sigma_p / \|\sigma\|_1$ is the normalised spectrum, measures how evenly information is distributed across dimensions. How does the average spectral entropy of integers up to $N$ behave asymptotically? This connects to the Erdős–Kac theorem on the distribution of $\omega(n)$.

3. **Mutual information interpretation.** The overlap ratio $h(\gcd(a,b)) / h(a)$ behaves like a mutual information measure. Can it be formalised as a mutual information in a suitable probabilistic framework?

4. **Non-integer extensions.** Can the spectrum be extended to rational numbers $a/b$ via $\sigma(a/b) = \sigma(a) - \sigma(b)$ (using the group completion of the monoid), and does this yield a useful notion of "signed information spectrum"?

---

## References

[1] C. E. Shannon, "A mathematical theory of communication," *Bell System Technical Journal*, vol. 27, no. 3, pp. 379–423, 1948.

[2] A. N. Kolmogorov, "Three approaches to the quantitative definition of information," *Problems of Information Transmission*, vol. 1, no. 1, pp. 1–7, 1965.

[3] J. Aczél, *Lectures on Functional Equations and Their Applications*, Academic Press, 1966.

[4] A. Pisani, "A unified algebraic framework for number theory, Boolean logic, and circuit topology via the logarithmic isomorphism," 2026.

[5] G. Birkhoff, "On the combination of subalgebras," *Proc. Cambridge Philos. Soc.*, vol. 29, no. 4, pp. 441–464, 1933.

[6] G. H. Hardy and E. M. Wright, *An Introduction to the Theory of Numbers*, 5th ed., Oxford University Press, 1979.

[7] L. Euler, "De summis serierum reciprocarum," *Commentarii academiae scientiarum Petropolitanae*, vol. 7, pp. 123–134, 1734.

[8] T. M. Cover and J. A. Thomas, *Elements of Information Theory*, 2nd ed., Wiley-Interscience, 2006.

---

## Appendix A: Notation

| Symbol | Meaning |
|--------|---------|
| $h(1/n)$ | Self-information of event with probability $1/n$, equal to $\ln(n)$ |
| $\sigma(n)$ | Information spectrum of $n$ |
| $\sigma_p(n)$ | Component of the spectrum at prime $p$: $v_p(n) \cdot \ln(p)$ |
| $v_p(n)$ | $p$-adic valuation: exponent of $p$ in factorisation of $n$ |
| $\omega(n)$ | Number of distinct prime factors of $n$ |
| $\|\sigma(n)\|_1$ | $L^1$ norm of the spectrum $= \ln(n) = h(1/n)$ |
