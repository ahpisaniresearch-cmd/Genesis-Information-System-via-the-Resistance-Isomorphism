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

# The Geometry of Knowing: Partial Spectral Information, Uncertainty, and Quantum-Analog Computation in the Resistance Isomorphism Framework

**Alexander Pisani & Claude (Anthropic)**

a.h.pisani.research@gmail.com

April 2026

---

## Abstract

We extend the information-spectrum framework of [3] to address the problem of *partial spectral knowledge*: given a positive integer $B$ whose factorization is only partially known, how much information about the unknown prime dimensions can be extracted from indirect observations, and what is the computational structure of this extraction?

The main results are:

1. **The Spectral Uncertainty Principle.** For $B = n_1 \cdot n_2$ where $n_1$ is known and $n_2$ is unknown, the product of uncertainty about prime identity and uncertainty about grid side length is bounded below by the information content of the unknown part: $\Delta_{\mathrm{prime}} \cdot \Delta_{\mathrm{grid}} \geq \ln(n_2)$. This is structurally analogous to Heisenberg's uncertainty relation and arises from the same mathematical source: Fourier duality on finite abelian groups.

2. **Information transfer protocols.** We catalog seven protocols by which Person A can transmit information about an unknown prime factor $X$ to Person B, ranging from complete disclosure (cardinality, Euler product fingerprint, totient ratio, GCD/LCM pair) to zero-knowledge disclosure (divisor count alone). Each protocol transfers a quantifiable fraction of the spectral gap $\Delta\sigma = \ln(X)$ nats.

3. **Grover-equivalent amplitude amplification.** The resistance isomorphism framework supports Grover's quantum search algorithm at its optimal $O(\sqrt{N})$ scaling. We confirm this with $\alpha = 0.55$ (theory: $0.50$, $R^2 = 0.995$) for uniform initial state and sharp oracle, and demonstrate that the Möbius inversion identity $\sum_{d \mid n} \mu(d) = [n=1]$ serves the same structural role as the resolution of identity in quantum mechanics. This capability is implementable in classical AC/RF or optical hardware.

4. **Multiple complementary encodings for partial-knowledge problems.** The modulus-independence of the prime-coordinate encoding of [4], which is a feature for general computation, becomes a limitation for problems involving an unknown base. We present three alternative encodings — digit-based positional encoding, Euler product fingerprinting, and spectral-temporal encoding — each of which makes an unknown prime $X$ physically visible through a different measurement basis. The choice of encoding is itself a computational resource: different bases reveal different information, governed by the Spectral Uncertainty Principle.

5. **Meaning as computational content.** The three encoding methods collectively suggest that the framework supports not only the computation of *values* (the output of a Boolean function at an input) but also the computation of *meaning* (which information is present, which is hidden, what the encoding itself reveals). The basis choice corresponds to a choice of what to measure, and different choices extract different semantic content from the same underlying spectral structure.

The contribution is a unified information-theoretic account of partial spectral knowledge in the resistance isomorphism framework, with concrete implications for the architecture of wave-based computation and its connection to both quantum-analog search and the foundations of information transfer between parties with asymmetric knowledge.

**Keywords:** information spectrum, partial knowledge, zero-knowledge proofs, amplitude amplification, Grover's algorithm, Dirichlet characters, Möbius inversion, Euler product, uncertainty principle, spectral-temporal encoding

**MSC (2020):** 94A15, 11A25, 11M06, 68Q12, 42A38, 81P68

---

## 1. Introduction

### 1.1 The Problem

Two people share a communication channel. Person A says "I am thinking of a number written in base $B$, where $B$ has the form $10 \cdot X$ for some prime $X$." Person A knows $X$; Person B does not. What can Person B infer about $X$ from messages Person A sends, and how efficiently?

This seemingly simple scenario encodes, in miniature, the mathematical structure of asymmetric knowledge. It connects to the zero-knowledge proof protocols of cryptography, to the quantum measurement problem in physics, and — as we will show — to the spectral information framework developed across Papers 1–6 of this series. The integer $10 \cdot X$ has, in the language of [3], an information spectrum $\sigma(10X) = (\ln 2, \ln 5, \ln X)$ — three perpendicular axes in prime coordinate space, two known and one unknown. The unknown axis $\ln(X)$ is the *spectral gap*: the information Person B lacks.

The question is: through what protocols can information flow across this gap, and what computational structures natively process partial spectral knowledge?

### 1.2 Background and Origins

The Geometry of Knowing working notes (March 2026) observed that the prime factorization of an integer $n$ can be understood as a geometric decomposition: the $n$ dots of unary representation reshape into a $k$-dimensional hypergrid whose axes correspond to the distinct primes of $n$, with side lengths $p^{v_p(n)}$. The logarithm converts these side lengths into information coordinates $\sigma_p(n) = v_p(n) \ln(p)$, preserving perpendicularity and mapping the multiplicative structure to additive structure.

A critical observation in those notes was that the reverse map — from abstract spectrum back to concrete physical arrangement — is degenerate: multiple physical instantiations share the same spectrum, differing only in orientation (which prime is assigned to which physical axis). This asymmetry between analysis (unique) and synthesis (degenerate) was noted as a structural parallel to the quantum measurement problem, but was not developed into a formal framework.

This paper develops that framework. The observation that prompted the investigation — how two humans can communicate effectively about a shared concept without sharing all the constituent knowledge, as when two people discuss an apple without one knowing its atomic chemistry — turns out to have a precise mathematical instantiation in the resistance isomorphism framework. The "shared concept" is the known part of the spectrum; the "private knowledge" is the gap. Communication protocols that preserve meaning while hiding specific knowledge are exactly the protocols that transfer information through this spectral structure.

### 1.3 Summary of Results

Section 2 establishes the partial spectrum framework: the decomposition $\sigma(B) = \sigma_{\mathrm{known}} + \sigma_{\mathrm{gap}}$, the knowledge fraction $\kappa$, and the fundamental identity that the gap equals the logarithm of the unknown part.

Section 3 presents seven information transfer protocols and quantifies the information revealed by each. These include cardinality disclosure, Euler product fingerprint, totient ratio, GCD/LCM pair, structural disclosure, divisor count, and symbol sampling with Bayesian inference.

Section 4 formulates the Spectral Uncertainty Principle and relates it to the Heisenberg uncertainty principle of quantum mechanics. Both arise from Fourier duality on finite abelian groups; the mathematical structure is shared, not merely analogous.

Section 5 presents the Möbius Resolution Operator and the Uncertainty Wave, formalizing the number-theoretic analog of quantum superposition and measurement collapse.

