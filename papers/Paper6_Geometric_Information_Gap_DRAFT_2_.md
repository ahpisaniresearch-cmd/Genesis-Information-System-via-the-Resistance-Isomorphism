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

# The Geometric Information Gap: How Arithmetic Operations Lose Spatial Structure and Why ζ(2) Governs the Loss

**Alexander Pisani & Claude (Anthropic)**

a.h.pisani.research@gmail.com

April 2026

---

## Abstract

Every positive integer $n$ can be represented as $n$ identical objects arranged in space. The spatial arrangement carries geometric information — which axes exist, how they are oriented, how their lengths relate — that is progressively discarded as we move through the arithmetic hierarchy: counting compresses spatial arrangements into symbols, addition loses partition identity, multiplication loses factor ordering, and exponentiation loses sign and dimensional direction. We define the *geometric information gap* $G(n, \oplus)$ as the logarithm of the number of valid preimages of $n$ under operation $\oplus$, measuring the information (in nats or bits) required to recover the original arrangement from the compressed output.

The main results are:

1. **Hierarchy of loss.** The gaps satisfy $G_{\mathrm{add}}(n) \gg G_{\mathrm{mult}}(n) \gg G_{\mathrm{exp}}(n)$: addition loses exponentially more geometric information than multiplication, which loses more than exponentiation. The additive gap grows as $\exp(\pi\sqrt{2n/3})$, the multiplicative gap as $n^{\varepsilon}$, and the exponential gap as $O(\log n)$.

2. **The multiplicative gap generating function.** The Dirichlet series $Z_G(s) = \sum_{n=1}^{\infty} \ln d(n) \cdot n^{-s}$ admits the decomposition
$$Z_G(s) = \zeta(s) \cdot \sum_{p \text{ prime}} \sum_{a=1}^{\infty} \ln\!\left(1 + \frac{1}{a}\right) p^{-as}$$
where each term $\ln(1 + 1/a)$ is the incremental geometric ambiguity of one additional prime power. This is proved by differentiating the parametric family $F(\alpha, s) = \sum d(n)^{\alpha} n^{-s}$ at $\alpha = 0$.

3. **The additive–multiplicative bridge.** The additive gap satisfies $G_{\mathrm{add}}(n) = \ln p(n) \approx 2\sqrt{n \cdot \zeta(2)}$, where $p(n)$ is the partition function. The constant $\zeta(2) = \pi^2/6$ — the Euler product at $s = 2$ — simultaneously governs the additive degeneracy, the multiplicative gap generating function, the coprimality probability $6/\pi^2$, and the density of geometric independence in the prime coordinate space of [3]. It is the universal constant of geometric information loss.

4. **The universal search cost.** Factoring and discrete logarithm both require approximately $R(n)/2 = \ln(n)/2$ nats of search, where $R(n) = \ln(n)$ is the informational resistance of [1]. This shared cost equals half the total information content and may explain the equivalent computational hardness of these problems.

The individual mathematical ingredients are classical (the partition function, the divisor function, the Euler product). The contribution is the information-geometric framework: a unified account of *what is lost and what is preserved* at each level of the arithmetic hierarchy, connected through the generating function $Z_G(s)$ and the universal constant $\zeta(2)$.

**Keywords:** geometric information, partition function, divisor function, Euler product, zeta function, information spectrum, informational resistance, arithmetic hierarchy

**MSC (2020):** 11A25, 11P82, 94A15, 11M06, 68Q17

---

## 1. Introduction

### 1.1 The Problem

Consider the number 12. It can be physically instantiated as 12 identical objects arranged in space — for instance, as 3 rows of 4, or 4 rows of 3, or 2 rows of 6, or 6 rows of 2, or 12 in a line. Each arrangement carries geometric information: how many spatial axes exist, what their lengths are, and how they are oriented relative to one another.

When we write the symbol "12," all of this geometric detail is discarded. The symbol preserves the *quantity* (12 nats of self-information, per Shannon [6]) but not the *geometry* (which arrangement produced it). To reverse the encoding — to reconstruct a specific arrangement from the symbol — we must supply the missing geometric information.

This paper asks: *how much geometric information is lost at each level of the arithmetic hierarchy?* The hierarchy is:

- **Counting:** $n$ objects $\to$ symbol "$n$" (loses spatial arrangement)
- **Addition:** $(a, b) \to a + b$ (loses which partition)
- **Multiplication:** $(a, b) \to a \times b$ (loses factor ordering)
- **Exponentiation:** $(a, b) \to a^b$ (loses sign, dimension, phase)

At each level, the forward operation is deterministic and unique. The reverse operation is degenerate: multiple inputs map to the same output. The *geometric information gap* $G(n, \oplus)$ quantifies this degeneracy.

### 1.2 Summary of Results

We establish four main results:

1. The geometric information gap forms a strict hierarchy: $G_{\mathrm{add}} \gg G_{\mathrm{mult}} \gg G_{\mathrm{exp}}$ (Section 4).

2. The multiplicative gap generating function $Z_G(s) = \sum \ln d(n) \cdot n^{-s}$ admits an Euler-product-like decomposition into incremental per-prime contributions (Section 5, Theorem 5.1).

3. The additive and multiplicative gaps are connected through $\zeta(2) = \pi^2/6$, which governs both the partition asymptotics and the Euler product structure (Section 6).

4. Factoring and discrete logarithm share the universal search cost $R(n)/2$, suggesting a common information-theoretic origin for their equivalent computational hardness (Section 7).

### 1.3 Relation to Prior Work

This paper builds on the algebraic and information-theoretic framework developed in [1]–[5]:

| Paper | Contribution used here |
|-------|----------------------|
| [1] The Logarithmic Isomorphism | Informational resistance $R(n) = \ln(n)$; series/parallel correspondence |
| [2] The Natural Operating System | Master equation; Möbius signs as inclusion-exclusion |
| [3] Structured Self-Information | Information spectrum $\sigma_p(n) = v_p(n) \ln(p)$; conservation law $\sigma(a) + \sigma(b) = \sigma(\gcd) + \sigma(\mathrm{lcm})$ |
| [4] Multi-State Wave Computation | Dirichlet characters as wave phases; functional completeness |
| [5] Spectral-Temporal Encoding | Multi-wavelength encoding; GCD/LCM as physical operations |
| [*] The Geometry of Knowing | Unary-to-symbol encoding; prime hypergrid; degeneracy of the reverse map |

The working notes [*] introduced the observation that encoding $n$ dots as a symbol preserves the quantity but loses the spatial arrangement, and that the prime coordinate space captures the *structure* (which axes exist) but not the *orientation* (how axes are assigned to physical directions). The present paper formalises and extends this observation across the full arithmetic hierarchy.

The connection between the partition function and $\zeta(2)$ in the asymptotic $\ln p(n) \approx 2\sqrt{n \cdot \zeta(2)}$ is classical (Hardy and Ramanujan [7]). The decomposition of $Z_G(s)$ as $\zeta(s)$ times a prime sum appears to be new, as is the interpretation of $\zeta(2)$ as a universal geometric information constant.

**What this paper does not claim.** We do not claim that the geometric information gap resolves open problems in computational complexity. The observation that factoring and discrete logarithm share the search cost $R(n)/2$ is suggestive but does not constitute a proof of equivalence or a lower bound. The framework is descriptive — it quantifies what is lost — not prescriptive.

---

## 2. Background

### 2.1 Notation

Throughout, $n$ denotes a positive integer with prime factorisation $n = \prod_p p^{v_p(n)}$. We write $d(n) = \prod_p (v_p(n) + 1)$ for the number of (positive) divisors, $p(n)$ for the number of unrestricted partitions of $n$, and $f(n)$ for the number of ordered factorisations of $n$ into factors $\geq 2$. Logarithms are natural (base $e$) unless otherwise stated; information is measured in nats (1 nat $= \log_2 e \approx 1.443$ bits).

### 2.2 The Information Spectrum ([3])

The information spectrum of $n$ is $\sigma(n) : \text{Primes} \to \mathbb{R}_{\geq 0}$ with $\sigma_p(n) = v_p(n) \cdot \ln(p)$. It satisfies:

- **Additivity:** $\sigma(ab) = \sigma(a) + \sigma(b)$ (componentwise).
- **Total recovery:** $\|\sigma(n)\|_1 = \ln(n)$.
- **Overlap:** $\sigma(\gcd(a,b)) = \min(\sigma(a), \sigma(b))$ and $\sigma(\mathrm{lcm}(a,b)) = \max(\sigma(a), \sigma(b))$.
- **Conservation:** $\sigma(a) + \sigma(b) = \sigma(\gcd) + \sigma(\mathrm{lcm})$ (componentwise).

### 2.3 Informational Resistance ([1])

The map $R(n) = \ln(n)$ is the unique continuous monoid isomorphism from $(\mathbb{Z}^+, \times)$ to $(\mathbb{R}_{\geq 0}, +)$. Under the circuit analogy of [1], $R(n)$ is the informational *resistance* of $n$: resistances in series correspond to multiplication ($R(ab) = R(a) + R(b)$), and the GCD/LCM operations correspond to minimum/maximum resistance paths.

### 2.4 The Geometry of Knowing ([*])

Every positive integer $n = p_1^{a_1} \times \cdots \times p_k^{a_k}$ can be arranged as a $k$-dimensional hypergrid with side lengths $p_i^{a_i}$ along perpendicular axes. The logarithm converts each side length to an information coordinate: $\sigma_{p_i}(n) = \ln(p_i^{a_i})$. The volume (product of side lengths) is $n$; the total information (sum of coordinates) is $\ln(n)$.

The reverse map — from the spectrum $\sigma(n)$ back to a physical arrangement — is degenerate: the symmetric group $S_k$ acts on the axis assignments, and the spectrum is invariant under this action. For $k$ distinct prime factors, there are $k!$ valid orientations. This degeneracy is the simplest instance of the geometric information gap.

### 2.5 The Euler Product

The Riemann zeta function $\zeta(s) = \sum_{n=1}^{\infty} n^{-s}$ admits the Euler product:

$$\zeta(s) = \prod_{p \text{ prime}} \frac{1}{1 - p^{-s}}, \qquad \mathrm{Re}(s) > 1.$$

At $s = 2$: $\zeta(2) = \pi^2/6$. The factor $(1 - p^{-s})^{-1} = \sum_{a=0}^{\infty} p^{-as}$ generates all powers of the prime $p$, and the product over primes generates all positive integers via the Fundamental Theorem of Arithmetic. The coprimality probability is $P(\gcd(a,b) = 1) = 1/\zeta(2) = 6/\pi^2$.

---

## 3. The Geometric Information Gap: Definition

### 3.1 Formal Definition

**Definition 3.1 (Geometric Information Gap).** For an arithmetic operation $\oplus$ and a positive integer $n$ in the range of $\oplus$, the *geometric information gap* is:

$$G(n, \oplus) = \ln \left| \{ (a, b) : a \oplus b = n, \; a, b \in \mathrm{dom}(\oplus) \} \right|$$

measured in nats. When the operation is clear from context, we write $G_{\mathrm{add}}(n)$, $G_{\mathrm{mult}}(n)$, or $G_{\mathrm{exp}}(n)$.

**Remark 3.2.** We use the natural logarithm for consistency with the information spectrum. In bits: $G_{\mathrm{bits}} = G / \ln 2$.

**Remark 3.3.** Definition 3.1 counts *ordered* preimages. The *unordered* gap $G^{\mathrm{un}}(n, \oplus)$ uses unordered pairs $\{a, b\}$ and satisfies $G^{\mathrm{un}} \leq G$ in general. The distinction matters: the ordering information is precisely the axis orientation that encoding discards.

### 3.2 Interpretation

$G(n, \oplus)$ measures the information (in nats) required to identify which specific preimage $(a, b)$ produced the output $n$. If the reverse operation is unique ($|\text{preimages}| = 1$), then $G = 0$. If there are $k$ preimages, an observer must supply $\ln(k)$ nats to disambiguate.

---

## 4. The Hierarchy of Loss

### 4.1 Layer 1: Addition

**Definition 4.1.** The *additive gap* of $n$ is:

$$G_{\mathrm{add}}(n) = \ln p(n)$$

where $p(n)$ is the number of unrestricted partitions of $n$.

The ordered-pair count is $n - 1$ (compositions into two parts), and the total number of compositions (into any number of positive parts) is $2^{n-1}$. We use the partition function $p(n)$ as the canonical measure because it counts the distinct *structures* (unordered), removing the trivial reordering ambiguity.

**Theorem 4.2** (Hardy–Ramanujan [7]). As $n \to \infty$:

$$p(n) \sim \frac{1}{4n\sqrt{3}} \exp\!\left(\pi \sqrt{\frac{2n}{3}}\right).$$

Therefore $G_{\mathrm{add}}(n) \sim \pi\sqrt{2n/3}$ nats, which grows exponentially in $\sqrt{n}$.

### 4.2 Layer 2: Multiplication

**Definition 4.3.** The *multiplicative pair gap* of $n$ is:

$$G_{\mathrm{mult}}^{\mathrm{pair}}(n) = \ln d(n)$$

where $d(n)$ is the divisor function. The *multiplicative factorisation gap* is:

$$G_{\mathrm{mult}}^{\mathrm{fact}}(n) = \ln f(n)$$

where $f(n)$ is the number of ordered factorisations of $n$ into factors $\geq 2$.

**Fact 4.4.** The average order of $\ln d(n)$ is $(\ln 2)(\ln \ln n)$ (see [8, Theorem 317]). In particular, $G_{\mathrm{mult}}(n) = O((\ln n)^{\varepsilon})$ for any $\varepsilon > 0$ — sub-polynomial growth.

**Remark 4.5.** The *axis orientation gap* $G_{\mathrm{orient}}(n) = \ln(k!)$, where $k = \omega(n)$ is the number of distinct prime factors, measures the $S_k$ symmetry identified in [*]. This is a component of $G_{\mathrm{mult}}^{\mathrm{fact}}$: the total factorisation ambiguity decomposes as orientation (which prime axis is which) plus grouping (how primes combine into composite factors).

### 4.3 Layer 3: Exponentiation

**Definition 4.6.** The *exponential gap* of $n$ is:

$$G_{\mathrm{exp}}(n) = \ln \left| \{ (a, b) : a^b = n, \; a \geq 1, \; b \geq 1 \} \right|.$$

**Fact 4.7.** For most integers $n$, the only representation is $(n, 1)$, giving $G_{\mathrm{exp}}(n) = 0$. The set of perfect powers has density zero among the integers. When $n$ is a perfect power, $G_{\mathrm{exp}}(n) = O(\ln \ln n)$.

Exponentiation additionally loses:

- **Sign:** $(-a)^{2k} = a^{2k}$. The sign (direction) of the base is discarded for even exponents.
- **Dimension:** A length $a$ raised to the $b$-th power becomes an area ($b = 2$), volume ($b = 3$), etc. The exponent carries dimensional meaning that is not recoverable from the value alone.
- **Complex roots:** The equation $x^b = n$ has $b$ roots in $\mathbb{C}$, of which at most 2 are real. The $b - 1$ (or $b - 2$) discarded roots are the complex phases — precisely the Dirichlet character values used in [4] for multi-state computation.

### 4.4 The Hierarchy

**Proposition 4.8 (Hierarchy of Loss).** For all sufficiently large $n$:

$$G_{\mathrm{exp}}(n) \ll G_{\mathrm{mult}}(n) \ll G_{\mathrm{add}}(n).$$

More precisely:

| Layer | Gap growth | Asymptotics |
|-------|-----------|-------------|
| Addition | Exponential in $\sqrt{n}$ | $G_{\mathrm{add}}(n) \sim \pi\sqrt{2n/3}$ |
| Multiplication | Sub-polynomial | $G_{\mathrm{mult}}(n) = O(n^{\varepsilon})$ for any $\varepsilon > 0$ |
| Exponentiation | Zero for most $n$ | $G_{\mathrm{exp}}(n) = 0$ for non-perfect-powers |

*Proof.* Immediate from Theorem 4.2, Fact 4.4, and Fact 4.7. $\square$

**Interpretation.** Addition is the most geometrically destructive operation: it creates exponentially many valid preimages, each a distinct spatial arrangement. Multiplication preserves far more geometric structure — the Fundamental Theorem of Arithmetic guarantees a *unique* prime factorisation, so the only ambiguity is in how primes are grouped and ordered. Exponentiation preserves the most structure: almost no integers can be expressed as non-trivial powers.

