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

# A Unified Algebraic Framework for Number Theory, Boolean Logic, and Circuit Topology via the Logarithmic Isomorphism

**Alexander Pisani**

a.h.pisani.research@gmail.com

March 2026

---

## Abstract

The logarithm $\Omega(1/n) = \ln(n)$ establishes a monoid isomorphism from inverse integers under multiplication to non-negative reals under addition. This isomorphism, combined with the divisibility lattice and prime coordinate vectors, reveals that number-theoretic operations (GCD, LCM, prime factorisation), Boolean logic (AND, OR, NOT), and informational resistance topology (series combination, inclusion-exclusion) are instances of a single abstract algebraic structure.

We present a four-layer framework — natural language, inverse integers, resistance, and prime coordinate vectors — in which a proof in one layer translates mechanically to proofs in the others. As a centrepiece demonstration, we derive the coprimality probability $6/\pi^2$ simultaneously through all four layers. We further show that relational database operations (intersection, union, difference) map exactly to the same lattice structure, and that the framework accommodates Turing completeness via classical Gödel encoding of counter machines.

The individual results are classical. The contribution of this paper is the framework itself: a unified algebraic lens through which the structural parallels among these domains become transparent.

**Keywords:** logarithmic isomorphism, monoid homomorphism, divisibility lattice, Boolean algebra, prime coordinates, coprimality, Gödel numbering

**MSC (2020):** 11A25, 06D99, 03G05, 94C10

---

## 1. Introduction

It has long been observed that certain operations in number theory, Boolean logic, and circuit analysis share structural similarities. The logarithm converts multiplication to addition — a fact known since Napier [1]. The positive integers under divisibility form a distributive lattice with GCD as meet and LCM as join — a standard result in lattice theory since Birkhoff [2]. Boolean algebras are themselves distributive lattices. And Gödel's encoding of syntax into arithmetic [3] demonstrated that number-theoretic operations can simulate logical computation.

These observations, while individually well-established, are typically treated as belonging to separate mathematical traditions. The purpose of this paper is to show that they are all manifestations of a *single* algebraic structure, made visible by a systematic change of representation.

The key object is the set of **inverse integers** $\mathcal{I} = \{1/n : n \in \mathbb{Z}^+\}$ equipped with multiplication, and the mapping $\Omega(1/n) = \ln(n)$, which is a monoid isomorphism from $(\mathcal{I}, \times)$ to $(\ln(\mathbb{Z}^+), +)$. This mapping is unique up to multiplicative constant by Cauchy's functional equation [4]. Under this isomorphism, we establish a four-layer correspondence:

1. **Natural language** — set-theoretic and logical descriptions.
2. **Inverse integers** — arithmetic operations on $\mathcal{I}$.
3. **Resistance** — additive informational costs, following the terminology of self-information from information theory [5].
4. **Prime coordinate vectors** — operations in the vector space spanned by $\{\ln(p) : p \text{ prime}\}$.

A proof given in any one layer translates mechanically to the others. We demonstrate this with a detailed four-layer derivation of the coprimality probability $P(\gcd(a,b) = 1) = 6/\pi^2$ (Section 5), and exhibit the lattice-theoretic structure underlying both number-theoretic and relational database operations (Section 6). We further show that the framework naturally accommodates Turing completeness via Minsky's counter machines [6] encoded by Gödel numbering (Section 7).

**What this paper is not.** We do not claim new theorems. The individual results — the logarithmic homomorphism, the divisibility lattice, the coprimality formula, the Turing completeness of counter machines — are all classical. The contribution is the *framework*: a unified presentation that makes the structural parallels among these domains explicit, together with a four-layer proof methodology that provides independent verification of results across representations.

### 1.1 Organisation

Section 2 establishes the fundamental mapping and its uniqueness. Section 3 develops the Boolean operations (AND, OR, NOT) within the framework, with an honest discussion of the algebraic cost of complement. Section 4 introduces the prime coordinate vector space. Section 5 presents the four-layer coprimality proof. Section 6 covers database operations and the distributive lattice structure. Section 7 establishes Turing completeness via counter machine simulation. Section 8 characterises primes as irreducible elements. Section 9 discusses the framework's scope and connections to the zeta function.

---

## 2. The Fundamental Mapping

### 2.1 Inverse Integers