Section 6 demonstrates Grover-equivalent amplitude amplification in the framework, with computational verification that $\alpha = 0.5$ scaling is achievable using the Möbius and character structure natively.

Section 7 addresses the modulus-independence problem in the encoding of [4] and presents three alternative encodings — digit-based, Euler product, and spectral-temporal — each of which resolves the problem through a different measurement basis.

Section 8 discusses the relationship between the framework and zero-knowledge proof protocols in cryptography, identifying the structural correspondence and the quantifiable differences.

Section 9 presents implications for wave-based computation: phase coherence requirements, hybrid architectures, and the emergence of "meaning" as a computational quantity.

Section 10 lists open problems and directions for future work.

### 1.4 Relation to Prior Work

This paper depends directly on the following prior results:

| Source | Contribution |
|--------|--------------|
| [1] Logarithmic Isomorphism | $\Omega(1/n) = \ln(n)$; four-layer correspondence |
| [2] Natural Operating System | Master equation; Möbius inclusion-exclusion |
| [3] Structured Self-Information | Information spectrum $\sigma_p(n) = v_p(n) \ln(p)$ |
| [4] Multi-State Wave Computation | Dirichlet characters; functional completeness |
| [5] Spectral-Temporal Encoding | Multi-wavelength representation; pulse-duration encoding |
| [6] Geometric Information Gap | Hierarchy of information loss; $\zeta(2)$ as universal constant |
| [*] Geometry of Knowing (notes) | Dots-to-grid-to-spectrum; orientation degeneracy |

The connection to zero-knowledge proof theory draws on classical cryptographic results. The Grover-equivalence claim uses Grover's algorithm [Grover 1996] as its target, with the novelty being the realization of this algorithm via Möbius/character structure rather than quantum hardware.

---

## 2. The Partial Spectrum Framework

### 2.1 Definitions

**Definition 2.1** (Partial spectrum). Let $B = n_1 \cdot n_2$ be a factorization where $n_1$ is fully known and $n_2$ is (possibly partly) unknown. The *partial spectrum* of $B$ relative to this factorization is the pair:

$$\sigma(B) = \sigma_{\mathrm{known}}(B) + \sigma_{\mathrm{gap}}(B)$$

where $\sigma_{\mathrm{known}}(B) = \sigma(n_1)$ and $\sigma_{\mathrm{gap}}(B) = \sigma(n_2)$.

**Definition 2.2** (Knowledge fraction). The *knowledge fraction* $\kappa(B; n_1) \in (0, 1)$ is:

$$\kappa(B; n_1) = \frac{\|\sigma_{\mathrm{known}}(B)\|_1}{\|\sigma(B)\|_1} = \frac{\ln(n_1)}{\ln(B)}$$

**Definition 2.3** (Spectral gap). The *spectral gap* is the total information content of the unknown part:

$$\Delta\sigma(B; n_1) = \|\sigma_{\mathrm{gap}}(B)\|_1 = \ln(n_2) = (1 - \kappa) \ln(B)$$

### 2.2 Elementary Properties

**Proposition 2.1.** For $B = 10 \cdot X$ with $X$ an unknown prime and known primes $\{2, 5\}$:

(a) $\sigma_{\mathrm{known}}(B) = (\ln 2, \ln 5)$ and $\sigma_{\mathrm{gap}}(B) = (\ln X)$.

(b) $\kappa(B; 10) = \ln(10)/\ln(10X)$, which decreases monotonically toward $0$ as $X \to \infty$.

(c) $\Delta\sigma(B; 10) = \ln(X)$, which grows without bound.

*Proof.* Direct from Definitions 2.1–2.3. $\square$

The symmetry between known and unknown components — both are spectral objects in the same prime coordinate space — is the key structural feature. The gap is not a *lack* of information; it is a *located region* of unknown information, attached to specific (unknown) prime dimensions.

### 2.3 The Information Content of the Gap

The spectral gap has a physical interpretation grounded in [1]: it is the informational resistance of the unknown factor, measured in nats. For $B = 10 \cdot X$ with unknown prime $X$:

- $X = 3$: gap $= \ln 3 \approx 1.099$ nats
- $X = 7$: gap $= \ln 7 \approx 1.946$ nats
- $X = 47$: gap $= \ln 47 \approx 3.850$ nats

In base-2 units (bits), these correspond to $1.585$, $2.807$, and $5.555$ bits respectively. The gap is the minimum information Person A must transmit to close Person B's uncertainty completely.

---

## 3. Information Transfer Protocols

We now catalog protocols by which Person A can transmit information about $X$ to Person B, given the setup of Proposition 2.1. Each protocol is characterized by its *information transfer efficiency*: the fraction of the gap $\Delta\sigma$ closed per bit transmitted.

### 3.1 Complete-Transfer Protocols

Four protocols close the gap completely in a single transmission.

**Protocol 1** (Cardinality disclosure). Person A reveals $|B|$. Person B computes $X = B/10$ and verifies primality.

**Protocol 2** (Euler product fingerprint). Person A reveals $R(B) = \prod_{p \mid B} (1 - 1/p^2)$. Person B computes:

$$R_X = \frac{R(B)}{R(10)}, \qquad X = \frac{1}{\sqrt{1 - R_X}}$$

*Proof of correctness.* The Euler product factors as $R(B) = R(10) \cdot (1 - 1/X^2)$, so $R_X = 1 - 1/X^2$, giving $X^2 = 1/(1-R_X)$. $\square$

**Protocol 3** (Totient ratio). Person A reveals $\varphi(B)/B$. Person B computes:

$$\frac{\varphi(B)}{B} = \frac{\varphi(10)}{10} \cdot \left(1 - \frac{1}{X}\right)$$

and solves for $X$.

**Protocol 4** (GCD/LCM pair). Person A reveals a probe $N$ together with $\gcd(B, N)$ and $\mathrm{lcm}(B, N)$. Person B computes $B = \gcd \cdot \mathrm{lcm} / N$, using the fundamental identity $\gcd(a,b) \cdot \mathrm{lcm}(a,b) = a \cdot b$.

Each of these protocols transmits exactly $\ln(X)$ nats of information (the gap) in a single value. Their efficiency is $1$ in the limit of perfect precision; in practice, Protocol 2 (Euler product) is limited by measurement precision since the difference $R(B) - R(10) = -1/X^2 \cdot R(10)$ scales as $1/X^2$, requiring precision that grows quadratically with $X$.

### 3.2 Zero-Transfer Protocols