---

## 5. The Multiplicative Gap Generating Function

### 5.1 Definition and Decomposition

**Definition 5.1.** The *multiplicative geometric gap generating function* is:

$$Z_G(s) = \sum_{n=1}^{\infty} \ln d(n) \cdot n^{-s}, \qquad \mathrm{Re}(s) > 1.$$

**Theorem 5.2 (Euler-type decomposition of $Z_G$).** For $\mathrm{Re}(s) > 1$:

$$Z_G(s) = \zeta(s) \cdot \sum_{p \text{ prime}} \sum_{a=1}^{\infty} \ln\!\left(1 + \frac{1}{a}\right) p^{-as}.$$

*Proof.* Define the parametric family:

$$F(\alpha, s) = \sum_{n=1}^{\infty} d(n)^{\alpha} \cdot n^{-s}.$$

Since $d(n)$ is a multiplicative function with $d(p^a) = a + 1$, the Dirichlet series admits an Euler product:

$$F(\alpha, s) = \prod_{p} F_p(\alpha, s), \qquad F_p(\alpha, s) = \sum_{a=0}^{\infty} (a+1)^{\alpha} \cdot p^{-as}.$$

At $\alpha = 0$: $F_p(0, s) = \sum_{a=0}^{\infty} p^{-as} = (1 - p^{-s})^{-1}$, and $F(0, s) = \zeta(s)$.

At $\alpha = 1$: $F_p(1, s) = \sum_{a=0}^{\infty} (a+1) p^{-as} = (1 - p^{-s})^{-2}$, and $F(1, s) = \zeta(s)^2$.

The gap generating function is:

$$Z_G(s) = \frac{\partial F}{\partial \alpha}\bigg|_{\alpha = 0} = \sum_{n=1}^{\infty} d(n)^0 \cdot \ln d(n) \cdot n^{-s} = \sum_{n=1}^{\infty} \ln d(n) \cdot n^{-s}.$$

By the product rule for the logarithmic derivative:

$$Z_G(s) = F(0, s) \cdot \sum_{p} \frac{1}{F_p(0,s)} \cdot \frac{\partial F_p}{\partial \alpha}\bigg|_{\alpha = 0}.$$

Now:

$$\frac{\partial F_p}{\partial \alpha}\bigg|_{\alpha = 0} = \sum_{a=0}^{\infty} \ln(a+1) \cdot p^{-as}.$$

Therefore:

$$\frac{1}{F_p(0,s)} \cdot \frac{\partial F_p}{\partial \alpha}\bigg|_{\alpha = 0} = (1 - p^{-s}) \sum_{a=0}^{\infty} \ln(a+1) \cdot p^{-as}.$$

Multiplying through and collecting terms:

$$(1 - p^{-s}) \sum_{a=0}^{\infty} \ln(a+1) \cdot p^{-as} = \sum_{a=1}^{\infty} \left[\ln(a+1) - \ln(a)\right] p^{-as} = \sum_{a=1}^{\infty} \ln\!\left(1 + \frac{1}{a}\right) p^{-as}.$$

(The $a = 0$ term vanishes since $\ln(1) = 0$, and the subtraction telescopes.)

Combining: $Z_G(s) = \zeta(s) \cdot \sum_p \sum_{a \geq 1} \ln(1 + 1/a) \cdot p^{-as}$. $\square$

### 5.2 The Incremental Geometric Information

Each term $\Delta_a = \ln(1 + 1/a)$ in the decomposition has a precise interpretation: it is the *incremental geometric ambiguity* of increasing a prime's exponent from $a - 1$ to $a$. When the exponent of $p$ in $n$ increases from $a-1$ to $a$, the divisor count grows from $a$ to $a + 1$, adding one new divisor pair. The information cost of this additional pair is $\ln((a+1)/a) = \ln(1 + 1/a)$.

Key properties of the incremental sequence:

- **Decreasing:** $\Delta_1 = \ln 2 > \Delta_2 = \ln(3/2) > \Delta_3 = \ln(4/3) > \cdots$. Diminishing returns.
- **Telescoping:** $\sum_{a=1}^{A} \Delta_a = \ln(A + 1)$. The increments sum to the total ambiguity $\ln d(p^A)$.
- **Asymptotic:** $\Delta_a \sim 1/a$ for large $a$. The harmonic-like decay explains the slow growth of $G_{\mathrm{mult}}$.

### 5.3 Per-Prime Structure

Define the *per-prime geometric contribution*:

$$C_p(s) = \sum_{a=1}^{\infty} \ln\!\left(1 + \frac{1}{a}\right) p^{-as}.$$

Then $Z_G(s) = \zeta(s) \cdot \sum_p C_p(s)$. For $s = 2$, numerical evaluation gives:

| Prime $p$ | $C_p(2)$ | Cumulative % of $\sum C_p(2)$ |
|-----------|----------|-------------------------------|
| 2 | 0.20422 | 58.3% |
| 3 | 0.08245 | 81.9% |
| 5 | 0.02839 | 90.0% |
| 7 | 0.01432 | 94.1% |
| 11 | 0.00576 | 95.7% |

The geometric gap is dominated by the smallest primes. Primes 2 and 3 alone account for over 80% of the total gap at $s = 2$.

**Leading behaviour.** For each prime, $C_p(s)$ is dominated by the $a = 1$ term:

$$C_p(s) \approx \ln(2) \cdot p^{-s} + O(p^{-2s}).$$

Therefore $\sum_p C_p(s) \approx \ln(2) \cdot P(s)$, where $P(s) = \sum_p p^{-s}$ is the prime zeta function.

### 5.4 Numerical Verification

The decomposition $Z_G(s) = \zeta(s) \cdot \sum_p C_p(s)$ is verified by comparing direct summation $\sum_{n \leq N} \ln d(n) \cdot n^{-s}$ with the Euler product form, using 168 primes up to 1000:

| $s$ | Direct sum ($N = 50000$) | Euler form | Relative error |
|-----|-------------------------|------------|----------------|
| 2.0 | 0.57689825 | 0.57672395 | $3 \times 10^{-4}$ |
| 3.0 | 0.15469912 | 0.15469906 | $4 \times 10^{-7}$ |
| 5.0 | 0.02612579 | 0.02612579 | $< 10^{-12}$ |

The agreement improves as $s$ increases (faster convergence of both the direct sum and the Euler product).

---

## 6. The Additive–Multiplicative Bridge

### 6.1 The Partition Asymptotic and ζ(2)

The Hardy–Ramanujan asymptotic (Theorem 4.2) gives:

$$G_{\mathrm{add}}(n) = \ln p(n) \sim \pi \sqrt{\frac{2n}{3}}.$$

We observe the algebraic identity:

$$\pi \sqrt{\frac{2n}{3}} = \sqrt{\frac{2\pi^2 n}{3}} = \sqrt{4n \cdot \frac{\pi^2}{6}} = 2\sqrt{n \cdot \zeta(2)}.$$

**Corollary 6.1 (Additive gap in terms of ζ(2)).**

$$G_{\mathrm{add}}(n) \approx 2\sqrt{n \cdot \zeta(2)} \qquad \text{as } n \to \infty.$$

This is an exact algebraic rewriting: $2\sqrt{\zeta(2)} = \pi\sqrt{2/3}$ is verified to full numerical precision.

### 6.2 The Generating Function Connection

The partition generating function is:

$$\sum_{n=0}^{\infty} p(n) x^n = \prod_{k=1}^{\infty} \frac{1}{1 - x^k}.$$

The Euler product for $\zeta(s)$ is:

$$\zeta(s) = \prod_{p \text{ prime}} \frac{1}{1 - p^{-s}}.$$

Both are infinite products of factors $(1 - q)^{-1}$, but over different index sets:

- **Partitions:** factors $(1 - x^k)^{-1}$ for $k = 1, 2, 3, 4, 5, 6, \ldots$ (all positive integers).
- **Euler product:** factors $(1 - p^{-s})^{-1}$ for $p = 2, 3, 5, 7, 11, \ldots$ (primes only).

The partition product *includes* the Euler product as a sub-product:

$$\prod_{k=1}^{\infty} \frac{1}{1 - x^k} = \prod_{p \text{ prime}} \frac{1}{1 - x^p} \cdot \prod_{\substack{k \geq 1 \\ k \text{ composite}}} \frac{1}{1 - x^k}.$$

In logarithmic form, setting $x = e^{-t}$:

$$\sum_{k=1}^{\infty} \sum_{m=1}^{\infty} \frac{e^{-kmt}}{m} = \sum_p \sum_{m=1}^{\infty} \frac{e^{-pmt}}{m} + \sum_{\substack{k \text{ composite}}} \sum_{m=1}^{\infty} \frac{e^{-kmt}}{m}.$$

As $t \to 0^+$, the left side has leading asymptotic $\pi^2/(6t) = \zeta(2)/t$. This is the origin of $\zeta(2)$ in the partition asymptotic: the total additive ambiguity is governed by the sum over all integers, and its leading coefficient is the Euler product at $s = 2$.

### 6.3 ζ(2) as the Universal Geometric Information Constant

The constant $\zeta(2) = \pi^2/6$ now appears in four related roles:

1. **Additive gap:** $G_{\mathrm{add}}(n) \approx 2\sqrt{n \cdot \zeta(2)}$ (Corollary 6.1).
2. **Multiplicative gap generating function:** $Z_G(s) = \zeta(s) \cdot \sum_p C_p(s)$, evaluated at $s = 2$ (Theorem 5.2).
3. **Coprimality probability:** $P(\gcd(a,b) = 1) = 1/\zeta(2) = 6/\pi^2$ — the probability that two integers share zero geometric structure in the prime coordinate space of [3].
4. **Geometric independence density:** $6/\pi^2$ is the fraction of integer pairs with orthogonal spectra $\langle \sigma(a), \sigma(b) \rangle = 0$ in the sense of [*], Section 5.

These four roles are not coincidental. They are connected through the Euler product, which bridges the additive universe (sum over integers, partition generating function) and the multiplicative universe (product over primes, Dirichlet series). The constant $\zeta(2) = \pi^2/6$ encodes the *density of geometric structure* — how much shared geometry exists among the integers — and this density governs information loss in both domains.

### 6.4 The Role of π

The appearance of $\pi$ in the geometric information gap at every level of the arithmetic hierarchy has a unified source:

- **Additive (partitions):** $\pi$ enters through the circle method of Hardy, Ramanujan, and Rademacher, which uses the modular properties of the Dedekind eta function — an object defined on the upper half-plane via $e^{2\pi i \tau}$.
- **Multiplicative (Euler product):** $\pi$ enters through $\zeta(2k) = (-1)^{k+1} B_{2k} (2\pi)^{2k} / (2(2k)!)$, where $B_{2k}$ are Bernoulli numbers. The even zeta values are rational multiples of powers of $\pi$.
- **Exponential (roots of unity):** $\pi$ enters through the unit circle $e^{2\pi i k/b}$, on which the $b$-th roots of unity are uniformly distributed.
- **Wave computation ([4]):** The Dirichlet characters used for multi-state computation take values at these same roots of unity. The wave interference that performs computation *is* the rotational geometry that produces $\pi$.

$\pi$ is the fundamental constant of rotational geometry, and the geometric information gap is governed by rotational symmetry at every level.

---

## 7. The Search Cost: G_location

### 7.1 Two Components of the Gap

The geometric information gap as defined in Section 3 measures *combinatorial degeneracy* — how many preimages exist. However, the computational difficulty of reversing an operation depends on a second quantity: the *search cost* of locating the correct preimage.

**Definition 7.1 (Informal).** The *locational gap* $G_{\mathrm{loc}}(n, \oplus)$ is the number of nats of information required to locate a specific preimage of $n$ under $\oplus$ by the best known algorithm.

We distinguish $G_{\mathrm{deg}}$ (degeneracy, Section 3) from $G_{\mathrm{loc}}$ (search):

| Operation | $G_{\mathrm{deg}}(n)$ | $G_{\mathrm{loc}}(n)$ | $G_{\mathrm{total}}$ |
|-----------|----------------------|----------------------|----------------------|
| Addition (partition) | $\sim \pi\sqrt{2n/3}$ (exponential in $\sqrt{n}$) | $\approx 0$ (trivial) | $\sim \pi\sqrt{2n/3}$ |
| Multiplication (factor) | $\sim \ln d(n)$ (sub-polynomial) | $\sim R(n)/2$ (trial division) | $\sim R(n)/2$ |
| Exponentiation (discrete log) | $\approx 0$ (most $n$) | $\sim R(n)/2$ (baby-step giant-step) | $\sim R(n)/2$ |

### 7.2 The Universal Search Cost R(n)/2

The search cost for both factoring (via trial division to $\sqrt{n}$) and discrete logarithm (via baby-step giant-step) is approximately:

$$G_{\mathrm{loc}} \approx \frac{1}{2} \ln(n) = \frac{R(n)}{2}$$

where $R(n) = \ln(n)$ is the informational resistance of [1]. This is exactly *half* the total informational content of $n$.

The resistance interpretation is direct: trial division tests all potential factors up to $\sqrt{n}$, which has resistance $R(\sqrt{n}) = \frac{1}{2} R(n)$. The search probes *half* the total resistance.

**Observation 7.3.** Factoring and discrete logarithm have the same $G_{\mathrm{total}} \approx R(n)/2$ despite distributing it differently between degeneracy and location:

- **Factoring:** $G_{\mathrm{deg}} = \ln d(n) \approx \varepsilon \ln n$, $G_{\mathrm{loc}} \approx \frac{1}{2} \ln n - \varepsilon \ln n$.
- **Discrete log:** $G_{\mathrm{deg}} = 0$, $G_{\mathrm{loc}} = \frac{1}{2} \ln n$.

The total is the same. This coincidence of total cost may be the information-theoretic reason that factoring and discrete logarithm are believed to be of equivalent computational hardness — a relationship well-established via reductions (e.g., [9]) but not previously explained in information-geometric terms.

### 7.3 Additive Dominance

The additive gap $G_{\mathrm{add}}(n) = 2\sqrt{n \cdot \zeta(2)}$ exceeds $G_{\mathrm{loc}}(n) = R(n)/2 = \frac{1}{2}\ln n$ for all $n \geq 2$. The additive universe *always* has more degeneracy than the multiplicative universe has search cost. Addition is fundamentally more ambiguous than multiplication is difficult to reverse.

---

## 8. GCD as Information Recovery

The GCD operation occupies a special role in this framework: it *recovers* shared geometric information without requiring the original arrangement.

Given two integers $a$ and $b$, the information spectrum of $\gcd(a,b)$ is the componentwise minimum of $\sigma(a)$ and $\sigma(b)$ ([3], Theorem 5.1). This is the largest common sub-grid — the geometric structure shared by every valid arrangement of both $a$ and $b$.

Three properties are relevant:

1. **Ambiguity reduction.** $d(\gcd(a,b)) \leq \min(d(a), d(b))$: the shared structure has fewer valid arrangements than either input. The GCD *concentrates* geometric information.

2. **Conservation.** The nat conservation law $\ln(a) + \ln(b) = \ln(\gcd) + \ln(\mathrm{lcm})$ is the information-theoretic statement that the total geometric content is partitioned exactly between what is shared and what is combined.

3. **Factor-free computability.** The GCD is computable via the Euclidean algorithm in $O(\log n)$ steps — without knowing the factorisation of either input. It extracts the shared prime geometry *despite* the geometric information gap.

The GCD thus provides a partial recovery mechanism: it cannot recover the full arrangement (orientation, ordering) but it can identify the shared dimensional structure. In the circuit analogy of [1], the GCD computes the minimum-resistance path through the shared sub-network.

---

## 9. Discussion and Open Problems

### 9.1 Summary

We have defined the geometric information gap $G(n, \oplus)$, shown that it forms a strict hierarchy across the arithmetic operations, derived the Euler-type decomposition of the multiplicative gap generating function $Z_G(s)$, and identified $\zeta(2) = \pi^2/6$ as the universal constant connecting the additive and multiplicative domains.

### 9.2 Limitations

