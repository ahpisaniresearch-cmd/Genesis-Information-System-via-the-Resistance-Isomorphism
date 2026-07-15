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

# Multi-State Wave Computation via Dirichlet Characters: A Generalisation of the Möbius Interference Architecture

**Alexander Pisani & Claude (Anthropic)**

a.h.pisani.research@gmail.com

April 2026

---

## Abstract

We generalise the Möbius wave computer architecture of [1] from binary to arbitrary $q$-state computation by replacing the Möbius function $\mu(n) \in \{-1, 0, +1\}$ with Dirichlet characters $\chi(n)$ of order $q$, whose values are $q$-th roots of unity. In the binary case, the Möbius function assigns two phases (0° and 180°) to signal paths, and Boolean logic emerges from two-phase wave interference. In the generalised case, a Dirichlet character of order $q$ assigns $q$ uniformly spaced phases ($2\pi k/q$ for $k = 0, \ldots, q-1$), and $q$-state logic emerges from multi-phase interference.

We prove **multi-state functional completeness**: for any number of states $q$ and any number of inputs $k$, every function $f: \{0, \ldots, q-1\}^k \to \{0, \ldots, q-1\}$ can be implemented as a character-weighted wave superposition. The proof uses the Fourier inversion theorem on finite abelian groups. We verify the theory computationally: all 27 single-input ternary functions (characters mod 7), all 256 single-input quaternary functions (characters mod 5), and large samples of multi-input gates all produce correct outputs.

We establish a **polynomial cascade theorem**: the output of one gate can feed into the next via polynomial evaluation in the complex amplitude, without intermediate phase detection or digital re-encoding. The polynomial degree required is $q - 1$. For binary ($q = 2$), this is degree 1 — cascading is **purely linear** and requires no nonlinear elements. For ternary ($q = 3$), cascading requires a single quadratic nonlinearity (second-harmonic generation in optics). This result resolves the cascading problem — previously identified as the critical engineering bottleneck — for the binary case entirely, and reduces it to well-studied nonlinear optics for the multi-state case.

We discuss the physical implementation hierarchy: water waves support binary computation only (real-valued amplitude admits two phases), while electromagnetic waves natively support arbitrary $q$-state computation via complex amplitude. The generalised Euler product $L(s, \chi)$ is a native program in the multi-state architecture, connecting the computational framework to analytic number theory.

**Keywords:** Dirichlet characters, multi-valued logic, wave interference, Möbius function, functional completeness, $L$-functions, polynomial cascade, multi-phase computation

**MSC (2020):** 11A25, 03B50, 68Q05, 11M06, 42A38

---

## 1. Introduction

In [1], we presented a computational architecture — the "Natural Operating System" — in which Boolean logic emerges from the multiplicative structure of the integers. The architecture is governed by the master equation

$$y(S) = \sum_{n \in D} \mu(n) \cdot O_n \cdot [n \mid S] \cdot P_n(S)$$

where $\mu(n)$ is the Möbius function, $O_n$ is a database output, $[n \mid S]$ is a divisibility-based activation indicator, and $P_n(S)$ tests a condition. We proved that the four standard Boolean gates (NOT, AND, OR, NAND) are implementable within this framework, establishing functional completeness for binary logic.

The Möbius signs $\mu(n) \in \{-1, +1\}$ (for squarefree $n$) implement the inclusion-exclusion principle: the OR gate uses three terms with coefficients $+1, +1, -1$, and the NOT gate operates by destructive interference between a constant reference and a phase-shifted input. These signs map directly to wave phases: $\mu(n) = +1$ corresponds to phase 0° (in-phase) and $\mu(n) = -1$ to phase 180° (anti-phase).

Water waves — real-valued displacements — support exactly two phases. But electromagnetic waves carry complex amplitude with continuous phase. This paper shows that by replacing $\mu(n)$ with Dirichlet characters $\chi(n)$ of arbitrary order $q$, the architecture generalises from binary to $q$-state computation. The mathematical foundation is Fourier analysis on finite abelian groups; the physical foundation is multi-phase wave interference.

### 1.1 Summary of Results

1. **Generalised master equation** (Section 3): The output is $y(x) = \sum_j \hat{F}_j \cdot \chi_j(x \bmod m)$, a weighted sum over Dirichlet characters.