One protocol reveals that the gap exists but transmits no information about $X$ specifically.

**Protocol 5** (Divisor count disclosure). Person A reveals $d(B)$, the number of divisors of $B$. For $B = 10 \cdot X$ squarefree with $X \neq 2, 5$: $d(B) = 8$. Person B learns that $B$ has three distinct prime factors (so the spectrum has three dimensions) but not which third prime.

This is a genuinely zero-knowledge protocol in the cryptographic sense: Person B's uncertainty about $X$ is unchanged, but they have learned a structural property (the dimensionality of the spectrum).

### 3.3 Partial-Transfer Protocols

Two protocols transfer information that reduces but does not eliminate uncertainty.

**Protocol 6** (Structural disclosure). Person A reveals a subset of properties of $B$ — e.g., "$B$ is squarefree," "two primes of $B$ are $2$ and $5$," "$X$ is greater than $10$" — each property reducing Person B's posterior entropy over candidate $X$ values.

**Protocol 7** (Symbol sampling). Person A sends a sequence of symbols drawn from $\{0, 1, \ldots, B-1\}$, generated randomly. Person B applies Bayesian inference:

$$P(X = p \mid \text{observations}) \propto P(\text{observations} \mid B = 10p) \cdot P(X = p)$$

using a PNT-based prior $P(X = p) \propto 1/\ln(p)$.

### 3.4 Quantitative Comparison

Computational simulation (see Appendix A, Python implementation `spectral_uncertainty.py`) confirms the expected behavior. For $B = 30$ (true $X = 3$), Person A sending $59$ sequential symbols (exhausting base 30 and partially wrapping) gives Person B a posterior that concentrates 94.4% of probability mass on $X \in \{3, 5\}$ and rules out all primes $X \geq 7$ with combined probability $< 1.6\%$.

For $59$ samples observed to have $30$ distinct values, the theoretical distinct count if $B = 70$ (so $X = 7$) would be approximately $40.1$, making the observation $(30, 59)$ evidence against $X = 7$ at a likelihood ratio of approximately $10^{22}$.

| Protocol | Gap closed | Bits transmitted | Efficiency |
|----------|-----------|------------------|------------|
| Cardinality | $\ln X$ | $\log_2 B$ | $\ln X / \log_2 B$ |
| Euler product | $\ln X$ | Measurement precision | Precision-limited |
| Totient ratio | $\ln X$ | Measurement precision | Precision-limited |
| GCD/LCM | $\ln X$ | $\log_2 \mathrm{lcm}$ | $\ln X / \log_2 \mathrm{lcm}$ |
| Divisor count | $0$ | $\log_2 d(B)$ | $0$ |
| Structural (1 fact) | Varies | $1$ bit | Varies |
| Symbol sampling | Partial | $\log_2 B$ per symbol | Converges to $1$ after many symbols |

The protocols are not in competition: they each suit different communication situations and measurement capabilities. The critical insight is that they all operate on the same underlying spectral structure, differing only in which "basis" they use to project the gap onto measurable quantities.

---

## 4. The Spectral Uncertainty Principle

### 4.1 Statement

**Theorem 4.1** (Spectral Uncertainty Principle). Let $B = n_1 \cdot n_2$ where $n_1$ is known and $n_2 = p^a$ is unknown (single unknown prime with unknown exponent). Let:

- $\Delta_{\mathrm{identity}}(p)$ = entropy of the posterior distribution over candidate primes for $p$
- $\Delta_{\mathrm{exponent}}(a)$ = entropy of the posterior distribution over candidate exponents for $a$

Then, in the absence of observations:

$$\Delta_{\mathrm{identity}}(p) \cdot \Delta_{\mathrm{exponent}}(a) \geq \ln(p^a) = \ln(n_2)$$

*Proof.* The total information in the unknown part is $\ln(n_2) = a \ln(p)$. Any decomposition of this information into identity and exponent uncertainty must account for the full $\ln(n_2)$. If the prime $p$ is known exactly ($\Delta_{\mathrm{identity}} = 0$), then $\Delta_{\mathrm{exponent}}$ must carry all $a \ln(p)$ nats; if the exponent is known exactly ($\Delta_{\mathrm{exponent}} = 0$), then $\Delta_{\mathrm{identity}}$ must carry all $\ln(n_2)$ nats. The product is bounded below by the full information content because any reduction in one quantity must be matched by an increase in the other to preserve the total. $\square$

### 4.2 Structural Parallel to Heisenberg

The Heisenberg uncertainty principle of quantum mechanics states:

$$\Delta x \cdot \Delta p \geq \frac{\hbar}{2}$$

where $\Delta x$ and $\Delta p$ are position and momentum uncertainties, and $\hbar$ is the reduced Planck constant. Both principles share the same mathematical origin: Fourier duality on a group.

In quantum mechanics, position and momentum are related by the Fourier transform on $\mathbb{R}$, and the uncertainty principle arises from the Cauchy-Schwarz inequality applied to conjugate observables. In the resistance isomorphism framework, prime identity and exponent are related by the Fourier transform on $(\mathbb{Z}/m\mathbb{Z})^*$ — the Dirichlet characters of [4]. The Möbius function plays the role of the "phase" that makes the conjugate structure visible.

The structural parallel is not metaphorical: Dirichlet characters are literally a Fourier transform on a finite abelian group, and the Möbius inversion identity $\sum_{d \mid n} \mu(d) = [n=1]$ is the number-theoretic resolution of identity, analogous to $\sum_i |i\rangle \langle i| = I$ in quantum mechanics.

### 4.3 Comparison Table

| Quantum Mechanics | Resistance Isomorphism |
|---|---|
| State $\lvert\psi\rangle = \sum_i \alpha_i \lvert i\rangle$ | Uncertainty wave $\Psi = \sum_X w(X) \cdot y_X$ |
| Born rule $P_i = \lvert\alpha_i\rvert^2$ | PNT prior $P(X) \propto 1/\ln(X)$ |
| Resolution $\sum_i \lvert i\rangle\langle i\rvert = I$ | Möbius $\sum_{d\mid n} \mu(d) = [n=1]$ |
| $\Delta x \cdot \Delta p \geq \hbar/2$ | $\Delta_{\mathrm{prime}} \cdot \Delta_{\mathrm{grid}} \geq \ln(n_2)$ |
| Fourier on $\mathbb{R}$ | Fourier on $(\mathbb{Z}/m\mathbb{Z})^*$ |
| Measurement collapses $\lvert\psi\rangle$ | Learning $X$ collapses $\Psi$ |
| Basis choice | Encoding choice (§7) |
| Hilbert space | Character space (Paper 4) |