1. **G_location is informal.** The locational gap $G_{\mathrm{loc}}$ is defined by reference to specific algorithms (trial division, baby-step giant-step), not as an intrinsic property of $n$. A formal definition would require connecting $G_{\mathrm{loc}}$ to circuit complexity or communication complexity, which we do not attempt here.

2. **The conservation of G is unproven.** The nat conservation law $\sigma(a) + \sigma(b) = \sigma(\gcd) + \sigma(\mathrm{lcm})$ holds exactly for the information spectrum. Whether an analogous conservation law holds for $G$ itself (across the full hierarchy, not just at the multiplicative level) is an open question.

3. **The generating function bridge is incomplete.** We have shown that $\zeta(2)$ appears in both $G_{\mathrm{add}}$ (via the partition asymptotic) and $Z_G$ (via the Euler product). A direct functional equation relating $Z_{G,\mathrm{add}}(s) = \sum \ln p(n) \cdot n^{-s}$ and $Z_G(s)$ has not been established.

### 9.3 Open Problems

1. **Closed form for $Z_G(2)$.** Can the value $Z_G(2) = \zeta(2) \cdot \sum_p C_p(2)$ be expressed in terms of known constants? This requires evaluating $\sum_p C_p(2)$, which involves the prime zeta function $P(s)$ at $s = 2$ — an object with no known closed form.

2. **Analytic continuation of $Z_G$.** Does $Z_G(s)$ admit meromorphic continuation to $\mathrm{Re}(s) > 0$? The factor $\zeta(s)$ has a pole at $s = 1$, and the prime sum $\sum_p C_p(s)$ converges for $\mathrm{Re}(s) > 1$. The behaviour near $s = 1$ would reveal the average geometric gap of the integers.

3. **A functional equation.** Is there a relationship of the form $Z_{G,\mathrm{add}}(s) = h(\zeta(s), Z_G(s))$ connecting the additive and multiplicative gap generating functions? The partition–Euler product connection (Section 6.2) suggests such a relationship exists at the level of generating functions.

4. **Formalising G_location.** Can the locational gap be defined intrinsically (without reference to specific algorithms) as a property of the number $n$ and the operation $\oplus$? A candidate: $G_{\mathrm{loc}}(n, \oplus) = \min_A \ln T(A, n)$, where $T(A, n)$ is the running time of the optimal algorithm $A$ for inverting $\oplus$ at $n$.

5. **Connection to the wave architecture.** The multi-state wave computer of [4] uses Dirichlet characters (roots of unity) for computation via interference. The geometric information gap is governed by the same rotational structure. Can the wave architecture be used to *compute* $G(n, \oplus)$ — or, more ambitiously, to *exploit* the gap for computational advantage? The quantum-like cascade results of the companion simulation work suggest that wave interference naturally processes the fuzzy regions of the prime coordinate space where the lost geometry resides.

6. **The golden ratio threshold.** Preliminary simulations (companion code) suggest that the measurement threshold in the fuzzy prime coordinate space — the point where discrete classification fails — occurs at a spread-to-spacing ratio near $1/\varphi^2 \approx 0.382$, where $\varphi = (1+\sqrt{5})/2$ is the golden ratio. Whether this threshold is universal or an artifact of the specific gate sequence used in simulations is unknown.

7. **Path information in counting.** The counting layer (unary $\to$ symbol) loses not only the grid shape but also the *traversal path* through the objects. For $n$ objects in a 2D grid, the number of Hamiltonian paths grows combinatorially (e.g., 124 paths through a $3 \times 4$ grid of 12 objects — far exceeding $\ln(12)$ nats). This path information is the "vector direction" component that connects the counting loss to the travelling salesman problem, and its inclusion would substantially increase $G_{\mathrm{count}}$ in the hierarchy.

---

## 10. The Geometry–Concept Duality

### 10.1 Conceptual Information

Moving *up* the arithmetic hierarchy (counting $\to$ addition $\to$ multiplication $\to$ exponentiation), each operation *loses* geometric information but *gains* conceptual structure. At the bottom (unary), objects have maximum spatial detail but zero conceptual identity — all symbols are identical and interchangeable. At the top (exponentiation), there is minimal geometric ambiguity but rich conceptual content — dimensional hierarchy, sign, and the full phase structure of roots of unity.

We identify the conceptual gain at each transition:

| Transition | Geometric loss | Conceptual gain |
|------------|---------------|-----------------|
| Counting $\to$ Addition | Path and arrangement | Quantity (cardinal number) |
| Addition $\to$ Multiplication | Partition identity | Type/structure (prime decomposition) |
| Multiplication $\to$ Exponentiation | Factor ordering | Dimension and phase (roots of unity) |

The critical transition is **addition $\to$ multiplication**. Below this boundary, numbers are pure quantities: $3 + 5 = 8$ regardless of what the objects represent. Above this boundary, numbers carry *type*: $5 \times \text{apple} = 5\text{ apples}$. Multiplication is the operation where qualitative meaning first enters the number system.

### 10.2 The Duality of Forward and Reverse Operations

The geometry–concept duality extends to reverse operations. Going backward through the hierarchy (root, divide, subtract) *loses* conceptual information:

- **Subtraction** completely transforms prime structure: $360 - 120 = 240$ has prime signature $(4,1,1)$ versus the input's $(3,2,1)$. Subtraction destroys type.
- **Division** removes one factor's prime contribution but preserves the remaining substructure. Division reduces type.
- **Root extraction** loses only the dimensional identity (which exponent was used). Root extraction weakens type.

The pattern is exactly inverted:

$$G_{\mathrm{count}} \gg G_{\mathrm{add}} \gg G_{\mathrm{mult}} \gg G_{\mathrm{exp}} \qquad \text{(forward: geometry lost)}$$

$$C_{\mathrm{subtract}} \gg C_{\mathrm{divide}} \gg C_{\mathrm{root}} \qquad \text{(reverse: concept lost)}$$

The operation that destroys the most geometry going forward is the one whose inverse destroys the most conceptual structure going backward.

### 10.3 Addition Cannot Support the Resistance Isomorphism

The resistance isomorphism $R(n) = \ln(n)$ of [1] requires $R(ab) = R(a) + R(b)$: the logarithm converts multiplication to addition. This works because multiplication composes independent structural dimensions — the prime axes are orthogonal and their information contributions add.

Addition violates this: $\ln(a + b) \neq \ln(a) + \ln(b)$ in general. Conceptual structure does not add — "5 apples + 3 oranges" is not "8 appanges." The types fail to combine under addition because addition operates on *quantity*, not on *structure*.

This asymmetry is the information-theoretic reason that the additive gap is exponentially larger than the multiplicative gap: addition treats all partitions as equivalent (destroying structural distinctions), while multiplication preserves the prime decomposition (maintaining structural identity).

---

## 11. Primes as Irreducible Concepts

### 11.1 The Type Interpretation

In the framework of Section 10, prime numbers are the *irreducible concepts* of the multiplicative universe — the types that cannot be decomposed into simpler types. Composite numbers are compound concepts: $6 = 2 \times 3$ is a compound type built from two prime types, just as "fruit salad" might be a compound concept built from "apple" and "banana."

The Fundamental Theorem of Arithmetic is then the statement that *every compound type decomposes uniquely into irreducible types*. This is the number-theoretic analog of conceptual irreducibility.

The information spectrum $\sigma(n) = (v_2 \ln 2, v_3 \ln 3, v_5 \ln 5, \ldots)$ of [3] is the *decomposition of $n$'s total information content into contributions from each irreducible conceptual dimension*. Each component $\sigma_p(n)$ measures how much of $n$'s structure comes from the prime type $p$.

### 11.2 Connection to Embedding Spaces

The prime coordinate space has a structural parallel to the embedding spaces used in machine learning:

| Embedding space (ML) | Prime coordinate space |
|----------------------|----------------------|
| Discrete tokens | Discrete states $\{0, \ldots, q-1\}$ |
| Embedding dimension | Number of prime axes |
| Embedding vector | Information spectrum $\sigma(n)$ |
| Continuous hidden state | Fuzzy wave amplitude (Section 12) |
| Irreducible features | Prime dimensions |
| Softmax $\to$ token | Phase classification $\to$ state |