2. **Multi-state functional completeness** (Section 5): Every function $\{0,\ldots,q-1\}^k \to \{0,\ldots,q-1\}$ is implementable.

3. **Polynomial cascade theorem** (Section 6): Gates cascade via degree-$(q-1)$ polynomial evaluation in the complex output, without intermediate detection. Binary cascading is linear.

4. **Computational verification** (Section 7): Exhaustive tests for $q = 2, 3, 4$ and large samples for $q = 5$.

5. **Physical hierarchy** (Section 8): Water → binary; EM → arbitrary $q$.

6. **Noise margin analysis** (Section 9): Quantitative bounds on tolerable per-source error.

7. **Generalised Euler product** (Section 10): $L(s, \chi)$ is a native program.

### 1.2 Relation to Prior Work

This paper extends [1] (the binary Möbius architecture) and draws on [2] (the logarithmic isomorphism) and [3] (the information spectrum). Multi-valued logic originates with Post [4] and Łukasiewicz [5]; ternary computing was explored by Brusentsov [6]. Wave-based computation is an active area in photonic computing [7, 8]. The connection between Dirichlet characters and multi-phase wave computation appears to be new.

### 1.3 Relation to Paper 2's Architecture

Papers [1] and the present work use compatible but structurally distinct architectures. Paper [1] uses **amplitude modulation**: fixed-phase sources with variable gates (physical barriers that open or close wave paths based on divisibility). The present paper uses **phase modulation**: variable-phase sources with no gates, where each source's phase is set by the character value $\chi_j(x)$ at the input. Both are physically realisable; the phase modulation approach is standard in phased array technology and telecommunications. For binary, either approach works. For multi-state, only the phase modulation (character-based) approach applies.

Paper [1]'s processor function $P_n(S)$ — a secondary condition test on the input — is absorbed into the character framework: the Fourier coefficients $\hat{F}_j$ already encode the complete logic function, including any conditional behaviour. The character evaluation $\chi_j(x)$ provides all routing information without a separate condition gate.

---

## 2. Mathematical Preliminaries

### 2.1 Dirichlet Characters

**Definition 2.1.** Let $q \geq 1$ be a positive integer. A *Dirichlet character* modulo $q$ is a function $\chi : \mathbb{Z} \to \mathbb{C}$ satisfying: (1) $\chi(n) = 0$ if $\gcd(n, q) > 1$; (2) $\chi(n + q) = \chi(n)$ for all $n$; (3) $\chi(mn) = \chi(m)\chi(n)$ for all $m, n$.

The characters mod $q$ form a group of order $\varphi(q)$ under pointwise multiplication. When $q$ is prime, this group is cyclic. A character of order $d$ takes values that are $d$-th roots of unity.

### 2.2 Character Orthogonality

**Theorem 2.2.** For $a, b \in (\mathbb{Z}/q\mathbb{Z})^*$:

$$\sum_{\chi \bmod q} \chi(a) \overline{\chi(b)} = \begin{cases} \varphi(q) & \text{if } a \equiv b \pmod{q}, \\ 0 & \text{otherwise.} \end{cases}$$

### 2.3 Fourier Inversion

**Theorem 2.3.** Any function $f: (\mathbb{Z}/q\mathbb{Z})^* \to \mathbb{C}$ has a unique decomposition

$$f(a) = \sum_{\chi \bmod q} \hat{f}(\chi) \cdot \chi(a), \qquad \hat{f}(\chi) = \frac{1}{\varphi(q)} \sum_{a \in (\mathbb{Z}/q\mathbb{Z})^*} f(a) \cdot \overline{\chi(a)}.$$

### 2.4 Recovery of the Möbius Function

The Möbius function $\mu(n)$ is not a Dirichlet character: it is not completely multiplicative ($\mu(p^2) = 0$ while $\chi(p^2) = \chi(p)^2$ for any character $\chi$), and it is not periodic. The Liouville function $\lambda(n) = (-1)^{\Omega(n)}$ is completely multiplicative but also not periodic; hence it too is not a Dirichlet character.