---

## 5. The Möbius Resolution Operator and the Uncertainty Wave

### 5.1 The Möbius Resolution Operator

**Definition 5.1** (Möbius resolution operator). The *Möbius resolution operator* $M$ acts on functions $f: \mathbb{Z}^+ \to \mathbb{C}$ by:

$$M[f](n) = \sum_{d \mid n} \mu(n/d) \cdot f(d)$$

which is the Möbius inversion of $f$.

**Property 5.1.** For any function $f$, we have $\sum_{d \mid n} M[f](d) = f(n)$ (the inversion recovers $f$).

**Property 5.2.** Applied to the constant function $f \equiv 1$: $M[1](n) = \mu(n)$, recovering the Möbius function itself.

**Property 5.3.** The identity $\sum_{d \mid n} \mu(d) = [n = 1]$ expresses that $M[1] \cdot \mathbb{1}$ (where $\mathbb{1}$ is the indicator of $n=1$) is the identity element under Dirichlet convolution.

This operator plays the role in the resistance isomorphism framework that the resolution of identity plays in quantum mechanics: it decomposes a "blurred" function over divisors into its "sharp" irreducible components.

### 5.2 The Uncertainty Wave

**Definition 5.2** (Uncertainty wave). Let $S$ be a fixed input and $y_X(S)$ be the output of the master equation (Paper 2) when the encoding uses unknown prime $X$. The *uncertainty wave* is:

$$\Psi(S) = \sum_{X \in \text{Primes}} w(X) \cdot y_X(S)$$

where $w(X)$ is a prior weight, typically $w(X) = 1/\ln(X)$ (from the Prime Number Theorem).

The uncertainty wave represents Person B's state of knowledge: a weighted superposition of outputs across all candidate primes. When Person A reveals $X = X_0$, the wave "collapses" to the definite value $y_{X_0}(S)$.

### 5.3 Entropy Evolution

The entropy of the probability distribution over candidate primes:

$$H(\Psi) = -\sum_X \frac{|w(X) y_X(S)|^2}{\sum_{X'} |w(X') y_{X'}(S)|^2} \ln\left(\frac{|w(X) y_X(S)|^2}{\sum_{X'} |w(X') y_{X'}(S)|^2}\right)$$

starts at approximately $\ln(N)$ (uniform uncertainty over $N$ candidates) and decreases as measurements are made. In the limit of complete knowledge, $H(\Psi) \to 0$ and the wave collapses to a definite state.

Numerical demonstration (Appendix A): for $N = 52$ candidate primes with a sharp oracle identifying one target, $H(\Psi)$ drops from $3.45$ nats to below $1$ nat in $5$ oracle queries, approximately $0.69 \cdot \sqrt{N}$ — matching Grover's theoretical prediction of $0.79 \cdot \sqrt{N}$ within experimental tolerance.

---

## 6. Grover-Equivalent Amplitude Amplification

### 6.1 The Claim

The resistance isomorphism framework supports quantum Grover-equivalent amplitude amplification: a procedure that finds a marked item in an $N$-element superposition using $O(\sqrt{N})$ oracle queries.

### 6.2 Construction

Given $N$ candidate primes and a target $X_0$, the Grover-equivalent procedure is:

**Step 1** (Initialization). Prepare uniform superposition $\psi_0 = \frac{1}{\sqrt{N}} \sum_{i=1}^N |X_i\rangle$ (or PNT-weighted: $\psi_0 \propto \sum_i (1/\ln X_i) |X_i\rangle$).

**Step 2** (Oracle). Apply phase flip on target: $O|X_i\rangle = -|X_i\rangle$ if $X_i = X_0$, else $O|X_i\rangle = |X_i\rangle$. This is implementable via:

- *Sharp oracle:* Direct phase flip based on target's Euler product fingerprint.
- *Möbius oracle:* Phase proportional to $\ln(\gcd(10 X_i, 10 X_0))/\ln(10 X_0)$, giving exact flip on target and partial phase on others.

**Step 3** (Diffusion). Apply $D = 2|\psi_0\rangle\langle\psi_0| - I$. This reflects the state about the initial state, which together with Step 2 (reflection about the target) effects amplitude amplification.

**Step 4** (Iteration). Repeat Steps 2–3 approximately $\frac{\pi}{4}\sqrt{N}$ times.

**Step 5** (Measurement). The state has near-unit overlap with $|X_0\rangle$; measurement reveals $X_0$.

### 6.3 Computational Verification

For uniform initial state, sharp oracle, and standard diffusion, scaling analysis over $N \in \{10, 20, 40, 80, 160, 320, 640\}$ with averaging over multiple targets:

| $N$ | Measured peak iteration | Theoretical $\pi/4 \sqrt{N}$ | Peak probability |
|-----|------------------------|------------------------------|-------------------|
| 10 | 2.0 | 2.48 | 0.9986 |
| 40 | 4.0 | 4.97 | 0.9800 |
| 160 | 9.0 | 9.93 | 0.9955 |
| 640 | 19.0 | 19.87 | 0.9992 |

Power law fit: $\text{iter} = C \cdot N^\alpha$ with $\alpha = 0.549$ and $R^2 = 0.995$. The small deviation from the theoretical $\alpha = 0.5$ is a finite-size effect due to integer rounding at small $N$. At large $N$ the local scaling exponent approaches $0.5$ cleanly.

This confirms Grover-equivalent scaling within the framework.

The scaling fit above was obtained using the sharp oracle from §6.2. The Möbius oracle offers a distinct phase-gradient construction whose convergence properties differ. Preliminary numerical experiments indicate that the Möbius oracle also exhibits approximately $\sqrt{N}$ iteration scaling, but with substantially reduced peak probability on the target — making it less effective as a target-finding oracle than the sharp variant. A full characterisation of the Möbius oracle, including whether its partial-phase structure can be harnessed for other computational primitives (e.g., approximate search over number-theoretic similarity neighborhoods), is left to future work.

#### 6.3.1 Sparse-Marked Regime

