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

# Spectral-Temporal Wave Encoding: The Information Spectrum as Physical Wave Structure

**Alexander Pisani & Claude (Anthropic)**

a.h.pisani.research@gmail.com

April 2026

---

## Abstract

We show that the information spectrum of a positive integer — the prime coordinate decomposition $\sigma_p(n) = v_p(n) \cdot \ln(p)$ developed in [3] — admits a faithful physical realisation as a multi-wavelength electromagnetic pulse packet. Each prime $p$ is assigned a distinct wavelength channel $\lambda_p$. Each exponent $v_p(n)$ is encoded as the pulse duration $v_p(n) \cdot \tau$ in that channel. The resulting wave packet *is* the number $n$, represented not as a symbol or a residue class but as a physical object whose measurable properties are the prime coordinates of $n$.

Under this encoding, the fundamental operations of the divisibility lattice become physical measurements: the GCD of two integers is the temporal overlap of their wave packets (componentwise minimum of pulse durations), and the LCM is the temporal union (componentwise maximum). The information conservation law $\sigma(a) + \sigma(b) = \sigma(\gcd(a,b)) + \sigma(\operatorname{lcm}(a,b))$ from [3] becomes conservation of total pulse energy. No gates, no interference, and no computation are required — the physics of overlapping wave packets performs the lattice operations directly.

For computation beyond lattice operations (arbitrary $q$-state functions), we show that the multi-wavelength encoding resolves the exponential scaling problem of the single-wavelength architecture in [4]: $k$ inputs require $O(k)$ wave sources (linear) rather than $O(q^k)$ (exponential), at the cost of requiring nonlinear frequency mixing for multi-input interactions. Feedback via fibre loops produces counters and oscillators whose periods are determined by the gate function, with the system's recurrence time equal to the primorial of the gate periods — an emergent, self-encoded clock.

We connect the encoding to the knowledge framework of [5]: the choice of wavelength channels is a *knowledge investment* analogous to the choice of number base. Operations involving pre-invested primes (those with assigned wavelengths) are free — linear wave physics. Operations involving non-invested primes require nonlinear interaction — the energetic cost of accessing structure not pre-encoded. The total information is conserved across the encoding; only its *form* changes.

**Keywords:** information spectrum, wavelength division, prime encoding, pulse duration, GCD, LCM, fibre loop feedback, knowledge investment, multi-wavelength computation

**MSC (2020):** 94A15, 11A25, 78A60, 42A38

---

## 1. Introduction

### 1.1 The Problem

The wave computation architecture of [4] encodes multi-state inputs as residues modulo a prime $m$, with $\varphi(m)$ Dirichlet characters serving as wave sources. For $k$ inputs of $q$ states each, the modulus must satisfy $m > \prod_{i=1}^k p_i^{q-1}$, giving $\varphi(m) \sim q^k$ wave sources — exponential in the number of inputs. This is the principal practical limitation identified in [4, Remark 4.3].

Simultaneously, the information spectrum of [3] decomposes the self-information $\ln(n)$ into independent prime dimensions $\sigma_p(n) = v_p(n) \cdot \ln(p)$, with the key structural properties that the GCD corresponds to the componentwise minimum and the LCM to the componentwise maximum of the spectra. This decomposition is the unique continuous structured refinement of Shannon's self-information compatible with the multiplicative structure of the integers.

This paper shows that the information spectrum has a *direct physical realisation* as a multi-wavelength pulse packet, and that this realisation simultaneously resolves the scaling problem and provides a physical mechanism for the lattice operations.

### 1.2 Summary of Results

1. **Spectral-temporal encoding** (Section 3): The integer $n = \prod_p p^{a_p}$ is encoded as a wave packet with one wavelength channel per prime and pulse duration proportional to the exponent. The encoding is faithful: distinct integers produce physically distinguishable wave packets.

2. **GCD and LCM as physical measurements** (Section 4): Temporal overlap of two wave packets computes the GCD spectrum; temporal union computes the LCM spectrum. The conservation law becomes energy conservation.

3. **Linear scaling** (Section 5): $k$ inputs of $q$ states require $O(k \cdot \varphi(m_0))$ sources, where $m_0$ is a fixed modulus per channel — linear in $k$.