On the domain relevant to [1] — squarefree integers — $\mu(n) = \lambda(n) = (-1)^{\omega(n)}$, and both agree with the non-trivial real character of order 2 for each prime factor individually. Paper [1]'s binary architecture works because it restricts to squarefree addresses where this agreement holds. The present paper's character-based formulation is the cleaner generalisation; the Möbius-based formulation of [1] is the historically motivated special case.

### 2.5 Dirichlet $L$-Functions

For a character $\chi$ mod $q$ and $\mathrm{Re}(s) > 1$:

$$L(s, \chi) = \sum_{n=1}^{\infty} \frac{\chi(n)}{n^s} = \prod_{p \text{ prime}} \frac{1}{1 - \chi(p) p^{-s}}.$$

---

## 3. The Generalised Master Equation

### 3.1 Definition

**Definition 3.1.** For a prime modulus $m$, with Dirichlet characters $\chi_0, \ldots, \chi_{\varphi(m)-1}$ mod $m$, and complex coefficients $\hat{F}_0, \ldots, \hat{F}_{\varphi(m)-1}$ (the *database*), the **generalised master equation** computes:

$$y(x) = \sum_{j=0}^{\varphi(m)-1} \hat{F}_j \cdot \chi_j(x \bmod m)$$

where $x$ is the encoded input.

Each term is a **wave source**: source $j$ emits with complex amplitude $\hat{F}_j \cdot \chi_j(x \bmod m)$. The detector measures the total complex amplitude $y(x)$. The output state is:

$$\text{output} = \operatorname{argmin}_{k \in \{0, \ldots, q-1\}} \left| \arg(y(x)) - \frac{2\pi k}{q} \right|.$$

### 3.2 Physical Interpretation

Each wave source $j$ has a fixed complex amplitude $\hat{F}_j$ (programmed from the Fourier coefficients of the target function) and a variable phase determined by $\chi_j(x \bmod m)$ (set by the input). The superposition at the detector is the Fourier synthesis. The output state is read from the phase sector of the total amplitude.

---

## 4. Input Encoding

### 4.1 Single-Input Encoding

A $q$-state input $A \in \{0, \ldots, q-1\}$ is encoded as $A \mapsto g^A \bmod m$, where $g$ is a generator of $(\mathbb{Z}/m\mathbb{Z})^*$ and $m$ is chosen with $\varphi(m) \geq q$. The $q$ residues $g^0, \ldots, g^{q-1}$ are distinct.

**Example 4.1 (Ternary).** $q = 3$, $m = 7$, generator $g = 3$: $A = 0 \mapsto 1$, $A = 1 \mapsto 3$, $A = 2 \mapsto 2$. The order-3 character $\chi_2$ mod 7 maps these to distinct cube roots of unity, naturally distinguishing the three states.

### 4.2 Multi-Input Encoding

For $k$ inputs, encode $(A_1, \ldots, A_k) \mapsto \prod_{i=1}^k p_i^{A_i} \bmod m$ where $p_1, \ldots, p_k$ are distinct primes.

**Theorem 4.2 (Encoding existence).** For any $q, k \geq 1$, there exists a prime $m$ such that the $q^k$ products $\prod_{i=1}^k p_i^{A_i}$ are distinct modulo $m$.

*Proof.* The products are distinct positive integers by the Fundamental Theorem of Arithmetic. Let $M = \prod_{i=1}^k p_i^{q-1}$ be the largest such product. Any prime $m > M$ makes all products distinct mod $m$ (since they are positive integers less than $m$). By Bertrand's postulate, such a prime exists in $(M, 2M]$. $\square$

**Remark 4.3 (Scaling).** Using the first $k$ primes, $M = \prod_{i=1}^k p_i^{q-1}$, so $m$ (and hence $\varphi(m)$, the number of wave sources) grows exponentially in both $q$ and $k$. This is worse than binary, where each input adds one prime with linear growth. The exponential scaling of multi-input encodings is the principal practical limitation of the framework.

---

## 5. Multi-State Functional Completeness

### 5.1 Statement and Proof

**Theorem 5.1.** For any $q \geq 2$ and $k \geq 1$, every function $f: \{0, \ldots, q-1\}^k \to \{0, \ldots, q-1\}$ is implementable by the generalised master equation.