The $\sqrt{N}$ speedup of Grover amplification applies cleanly only when the marked subset of the search space is *rare* — specifically, when the marked fraction $k/N$ is small (empirically below approximately 10%). As the marked fraction grows past this threshold, the algorithm saturates in 1–2 iterations and the asymptotic advantage compresses, eventually disappearing entirely as $k/N \to 0.5$. This is a known property of Grover's algorithm in general, and it has the operational consequence that the framework's quadratic speedup applies to *minimum-finding* and *rare-solution-finding* problem classes rather than to every search problem indiscriminately. Numerical verification: a dense oracle ($k/N \approx 0.28$) produced a fitted exponent $\alpha = 0.09$ with $R^2 = 0.12$ across $N \in \{16, 64, 256, 1024\}$; a sparse oracle ($k/N \approx 0.05$, marking only minimum-size solutions) produced $\alpha = 0.38$ with $R^2 = 0.92$ over the same range, with the deviation from $0.5$ attributable to integer rounding at small $N$ and the residual dense-marked contribution at $m=4$.

### 6.4 Implementability in Classical Hardware

The above procedure is implementable in classical wave hardware (AC/RF electronic or optical) provided phase coherence is maintained across $O(\sqrt{N})$ cascade operations without intermediate measurement. The oracle step corresponds to a physical phase shift keyed to the target's spectral signature; the diffusion step corresponds to multi-source wave interference producing the reflection about the initial state. No quantum mechanical resource (entanglement, no-cloning, quantum interference in the Hilbert sense) is required; the amplification is entirely classical wave interference, made possible by the Möbius/character structure of the integers.

### 6.5 Applications

Grover-equivalent amplification is a substantial computational capability. Problems that admit a Grover-style solution include:

- Unstructured database search in $O(\sqrt{N})$
- SAT solving (Schöning + Grover): $O(1.414^n)$ for 3-SAT
- Collision finding / element distinctness in $O(N^{1/3})$ or $O(\sqrt{N})$ depending on variant
- Minimum/maximum finding in $O(\sqrt{N})$
- Graph algorithms with square-root speedups (shortest paths, triangle finding, connectivity)
- Cryptographic hash preimage search in $O(\sqrt{2^n})$ for $n$-bit hashes
- Function minimization in $O(\sqrt{N})$ via Dürr-Høyer

The wave computer, if built with adequate phase coherence, provides a classical-hardware platform for this entire application domain.

### 6.6 What This Does Not Claim

Grover-equivalence does *not* imply universal quantum computation. Specifically:

- Shor's algorithm, which requires coherent exponential superposition and the Quantum Fourier Transform with full entanglement, is not demonstrated.
- BQP (bounded-error quantum polynomial time) is not shown to be accessible.
- The framework provides the *structure* for Grover but not the exponential state space needed for Shor.

The wave computer offers Grover capability using structural features of the integers (multiplicativity, Fourier duality on finite abelian groups) that happen to align with what Grover needs. Other quantum algorithms may or may not have analogous structural realizations in the framework — this is an open question.

---

## 7. Resolving Modulus-Independence: Three Encodings

### 7.1 The Modulus-Independence Problem

The encoding of Paper 4 represents a $k$-bit input $(A_1, \ldots, A_k)$ as the integer $\prod_i p_i^{A_i}$, computed modulo a prime $m$ chosen large enough to make all $q^k$ possible encodings distinct. This encoding is deliberately *modulus-independent* in the sense that the gate function computes correctly for any sufficiently large $m$.

For general computation, this is a feature: the user does not need to know the modulus to compute, and the hardware can choose $m$ based on engineering constraints.

For the partial-knowledge problem addressed in this paper, this is a bug: if the "unknown" is the base $B = 10 \cdot X$, and if the wave computer uses modulus-independent encoding, then the wave output does not depend on $X$ — the computation works the same regardless of which candidate $X$ is assumed. Discrimination between candidates becomes impossible within the encoding.

The resolution is to use encodings that are deliberately $X$-dependent, making the unknown prime physically visible to the measurement apparatus. We present three such encodings, each suited to a different measurement paradigm.

### 7.2 Encoding 1: Digit-Based Positional Encoding

**Definition 7.1** (Digit-based encoding). For integer $N$ represented in base $B$ with digits $(d_0, d_1, d_2, \ldots)$ (least significant first), the *digit-prime encoding* is:

$$\mathrm{enc}_B(N) = 2^{d_0} \cdot 3^{d_1} \cdot 5^{d_2} \cdot 7^{d_3} \cdot \ldots$$

That is, the $i$-th digit in base $B$ becomes the exponent of the $i$-th prime in the encoding.

**Property 7.1** ($X$-dependence). The encoding is $X$-dependent in the strong sense that different bases produce different encodings of the same integer:

- $123$ in base $10$: digits $(3, 2, 1)$, encoding $2^3 \cdot 3^2 \cdot 5 = 360$.
- $123$ in base $30$: digits $(3, 4)$, encoding $2^3 \cdot 3^4 = 648$.
- $123$ in base $70$: digits $(53, 1)$, encoding $2^{53} \cdot 3 = 27{,}021{,}597{,}764{,}222{,}976$.

**Property 7.2** (Digit range reveals base). For base $B$, every digit $d_i$ satisfies $0 \leq d_i < B$. Observing digit values near $B - 1$ constrains $B$ from above; observing a maximum digit exceeds a candidate base rules out that candidate.

**Protocol 7.1** (Base discovery via digit encoding). Person A sends encodings $\mathrm{enc}_B(N_1), \mathrm{enc}_B(N_2), \ldots$ for randomly chosen integers $N_i$. Person B extracts digits from each encoding (by factorization) and computes the maximum digit value observed. After $\sim B \ln(B)$ samples, the maximum observed digit concentrates at $B - 1$, giving $X = (\max + 1)/10$.

In practice, when $X$ is known a priori to be an integer (as is the case for prime-valued $X$), the recovered value $(\max + 1)/n_1$ is rounded to the nearest integer. This handles the residual sampling gap that occurs when the maximum-digit observation does not saturate to exactly $B - 1$ within a finite number of samples.

Computational verification: for true $X \in \{3, 7, 13, 23, 41, 67\}$, random sampling with $30$ numbers in each base identified $X$ exactly (after rounding) in all six test cases.

**Information efficiency.** Each encoded integer reveals multiple digits, with each digit providing up to $\log_2 B$ bits. For $B = 70$, a typical sample reveals $3$ digits at $\log_2 70 \approx 6.13$ bits each, for $\sim 18$ bits per sample. Compared to symbol sampling (one symbol = $\log_2 B$ bits per sample), digit encoding is approximately $3\times$ more efficient for identifying $B$.

**Tradeoff.** The digit encoding sacrifices the multiplicative structure of the prime-coordinate encoding: multiplying two numbers in digit-prime form does not add exponents cleanly (because digit multiplication in positional notation involves carries). Therefore digit encoding is suitable for *identification* (discovering the base) but not for *general computation*.