In both cases, discrete symbols are embedded in a continuous space where "meaning" (or structural content) is encoded by position. The irreducible directions of the space — the prime axes in number theory, the learned feature directions in ML — are the atomic concepts from which all others are built.

### 11.3 The Euler Product as a Quantity–Type Bridge

The Euler product formula

$$\sum_{n=1}^{\infty} n^{-s} = \prod_{p \text{ prime}} \frac{1}{1 - p^{-s}}$$

equates a sum over all quantities (left side, additive universe) with a product over all types (right side, multiplicative universe). It is the generating function that converts between quantity-space and type-space, and $\zeta(2) = \pi^2/6$ is the conversion constant at the scale where geometric structure is measured.

---

## 12. The Three-Step Bridge Between Additive and Multiplicative Gaps

### 12.1 Why the Bridge Is Not a Ratio

Numerical investigation shows that the ratio $Z_{G,\mathrm{add}}(s) / Z_G(s)$ is not constant — it varies from approximately 5.25 at $s = 1.5$ to 1.07 at $s = 6$, converging toward 1 as $s \to \infty$. The bridge between additive and multiplicative gaps cannot be expressed as a simple algebraic relationship $Z_{G,\mathrm{add}} = f(Z_G)$.

The reason is structural: the bridge involves *counting operations* — algorithms that transform between the two domains — rather than algebraic identities. Three such operations have been identified, each corresponding to a classical mathematical transformation.

### 12.2 The Sieve (Discrete Counting)

The partition generating function factors as:

$$\prod_{k=1}^{\infty} \frac{1}{1-x^k} = \prod_{p \text{ prime}} \frac{1}{1-x^p} \cdot \prod_{\substack{k \geq 1 \\ k \text{ composite}}} \frac{1}{1-x^k}.$$

The Sieve of Eratosthenes removes composite factors from the full product to isolate the Euler product. In geometric gap terms: $\log P_{\mathrm{all}} = \log P_{\mathrm{prime}} + \log P_{\mathrm{composite}}$, decomposing the total additive ambiguity into a prime contribution (which has multiplicative meaning) and a composite contribution (which does not).

Numerical evaluation shows that as $x \to 1^-$, the prime fraction $\log P_{\mathrm{prime}} / \log P_{\mathrm{all}} \to 0$: the primes become a vanishing fraction of the total additive structure. For large $n$, most of the additive geometry has *no multiplicative counterpart*. The composite excess is the information that the FTA compresses away.

### 12.3 The Modular Transformation (Symmetric Exchange)

The Dedekind eta function $\eta(\tau) = e^{\pi i \tau / 12} \prod_{n=1}^{\infty}(1 - e^{2\pi i n \tau})$ satisfies the modular S-transformation:

$$\eta(-1/\tau) = \sqrt{-i\tau} \cdot \eta(\tau).$$

Setting $\tau = it$ with $t > 0$, this becomes $\eta(i/t) = \sqrt{t} \cdot \eta(it)$, which maps the additive regime ($t < 1$, where the partition function dominates) to the multiplicative regime ($t > 1$, where the Euler product converges rapidly), with the modular boundary $t = 1$ as the fixed point.

The $\sqrt{t}$ factor is the *exchange rate* between the two regimes. It is not a constant — it depends on the position relative to the boundary — which is why $Z_{G,\mathrm{add}} / Z_G$ is not constant. The modular transformation exchanges additive and multiplicative structure, and $\zeta(2) = \pi^2/6$ enters through the leading asymptotic of the partition function at the saddle point of this transformation.

### 12.4 The Mellin Transform (Continuous Counting)

The Mellin transform $\mathcal{M}[f](s) = \int_0^{\infty} f(x) \, x^{s-1} \, dx$ converts power series (additive world) to Dirichlet series (multiplicative world). For the partition generating function with $x = e^{-t}$:

$$\int_0^{\infty} \left[\sum_{n=0}^{\infty} p(n) e^{-nt}\right] t^{s-1} \, dt = \Gamma(s) \cdot \sum_{n=1}^{\infty} p(n) \cdot n^{-s}.$$

The Mellin transform is the formal bridge between the power series $\sum p(n) x^n$ (which encodes additive structure) and the Dirichlet series $\sum p(n) n^{-s}$ (which lives alongside $Z_G(s)$ in the multiplicative world). The critical line of the Mellin transform — where the integral transitions from convergent to divergent — is the asymptote separating the two regimes.

### 12.5 The Bridge as a Counting Algorithm

Together, the three transformations form a bridge:

$$Z_{G,\mathrm{add}}(s) \xleftarrow{\text{Mellin}} \log(\text{partition GF}) \xrightarrow{\text{Modular}} \text{Euler product} \xrightarrow{\text{Sieve}} Z_G(s) = \zeta(s) \cdot \sum_p C_p(s).$$

Each arrow is a *counting operation*: the Mellin transform integrates (counts continuously) over scales, the modular transformation exchanges (counts inversely) between regimes, and the sieve removes (counts by elimination) composite contributions. The bridge between additive and multiplicative geometric information is not an equation — it is a *computation*.

This observation connects to the wave architecture of [2]–[5]: the Euler product formula, which our wave computer physically implements via Dirichlet character interference, is the generating function for the bridge computation. The wave computer does not merely use the Euler product as a mathematical convenience — it physically performs the counting algorithm that converts between the additive and multiplicative information universes.

---

## 13. The Circuit Counting Function

### 13.1 Definition and Closed Form

**Definition 13.1 (Multiplication Tree Count).** For a positive integer $n$, the *multiplication tree count* $t(n)$ is the number of distinct ordered binary trees whose leaves are primes and whose product of leaves equals $n$. Each tree represents a distinct circuit topology for assembling $n$ from its prime components.

**Theorem 13.2 (Closed Form for $t(n)$).** For $n = p_1^{a_1} \cdots p_k^{a_k}$ with $\Omega(n) = \sum a_i \geq 2$:

$$t(n) = C(\Omega(n) - 1) \cdot \frac{\Omega(n)!}{a_1! \cdot a_2! \cdots a_k!}$$

where $C(m) = \binom{2m}{m}/(m+1)$ is the $m$-th Catalan number. For primes, $t(p) = 1$.

*Proof.* A binary tree with $\Omega$ leaves has $\Omega - 1$ internal nodes. The number of distinct full binary tree topologies with $\Omega$ labelled positions is $C(\Omega - 1)$, the $(\Omega-1)$-th Catalan number. Given a fixed topology, the $\Omega$ leaf positions must be filled with the prime factors of $n$: $a_1$ copies of $p_1$, $a_2$ copies of $p_2$, etc. The number of distinct assignments is the multinomial coefficient $\Omega! / \prod a_i!$. Since the topology and labelling are independent, the total is their product. $\square$

Verified computationally for all $n \leq 360$ by comparison with direct recursive enumeration.

**Interpretation.** The closed form factors cleanly into two components:

- $C(\Omega - 1)$: the number of circuit **topologies** (tree shapes). This is pure combinatorial structure — it depends only on how many components exist, not on what they are.
- $\Omega! / \prod a_i!$: the number of **labellings** (prime assignments). This is the multinomial coefficient counting distinguishable arrangements of typed components within a fixed topology.

The circuit count is thus **Shape × Content**: how many ways to wire the circuit, times how many ways to populate it with specific primes.

### 13.2 Asymptotics

Using the Catalan asymptotic $C(m) \sim 4^m / (m^{3/2}\sqrt{\pi})$:

$$\ln t(n) \approx (\Omega(n) - 1) \ln 4 + \ln\!\left(\frac{\Omega(n)!}{\prod a_i!}\right) - \frac{3}{2}\ln(\Omega(n) - 1) + O(1).$$

The growth rate depends critically on $\Omega(n)$:

- **Typical integers** (Erdős–Kac [10]): $\Omega(n) \sim \ln \ln n$, so $\ln t(n) \sim (\ln \ln n) \cdot \ln 4$. This barely grows — circuit complexity is negligible for typical numbers.
- **Prime powers** $n = p^k$: $\Omega = k = \ln n / \ln p$, multinomial $= 1$, so $\ln t(n) \sim 2 \ln n$. Circuit complexity is polynomial ($t(n) \sim n^2$).
- **Highly composite numbers**: $\Omega \sim \ln n / \ln \ln n$, giving sub-exponential growth.