4. **Knowledge investment** (Section 6): The choice of wavelength channels is a pre-investment of knowledge about specific primes. Operations on invested primes are free (linear optics); operations on non-invested primes require nonlinear interaction.

5. **Feedback and the emergent clock** (Section 7): Fibre loop feedback produces oscillators and counters. The system's recurrence time is the primorial of the individual gate periods — an emergent clock whose frequency encodes the prime structure.

### 1.3 Relation to Prior Work

This paper unifies [3] (the information spectrum), [4] (the wave computation architecture), and [5] (the geometry of knowing). It draws on [1] (the logarithmic isomorphism) as the algebraic foundation and [2] (the master equation) for the Boolean computation framework. The multi-wavelength encoding is physically standard — wavelength division multiplexing (WDM) is the backbone of modern telecommunications [9]. The novel contribution is the interpretation of WDM channels as prime coordinate dimensions, with pulse duration encoding prime exponents.

---

## 2. Background

### 2.1 The Information Spectrum ([3])

For a positive integer $n = \prod_p p^{a_p}$, the information spectrum is $\sigma(n) : \text{Primes} \to \mathbb{R}_{\geq 0}$ defined by $\sigma_p(n) = v_p(n) \cdot \ln(p)$. The total self-information is $h(1/n) = \ln(n) = \sum_p \sigma_p(n)$. The spectrum satisfies:

- **Additivity**: $\sigma(ab) = \sigma(a) + \sigma(b)$ (componentwise).
- **Overlap**: $\sigma(\gcd(a,b)) = \min(\sigma(a), \sigma(b))$, $\sigma(\operatorname{lcm}(a,b)) = \max(\sigma(a), \sigma(b))$.
- **Conservation**: $\sigma(a) + \sigma(b) = \sigma(\gcd(a,b)) + \sigma(\operatorname{lcm}(a,b))$.

### 2.2 The Wave Computation Architecture ([4])

The generalised master equation computes $y(x) = \sum_j \hat{F}_j \cdot \chi_j(x \bmod m)$, where $\chi_j$ are Dirichlet characters mod $m$ and $\hat{F}_j$ are Fourier coefficients encoding the target function. The polynomial cascade theorem shows that gate outputs can be fed into subsequent gates via polynomial evaluation: degree $q-1$ in the complex amplitude, with binary cascading being purely linear.

### 2.3 The Geometry of Knowing ([5])

The factorisation of $n$ into a prime hypergrid is a geometric reorganisation of information: $n$ dots on a line are reshaped into a $k$-dimensional grid with perpendicular axes corresponding to prime factors. The logarithm converts grid side lengths into information coordinates, preserving perpendicularity. The forward map (dots $\to$ grid $\to$ spectrum) is unique; the reverse map is degenerate (requiring an orientation choice). Moving from quantitative to qualitative representation conserves information but costs knowledge.

---

## 3. The Spectral-Temporal Encoding

### 3.1 Definition

**Definition 3.1 (Spectral-Temporal Wave Packet).** Let $\mathcal{P} = \{p_1, p_2, \ldots, p_K\}$ be a finite set of primes (the *invested primes*). For each $p_i \in \mathcal{P}$, assign a distinct carrier wavelength $\lambda_{p_i}$. Let $\tau > 0$ be a base time unit.

The *wave encoding* of a positive integer $n$ with prime factorisation supported on $\mathcal{P}$ (i.e., all prime factors of $n$ lie in $\mathcal{P}$) is the multi-wavelength pulse packet:

$$W_n(t) = \sum_{p \in \mathcal{P}} A_p \cdot \Pi\!\left(\frac{t}{v_p(n) \cdot \tau}\right) \cdot e^{i(2\pi c/\lambda_p) t + \phi_p}$$

where:
- $A_p$ is the amplitude in channel $\lambda_p$ (uniform across channels for encoding; variable for computation),
- $\Pi(t/T)$ is the rectangular pulse of duration $T$: $\Pi(t/T) = 1$ for $0 \leq t < T$, and $0$ otherwise,
- $v_p(n)$ is the exponent of $p$ in the factorisation of $n$,
- $\phi_p$ is a phase encoding the computational state in channel $p$ (from the character framework of [4]).