**Definition 2.1.** An *inverse integer* is a number of the form $1/n$ where $n \in \mathbb{Z}^+$. The set of inverse integers is denoted $\mathcal{I} = \{1/n : n \in \mathbb{Z}^+\} \subset (0, 1]$.

Every inverse integer inherits unique prime factorisation from its denominator:
$$\frac{1}{n} = \frac{1}{p_1^{a_1} \cdot p_2^{a_2} \cdots p_k^{a_k}}.$$

The set $\mathcal{I}$ is a commutative monoid under multiplication with identity $1/1 = 1$, since $\frac{1}{a} \cdot \frac{1}{b} = \frac{1}{ab} \in \mathcal{I}$ for all $a, b \in \mathbb{Z}^+$.

### 2.2 Informational Resistance

**Definition 2.2 (Informational Resistance).** For an inverse integer $1/n$, the *informational resistance* is
$$\Omega(1/n) := \ln(n).$$

We write $\Omega_a$ as shorthand for $\Omega(1/a) = \ln(a)$.

**Remark.** The quantity $\ln(n) = -\ln(1/n)$ is the self-information of an event with probability $1/n$, measured in nats [5]. This connection to information theory motivates the "resistance" terminology: $\Omega_a$ measures the informational cost of the event $1/a$, and costs combine additively under independent conjunction, just as resistances combine in series in a circuit.

### 2.3 The Isomorphism Theorem

**Theorem 2.3 (Monoid Isomorphism).** The map $\Omega \colon \mathcal{I} \to \ln(\mathbb{Z}^+)$ defined by $\Omega(1/n) = \ln(n)$ is a monoid isomorphism from $(\mathcal{I}, \times)$ to $(\ln(\mathbb{Z}^+), +)$. That is:
$$\Omega\!\left(\frac{1}{a} \cdot \frac{1}{b}\right) = \Omega\!\left(\frac{1}{a}\right) + \Omega\!\left(\frac{1}{b}\right).$$

*Proof.* $\Omega(1/(ab)) = \ln(ab) = \ln(a) + \ln(b) = \Omega(1/a) + \Omega(1/b)$. The map is bijective: for each $\ln(n) \in \ln(\mathbb{Z}^+)$, the unique preimage is $1/n$. The identity $1/1$ maps to $\ln(1) = 0$. $\square$

### 2.4 Uniqueness

**Theorem 2.4 (Uniqueness, Cauchy [4]).** Any continuous function $f \colon (0, 1] \to \mathbb{R}$ satisfying $f(xy) = f(x) + f(y)$ for all $x, y \in (0,1]$ has the form $f(x) = c \cdot \ln(x)$ for some constant $c$.

*Proof.* This is Cauchy's logarithmic functional equation. Under the continuity hypothesis (or indeed measurability, or monotonicity), the unique solutions are $f(x) = c \cdot \ln(x)$. See Aczél [4], Theorem 1.4.1. $\square$

**Corollary 2.5.** The informational resistance mapping $\Omega(1/n) = \ln(n)$ is forced (up to positive scale) by the requirement that series combination be additive.

### 2.5 Series Combination

When two inverse integers combine multiplicatively, their resistances add:
$$\frac{1}{a} \cdot \frac{1}{b} = \frac{1}{ab}, \qquad \Omega_{ab} = \Omega_a + \Omega_b.$$

This is the direct analogue of series resistance in electrical circuits, and of the additivity of self-information for independent events.

---

## 3. Boolean Operations

In this section we show that the classical Boolean operations AND, OR, NOT have natural expressions within the framework, using the restriction to *squarefree* integers as set encodings.

### 3.1 Set Encoding

**Definition 3.1.** A *squarefree integer* is a positive integer with no repeated prime factors. Sets are encoded as squarefree integers: each element maps to a distinct prime, and presence of the element in the set corresponds to the prime dividing the encoding integer.

*Example.* With the assignment $a \mapsto 2$, $b \mapsto 3$, $c \mapsto 5$: the set $\{a, b\}$ is encoded as $6 = 2 \times 3$; the set $\{a, c\}$ as $10 = 2 \times 5$; the full set $\{a, b, c\}$ as $30 = 2 \times 3 \times 5$.

### 3.2 AND (Intersection via GCD)

**Theorem 3.2 (AND = GCD).** For squarefree integers $a, b$ encoding sets $A, B$:
$$A \cap B \text{ is encoded by } \gcd(a, b).$$

In resistance terms:
$$\Omega_{\gcd} = \Omega_{\text{AND}}.$$