*Proof.* (1) Choose primes $p_1, \ldots, p_k$ and a prime modulus $m$ as in Theorem 4.2 such that all $q^k$ encoded residues are distinct in $(\mathbb{Z}/m\mathbb{Z})^*$.

(2) Define $F: (\mathbb{Z}/m\mathbb{Z})^* \to \mathbb{C}$ by $F(r) = \omega_q^{f(A_1, \ldots, A_k)}$ when $r$ is the encoding of $(A_1, \ldots, A_k)$, and $F(r) = 0$ for non-encoding residues, where $\omega_q = e^{2\pi i/q}$.

(3) By Theorem 2.3, $F(a) = \sum_{j=0}^{\varphi(m)-1} \hat{F}_j \cdot \chi_j(a)$ with $\hat{F}_j = \frac{1}{\varphi(m)} \sum_{a} F(a) \cdot \overline{\chi_j(a)}$.

(4) Set the database coefficients to $\hat{F}_0, \ldots, \hat{F}_{\varphi(m)-1}$. The generalised master equation then computes $y(x) = \sum_j \hat{F}_j \cdot \chi_j(x \bmod m) = F(x \bmod m) = \omega_q^{f(\text{inputs})}$.

(5) Since $|y(x)| = 1$ and $\arg(y(x)) = 2\pi f(\text{inputs})/q$, the output state is exactly $f(\text{inputs})$. $\square$

---

## 6. The Polynomial Cascade Theorem

### 6.1 The Cascading Problem

A multi-gate computation requires feeding the output of one gate into the input of the next. Gate 1 produces a complex amplitude $z_1 = \omega_q^{k}$ encoding state $k$. Gate 2 expects an encoded residue $r \in (\mathbb{Z}/m\mathbb{Z})^*$. The naive approach — detect the phase of $z_1$, classify into state $k$, re-encode as $g^k \bmod m$, and re-emit — requires nonlinear detection and digital logic at each stage, which undermines the wave-based approach.

### 6.2 Polynomial Cascade

We show that this intermediate detection can be avoided entirely.

**Theorem 6.1 (Polynomial cascade).** Let gate 1 output $z_1 = \omega_q^k$ for input state $k$. The character value $\chi_j(g^k)$ needed by gate 2 is a polynomial of degree at most $q - 1$ in $z_1$:

$$\chi_j(g^k) = \sum_{p=0}^{q-1} c_{j,p} \cdot z_1^p$$

for unique coefficients $c_{j,p} \in \mathbb{C}$. Therefore gate 2's output can be computed as:

$$y_2 = \sum_j \hat{F}_{2,j} \cdot \left( \sum_{p=0}^{q-1} c_{j,p} \cdot z_1^p \right) = \sum_{p=0}^{q-1} \left( \sum_j \hat{F}_{2,j} \cdot c_{j,p} \right) z_1^p$$

which is a degree-$(q-1)$ polynomial in $z_1$.

*Proof.* The values $\chi_j(g^k)$ for $k = 0, \ldots, q-1$ are determined by $q$ constraints. The matrix $V_{kp} = (\omega_q^k)^p = \omega_q^{kp}$ for $k, p \in \{0, \ldots, q-1\}$ is the DFT matrix, which is invertible (its rows are distinct characters of $\mathbb{Z}/q\mathbb{Z}$, and characters of a finite group are linearly independent). Therefore there exist unique coefficients $c_{j,0}, \ldots, c_{j,q-1}$ satisfying $\chi_j(g^k) = \sum_p c_{j,p} \cdot \omega_q^{kp}$ for all $k$. Since $z_1 = \omega_q^k$, we have $z_1^p = \omega_q^{kp}$, giving $\chi_j(g^k) = \sum_p c_{j,p} \cdot z_1^p$. $\square$

### 6.3 Binary Cascading is Linear

**Corollary 6.2.** For $q = 2$, the cascade polynomial has degree 1. Gate 2's output is:

$$y_2 = c_0 + c_1 \cdot z_1$$

This is a **linear** function of gate 1's output: a fixed complex constant plus a scaled copy of the input wave. Physically, this is just one more wave interfering with the output — no nonlinear element is required.