Each channel carries:
- **Wavelength** $\lambda_p$: identifies *which* prime.
- **Pulse duration** $v_p(n) \cdot \tau$: encodes *what exponent*.
- **Phase** $\phi_p$: encodes computational state (from the character framework of [4]).

### 3.2 Faithfulness

**Theorem 3.2 (Faithful Encoding).** Distinct positive integers with prime support in $\mathcal{P}$ produce physically distinguishable wave packets.

*Proof.* If $n \neq n'$, then by the Fundamental Theorem of Arithmetic, there exists a prime $p \in \mathcal{P}$ with $v_p(n) \neq v_p(n')$. The pulse durations in channel $\lambda_p$ differ: $v_p(n) \cdot \tau \neq v_p(n') \cdot \tau$. The duration of a pulse is a physically measurable quantity (by any time-resolved detector). $\square$

### 3.3 The Wave Packet as Information Spectrum

**Theorem 3.3 (Physical Realisation of the Spectrum).** The measurable properties of the wave packet $W_n$ directly encode the information spectrum $\sigma(n)$:

$$\sigma_p(n) = v_p(n) \cdot \ln(p) = \frac{\text{pulse duration in channel } \lambda_p}{\tau} \cdot \ln(p).$$

The total self-information is:

$$\ln(n) = \sum_{p \in \mathcal{P}} \sigma_p(n) = \sum_p \frac{T_p}{\tau} \cdot \ln(p)$$

where $T_p$ is the measured pulse duration in channel $\lambda_p$.

The information spectrum, which [3] defined as a mathematical decomposition, is now a *physical measurement*: set up a spectrograph (prism or diffraction grating) to separate wavelength channels, measure the pulse duration in each channel, and the resulting vector is $\sigma(n)$.

### 3.4 The Grid Interpretation

From [5], the integer $n$ can be viewed as a $k$-dimensional hypergrid with side length $p^{v_p}$ along each prime axis. The wave encoding maps this grid to spacetime: the grid's prime axes become wavelength channels (spectral dimension), and the grid's side lengths become pulse durations (temporal dimension). The perpendicularity of prime axes in the abstract grid corresponds to the physical independence of wavelength channels (different wavelengths do not interfere in linear media).

---

## 4. GCD and LCM as Physical Measurements

### 4.1 Temporal Overlap Computes GCD

**Theorem 4.1.** Let $W_a$ and $W_b$ be wave encodings of integers $a$ and $b$, launched simultaneously (both starting at $t = 0$). In each wavelength channel $\lambda_p$, the time window during which *both* pulses are present has duration:

$$T_p^{\cap} = \min(v_p(a), v_p(b)) \cdot \tau.$$

The integer whose spectrum matches these durations is $\gcd(a, b)$.

*Proof.* Two rectangular pulses of durations $v_p(a) \cdot \tau$ and $v_p(b) \cdot \tau$, both starting at $t = 0$, overlap for $\min(v_p(a), v_p(b)) \cdot \tau$. By [3, Theorem 5.1], $v_p(\gcd(a,b)) = \min(v_p(a), v_p(b))$ for every prime $p$. $\square$

**Physical implementation.** A photodetector gated by the logical AND of the two pulses in each channel measures the overlap duration. No arithmetic is performed — the GCD is read directly from the temporal overlap.

### 4.2 Temporal Union Computes LCM

**Theorem 4.2.** The time window during which *at least one* pulse is present in channel $\lambda_p$ has duration:

$$T_p^{\cup} = \max(v_p(a), v_p(b)) \cdot \tau.$$

The integer whose spectrum matches these durations is $\operatorname{lcm}(a, b)$.

*Proof.* Two rectangular pulses starting at $t = 0$ have union $\max(v_p(a), v_p(b)) \cdot \tau$. By [3, Theorem 5.1], $v_p(\operatorname{lcm}(a,b)) = \max(v_p(a), v_p(b))$. $\square$

### 4.3 Conservation of Energy

**Theorem 4.3 (Energy Conservation = Information Conservation).** For simultaneous wave encodings of $a$ and $b$:

$$\sum_p T_p^{(a)} + \sum_p T_p^{(b)} = \sum_p T_p^{\cap} + \sum_p T_p^{\cup}$$

That is, the total pulse duration across all channels is conserved when two wave packets are decomposed into their overlap and union.

*Proof.* For each prime $p$: $v_p(a) + v_p(b) = \min(v_p(a), v_p(b)) + \max(v_p(a), v_p(b))$, which is the identity $x + y = \min(x,y) + \max(x,y)$ for non-negative reals. Multiplying by $\tau$ and summing over all primes gives the result. This is the information conservation law $\sigma(a) + \sigma(b) = \sigma(\gcd) + \sigma(\operatorname{lcm})$ from [3], with pulse durations replacing information components. $\square$

**Interpretation.** If pulse amplitude is uniform across channels, the total energy (proportional to total duration) is conserved exactly when two wave packets are separated into their shared and combined components. Information conservation *is* energy conservation under the spectral-temporal encoding.

---

## 5. Resolution of the Scaling Problem

### 5.1 Single-Wavelength Scaling (the Problem)

In the architecture of [4], $k$ inputs are encoded as $\prod_{i=1}^k p_i^{A_i} \bmod m$ for a single modulus $m$. The modulus must distinguish all $q^k$ possible input combinations, requiring $m > \prod_{i=1}^k p_i^{q-1}$, which grows exponentially in $k$.

### 5.2 Multi-Wavelength Scaling (the Solution)

With the spectral-temporal encoding, each input $A_i$ is assigned its own wavelength channel $\lambda_{p_i}$. Within each channel, the state of input $i$ is encoded via the character framework of [4] using a fixed, small modulus $m_0$ (e.g., $m_0 = 7$ for ternary, giving $\varphi(7) = 6$ sources per channel).

**Theorem 5.1 (Linear Scaling).** $k$ inputs of $q$ states each require $k \cdot \varphi(m_0)$ wave sources in total, where $m_0$ depends only on $q$, not on $k$.

*Proof.* Each input occupies an independent wavelength channel with $\varphi(m_0)$ sources. Different wavelengths do not interfere in linear media, so the channels are physically independent. The total source count is $k \cdot \varphi(m_0)$, which is $O(k)$. $\square$

### 5.3 The Interaction Cost

The linear scaling comes with a trade-off: computing functions that depend on *multiple* inputs (e.g., AND($A$, $B$)) requires interaction between wavelength channels. In linear optics, different wavelengths pass through each other without interacting. Interaction requires nonlinear optical processes:

- **Sum-frequency generation (SFG)**: $\omega_A + \omega_B \to \omega_C$
- **Difference-frequency generation (DFG)**: $\omega_A - \omega_B \to \omega_D$
- **Four-wave mixing (FWM)**: $\omega_A + \omega_B - \omega_C \to \omega_D$

These are well-established processes in nonlinear optics [10], but each introduces a nonlinear crystal and associated efficiency losses. The trade-off is: exponential source count (single-wavelength) vs. linear source count with nonlinear interaction stages (multi-wavelength).

For functions of a single input per channel, no nonlinear interaction is needed — the full character framework of [4] operates independently in each channel using only linear optics.

---

## 6. Knowledge Investment

### 6.1 The Base Analogy

In the positional number system base $b$, the factors of $b$ are *pre-invested*: divisibility by any factor of $b$ is immediately visible from the representation (the last digit), at no computational cost. Divisibility by primes not dividing $b$ requires work — trial division or equivalent.

The spectral-temporal encoding makes the same trade-off in the physical domain.

**Definition 6.1 (Knowledge Investment).** The set of invested primes $\mathcal{P} = \{p_1, \ldots, p_K\}$ — those assigned wavelength channels — constitutes the system's *knowledge investment*. The investment is made once (when the optical hardware is configured) and persists for all subsequent computations.

### 6.2 Free and Costly Operations

**Theorem 6.2.** Let $n$ be an integer with prime support in $\mathcal{P}$. The following operations on the wave encoding of $n$ are *free* (require only linear optics and temporal measurement):

1. Reading any component $\sigma_p(n)$ (measure pulse duration in channel $\lambda_p$).
2. Computing $\gcd(a, b)$ for any $a, b$ with support in $\mathcal{P}$ (temporal overlap).
3. Computing $\operatorname{lcm}(a, b)$ (temporal union).
4. Testing coprimality $\gcd(a, b) = 1$ (no temporal overlap in any channel).
5. Single-input $q$-state functions (character framework per channel).
6. Feedback / counting (fibre loop with phase shift per channel).

The following operations are *costly* (require nonlinear optical interaction):

1. Multi-input functions (AND, OR across different inputs at different wavelengths).
2. Accessing primes not in $\mathcal{P}$ (require generating new wavelength channels via frequency conversion).

### 6.3 Conservation of Information Across Encoding

The spectral-temporal encoding conserves information in the sense of [5, Section 1]: the total information $\ln(n) = \|\sigma(n)\|_1$ is preserved; only its physical form changes — from an abstract number to a measurable wave packet. The knowledge investment $\mathcal{P}$ determines *which* aspects of the structure are directly accessible (the invested prime dimensions) and which require additional work (non-invested primes or cross-channel interactions).

This is the physical realisation of the central observation of [5]: moving from the quantitative extreme (n dots) toward the qualitative extreme (the spectrum) costs knowledge but conserves information.

---

## 7. Feedback and the Emergent Clock

### 7.1 Single-Channel Feedback

The polynomial cascade theorem of [4, Section 6] shows that a gate's self-feedback is a polynomial in the complex amplitude. For cyclic permutation gates (INCREMENT, DECREMENT), the self-cascade polynomial reduces to degree 1 — a pure phase rotation:

$$z \mapsto \omega_q \cdot z$$

where $\omega_q = e^{2\pi i / q}$ is the primitive $q$-th root of unity. Physically, this is a fibre loop with an additional path length of $\lambda_p / q$, producing a phase shift of $2\pi/q$ per transit.

**Result.** A fibre loop carrying wavelength $\lambda_p$ with a $q$-state INCREMENT gate produces a counter with period $q$: the phase cycles through $0, 2\pi/q, 4\pi/q, \ldots, 2\pi(q-1)/q, 0, \ldots$ The feedback requires no nonlinear elements, no detection, and no electronics.

### 7.2 Multi-Channel Feedback: The Primorial Clock

When multiple wavelength channels share a single fibre loop, each channel cycles independently at its own rate:

- Channel $\lambda_{p_1}$ with $q_1$-state gate: period $q_1$ transits.
- Channel $\lambda_{p_2}$ with $q_2$-state gate: period $q_2$ transits.
- Channel $\lambda_{p_k}$ with $q_k$-state gate: period $q_k$ transits.

**Theorem 7.1 (Emergent Clock).** The system's recurrence time — the number of loop transits after which *all* channels simultaneously return to their initial state — is:

$$T_{\text{recurrence}} = \operatorname{lcm}(q_1, q_2, \ldots, q_k).$$

When the gate periods $q_i$ are distinct primes, $T_{\text{recurrence}} = q_1 \cdot q_2 \cdots q_k$ (the primorial of the gate periods).

*Proof.* Each channel returns to its initial state after $q_i$ transits. All channels simultaneously return when the transit count is divisible by every $q_i$, i.e., at $\operatorname{lcm}(q_1, \ldots, q_k)$. For distinct primes, $\operatorname{lcm} = \prod$. $\square$

**Interpretation.** The clock is not imposed externally — it *emerges* from the prime structure of the computation. The loop transit time determines the base frequency; the gate periods determine the harmonic structure. The primorial gives the fundamental period of the composite system. This is a physical system whose timing encodes the prime factorisation of its own period.

### 7.3 Noise Tolerance

Computational verification (Section 9) shows that the ternary INCREMENT feedback loop tolerates phase noise of $\sigma \approx 0.05$ radians per pass ($\approx 3°$) for 200+ error-free iterations. The noise margin is $\pm \pi/q$ per state (±60° for ternary, ±90° for binary). Phase noise accumulates as a random walk with standard deviation $\sigma\sqrt{N}$ after $N$ iterations, giving an error-free horizon of approximately $N_{\max} \approx (\pi/q)^2 / \sigma^2$ iterations.

---

## 8. The Five-Layer Correspondence

The spectral-temporal encoding adds a fifth layer to the four-layer framework of [1]:

| Layer | Integer $n$ | GCD | LCM | Complement |
|-------|-------------|-----|-----|------------|
| Natural language | The number $n$ | Shared factors | Combined factors | Non-factors |
| Inverse integer | $1/n$ | $1/\gcd(a,b)$ | $1/\operatorname{lcm}(a,b)$ | $(n-1)/n$ |
| Resistance | $\Omega_n = \ln(n)$ | $\Omega_{\gcd}$ | $\Omega_a + \Omega_b - \Omega_{\gcd}$ | Phase interference |
| Prime coordinates | $(v_2, v_3, v_5, \ldots)$ | $\min(v_a, v_b)$ | $\max(v_a, v_b)$ | Not closed |
| **Wave packet** | **Multi-$\lambda$ pulse** | **Temporal overlap** | **Temporal union** | **Destructive interference** |

The fifth layer is the first that is *directly physical*: the operations are not mathematical abstractions but measurable properties of electromagnetic waves in spacetime.

---

## 10. Computational Verification

### 9.1 GCD/LCM via Temporal Overlap

We verified the temporal overlap/union computation for the integers $a = 72 = 2^3 \times 3^2$ and $b = 108 = 2^2 \times 3^3$:

| Channel | $v_p(72)$ | $v_p(108)$ | Overlap (min) | Union (max) | $v_p(\gcd)$ | $v_p(\operatorname{lcm})$ |
|---------|-----------|------------|---------------|-------------|-------------|--------------------------|
| $\lambda_2$ | 3 | 2 | 2 | 3 | 2 ✓ | 3 ✓ |
| $\lambda_3$ | 2 | 3 | 2 | 3 | 2 ✓ | 3 ✓ |

$\gcd(72, 108) = 2^2 \times 3^2 = 36$ ✓. $\operatorname{lcm}(72, 108) = 2^3 \times 3^3 = 216$ ✓.

Conservation: $(3+2) + (2+3) = (2+2) + (3+3)$: $10 = 10$ ✓.

### 9.2 Feedback Verification

The ternary INCREMENT self-feedback loop was verified for 200 iterations from each starting state, producing perfect cycling ($0 \to 1 \to 2 \to 0 \to \cdots$) with zero errors in the ideal case and zero errors with phase noise $\sigma = 0.05$ rad/pass. The cascade polynomial is $z \mapsto \omega_3 \cdot z$ (degree 1, linear), requiring only a fixed $120°$ phase shift per loop transit.

All 49 compositions of named ternary gates (IDENTITY, INCREMENT, DECREMENT, NEGATE, CONST\_0, CONST\_1, CONST\_2) via the cascade polynomial were verified correct.

---

## 11. Discussion

### 10.1 What Is New

The individual ingredients — wavelength division multiplexing, pulse duration encoding, Dirichlet character computation, fibre loop feedback — are all established technologies. The contribution is the *framework* that unifies them via the information spectrum: the recognition that the prime coordinate decomposition of a number has a direct physical realisation as a multi-wavelength pulse, and that this realisation makes the divisibility lattice operations free.

### 10.2 The Knowledge Hierarchy

The spectral-temporal encoding makes explicit a hierarchy of knowledge investment:

1. **No investment** (unary): the number is $n$ dots. All operations cost $O(n)$. No structure is exploited.
2. **Base investment** (positional): the number is written in base $b$. Divisibility by factors of $b$ is free. Other divisibility costs work.
3. **Full spectral investment** (wave encoding): each prime has a wavelength channel. All GCD/LCM operations are free (temporal overlap/union). Cross-channel functions cost nonlinear interaction.
4. **Computation investment** (character programming): Fourier coefficients encode specific gate functions. Arbitrary $q$-state computation is free (wave interference). Changing the function costs reprogramming.

Each level invests more knowledge and makes more operations free. The total information is conserved across all levels — only the balance between "known" and "unknown" structure shifts.

### 10.3 Limitations

1. **Bandwidth**: Each wavelength channel requires physical bandwidth for its pulse. The number of channels is limited by the optical bandwidth of the medium and the minimum channel spacing (determined by the pulse duration via the time-bandwidth product $\Delta f \cdot \Delta t \geq 1/2$).

2. **Dispersion**: Different wavelengths travel at different speeds in dispersive media (optical fibre). This causes pulses in different channels to drift apart temporally. While this can be compensated (dispersion compensation is standard in telecommunications), it complicates the temporal overlap measurement. Alternatively, dispersion can be *exploited*: it naturally separates channels in time, simplifying sequential readout.

3. **Nonlinear interaction efficiency**: Cross-channel computation via frequency mixing has limited efficiency (typically $10^{-4}$ to $10^{-2}$ in standard nonlinear crystals). Cascaded nonlinear operations lose signal rapidly without amplification.

4. **No Turing completeness**: As with [4], the architecture provides functional completeness for combinational logic and simple sequential elements (counters, oscillators). Full Turing computation requires conditional feedback (latches, registers), which is not addressed here.

### 10.4 Open Problems

1. **Nonlinear gate design**: Can the character framework be extended to design specific nonlinear interactions that implement multi-input gates across wavelength channels? The frequency structure of the output (sum/difference frequencies) encodes prime *sums* rather than products — connecting to additive, rather than multiplicative, number theory.

2. **Dispersion as computation**: Can the velocity difference between wavelength channels be exploited to create time-dependent overlap patterns that perform computation during propagation?

3. **Optical bistability for latches**: Can a nonlinear resonator with multiple stable modes (one per computational state) serve as a $q$-state latch, completing the path to sequential logic?

4. **The time-bandwidth limit**: The pulse duration encodes the exponent $v_p(n)$, but shorter pulses have wider bandwidth, potentially overlapping adjacent wavelength channels. What is the maximum information density (bits per second per unit bandwidth) achievable under this encoding?

5. **Connection to the Riemann zeta function**: The wave packet for $n$ has total energy proportional to $\ln(n) = \sum_p \sigma_p(n)$. The expected energy for a "random" integer relates to $\zeta(s)$ via the Euler product. Does the physical wave system exhibit spectral properties related to the zeta zeros?

---

## References

[1] A. Pisani, "A unified algebraic framework for number theory, Boolean logic, and circuit topology via the logarithmic isomorphism," 2026.

[2] A. Pisani, "The Natural Operating System: Boolean computation via Möbius inversion and prime-encoded databases," 2026.

[3] A. Pisani, "Structured self-information: A prime coordinate decomposition of Shannon's information measure," 2026.

[4] A. Pisani and Claude (Anthropic), "Multi-state wave computation via Dirichlet characters: A generalisation of the Möbius interference architecture," 2026.

[5] A. Pisani, "The geometry of knowing: From dots to dimensions," 2026 (working notes).

[6] C. E. Shannon, "A mathematical theory of communication," *Bell System Technical Journal*, vol. 27, no. 3, pp. 379–423, 1948.

[7] Y. Shen et al., "Deep learning with coherent nanophotonic circuits," *Nature Photonics*, vol. 11, pp. 441–446, 2017.

[8] E. L. Post, "Introduction to a general theory of elementary propositions," *Amer. J. Math.*, vol. 43, no. 3, pp. 163–185, 1921.

[9] G. P. Agrawal, *Fiber-Optic Communication Systems*, 4th ed., Wiley, 2010.

[10] R. W. Boyd, *Nonlinear Optics*, 3rd ed., Academic Press, 2008.

---

## Appendix A: Notation

| Symbol | Meaning |
|--------|---------|
| $\mathcal{P}$ | Set of invested primes (assigned wavelength channels) |
| $\lambda_p$ | Carrier wavelength assigned to prime $p$ |
| $\tau$ | Base time unit for pulse duration |
| $v_p(n)$ | Exponent of $p$ in factorisation of $n$ |
| $\sigma_p(n)$ | Information spectrum component: $v_p(n) \cdot \ln(p)$ |
| $W_n(t)$ | Wave encoding of integer $n$ |
| $T_p^{\cap}$ | Overlap duration in channel $\lambda_p$ (encodes $v_p(\gcd)$) |
| $T_p^{\cup}$ | Union duration in channel $\lambda_p$ (encodes $v_p(\operatorname{lcm})$) |
| $T_{\text{recurrence}}$ | System recurrence time (primorial of gate periods) |
| $m_0$ | Fixed modulus per wavelength channel |
| $\omega_q$ | Primitive $q$-th root of unity |