*Proof.* A prime $p$ divides $\gcd(a,b)$ if and only if $p \mid a$ and $p \mid b$, i.e., the corresponding element is in both $A$ and $B$. $\square$

For inverse integers representing independent probabilities, AND corresponds to multiplication: $P(A \wedge B) = P(A) \cdot P(B) = \frac{1}{a} \cdot \frac{1}{b} = \frac{1}{ab}$, with resistance $\Omega_a + \Omega_b$ (series combination).

### 3.3 OR (Union via LCM)

**Theorem 3.3 (Union Formula).** For squarefree integers $a, b$ encoding sets $A, B$:
$$A \cup B \text{ is encoded by } \operatorname{lcm}(a,b).$$

The resistance of the union satisfies:
$$\Omega_{\operatorname{lcm}} = \Omega_a + \Omega_b - \Omega_{\gcd}.$$

*Proof.* A prime $p$ divides $\operatorname{lcm}(a,b)$ if and only if $p \mid a$ or $p \mid b$. The resistance formula follows from the fundamental identity $\operatorname{lcm}(a,b) \cdot \gcd(a,b) = a \cdot b$. Taking logarithms: $\ln(\operatorname{lcm}) + \ln(\gcd) = \ln(a) + \ln(b)$, hence $\Omega_{\operatorname{lcm}} = \Omega_a + \Omega_b - \Omega_{\gcd}$. $\square$

**Remark.** The formula $\Omega_{\operatorname{lcm}} = \Omega_a + \Omega_b - \Omega_{\gcd}$ is the resistance-layer expression of the inclusion-exclusion principle: $|A \cup B| = |A| + |B| - |A \cap B|$.

### 3.4 NOT (Complement)

The complement of $1/a$ in the interval $(0, 1)$ is defined as:
$$\operatorname{NOT}(1/a) = 1 - 1/a = \frac{a - 1}{a}.$$

**Algebraic closure.** Unlike AND and OR, the NOT operation does *not* preserve the set of inverse integers. The value $(a-1)/a$ is a positive rational in $(0,1)$ but is generally not of the form $1/n$ for any integer $n$. For example, $\operatorname{NOT}(1/3) = 2/3$, which is not an inverse integer.

This is a genuine structural feature, not a defect to be hidden. The monoid $(\mathcal{I}, \times)$ does not support complement; to obtain a Boolean algebra, one must extend the domain to the positive rationals in $(0,1)$ — or, equivalently, work within the lattice of divisors of a fixed integer, where relative complement is well-defined.

In the resistance layer, $\operatorname{NOT}$ corresponds to a subtraction $\Omega_{\operatorname{NOT}} = -\ln(1 - 1/a) = -\ln((a-1)/a)$, which does not decompose as a simple combination of the resistance $\Omega_a$. This reflects the fact that complement is algebraically more complex than conjunction or disjunction in this framework.

### 3.5 Functional Completeness

**Theorem 3.4.** The set $\{\text{AND}, \text{OR}, \text{NOT}\}$ is functionally complete for Boolean logic.

*Proof.* This is a standard result (see, e.g., Sheffer [7]). Any Boolean function can be expressed using AND, OR, and NOT. Equivalently, NAND alone suffices, where $\operatorname{NAND}(A, B) = \operatorname{NOT}(\operatorname{AND}(A, B)) = 1 - 1/\gcd(a,b)$ for coprime indicator inputs. $\square$

### 3.6 Four-Layer Summary

| Layer | AND (Intersection) | OR (Union) | NOT (Complement) |
|-------|-------------------|-----------|-----------------|
| English | $A \cap B$ | $A \cup B$ | $\bar{A}$ |
| Inverse Integer | $1/\gcd(a,b)$ | $1/\operatorname{lcm}(a,b)$ | $(a-1)/a \in \mathbb{Q}^+$ |
| Resistance | $\Omega_{\gcd}$ | $\Omega_a + \Omega_b - \Omega_{\gcd}$ | Phase interference |
| Vector | $\min(\mathbf{v}_a, \mathbf{v}_b)$ | $\max(\mathbf{v}_a, \mathbf{v}_b)$ | (not closed) |

---

## 4. The Prime Coordinate Vector Space

### 4.1 Coordinate Representation

By the Fundamental Theorem of Arithmetic, each $n > 1$ has a unique representation $n = 2^{a_2} \cdot 3^{a_3} \cdot 5^{a_5} \cdots$.

