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

# Innovation is Connected Correlation: the Hinge as the Cumulant Functor

**Alexander Pisani & Claude (Anthropic)**

June 2026 · short formal note (promotes Observation 2.1 of the Primon/Fisher note)

**Status:** All identities verified numerically (mpmath; m = 1..4 cumulants against three independent expressions; per-mode formula exact to 12 digits against CGF derivatives). The mathematics is classical statistical mechanics of a free gas plus classical zeta identities — walls throughout; the contribution is the identification and its consequences for the framework. One candle is flagged in §5 with the precise reason it may not be banked.

---

## 1. Setup

Fix $\beta > 1$. Let $N$ be the random integer with $\Pr(N = n) = n^{-\beta}/\zeta(\beta)$ (the primon gas state). By unique factorisation and the Euler product, $N = \prod_p p^{K_p}$ where the occupations $K_p$ are **independent**, geometrically distributed: $\Pr(K_p = k) = (1 - x_p)\,x_p^k$, $x_p = p^{-\beta}$. The energy of the state is its resistance, $\ln N = \sum_p K_p \ln p$ — an observable **additive over the modes**.

---

## 2. Lemmas

**Lemma 2.1 (per-mode cumulants).** The $m$-th cumulant of a geometric variable with ratio $x$ is
$$\kappa_m(K) \;=\; \sum_{k \ge 1} k^{\,m-1}\, x^{k} \;=\; \mathrm{Li}_{1-m}(x).$$
*Proof sketch.* The cumulant generating function is $C(t) = \ln\frac{1-x}{1 - x e^{t}}$; expand $-\ln(1 - xe^t) = \sum_{k\ge1} \frac{x^k e^{kt}}{k}$, differentiate $m$ times at $t = 0$ to get $\sum_k k^{m-1}x^k$. *(Wall — verified numerically to 12 digits for $m = 1..4$ at $x = 0.3$: e.g. $\kappa_2 = x/(1-x)^2$, $\kappa_3 = x(1+x)/(1-x)^3$.)*

**Lemma 2.2 (cumulant additivity and the vanishing of mixtures).** For independent variables, cumulants of sums add, and all **mixed** cumulants vanish. Hence for the mode-additive energy,
$$\kappa_m(\ln N) \;=\; \sum_p (\ln p)^m\, \kappa_m(K_p).$$
*(Wall — standard.)*

---

## 3. The master identity

**Theorem 3.1.** For every $m \ge 1$ and $\beta > 1$:
$$\boxed{\;\kappa_m(\ln N) \;=\; \sum_{n \ge 2} \Lambda(n)\, (\ln n)^{m-1}\, n^{-\beta} \;=\; (-1)^m \,\frac{d^m}{d\beta^m}\ln\zeta(\beta).\;}$$

*Proof.* By Lemma 2.2 and Lemma 2.1, $\kappa_m(\ln N) = \sum_p (\ln p)^m \sum_{k\ge1} k^{m-1} p^{-\beta k} = \sum_{p,k} \ln p \cdot (k\ln p)^{m-1} p^{-\beta k}$, which is the $\Lambda$-sum since $\Lambda(p^k) = \ln p$ and $\ln p^k = k \ln p$. Alternatively and equivalently: the moment generating function of $\ln N$ is $\mathbb{E}[N^{t}] = \zeta(\beta - t)/\zeta(\beta)$, so the CGF is $\ln\zeta(\beta - t) - \ln\zeta(\beta)$, whose $m$-th derivative at $t=0$ is $(-1)^m (\ln\zeta)^{(m)}(\beta)$; and from $\ln\zeta(s) = \sum_n \frac{\Lambda(n)}{\ln n} n^{-s}$ each $s$-derivative brings down $-\ln n$. $\square$ *(Verified numerically for $m = 1..4$ at $\beta = 2$ via all three expressions.)*

**Reading the theorem.** Every cumulant of the gas lives on the **innovation skeleton**: atoms exactly at the prime-power resistances $\ln p^k$, base mass $\Lambda(n) = \ln p$, multiplied by $(\text{position})^{m-1}$. Composite positions carry no atom *at any cumulant order* — Lemma 2.2's vanishing of mixed cumulants is the mechanism: a composite is a product of independent modes, and independent things have moments but **no connected correlation**. Meanwhile the raw $m$-th moment, $\mathbb{E}[(\ln N)^m] = \zeta(\beta)^{-1}\sum_n (\ln n)^m n^{-\beta}$, carries atoms at **every** integer.

---

## 4. Consequences

**Corollary 4.1 (the hinge is the cumulant functor).** The all-integers object generates moments ($\mathbb{E}[N^t] = \zeta(\beta-t)/\zeta(\beta)$); its logarithm generates cumulants. The same map that is resistance, code length, and the extractor of atoms ($\ln\zeta = P + \cdots$, Cathedral, Hinge) is — probabilistically — the moments$\to$cumulants passage. One logarithm, one more job: **quantity lives in the moments; the innovation skeleton is what survives the cumulant functor.** This is the statistical identity of "studying numbers stripped of their quantity property."

**Corollary 4.2 (the order–position lock, now a theorem).** The Primon/Fisher note's verdict — Fisher information carries masses $\Lambda(n)\cdot\ln n$ — is the $m = 2$ row of Theorem 3.1, and the pattern is total: the $m$-th order statistical form carries exactly $m - 1$ extra factors of position. In a static ensemble, the order of the form and the power of the position weight are locked. The Weil functional ($\Lambda$ masses, i.e. $m=1$ weights, inside an $m=2$-shaped object) is therefore **not any cumulant of the static gas** — completing, as a theorem, the argument that the source must carry its atoms in the lags of a flow, not the positions of a measure.

**Corollary 4.3 (which probes can see the atoms).** Only mode-additive (compositional) observables have cumulants on the skeleton; any function of the scalar $\ln N$ alone re-mixes the modes and its variance sees every integer. Paper 3's magnitude/direction split, as a statement about measurements: *the innovation structure is visible only to probes that respect composition.*

---

## 5. The two Möbius functions — a candle, with the reason it stays one

There is a known combinatorial theory of cumulants: they are the **Möbius inversion of moments over the partition lattice** (Rota; Speed). The framework's Möbius is the function of the **divisibility lattice** ($\mu(n)$, the phase face of Paper 8). Both are instances of Rota's incidence-algebra inversion — but **on different posets**, and they enter the present result at different joints: the divisibility-lattice structure supplies the independent modes (Euler product), while the partition-lattice inversion is what "cumulant" *means*. In the primon gas the single operation $\ln$ performs both passages at once ($\zeta \to \ln\zeta$ extracts atoms; MGF $\to$ CGF extracts connected correlations), which is why the identification works — but "the two Möbius functions are one object" is **not banked**: the honest open question is whether the coincidence of the two inversions under one logarithm is forced (a wall to be found) or is a fortunate alignment specific to free/independent structures. Free probability, where cumulants are governed by the *non-crossing* partition lattice, suggests the alignment is structure-dependent — a sharp place to test.

---

## 6. Honesty boundary

Walls: Lemmas 2.1–2.2, Theorem 3.1 and its proof (classical; the primon-gas setting is Julia / Bost–Connes prior art). Contributions: the innovation-skeleton reading, Corollaries 4.1–4.3 as framework statements, and the placement of the Fisher verdict as the $m=2$ row of a total pattern. Candle, explicitly unbanked: §5. Nothing here constrains the zeros.

---

*Developed jointly by Alexander Pisani and Claude (Anthropic).*