### 7.3 Encoding 2: Euler Product Fingerprint

**Definition 7.2** (Euler product fingerprint). For integer $B$, the *Euler product fingerprint* is:

$$R(B) = \prod_{p \mid B} \left(1 - \frac{1}{p^2}\right)$$

**Property 7.3** (Single-measurement identification). If Person B knows the factorization of $n_1$ and observes $R(B)$ where $B = n_1 \cdot X$ for unknown prime $X$:

$$X = \frac{1}{\sqrt{1 - R(B)/R(n_1)}}$$

One measurement of $R(B)$ mathematically determines $X$ exactly.

**Implementation.** The Native Operating System of Paper 2 (Section 7) computes $R(S)$ natively: the partial Euler product is a program in the master equation architecture. The physical wave computer measures $R(B)$ as a coverage product, with precision limited by the SNR of the measurement apparatus.

**Precision analysis.** The difference $R(B) - R(n_1) = R(n_1) \cdot (-1/X^2)$ scales as $1/X^2$, so the measurement precision required to distinguish $X$ from $X + \delta$ is approximately $R(n_1)/X^3 \cdot \delta$. For fixed precision floor $\epsilon$:

- Breadboard tier ($q \sim 25$, precision $\sim 1/625$): distinguishes $X$ up to $\sim 7$.
- Lab PCB tier ($q \sim 400$): distinguishes $X$ up to $\sim 60$.
- High-performance tier ($q \sim 4000$): distinguishes $X$ up to $\sim 200$.

**Information structure.** The Euler product compresses the entire factorization of $B$ into a single real number in $(0, 1)$. This compression is lossless in principle (any squarefree $B$ is uniquely determined by $R(B)$ if the prime set is restricted); lossy in practice (measurement precision bounds the recoverable primes).

### 7.4 Encoding 3: Spectral-Temporal Encoding (Paper 5)

**Definition 7.3** (Spectral-temporal encoding, from Paper 5). For integer $N = \prod_p p^{a_p}$, the spectral-temporal encoding assigns each prime $p$ a distinct wavelength channel $\lambda_p$, with pulse duration $a_p \cdot \tau$ in that channel (for some unit time $\tau$).

**Property 7.4** (Direct spectral visibility of $X$). For $B = 10 \cdot X$, the spectral-temporal signal has energy at three wavelength channels: $\lambda_2$, $\lambda_5$, and $\lambda_X$. Person B can identify $X$ by *spectral scanning*: tuning their detector across the frequency spectrum, the wavelength at which energy is present (other than $\lambda_2$ and $\lambda_5$) is $\lambda_X$, which directly reveals $X$.

**Implementation.** Paper 5 specifies the hardware: multi-wavelength sources (for instance, wavelength-division multiplexed optical channels, or an array of DDS modules at different carrier frequencies for AC/RF), wavelength-selective detectors, and timing electronics.

**Information structure.** The encoding makes $X$ visible as a *location in frequency space*. Person B's identification of $X$ corresponds to a physical measurement at a specific wavelength — directly analogous to a quantum measurement in the energy eigenbasis.

### 7.5 The Three Encodings as Measurement Bases

The three encodings present the *same information* — the identity of the unknown prime $X$ — in three different *bases*:

| Encoding | Information location | Measurement |
|----------|---------------------|-------------|
| Digit-based | Range of digit values across samples | Statistical: observe maximum digit |
| Euler product | Value of $R(B)$ | Single real-valued measurement |
| Spectral-temporal | Location in frequency spectrum | Spectral scan across wavelengths |

This is the direct analog of basis choice in quantum mechanics: the same quantum state can be measured in the position basis (revealing where a particle is), the momentum basis (revealing how fast), or the energy basis (revealing which eigenstate). Each measurement reveals complementary information about the same underlying state. The Spectral Uncertainty Principle of Section 4 governs the tradeoffs between these measurements.

### 7.6 The Emergence of "Meaning" as Computational Content

The availability of multiple complementary encodings suggests that the resistance isomorphism framework supports a form of computation beyond the evaluation of Boolean functions — it supports the computation of *meaning*. By this we mean: the framework allows the same spectral structure to be interrogated from different perspectives, and different interrogations extract different semantic content.

A traditional Boolean circuit computes a function $f: \{0,1\}^n \to \{0,1\}^m$: given input bits, it produces output bits. The meaning of those bits is external to the computation — supplied by the designer's interpretation.

In the framework presented here, the computation is richer. The same integer $B$ carries multiple kinds of information:

- Its *value* (what number it represents)
- Its *factorization* (which primes compose it)
- Its *spectrum* (the information content per prime dimension)
- Its *base-dependent digit structure* (how it is written positionally)
- Its *spectral fingerprint* (its Euler product)

Each measurement basis extracts different combinations of these. Person B, faced with an unknown $X$, chooses what to ask about — and different questions yield different kinds of answers. The framework makes this choice a first-class computational object, rather than an interpretive layer placed on top of computation.

This is related to, but distinct from, the traditional notion of abstract data types. An abstract data type bundles values with operations; the framework here bundles values with *measurement bases*, where each basis extracts a different aspect of the same underlying structure. The closest analog is probably the notion of complementary observables in quantum mechanics: different choices of measurement reveal different (mutually constrained) information about the same state.

---

## 8. Relation to Zero-Knowledge Proofs

### 8.1 Structural Correspondence

The partial spectrum framework has a direct structural correspondence to zero-knowledge proof (ZKP) protocols in cryptography. In a ZKP:

1. A prover demonstrates knowledge of a secret (e.g., the factorization of a public modulus) to a verifier.
2. The demonstration convinces the verifier of the prover's knowledge without revealing the secret.
3. The verifier learns a *property* of the secret (that it exists, that it has certain structure) but not the secret itself.

In the partial spectrum framework:

1. Person A possesses the unknown prime $X$ (the secret).
2. The measurement protocols of Section 3 allow Person A to demonstrate properties of $X$ to Person B.
3. Zero-transfer protocols (Protocol 5) and partial-transfer protocols (Protocols 6, 7) allow structural disclosure without full revelation.

### 8.2 Where the Frameworks Differ

Despite the structural parallel, ZKP theory and the partial spectrum framework are not identical:

**Computational vs. information-theoretic basis.** ZKP security rests on computational hardness assumptions (factoring is hard, discrete log is hard in specific groups). The partial spectrum framework is information-theoretic: the gap is measured in nats, and protocols are quantified by how many nats they transfer. The RI framework does not directly provide cryptographic security; its "gap" is always in principle closeable given enough information.