In all cases, $\ln t(n)$ grows **at most polynomially** in $\ln n$, while $\ln p(n) \sim 2\sqrt{n \cdot \zeta(2)}$ grows **exponentially** in $\sqrt{n}$. The concept side is always less degenerate than the quantity side.

### 13.3 Non-Multiplicativity

The function $t(n)$ is **not** multiplicative: $t(6) = 2$ but $t(2) \cdot t(3) = 1$. For coprime $a, b$ with $\Omega(a) + \Omega(b) = \Omega(ab)$:

$$t(ab) = C(\Omega(ab) - 1) \cdot \frac{\Omega(ab)!}{\prod a_i!} \neq C(\Omega(a)-1) \cdot C(\Omega(b)-1) \cdot \frac{\Omega(a)!}{\prod a_i^{(a)}!} \cdot \frac{\Omega(b)!}{\prod a_i^{(b)}!}$$

because $C(\Omega(a) + \Omega(b) - 1) \neq C(\Omega(a) - 1) \cdot C(\Omega(b) - 1)$ — Catalan numbers do not factorise under addition of arguments. Physically, this means circuit topologies for coprime parts *interleave*: combining two independent sub-circuits creates new tree shapes that don't exist in either sub-circuit alone.

Consequently, the Dirichlet series $D_t(s) = \sum t(n) n^{-s}$ has **no Euler product**. Circuit complexity is inherently non-separable across prime dimensions.

### 13.4 The Circuit Gap Generating Function

**Definition 13.3.** The *circuit gap generating function* is:

$$Z_t(s) = \sum_{n=1}^{\infty} \ln t(n) \cdot n^{-s}, \qquad \mathrm{Re}(s) > 1.$$

Since $t(n)$ is not multiplicative and $\ln t(n)$ is not additive for coprime arguments, $Z_t(s)$ does not admit an Euler product decomposition. This is in contrast to $Z_G(s) = \zeta(s) \cdot \sum_p C_p(s)$ (Theorem 5.2), which does decompose via the multiplicativity of $d(n)$.

The absence of an Euler product for $Z_t$ is itself significant: it means the concept-side gap cannot be understood prime-by-prime but only in terms of the full prime factor structure simultaneously.

---

## 14. The Squarefree Bridge

### 14.1 The Squarefree Restriction

The resistance isomorphism of [1] operates naturally on squarefree integers — those for which $\mu(n) \neq 0$ — where each prime appears at most once. In this domain, primes function as irreducible qualitative types: one either has the concept (prime $p$ divides $n$) or does not ($p \nmid n$). Allowing repeated prime factors (e.g., $2^3$ in $n = 24$) reintroduces quantity into the concept side, conflating "how many times" with "which type."

This distinction is not merely aesthetic. When the analysis of Sections 13.2–13.4 is performed over all integers, the relationship $\langle \ln n \rangle_{\Omega}$ versus $\Omega$ is sublinear — each additional prime factor appears to cost *less* resistance. This is an artifact: repeated factors of prime 2 (the cheapest prime) dominate the high-$\Omega$ integers under Dirichlet weighting, making complexity appear cheap. Restricting to squarefree integers eliminates this contamination and reveals the true structure.

### 14.2 The Squarefree Circuit Count

For squarefree $n$ with $\omega(n) = \omega$ distinct prime factors and all exponents equal to 1, the closed form of Theorem 13.2 simplifies:

$$t(n) = C(\omega - 1) \cdot \omega!$$

The multinomial coefficient becomes $\omega!/1!^{\omega} = \omega!$ (its maximum value), and the circuit gap $\ln t(n) = \ln C(\omega-1) + \ln(\omega!)$ depends *only on $\omega$*, not on which specific primes appear. This is a decisive simplification: **the concept-side gap is exact and requires no averaging**.

### 14.3 The Bridge Function: Chebyshev's Theta

For squarefree $n = p_1 p_2 \cdots p_{\omega}$ with distinct primes:

$$\ln(n) = \ln(p_1) + \ln(p_2) + \cdots + \ln(p_{\omega}) = \sum_{i=1}^{\omega} \ln(p_i).$$

The smallest squarefree integer with $\omega$ distinct primes is the $\omega$-th primorial $P_{\omega} = 2 \cdot 3 \cdot 5 \cdots p_{\omega}$, whose logarithm is Chebyshev's theta function:

$$\ln(P_{\omega}) = \sum_{k=1}^{\omega} \ln(p_k) = \theta(p_{\omega}).$$

By the Prime Number Theorem, $\theta(x) \sim x$ as $x \to \infty$, and $p_{\omega} \sim \omega \ln(\omega)$ for the $\omega$-th prime. Therefore:

$$\ln(P_{\omega}) \sim p_{\omega} \sim \omega \ln(\omega).$$

The bridge function grows **superlinearly** in $\omega$: each additional prime concept costs more resistance than the last, because larger (rarer) primes carry more information. This is the opposite of the sublinear behaviour observed for all integers, and it reflects the true informational cost of conceptual complexity.

### 14.4 The Marginal Cost of Each Concept

The marginal cost of adding the $\omega$-th prime concept is:

$$\Delta(\omega) = \langle \ln n \rangle_{\omega} - \langle \ln n \rangle_{\omega-1} \approx \ln(p_{\omega}).$$

Numerical verification at $s = 2$ shows the ratio $\Delta(\omega) / \ln(p_{\omega})$ converging toward 1:

| $\omega$ | $\Delta(\omega)$ | $\ln(p_{\omega})$ | Ratio |
|----------|-----------------|-------------------|-------|
| 2 | 1.453 | 1.099 | 1.32 |
| 3 | 1.882 | 1.609 | 1.17 |
| 4 | 2.077 | 1.946 | 1.07 |

The convergence toward 1 confirms the resistance isomorphism prediction: the cost of the $\omega$-th concept is its resistance $\ln(p_{\omega})$. The residual excess above 1 reflects the Dirichlet weighting's preference for integers slightly above the primorial, and it diminishes as $\omega$ grows and the distribution concentrates.

### 14.5 The Squarefree Exchange Rate

The exchange rate for squarefree integers is:

$$\rho(\omega) = \frac{\langle \ln p(n) \rangle_{\omega}}{\ln C(\omega-1) + \ln(\omega!)}$$

where the denominator is **exact** (no averaging required) and the numerator involves the partition function evaluated at integers near the $\omega$-th primorial. Since $p(n) \sim \exp(\pi\sqrt{2n/3})$ and $n \sim P_{\omega} \sim e^{\omega \ln \omega}$, the numerator grows much faster than the Catalan-dominated denominator, and $\rho(\omega)$ increases with $\omega$.

### 14.6 The Per-$\omega$ Bridge Equation

The bridge equation for squarefree integers takes the form:

$$Z_p^{(\mathrm{sqf})}(s) = \sum_{\omega=2}^{\infty} \rho(\omega) \cdot Z_t^{(\omega, \mathrm{sqf})}(s)$$

where $Z_t^{(\omega, \mathrm{sqf})}(s) = [\ln C(\omega-1) + \ln(\omega!)] \cdot \zeta_{\omega}^{(\mathrm{sqf})}(s)$ and $\zeta_{\omega}^{(\mathrm{sqf})}(s) = \sum_{\substack{n \text{ sqfree} \\ \omega(n) = \omega}} n^{-s}$.

The squarefree-restricted $\omega$-zeta function $\zeta_{\omega}^{(\mathrm{sqf})}$ has a known Euler product structure:

$$\sum_{\omega=0}^{\infty} z^{\omega} \zeta_{\omega}^{(\mathrm{sqf})}(s) = \prod_{p} (1 + z \cdot p^{-s})$$

which is the squarefree analog of $F(z,s) = \prod_p (1 - z p^{-s})^{-1}$. At $z = 1$, this gives $\prod_p (1 + p^{-s}) = \zeta(s)/\zeta(2s)$, confirming the classical density of squarefree integers.

---

## 15. The Three Informations

### 15.1 Decomposition

The analysis of Sections 13–14 reveals that the bridge between quantity and concept involves three distinct types of information:

1. **Quantity information** $R(n) = \ln(n)$: the total resistance, measuring "how many objects." This lives on the geometry side and determines the geometric gap $G_{\mathrm{geom}} = \ln p(n)$.