**Definition 4.1 (Prime Coordinate Vector).** The prime coordinate vector of $n$ is
$$\mathbf{v}(n) = (a_2, a_3, a_5, a_7, \ldots)$$
where $a_p$ is the exponent of prime $p$ in the factorisation of $n$. Define $\mathbf{v}(1) = \mathbf{0}$.

*Examples.* $\mathbf{v}(12) = (2, 1, 0, \ldots)$; $\mathbf{v}(35) = (0, 0, 1, 1, 0, \ldots)$.

### 4.2 Linear Independence

**Theorem 4.2.** The set $\{\ln(p) : p \text{ prime}\}$ is linearly independent over $\mathbb{Q}$.

*Proof.* Suppose $\sum_{i=1}^k c_i \ln(p_i) = 0$ with $c_i \in \mathbb{Q}$. Clearing denominators, we may assume $c_i \in \mathbb{Z}$. Then $\ln(\prod p_i^{c_i}) = 0$, so $\prod p_i^{c_i} = 1$. By unique factorisation, each $c_i = 0$. $\square$

**Corollary 4.3.** The resistance $\Omega_n = \ln(n) = \sum_p a_p \ln(p)$ expresses each resistance as a unique linear combination over the basis $\{\ln(p)\}$.

### 4.3 Operations in Vector Space

| Arithmetic Operation | Vector Operation |
|---------------------|-----------------|
| $a \times b$ | $\mathbf{v}(a) + \mathbf{v}(b)$ |
| $\gcd(a, b)$ | $\min(\mathbf{v}(a), \mathbf{v}(b))$ componentwise |
| $\operatorname{lcm}(a, b)$ | $\max(\mathbf{v}(a), \mathbf{v}(b))$ componentwise |

**Theorem 4.4.** The componentwise min and max operations in the vector space correspond exactly to GCD and LCM respectively.

*Proof.* For each prime $p$: the exponent of $p$ in $\gcd(a,b)$ is $\min(a_p, b_p)$, and in $\operatorname{lcm}(a,b)$ is $\max(a_p, b_p)$. This follows directly from the definitions of GCD and LCM via prime factorisation. $\square$

**Remark.** The identity $\operatorname{lcm}(a,b) \cdot \gcd(a,b) = ab$ translates to the vector identity $\max(\mathbf{v}_a, \mathbf{v}_b) + \min(\mathbf{v}_a, \mathbf{v}_b) = \mathbf{v}_a + \mathbf{v}_b$, which holds componentwise.

---

## 5. The Coprimality Theorem: A Four-Layer Proof

The coprimality probability $P(\gcd(a,b) = 1) = 6/\pi^2$ is a classical result due to Euler [8]. We present its derivation simultaneously in all four layers as a demonstration of the framework's unity.

**Theorem 5.1.** Under natural density,
$$P(\gcd(a,b) = 1) = \lim_{N \to \infty} \frac{|\{(a,b) : 1 \le a, b \le N,\; \gcd(a,b) = 1\}|}{N^2} = \frac{6}{\pi^2}.$$

### 5.1 Layer 1: English

Two randomly chosen positive integers are coprime if and only if, for every prime $p$, it is not the case that $p$ divides both. Since divisibility by distinct primes is asymptotically independent, the coprimality probability is the product over all primes of the probability that $p$ does not divide both.

### 5.2 Layer 2: Inverse Integers

For each prime $p$: the probability that $p$ divides a random integer is $1/p$. The probability that $p$ divides both $a$ and $b$ is $1/p^2$. The probability that $p$ does *not* divide both is $1 - 1/p^2$. Therefore:
$$P(\gcd(a,b) = 1) = \prod_{p \text{ prime}} \left(1 - \frac{1}{p^2}\right).$$

### 5.3 Layer 3: Resistance

Each prime $p$ contributes a resistance $\Omega_p = -\ln(1 - 1/p^2)$ in series. The total coprimality resistance is:
$$\Omega_{\text{total}} = \sum_{p \text{ prime}} \left[-\ln\!\left(1 - \frac{1}{p^2}\right)\right] = -\ln\!\left(\prod_p \left(1 - \frac{1}{p^2}\right)\right).$$

### 5.4 Layer 4: Vector Space

Coprime condition: $\min(\mathbf{v}(a), \mathbf{v}(b)) = \mathbf{0}$ (the zero vector). That is, for every prime $p$, at least one of $a, b$ has exponent $0$ at $p$.