**Corollary 6.3.** Binary wave computation cascades via pure linear wave operations: superposition and fixed-amplitude scaling. No nonlinear optical elements, no detection, and no digital logic are needed at any intermediate stage.

This result means that arbitrarily deep binary circuits can be implemented in a single interference network — a mesh of linear wave paths with fixed complex weights. This is precisely the architecture of coherent photonic neural networks [7].

### 6.4 Ternary Cascading Requires Second-Harmonic Generation

For $q = 3$, the cascade polynomial has degree 2:

$$y_2 = c_0 + c_1 \cdot z_1 + c_2 \cdot z_1^2$$

The $z_1^2$ term requires squaring the complex amplitude. In optics, this is **second-harmonic generation** (SHG) — a well-studied process in nonlinear crystals (KDP, BBO, LiNbO₃). In electronics, it is analog multiplication.

More generally, $q$-state cascading requires generation of $z_1^{q-1}$, i.e., $(q-1)$-th harmonic generation. The nonlinearity order grows linearly with the number of states — a controlled, finite cost per cascade step.

### 6.5 Computational Verification of Cascading

We verified the polynomial cascade for the composition NEGATE $\circ$ INCREMENT in ternary ($q = 3$):

| Input $A$ | Gate 1 output $z_1$ | Polynomial $y_2$ | Phase | Detected | Expected | |
|:---------:|:-------------------:|:-----------------:|:-----:|:--------:|:--------:|:-:|
| 0 | $-0.500 + 0.866i$ | $-0.500 - 0.866i$ | −120° | 2 | 2 | ✓ |
| 1 | $-0.500 - 0.866i$ | $-0.500 + 0.866i$ | +120° | 1 | 1 | ✓ |
| 2 | $1.000$ | $1.000$ | 0° | 0 | 0 | ✓ |

The polynomial cascade produces exact results with no intermediate detection.

---

## 7. Computational Verification

### 7.1 Summary of Tests

| Test | States ($q$) | Modulus ($m$) | Functions tested | Correct | Method |
|------|:-----------:|:------------:|:---------------:|:-------:|--------|
| Binary gates | 2 | 3 | 4 (NOT, AND, OR, NAND) | 4/4 | Exhaustive |
| Ternary 1-input | 3 | 7 | 27 (all) | 27/27 | Exhaustive |
| Ternary 2-input | 3 | 19 | 500 (sampled) | 500/500 | Random |
| Quaternary 1-input | 4 | 5 | 256 (all) | 256/256 | Exhaustive |
| Quinary 1-input | 5 | 11 | 500 (sampled) | 500/500 | Random |
| Ternary cascade | 3 | 7 | 1 (NEGATE ∘ INCREMENT) | 3/3 | Exhaustive |

### 7.2 Named Ternary Gates

| Gate | Definition | Wave sources used |
|------|-----------|:-----------------:|
| IDENTITY | $A \mapsto A$ | 2 of 6 |
| INCREMENT | $A \mapsto (A+1) \bmod 3$ | 2 of 6 |
| NEGATE | $A \mapsto (-A) \bmod 3$ | 2 of 6 |
| CONSTANT($k$) | $A \mapsto k$ | 2 of 6 |
| MIN$(A,B)$ | ternary AND | 18 of 18 |
| MAX$(A,B)$ | ternary OR | 18 of 18 |
| ADD$(A,B) \bmod 3$ | ternary addition | 16 of 18 |

---

## 8. Physical Implementation Hierarchy

### 8.1 The Phase Constraint

| Medium | Amplitude | Phases | Max $q$ | Cascade nonlinearity |
|--------|-----------|--------|:-------:|---------------------|
| Water | Real | $\{0, \pi\}$ | 2 | Linear (none needed) |
| Sound | Real | $\{0, \pi\}$ | 2 | Linear |
| Electronic (I/Q) | Complex | $[0, 2\pi)$ | Arbitrary | Analog polynomial |
| Optical (EM) | Complex | $[0, 2\pi)$ | Arbitrary | Harmonic generation |
| Quantum photonic | Complex | $[0, 2\pi)$ | Arbitrary | Gate-native |

Water waves are limited to binary because surface displacement is real-valued: a crest is "positive" and a trough is "negative," giving exactly two phases. Electromagnetic waves carry a complex electric field, supporting arbitrary phase. The ternary advantage (58.5% more information per measurement) and higher-$q$ advantages are accessible only with complex-valued media.