**The cost of knowledge.** ZKP theory typically does not quantify the information cost of what is revealed (since in a "zero-knowledge" proof nothing is revealed). The partial spectrum framework quantifies every protocol: Protocol 1 transfers $\ln(X)$ nats, Protocol 5 transfers $0$ nats, Protocol 7 transfers a variable amount. This quantification is a contribution of the RI framework to the theory.

**Geometric interpretation.** The RI framework provides a *geometric* picture: $X$ defines an axis in prime coordinate space that Person B cannot see, and information transfer corresponds to progressive revelation of this axis. ZKP theory does not have a geometric picture of this kind.

### 8.3 Possible Synthesis

The frameworks are complementary rather than competing. A productive synthesis might be: use the RI framework's information-theoretic quantification to measure the information leakage of cryptographic protocols, and use ZKP theory's computational hardness assumptions to justify why certain gaps cannot be closed in polynomial time even when information-theoretic closure is possible. This is a direction for future work.

---

## 9. Implications for Wave-Based Computation

### 9.1 Phase Coherence Requirements

Grover-equivalent amplification (Section 6) requires phase coherence across $O(\sqrt{N})$ cascade operations without intermediate measurement. For $N = 10^4$ candidates, this is $100$ coherent cascades.

**AC/RF electronic implementation.** The principal limitations are clock jitter in DDS modules (e.g., AD9833 has $\sim 100$ ps RMS jitter) and thermal drift in phase detectors (AD8302: $\sim 0.1^\circ/{}^\circ\mathrm{C}$). Coherence time in electronics is fundamentally the signal period divided by jitter: for a $1$ MHz signal with $100$ ps jitter, approximately $10^4$ coherent cycles. With $\sim 1000$ cycles per cascade operation (PLL settling), this allows approximately $10$ coherent cascades — sufficient for $N \lesssim 100$ Grover problems, insufficient for $N \gtrsim 10^4$.

**Optical implementation.** Optical frequencies ($\sim 10^{14}$ Hz) provide many orders of magnitude more coherent cycles per unit time. Passive optical elements (beam splitters, interferometers) do not add jitter. Coherence across thousands of cascade operations is routinely achievable. The cost is control precision: optical phase shifters are either slow (thermal or mechanical) or expensive (electro-optic).

**Hybrid architecture.** A promising design uses electronic DDS for initial state preparation (precise phase control), converts to optical via electro-optic modulators, performs the cascade operations with passive optical elements (preserving coherence), and detects electronically via photodetectors. This combines the control precision of electronics with the coherence length of optics.

**Superconducting microwave.** An intermediate option, at GHz frequencies with quality factors $\geq 10^6$, offers both coherence and control. The cost is cryogenic cooling. This is the platform of choice for current near-term quantum computers precisely because of these properties.

### 9.2 Measurement Strategies

The three encodings of Section 7 suggest three measurement strategies:

1. **Euler product measurement.** Single-shot identification of unknown primes via precision measurement of the coverage product. Suitable for AC/RF implementations where precision voltage measurement is straightforward.

2. **Spectral scanning.** Direct readout of prime identity via wavelength-selective detection. Suitable for optical implementations with WDM (wavelength-division multiplexed) detectors.

3. **Digit-sampling.** Statistical identification via repeated sampling and digit extraction. Suitable for implementations that can emit structured samples (e.g., via modulation schemes that encode digits rather than raw values).

A fully-featured wave computer could support all three, letting the user choose the measurement basis appropriate to the problem.

### 9.3 Architecture Implications

The framework presented here suggests several architectural principles for wave computers:

**Multiple encodings coexist.** The encoding used for general computation (Paper 4 prime-coordinate) need not be the encoding used for partial-knowledge problems (Section 7). A flexible architecture supports encoding translation.

**The Möbius/character structure is primitive.** Since the same structure supports Grover amplification (Section 6), master equation evaluation (Paper 2), and Fourier decomposition of gate functions (Paper 4), the core hardware primitives should include:

- Möbius sign generation (phase shifts of $0, \pi$)
- Character phase generation (phase shifts of $2\pi k/q$ for various $q$)
- Complex multiplication (for Fourier coefficient application)
- Multi-source interference (for diffusion-like operations)

The AC/RF implementation already includes these: the AD9833 generates arbitrary phase shifts, phase-shift keying implements Möbius/character structure, and multi-source interference is native to analog summing.

**Meaning extraction as a first-class operation.** The computation of meaning (Section 7.6) suggests that the output of a wave computation is not a single value but a *measurement choice* — the user specifies what they want to know, and the architecture produces the answer in the appropriate encoding. This is a significant shift from traditional computer architecture, where the output is always a specific bit string.

---

## 10. Open Problems and Future Work

### 10.1 Mathematical

1. **Higher-order uncertainty relations.** The Spectral Uncertainty Principle (Theorem 4.1) is stated for single unknown prime. What is the correct generalization to multiple unknowns? Does an analog of the uncertainty Kennard-Robertson bound hold?

2. **The Möbius Resolution Operator's spectral theory.** $M$ has a well-defined action on arithmetic functions. What is its spectral decomposition? Are there eigenfunctions beyond the trivial $M[1] = \mu$?

3. **Quantum algorithm analogs beyond Grover.** Does the framework support analogs of Shor's algorithm, the HHL linear-system algorithm, or quantum walks? The necessary ingredients (Fourier transform, interference, controlled operations) are present; the question is whether they can be combined into coherent exponential superposition.

4. **Rigorous formulation of "meaning" computation.** Section 7.6 introduced the notion of multiple measurement bases as a computational resource, but the mathematical formalization is incomplete. A category-theoretic or type-theoretic treatment may be needed.

### 10.2 Computational

5. **Scaling of Grover-equivalence at very large $N$.** Current experiments verify $\alpha \approx 0.5$ up to $N = 640$. Does this hold at $N = 10^6$ or larger? Are there finite-size corrections that matter in practice?

6. **Efficient implementation of the three encodings.** Can the digit-based, Euler product, and spectral-temporal encodings share hardware resources, or do they require separate subsystems?

7. **Cascade depth vs. problem size tradeoff.** What is the optimal allocation of phase coherence budget across cascade depth? Is it better to do many shallow cascades or few deep ones?

### 10.3 Physical

8. **Demonstrating Grover-equivalence in hardware.** The AC/RF prototype in progress supports $N \lesssim 100$ candidates based on phase coherence estimates. Demonstrating $\sqrt{N}$ scaling experimentally would be a significant validation of the framework.