### 5.5 Connection to the Zeta Function

By the Euler product [8]:
$$\zeta(s) = \prod_{p \text{ prime}} \frac{1}{1 - p^{-s}}, \qquad \text{Re}(s) > 1.$$

At $s = 2$: $\zeta(2) = \prod_p (1 - p^{-2})^{-1}$. Therefore:
$$\prod_p \left(1 - \frac{1}{p^2}\right) = \frac{1}{\zeta(2)} = \frac{6}{\pi^2}. \qquad \square$$

The four-layer proof illustrates the framework's value: each layer provides an independent verification route, and the final connection to $\zeta(2)$ ties the result to the deep structure of the primes.

---

## 6. Database Operations and the Distributive Lattice

### 6.1 Relational Operations as Number Theory

Using the squarefree encoding of Section 3.1, relational database operations on finite sets correspond directly to number-theoretic operations:

| SQL Operation | Set Operation | Encoding | Vector |
|--------------|--------------|----------|--------|
| `INTERSECT` | $A \cap B$ | $\gcd(a,b)$ | $\min(\mathbf{v}_a, \mathbf{v}_b)$ |
| `UNION` | $A \cup B$ | $\operatorname{lcm}(a,b)$ | $\max(\mathbf{v}_a, \mathbf{v}_b)$ |
| `EXCEPT` | $A \setminus B$ | $a / \gcd(a,b)$ | $\mathbf{v}_a - \min(\mathbf{v}_a, \mathbf{v}_b)$ |

### 6.2 Distributive Lattice Structure

**Theorem 6.1 (Birkhoff [2]).** The positive integers under divisibility form a distributive lattice with meet $\gcd$ and join $\operatorname{lcm}$. That is, for all positive integers $a, b, c$:
$$\gcd(a, \operatorname{lcm}(b, c)) = \operatorname{lcm}(\gcd(a, b), \gcd(a, c)),$$
$$\operatorname{lcm}(a, \gcd(b, c)) = \gcd(\operatorname{lcm}(a, b), \operatorname{lcm}(a, c)).$$

*Proof.* Both identities hold componentwise in prime coordinates: $\min(x, \max(y,z)) = \max(\min(x,y), \min(x,z))$ and $\max(x, \min(y,z)) = \min(\max(x,y), \max(x,z))$ for all non-negative integers $x, y, z$. $\square$

This means that both the number-theoretic operations and the corresponding database operations are instances of the *same* abstract distributive lattice. The four-layer framework makes this correspondence explicit.

### 6.3 Binary–Squarefree Bijection

**Theorem 6.2.** There is a bijection between finite binary strings of length $k$ and squarefree divisors of the $k$-th primorial $p_k\# = 2 \cdot 3 \cdot 5 \cdots p_k$.

*Proof.* Each squarefree divisor of $p_k\#$ corresponds to a subset of $\{p_1, \ldots, p_k\}$, and each subset corresponds to a binary string of length $k$ indicating membership. $\square$

---

## 7. Turing Completeness

The framework accommodates Turing completeness via a classical construction: Gödel numbering applied to Minsky's counter machines. We emphasise that the Turing completeness result is inherited from Minsky [6]; the framework's contribution is showing that the counter machine simulation has natural interpretations in all four layers.

### 7.1 Counter Machines

A two-counter machine has two counters $C_1, C_2 \in \mathbb{Z}_{\ge 0}$, with operations INCREMENT$(C_i)$, DECREMENT$(C_i)$, JUMP-IF-ZERO$(C_i, L)$, and GOTO$(L)$, together with a program counter.

**Theorem 7.1 (Minsky [6]).** Two-counter machines are Turing complete.

### 7.2 Encoding via Gödel Numbering

**Definition 7.2.** The machine state is encoded as a positive integer:
$$\text{State} = 2^{C_1} \cdot 3^{C_2} \cdot p_k$$
where $C_1, C_2$ are counter values and $p_k$ is the $k$-th prime, encoding the program counter at instruction $k$.

### 7.3 Operations in the Four Layers