### 8.2 Architecture Comparison

Paper [1] (binary Möbius) uses **fixed-phase sources + variable gates**: each wave source has a fixed phase determined by $\mu(n)$, and physical barriers open or close paths based on divisibility. The input determines *which* sources contribute.

The present paper uses **variable-phase sources + no gates**: each source's phase is set to $\chi_j(x \bmod m)$ at the input. There are no barriers. The input determines *what phase* each source emits at.

Both are physically standard. Paper [1]'s approach maps to switched optical paths (Mach-Zehnder with on/off modulators). The present paper's approach maps to phased arrays (sources with programmable phase shifters) — the same architecture used in 5G beamforming, radar, and coherent photonic processors.

---

## 9. Noise Margin Analysis

### 9.1 Phase Margin

The angular separation between adjacent output states is $2\pi/q$. A correct detection requires the measured phase to be within $\pm \pi/q$ of the true phase.

### 9.2 Error Tolerance

With $N = \varphi(m)$ sources and per-source amplitude error $\varepsilon$, the worst-case total output error is $N \varepsilon$ (by the triangle inequality). Detection succeeds when $N \varepsilon < \sin(\pi/q)$ (the projection of the error onto the decision boundary).

**Maximum tolerable error per source:**

$$\varepsilon_{\max} = \frac{\sin(\pi/q)}{\varphi(m)}$$

| $q$ | $\varphi(m)$ | Margin (°) | $\varepsilon_{\max}$ | Required SNR (dB) |
|:---:|:-----------:|:----------:|:-------------------:|:-----------------:|
| 2 | 2 | ±90 | 0.500 | 6.0 |
| 3 | 6 | ±60 | 0.144 | 16.8 |
| 4 | 4 | ±45 | 0.177 | 15.1 |
| 5 | 10 | ±36 | 0.059 | 24.6 |
| 8 | 16 | ±22.5 | 0.024 | 32.4 |

Binary is exceptionally robust: each source can err by up to 50% of its amplitude and the output is still correct. Ternary tolerates ~14% error per source. Beyond $q = 8$, the precision requirements become demanding.

### 9.3 Cascade Error Accumulation

In a cascade of $d$ gates, each contributing error $\varepsilon$ per source, the total accumulated error is bounded by $O(d \cdot N \cdot \varepsilon)$ for the detect-and-re-encode approach (errors reset at each stage) or potentially worse for the polynomial cascade (where errors compound multiplicatively through the polynomial). A detailed cascade error analysis is an open problem; the polynomial cascade's degree-$(q-1)$ amplification of errors is the key concern.

---

## 10. The Generalised Euler Product as a Native Program

In [1], the partial Euler product $R(S) = \prod_{p \in S}(1 - 1/p^2)$ is a program in the binary master equation with $O_n = 1/n^2$. The same structure generalises: the Dirichlet $L$-function

$$L_S(2, \chi) = \prod_{p \in S} \frac{1}{1 - \chi(p) p^{-2}} = \sum_{\substack{n \text{ squarefree} \\ p \mid n \Rightarrow p \in S}} \frac{\chi(n)}{n^2}$$

is a program in the multi-state architecture. Each prime $p$ is classified by $\chi$ into one of $q$ phase groups. For the order-3 character $\chi_2$ mod 7:

| Phase group | Residues mod 7 | Primes (first few) |
|:-----------:|:--------------:|:-------------------:|
| 0° (state 0) | 1, 6 | 13, 29, 41, 43 |
| 120° (state 1) | 3, 4 | 3, 11, 17, 31 |
| 240° (state 2) | 2, 5 | 2, 5, 19, 23 |