2. **Complexity information** $\omega(n)$: the number of distinct prime factors, measuring "how many irreducible concepts." This lives on the circuit side and determines the circuit gap $G_{\mathrm{circ}} = \ln t(n) = \ln C(\omega-1) + \ln(\omega!)$ for squarefree $n$.

3. **Concentration information**: *which* primes appear. For squarefree $n = p_1 \cdots p_{\omega}$, this is the specific set $\{p_1, \ldots, p_{\omega}\}$. It lives on neither the quantity side nor the concept side — it *is* the bridge. It determines $n$ given $\omega$, and therefore determines how the geometric and circuit gaps relate.

### 15.2 Why the Logarithm Is the Bridge

The resistance isomorphism $R(n) = \ln(n)$ is the unique continuous function (Cauchy's theorem, [1]) satisfying $R(ab) = R(a) + R(b)$. The three-information decomposition reveals *why* this is the bridge:

For squarefree $n = p_1 \cdots p_{\omega}$:

$$R(n) = \ln(p_1) + \ln(p_2) + \cdots + \ln(p_{\omega})$$

Each prime contributes its own resistance $\ln(p_i)$ independently. The total is the sum. The bridge is *not* a single parameter $\alpha$ but a *sequence*: the $i$-th prime's resistance $\ln(p_i)$ is the marginal cost of the $i$-th concept. The logarithm is the bridge because it converts multiplicative independence (distinct primes appearing as factors) into additive independence (separate resistances summing).

The increasing marginal cost — $\ln(2) < \ln(3) < \ln(5) < \cdots$ — is a feature: rarer concepts (larger primes) carry more information and therefore cost more resistance to specify.

### 15.3 The Concentration Information as the Bridge Carrier

The concentration information — the identity of which primes appear — carries approximately $\sum_{i=1}^{\omega} \ln(p_i) - \omega \cdot \overline{\ln p}$ nats of "bridge information" beyond what $\omega$ alone specifies, where $\overline{\ln p}$ is the average prime log at level $\omega$.

This information is discarded by the Selberg-Delange leading term (which treats all integers with the same $\omega$ as equivalent) and encoded in the correction factor $G(z, s)$. It is the information that connects a specific point on the quantity side (a particular $n$ with its specific geometric arrangements) to the corresponding point on the concept side (a specific circuit topology count determined by $\omega$).

In the wave architecture of [2]–[5], this bridge information corresponds to the *phase structure* of the Dirichlet characters: which primes are active determines which characters contribute to the wave interference, and therefore which computation is performed.

---

## 16. Summary of Identities

| Identity | Meaning |
|----------|---------|
| $G(n, \oplus) = \ln \|\text{preimages}\|$ | Geometric information gap (Definition 3.1) |
| $G_{\mathrm{add}}(n) \approx 2\sqrt{n \cdot \zeta(2)}$ | Additive gap governed by $\zeta(2)$ (Corollary 6.1) |
| $Z_G(s) = \zeta(s) \cdot \sum_p \sum_a \ln(1+1/a) \, p^{-as}$ | Multiplicative gap decomposition (Theorem 5.2) |
| $t(n) = C(\Omega-1) \cdot \Omega!/\prod a_i!$ | Circuit counting closed form (Theorem 13.2) |
| $t(n) = C(\omega-1) \cdot \omega!$ for squarefree $n$ | Squarefree specialisation (Section 14.2) |
| $\ln(P_{\omega}) = \theta(p_{\omega}) \sim \omega \ln \omega$ | Bridge function via Chebyshev (Section 14.3) |
| $\Delta(\omega) \to \ln(p_{\omega})$ | Marginal concept cost $\to$ prime resistance (Section 14.4) |
| $\Delta_a = \ln(1 + 1/a)$ | Incremental geometric ambiguity at exponent $a$ |
| $G_{\mathrm{loc}} \approx R(n)/2$ | Universal search cost = half the informational resistance |
| $\zeta(2) = \pi^2/6$ | The geometric information constant |

---

## References

[1] A. Pisani, "A unified algebraic framework for number theory, Boolean logic, and circuit topology via the logarithmic isomorphism," 2026.

[2] A. Pisani, "The Natural Operating System: Boolean computation via Möbius inversion and prime-encoded databases," 2026.

[3] A. Pisani, "Structured self-information: A prime coordinate decomposition of Shannon's information measure," 2026.

[4] A. Pisani and Claude (Anthropic), "Multi-state wave computation via Dirichlet characters: A generalisation of the Möbius interference architecture," 2026.

[5] A. Pisani, "Spectral-temporal wave encoding: A multi-wavelength architecture for linearly scalable wave computation," 2026.

[*] A. Pisani, "The geometry of knowing: From dots to dimensions," working notes, 2026.

[6] C. E. Shannon, "A mathematical theory of communication," *Bell System Technical Journal*, vol. 27, no. 3, pp. 379–423, 1948.

[7] G. H. Hardy and S. Ramanujan, "Asymptotic formulae in combinatory analysis," *Proceedings of the London Mathematical Society*, ser. 2, vol. 17, pp. 75–115, 1918.

[8] G. H. Hardy and E. M. Wright, *An Introduction to the Theory of Numbers*, 5th ed. Oxford University Press, 1979.

[9] E. Bach, "Discrete logarithms and factoring," Computer Science Division, UC Berkeley, Technical Report, 1984.

[10] P. Erdős and M. Kac, "The Gaussian law of errors in the theory of additive number theoretic functions," *American Journal of Mathematics*, vol. 62, no. 1/4, pp. 738–742, 1940.

---

## Appendix A: Computational Results

### A.1 G(n) Across the Hierarchy

Selected values of the geometric information gap (in nats):

| $n$ | $G_{\mathrm{add}}$ | $G_{\mathrm{mult}}$ | $G_{\mathrm{exp}}$ | Factorisation |
|-----|--------------------|--------------------|--------------------|--------------------|
| 6 | 2.398 | 1.099 | 0 | $2 \times 3$ |
| 12 | 4.344 | 2.079 | 0 | $2^2 \times 3$ |
| 30 | 8.631 | 2.565 | 0 | $2 \times 3 \times 5$ |
| 60 | 13.780 | 3.784 | 0 | $2^2 \times 3 \times 5$ |
| 64 | 14.369 | 3.466 | 1.386 | $2^6$ |
| 120 | 21.322 | 4.883 | 0 | $2^3 \times 3 \times 5$ |
| 360 | 40.810 | 6.403 | 0 | $2^3 \times 3^2 \times 5$ |

### A.2 Incremental Geometric Information

The first ten values of $\Delta_a = \ln(1 + 1/a)$:

| $a$ | $\Delta_a$ (nats) | Cumulative | $1/a$ (approximation) |
|-----|-------------------|------------|----------------------|
| 1 | 0.6931 | 0.6931 | 1.0000 |
| 2 | 0.4055 | 1.0986 | 0.5000 |
| 3 | 0.2877 | 1.3863 | 0.3333 |
| 4 | 0.2231 | 1.6094 | 0.2500 |
| 5 | 0.1823 | 1.7918 | 0.2000 |
| 6 | 0.1542 | 1.9459 | 0.1667 |
| 7 | 0.1335 | 2.0794 | 0.1429 |
| 8 | 0.1178 | 2.1972 | 0.1250 |
| 9 | 0.1054 | 2.3026 | 0.1111 |
| 10 | 0.0953 | 2.3979 | 0.1000 |

Cumulative at $a = A$ equals $\ln(A+1)$ exactly (telescoping).

### A.3 Per-Prime Contributions to Z_G(2)

$Z_G(2) \approx 0.5767$. The decomposition is $Z_G(2) = \zeta(2) \cdot \sum_p C_p(2)$, with $\zeta(2) = 1.6449$ and $\sum_p C_p(2) \approx 0.3506$.

| Prime $p$ | $C_p(2)$ | Cumulative % |
|-----------|----------|-------------|
| 2 | 0.20422 | 58.3% |
| 3 | 0.08245 | 81.9% |
| 5 | 0.02839 | 90.0% |
| 7 | 0.01432 | 94.1% |
| 11 | 0.00576 | 95.7% |
| 13 | 0.00412 | 96.9% |
| All $p \leq 113$ | — | 99.9% |