| Machine Operation | Integer | Resistance | Vector |
|------------------|---------|-----------|--------|
| INCREMENT($C_1$) | $\text{State} \times 2$ | $\Omega \mathrel{+}= \ln 2$ | $\mathbf{v} + (1,0,0,\ldots)$ |
| DECREMENT($C_1$) | $\text{State} / 2$ | $\Omega \mathrel{-}= \ln 2$ | $\mathbf{v} - (1,0,0,\ldots)$ |
| JUMP-IF-ZERO($C_1$) | Test $2 \nmid \text{State}$ | $\Omega_{\text{act}} > 0$? | $v_2 = 0$? |
| GOTO($L$) | $\text{State} \times p_L / p_k$ | $\Omega \mathrel{+}= \ln p_L - \ln p_k$ | Replace $k$-th with $L$-th |

The JUMP-IF-ZERO operation uses a *divisibility gate*: the test $2 \mid \text{State}$ is equivalent to checking whether $\gcd(2, \text{State}) = 2$, which in the resistance layer corresponds to zero activation resistance: $\Omega_{\text{act}}(2, \text{State}) = \ln(2 / \gcd(2, \text{State}))$.

### 7.4 Worked Example: Computing $2 + 3$

*Algorithm:* Decrement $C_2$ and increment $C_1$ until $C_2 = 0$.

*Initial state:* $C_1 = 2$, $C_2 = 3$, program counter at instruction 1 ($p = 5$). State $= 2^2 \cdot 3^3 \cdot 5 = 540$.

After three iterations: $C_1 = 5$, $C_2 = 0$. Final state $= 2^5 \cdot 5 = 160$. Result: $C_1 = 5 = 2 + 3$. $\checkmark$

### 7.5 Completeness

**Theorem 7.3.** The framework is Turing complete.

*Proof.* Every operation of a two-counter machine can be implemented using multiplication, division, and divisibility testing on the Gödel-encoded state integer. By Theorem 7.1 (Minsky), two-counter machines are Turing complete. $\square$

**Corollary 7.4.** There is no algorithm to decide, given an arbitrary counter machine encoded in this framework, whether it halts.

*Remark.* The Turing completeness demonstrated here is not a property unique to our framework — it is an inherited consequence of Gödel encoding applied to Minsky's result. The framework's contribution is that this encoding has coherent interpretations across all four layers: the increment of a counter is simultaneously a multiplication by a prime, an addition of a fixed resistance, and a unit vector addition in prime coordinate space.

---

## 8. Primes as Irreducible Elements

**Definition 8.1.** A positive integer $n > 1$ is *resistance-irreducible* if there do not exist positive integers $a, b > 1$ such that $\ln(n) = \ln(a) + \ln(b)$.

**Theorem 8.2 (Prime Characterisation).** A positive integer $n > 1$ is prime if and only if it is resistance-irreducible.

*Proof.* ($\Rightarrow$) If $n$ is prime and $\ln(n) = \ln(a) + \ln(b) = \ln(ab)$ with $a, b > 1$, then $n = ab$ with $a, b > 1$, contradicting primality. ($\Leftarrow$) If $n$ is composite, write $n = ab$ with $a, b > 1$. Then $\ln(n) = \ln(a) + \ln(b)$, so $n$ is not resistance-irreducible. $\square$

The four-layer translations of primality are:

| Layer | Characterisation of primes |
|-------|---------------------------|
| English | Cannot be expressed as a product of smaller factors |
| Inverse Integer | $1/p$ cannot be written as $1/a \cdot 1/b$ with $a, b > 1$ |
| Resistance | $\Omega_p$ is indecomposable: not a sum of smaller resistances |
| Vector | $\mathbf{v}(p)$ is a standard unit vector |

---

## 9. Discussion

### 9.1 The Framework as Synthesis

The four-layer framework developed in this paper unifies observations from several classical traditions. The logarithmic homomorphism is as old as Napier; the divisibility lattice is standard since Birkhoff; the connection to Boolean logic through set encoding is implicit in much of combinatorics; and the Turing completeness of counter machines is due to Minsky. What the framework provides is a *single algebraic lens* through which all of these become visible simultaneously.

The practical value of such a synthesis is pedagogical and methodological. A result proved in one layer (say, by direct computation with GCDs) can be independently verified in another layer (say, by vector operations), providing a check against error. The coprimality derivation of Section 5 illustrates this: the same result emerges from four different computational paths, all ultimately grounded in the Euler product.

### 9.2 Connections to the Zeta Function