Numerically, $L(2, \chi_2) \approx 0.799 - 0.102i$. This connects the wave architecture to the distribution of primes in arithmetic progressions (Dirichlet's theorem) and to deeper structures in algebraic number theory.

---

## 11. Encoding Efficiency

The encoding efficiency $\eta = q / \varphi(m)$ measures the fraction of wave sources that encode useful states.

| $q$ | Min prime $m$ | $\varphi(m)$ | $\eta$ | Information gain | Net advantage |
|:---:|:------------:|:-----------:|:------:|:---------------:|:-------------:|
| 2 | 3 | 2 | 1.000 | 1.000 bits | Baseline |
| 3 | 5 | 4 | 0.750 | 1.585 bits | 1.189× |
| 4 | 5 | 4 | 1.000 | 2.000 bits | 2.000× |
| 5 | 7 | 6 | 0.833 | 2.322 bits | 1.935× |
| 8 | 11 | 10 | 0.800 | 3.000 bits | 2.400× |

The "net advantage" column is $\eta \cdot \log_2(q)$: the effective bits per wave source. Binary achieves 1.0 bit/source (baseline). Quaternary achieves 2.0 bits/source — a genuine doubling. Ternary's net advantage of 1.189 bits/source is modest but nonzero. The optimal practical choice depends on the cascade architecture and the cost of nonlinear elements.

**Remark 11.1 (Choice of modulus for ternary).** The table shows that $m = 5$ with $\varphi(5) = 4$ suffices to distinguish 3 ternary states (efficiency $\eta = 0.75$). However, the ternary examples throughout this paper use $m = 7$ with $\varphi(7) = 6$, which has lower efficiency ($\eta = 0.5$) but provides a richer character group containing order-3 characters — whose values are exactly the cube roots of unity. This makes the ternary structure particularly transparent: the order-3 characters assign the three input states to phases $0°, 120°, 240°$ directly. Using $m = 5$ would encode 3 states among 4 characters, all of which have order dividing 4, so the phase assignment would use 4th roots of unity rather than 3rd roots — functional but less natural. The choice of $m$ involves a trade-off between encoding efficiency and algebraic elegance.

---

## 12. Discussion

### 12.1 What Holds and What Changed

The wave interference computer concept is **strengthened** by the revisions:

- The clean character-sum formulation (replacing the hand-wavy "divisibility activation at character addresses") makes the physics transparent: each wave source has a programmable phase, and the interference computes the Fourier synthesis.

- The polynomial cascade theorem resolves the cascading problem — the critical engineering bottleneck — at least for binary (linear cascade) and makes it tractable for ternary (quadratic nonlinearity via SHG).

- The noise margin analysis confirms that binary is exceptionally robust and ternary is practical with standard optical/electronic precision.

### 12.2 Physical Limitations

1. **Multi-input scaling**: The number of wave sources grows exponentially with the number of inputs ($\varphi(m) \sim q^k$). This is fundamental to the encoding scheme, not an artifact. Binary avoids this because each bit is an independent prime, but the multi-state encoding couples all inputs into a single residue class.

2. **Cascade nonlinearity**: For $q > 2$, cascading requires nonlinear elements of degree $q - 1$. Second-harmonic generation (ternary) is well-studied, but higher-order nonlinearities are progressively harder and less efficient.

3. **Phase stability**: All wave sources must maintain stable phase relationships throughout computation. Phase drift between sources causes errors that accumulate across the cascade.

4. **Not Turing complete**: The framework establishes functional completeness for combinational logic. Sequential computation (memory, loops) requires feedback mechanisms not addressed here.

### 12.3 Open Problems

1. **Efficient multi-input encoding**: Can the exponential scaling of $\varphi(m)$ with $k$ be avoided? Is there a $q$-ary analog of the binary "one prime per bit" scheme?

2. **Cascade error propagation**: How does error accumulate through polynomial cascades? The degree-$(q-1)$ polynomial may amplify or suppress errors depending on the function; a full error analysis is needed.

3. **Optimal $q$**: Given a specific SNR and nonlinearity budget, what value of $q$ maximises computational throughput? The net advantage table suggests $q = 4$ may be optimal for many settings.

4. **Connection to QAM**: The multi-phase output states are structurally identical to Phase-Shift Keying (PSK) constellations in telecommunications. The Fourier decomposition over characters is analogous to OFDM modulation. Are there deeper connections to be exploited?

5. **$L$-function computability**: Can the analytic properties of $L(s, \chi)$ be detected or computed within the wave architecture?

---

## References

[1] A. Pisani, "The Natural Operating System: Boolean computation via Möbius inversion and prime-encoded databases," 2026.

[2] A. Pisani, "A unified algebraic framework for number theory, Boolean logic, and circuit topology via the logarithmic isomorphism," 2026.

[3] A. Pisani, "Structured self-information: A prime coordinate decomposition of Shannon's information measure," 2026 (draft).

[4] E. L. Post, "Introduction to a general theory of elementary propositions," *Amer. J. Math.*, vol. 43, no. 3, pp. 163–185, 1921.

[5] J. Łukasiewicz, "O logice trójwartościowej," *Ruch Filozoficzny*, vol. 5, pp. 170–171, 1920.

[6] N. P. Brusentsov, "An experience in the design of computers with ternary number system," in *Small Digital Computer*, Sov. Radio, 1963.

[7] Y. Shen et al., "Deep learning with coherent nanophotonic circuits," *Nature Photonics*, vol. 11, pp. 441–446, 2017.

[8] X. Lin et al., "All-optical machine learning using diffractive deep neural networks," *Science*, vol. 361, pp. 1004–1008, 2018.

---

## Appendix A: Character Tables

### A.1 Characters mod 5 (Quaternary, $q = 4$)

Generator $g = 2$. Encoding: state 0 → 1, state 1 → 2, state 2 → 4, state 3 → 3.

Let $i = e^{2\pi i/4} = \sqrt{-1}$.

| $n$ | $\chi_0(n)$ | $\chi_1(n)$ | $\chi_2(n)$ | $\chi_3(n)$ |
|:---:|:-----------:|:-----------:|:-----------:|:-----------:|
| 0 | 0 | 0 | 0 | 0 |
| 1 | 1 | 1 | 1 | 1 |
| 2 | 1 | $i$ | $-1$ | $-i$ |
| 3 | 1 | $-i$ | $-1$ | $i$ |
| 4 | 1 | $-1$ | 1 | $-1$ |

$\chi_0$: trivial (order 1). $\chi_1$: order 4 (values are 4th roots of unity). $\chi_2$: order 2 (real-valued, Legendre-like). $\chi_3 = \overline{\chi_1}$: order 4.

### A.2 Characters mod 7 (Ternary, $q = 3$)

Generator $g = 3$. Let $\omega = e^{2\pi i/6}$, $\zeta = e^{2\pi i/3}$.

| $n$ | $\chi_0$ | $\chi_1$ | $\chi_2$ | $\chi_3$ | $\chi_4$ | $\chi_5$ |
|:---:|:--------:|:--------:|:--------:|:--------:|:--------:|:--------:|
| 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| 1 | 1 | 1 | 1 | 1 | 1 | 1 |
| 2 | 1 | $\omega^5$ | $\zeta^2$ | $-1$ | $\zeta$ | $\omega$ |
| 3 | 1 | $\omega$ | $\zeta$ | $-1$ | $\zeta^2$ | $\omega^5$ |
| 4 | 1 | $\omega^2$ | $\zeta^2$ | 1 | $\zeta$ | $\omega^4$ |
| 5 | 1 | $\omega^4$ | $\zeta$ | 1 | $\zeta^2$ | $\omega^2$ |
| 6 | 1 | $\omega^3$ | 1 | $-1$ | 1 | $\omega^3$ |

Characters of order 3: $\chi_2$ and $\chi_4 = \overline{\chi_2}$. These take values in $\{1, \zeta, \zeta^2\}$ — the cube roots of unity — and are the routing functions for ternary wave computation.

## Appendix B: Notation

| Symbol | Meaning |
|--------|---------|
| $q$ | Number of computational states |
| $m$ | Encoding modulus (prime) |
| $\chi_j$ | $j$-th Dirichlet character mod $m$ |
| $\hat{F}_j$ | Fourier coefficient / database entry for character $j$ |
| $\omega_q$ | Primitive $q$-th root of unity: $e^{2\pi i/q}$ |
| $g$ | Generator of $(\mathbb{Z}/m\mathbb{Z})^*$ |
| $\varphi(m)$ | Euler totient: number of characters mod $m$ |
| $L(s, \chi)$ | Dirichlet $L$-function |
| $\eta$ | Encoding efficiency: $q / \varphi(m)$ |
| $\varepsilon_{\max}$ | Maximum tolerable per-source error |