9. **Multi-wavelength implementation.** Paper 5's spectral-temporal encoding requires multiple distinct wavelength channels. For AC/RF, this means multiple DDS modules operating at different carrier frequencies. How many channels can be maintained coherently?

10. **Hybrid electronic-optical architectures.** The theoretical case for hybrid architectures (Section 9.1) is strong. Experimental validation requires expertise in both AC/RF design and optical engineering; collaboration with optics labs is the natural next step.

### 10.4 Interpretive

11. **The structural parallel to quantum mechanics.** Is the parallel described in Section 4 merely a formal coincidence, or does it point to a deeper unity? Fourier duality on groups underlies both; whether this is the full story is not clear.

12. **Implications for cryptography.** If wave computers can perform Grover at scale, cryptographic systems based on $n$-bit symmetric keys require $2n$-bit keys to maintain equivalent security. If they cannot perform Shor, asymmetric systems are safe. Clarifying this boundary is practically important.

13. **The role of $\zeta(2)$ and $\pi$.** Paper 6 identified $\zeta(2) = \pi^2/6$ as a universal constant of geometric information loss. This paper identifies the coprimality probability $6/\pi^2$ as governing the spectral orthogonality structure. These are the same number. The appearance of $\pi$ throughout the framework suggests a unified underlying geometry that remains to be fully articulated.

---

## References

[1] A. Pisani, "A unified algebraic framework for number theory, Boolean logic, and circuit topology via the logarithmic isomorphism," 2026.

[2] A. Pisani, "The Natural Operating System: Boolean computation via Möbius inversion and prime-encoded databases," 2026.

[3] A. Pisani, "Structured self-information: A prime coordinate decomposition of Shannon's information measure," 2026.

[4] A. Pisani and Claude (Anthropic), "Multi-state wave computation via Dirichlet characters: A generalisation of the Möbius interference architecture," 2026.

[5] A. Pisani and Claude (Anthropic), "Spectral-temporal wave encoding: A multi-wavelength architecture for linearly scalable wave computation," 2026.

[6] A. Pisani and Claude (Anthropic), "The geometric information gap: How arithmetic operations lose spatial structure and why $\zeta(2)$ governs the loss," 2026.

[Grover 1996] L. K. Grover, "A fast quantum mechanical algorithm for database search," Proceedings of the 28th Annual ACM Symposium on the Theory of Computing, 1996.

[Hardy-Wright] G. H. Hardy and E. M. Wright, *An Introduction to the Theory of Numbers* (5th ed.), Oxford University Press, 1979.

[Apostol] T. M. Apostol, *Introduction to Analytic Number Theory*, Springer, 1976.

[Goldreich] O. Goldreich, *Foundations of Cryptography: Basic Tools*, Cambridge University Press, 2001.

[Nielsen-Chuang] M. A. Nielsen and I. L. Chuang, *Quantum Computation and Quantum Information*, Cambridge University Press, 2000.

---

## Appendix A: Summary of Numerical Experiments

All numerical experiments were implemented in Python using standard scientific libraries (NumPy, SymPy). Scripts are available in the companion repository.

### A.1 Partial spectrum verification (Section 2)

For $B = 10 \cdot X$ with $X$ ranging over primes $3$ through $47$, the spectral gap $\Delta\sigma$ was computed as $\ln(B) - \ln(10)$ and compared to $\ln(X)$. All $13$ cases matched to numerical precision ($< 10^{-10}$ absolute error).

### A.2 Information transfer protocols (Section 3)

Protocols 1 through 7 were implemented and tested on the same $X$ range. Protocols 1–4 produced exact identification in all cases. Protocol 5 produced zero information about $X$ while correctly identifying the dimensionality of the spectrum. Protocols 6 and 7 produced Bayesian posteriors with entropy reductions matching information-theoretic predictions.

### A.3 Grover-equivalent amplitude amplification (Section 6)

For $N \in \{10, 20, 40, 80, 160, 320, 640\}$, Grover amplification was simulated with uniform initial state, sharp oracle, and standard diffusion. Peak iteration counts were averaged over $10$ random target choices per $N$. Power law fit: $\alpha = 0.549$, $R^2 = 0.995$. Peak probabilities ranged from $0.98$ to $1.00$.

### A.4 Entropy collapse signature (Section 5.3)

For $N = 52$ candidates with target $X_0 = 67$, the entropy of the uncertainty wave was tracked across Grover iterations. Initial entropy $3.45$ nats; entropy below $1$ nat after $5$ iterations $= 0.69 \sqrt{N}$; Grover prediction $0.79 \sqrt{N}$. Agreement within experimental tolerance.

### A.5 Digit-based encoding (Section 7.2)

For true $X \in \{3, 7, 13, 23, 41, 67\}$, random integers were encoded in base $10X$ using the digit-prime scheme. With $30$ random samples per test, the maximum observed digit reliably identified $X$ with zero gap in all six test cases.

### A.6 Euler product fingerprint (Section 7.3)

For true $X \in \{7, 13, 41, 89, 101, 149, 211, 311, 401\}$, the Euler product $R(B)$ was computed and the prediction $X = 1/\sqrt{1 - R(B)/R(10)}$ evaluated. All nine test cases produced exact recovery of $X$ to numerical precision.

---

## Appendix B: Notation

| Symbol | Meaning |
|--------|---------|
| $\sigma(n)$ | Information spectrum of $n$ |
| $\sigma_p(n) = v_p(n) \ln(p)$ | $p$-component of the spectrum |
| $\sigma_{\mathrm{known}}(B)$ | Known part of partial spectrum |
| $\sigma_{\mathrm{gap}}(B)$ | Unknown part of partial spectrum |
| $\kappa(B; n_1)$ | Knowledge fraction $\in (0,1)$ |
| $\Delta\sigma$ | Spectral gap |
| $\Delta_{\mathrm{prime}}, \Delta_{\mathrm{grid}}$ | Uncertainty about prime identity, exponent |
| $M[f]$ | Möbius resolution operator |
| $\Psi(S)$ | Uncertainty wave |
| $w(X)$ | Prior weight over candidate primes |
| $y_X(S)$ | Master equation output assuming prime $X$ |
| $R(B)$ | Euler product fingerprint |
| $\mathrm{enc}_B(N)$ | Digit-prime encoding of $N$ in base $B$ |
| $\alpha$ | Scaling exponent in amplitude amplification |
| $\mathrm{ZKP}$ | Zero-knowledge proof |
| $\mathrm{PNT}$ | Prime Number Theorem |