The Euler product $\zeta(s) = \prod_p (1 - p^{-s})^{-1}$ and its inverse $1/\zeta(s) = \sum_n \mu(n)/n^s$ arise naturally within the framework. The coprimality probability $6/\pi^2 = 1/\zeta(2)$ is a direct consequence (Section 5). The Möbius function $\mu(n)$, which assigns $(-1)^k$ to squarefree integers with $k$ prime factors and $0$ to non-squarefree integers, plays a natural role as the sign function for inclusion-exclusion within the lattice structure. These connections suggest that the framework may provide a useful perspective on other problems involving the zeta function and multiplicative number theory, though we do not pursue such directions here.

### 9.3 Limitations

The principal limitation of the framework is the behaviour of complement (NOT), discussed in Section 3.4. The monoid $(\mathcal{I}, \times)$ is not a group: inverse integers are closed under multiplication but not under the complement operation $1 - 1/a$. To obtain a full Boolean algebra, one must either restrict to the lattice of divisors of a fixed integer (where relative complement exists) or extend the domain to the positive rationals. This asymmetry between AND/OR (which preserve $\mathcal{I}$) and NOT (which does not) is an intrinsic algebraic feature of the framework.

The Turing completeness result (Section 7) is inherited rather than novel. The framework does not provide new computational capabilities; rather, it provides a unified language for describing classical constructions.

---

## References

[1] Napier, J. (1614). *Mirifici Logarithmorum Canonis Descriptio.* Edinburgh.

[2] Birkhoff, G. (1933). On the combination of subalgebras. *Proceedings of the Cambridge Philosophical Society*, 29(4), 441–464.

[3] Gödel, K. (1931). Über formal unentscheidbare Sätze der Principia Mathematica und verwandter Systeme I. *Monatshefte für Mathematik und Physik*, 38, 173–198.

[4] Aczél, J. (1966). *Lectures on Functional Equations and Their Applications.* Academic Press.

[5] Shannon, C. E. (1948). A mathematical theory of communication. *Bell System Technical Journal*, 27(3), 379–423.

[6] Minsky, M. L. (1967). *Computation: Finite and Infinite Machines.* Prentice-Hall.

[7] Sheffer, H. M. (1913). A set of five independent postulates for Boolean algebras. *Transactions of the American Mathematical Society*, 14(4), 481–488.

[8] Euler, L. (1734). De summis serierum reciprocarum. *Commentarii academiae scientiarum Petropolitanae*, 7, 123–134.

[9] Hardy, G. H. & Wright, E. M. (1979). *An Introduction to the Theory of Numbers* (5th ed.). Oxford University Press.

[10] Davey, B. A. & Priestley, H. A. (2002). *Introduction to Lattices and Order* (2nd ed.). Cambridge University Press.

[11] Cover, T. M. & Thomas, J. A. (2006). *Elements of Information Theory* (2nd ed.). Wiley-Interscience.

[12] Codd, E. F. (1970). A relational model of data for large shared data banks. *Communications of the ACM*, 13(6), 377–387.

[13] Riemann, B. (1859). Über die Anzahl der Primzahlen unter einer gegebenen Größe. *Monatsberichte der Berliner Akademie*, 671–680.

[14] Cauchy, A.-L. (1821). *Cours d'Analyse de l'École Royale Polytechnique.* Paris.

---

## Appendix A: Key Formulas

| Name | Formula |
|------|---------|
| Resistance mapping | $\Omega(1/n) := \ln(n)$ |
| Series (AND) | $\Omega(1/(ab)) = \Omega_a + \Omega_b$ |
| Union (OR via LCM) | $\Omega_{\operatorname{lcm}} = \Omega_a + \Omega_b - \Omega_{\gcd}$ |
| Fundamental identity | $\operatorname{lcm}(a,b) \cdot \gcd(a,b) = a \cdot b$ |
| Coprimality | $P(\gcd(a,b) = 1) = 6/\pi^2$ |
| Euler product | $\zeta(s) = \prod_p (1 - p^{-s})^{-1}$ |

## Appendix B: Notation

| Symbol | Meaning |
|--------|---------|
| $\mathcal{I}$ | Set of inverse integers $\{1/n : n \in \mathbb{Z}^+\}$ |
| $\Omega(1/n)$, $\Omega_n$ | Informational resistance $= \ln(n)$ |
| $\mathbf{v}(n)$ | Prime coordinate vector of $n$ |
| $D_p$ | Divisibility gate for prime $p$ |
| $\zeta(s)$ | Riemann zeta function |
| $\mu(n)$ | Möbius function |
