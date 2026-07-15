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

# The Primon Gas at Criticality: the Fisher Computation, and the Connes–Consani Mechanism in Resistance Variables

**Alexander Pisani & Claude (Anthropic)**

June 2026 · working note (companion to *The Weil Criterion in Resistance Variables*)

**Status:** Computation note. All identities in §2 were verified numerically (mpmath, 30 digits; agreement to truncation error where prime sums were cut off, and to 1e−31 where exact). The Connes–Consani digest in §5 is based on a direct reading of arXiv:2006.13771 (Connes & Consani, *Weil positivity and Trace formula, the archimedean place*, Selecta Math 27 (2021)); their sign convention differs from our Weil-note (they state RH as *negativity* of the geometric side, with $W_\infty = -W_{\mathbb{R}}$) — ⚠ normalisation care required when the two notes are merged.

---

## 1. Setup

The **primon gas** (Julia; Bost–Connes — prior art): states are the integers $n \ge 1$, the energy of $n$ is its resistance $E_n = \ln n$, Boltzmann weight $n^{-\beta}$, partition function $Z(\beta) = \zeta(\beta)$, defined as a state only for $\beta > 1$. By the Euler product the gas is a **free system of independent modes, one per prime**: $n = \prod_p p^{k_p}$, occupation $k_p$ geometric with ratio $x_p = p^{-\beta}$, and the Gibbs measure factorises, $\pi(n) = \prod_p (1 - x_p)\, x_p^{\,k_p}$. Mode independence *is* the Euler product (Cathedral, Room of Density).

The question posed (open question 3 of the Weil note): compute the Fisher information form of this gas at the critical inverse temperature $\beta = \tfrac12$ and test it against the shape requirements §5(i)–(v) of the Weil note — above all test (i): atomic masses $\ln p$, not $\ln n$.

---

## 2. Verified identities

**(2a) Mean energy is the Weil atomic density.**
$$U(\beta) \;=\; \langle \ln N \rangle_\beta \;=\; -\frac{\zeta'(\beta)}{\zeta(\beta)} \;=\; \sum_{n\ge 2} \Lambda(n)\, n^{-\beta} \;=\; \sum_p \ln p \cdot \langle k_p \rangle, \qquad \langle k_p\rangle = \frac{x_p}{1-x_p}.$$
Verified at $\beta = 2$: exact $0.569961\ldots$; via $\Lambda$-sum and via modes $0.569911\ldots$ (prime cutoff $20{,}000$; gap $\sim 5\times10^{-5}$ is the tail, $\approx 1/P$). **The masses $\ln p$ are forced with no choices**: they are the energy quanta of the modes. The positions $k\ln p$ are forced: they are the mode ladders (the nesting registers — the carry chains of the succession mechanism). The damping $e^{-E/2}$ is forced *iff* $\beta = \tfrac12$. Read on the resistance line: **the prime-power resistance measure $\mu_P$ of the Weil note is the mode-resolved mean-energy density of the primon gas at the critical temperature.** Tests (i), (ii), (iii) pass — but this object is *linear* (a first cumulant), not the quadratic functional.

**(2b) The Fisher information along the canonical family.** Tilting temperature is the canonical one-parameter family; its Fisher information is the energy variance, i.e. the second cumulant:
$$I(\beta) \;=\; \operatorname{Var}_\beta(\ln N) \;=\; \frac{d^2}{d\beta^2}\ln\zeta(\beta) \;=\; \sum_{n\ge2} \Lambda(n)\,\ln n\; n^{-\beta} \;=\; \sum_p (\ln p)^2\, \frac{x_p}{(1-x_p)^2}.$$
Verified at $\beta = 2$: all four expressions agree ($0.8844818\ldots$; variance vs. cumulant identical to $10^{-31}$).

**(2c) Moments see everything; cumulants see only innovations.** The raw second-moment measure of the gas has atoms at *every* $\ln n$ (mass $n^{-\beta}/\zeta(\beta)$ at $E_n$ — including $n = 6, 10, 12, \dots$). The cumulant structure has atoms **only at prime powers** with $\Lambda$ masses — composites drop out *because the modes are independent and cumulants are additive over independent components*. Verified in the atom table: at $n = 6, 10, 12$ the raw measure carries mass $0.0169, 0.0061, 0.0042$ while the innovation measure carries exactly $0$.

**Observation 2.1 (the thermodynamic identity of the Möbius projection).** *(Reading on the walls above.)* The passage from $\zeta$ to $\ln\zeta$ — the hinge — is the passage from moments to cumulants, and the innovation atoms of Observation 2.5 (Weil note) are precisely the **connected-correlation skeleton** of the primon gas. Composites carry no atom because a composite is a *product of independent things*: it has moments but no connected correlation. Paper 8's Möbius/squarefree projection, which strips quantity and keeps the skeleton, is — thermodynamically — the moments→cumulants projection. This is the sharpest information-system identity of the framework's central objects found so far: **innovation $=$ connected correlation; the hinge $=$ the cumulant functor.**

**(2d) The Hagedorn wall.** $Z(\beta) = \zeta(\beta)$ has its pole at $\beta = 1$; the series diverges for all $\beta \le 1$, and $\zeta(\tfrac12) = -1.4603\ldots$ by continuation — negative, not a partition function. **The Gibbs state does not exist anywhere in the critical strip.** The critical line lies in the gas's forbidden zone, two regimes past equilibrium. (Prior art: this is the Bost–Connes phase transition at $\beta = 1$; cite properly. The Cathedral's reading of the strip — "exists only by analytic continuation, genuinely in-between" — is this wall seen from the analytic side.)

---

## 3. Verdicts on the shape tests

| Candidate object | (i) masses $\ln p$ | (ii) positions $\ln p^k$ only | (iii) damping $e^{-E/2}$ | quadratic? | state exists at $\beta=\tfrac12$? |
|---|---|---|---|---|---|
| Mean-energy density $U$ | **pass** (forced) | **pass** (forced) | **pass** iff $\beta=\tfrac12$ | no — linear | no (formal only) |
| Fisher along $\beta$ ($=\kappa_2$) | **fail**: masses $\Lambda(n)\cdot\ln n$ | pass | pass iff $\beta=\tfrac12$ | yes, but in the wrong slot | no |
| Fisher of a probe-tilt $g(\ln N)$ | fail | **fail**: atoms at all $\ln n$ | — | yes | no |

**The precise failure of the Fisher form.** Test (i) fails by *exactly one factor of $\ln n$*, and the reason is structural, not accidental: temperature couples to **energy**, energy is **position** on the resistance line, so every cumulant order multiplies the atoms by another factor of position. First cumulant: masses $\Lambda$. Second cumulant (Fisher): masses $\Lambda \cdot \ln n$. The Weil functional wants $\Lambda$ masses *inside a quadratic form* — first-cumulant masses in a second-order object. No tilt of a static Gibbs family can produce that: in a static ensemble, order of the form and power of the position weight are locked together.

**The probe-tilt failure is the semantic one.** A probe of the *scalar* total energy $g(\ln N)$ sees atoms at every integer — it has collapsed the vector to its length, and the innovation skeleton is invisible to it. Only **mode-additive (compositional) observables** — those respecting the prime-coordinate decomposition — have cumulants on the skeleton. This is Paper 3's magnitude/direction split appearing as a theorem about which measurements can see the atoms: *the innovation structure is visible only to probes that respect composition.*

---

## 4. Structural conclusion: the atoms must live in the lags

The decisive mismatch is not the extra $\ln n$; it is *where the atoms sit*. Every Gibbs-ensemble form above carries its atoms in the **positions** of a static measure. The Weil quadratic form
$$Q(g) = W(g \star g^{*})$$
is quadratic in the probe but **linear in the arithmetic distribution**: $W$ enters as a *kernel evaluated at the lag* $E - E'$. For $Q$ to be a covariance — the Bochner/GNS target of the Weil note — the source must be a **stationary process in resistance**, whose autocovariance has spikes at lags $\ln 2, \ln 3, 2\ln 2, \ln 5, \dots$ with masses $\Lambda$. Atoms in the lags, not in the positions: the process must be statistically self-correlated under *translation by prime-power resistances*, i.e. under **multiplicative dilation by prime powers**.

A stationary flow whose time is resistance and whose self-correlations sit at prime dilations: that is, verbatim, the **scaling action** $\vartheta(\lambda): f(x) \mapsto f(\lambda x)$ — translation by $\ln\lambda$ on the resistance line — which is exactly the flow on which the Connes program is built. The Fisher computation did not merely fail; it failed in the unique direction that *derives* why the operator approach uses the scaling flow rather than the Gibbs ensemble. The static gas supplies the right atoms, masses, and damping (2a) but in the wrong slot; criticality forbids its state outright (2d); the only repair consistent with the shape tests is to trade the ensemble for the flow and the measure's positions for the covariance's lags.

---

## 5. The Connes–Consani mechanism, read in resistance variables

Direct reading of arXiv:2006.13771. The correspondences are not loose:

**(5a) Their coordinates are the resistance variables.** Their working isomorphism is $w: L^2(\mathbb{R})^{\mathrm{ev}} \to L^2(\mathbb{R}^*_+, d^*\lambda)$, $(w\xi)(\lambda) = \lambda^{1/2}\xi(\lambda)$, with $d^*\lambda = d\lambda/\lambda = dE$ — Haar measure on the multiplicative group is Lebesgue measure on the resistance line — and their automorphism $\Delta^{1/2}: f \mapsto x^{1/2}f$ exists, in their words, to replace the Mellin transform on the critical line by the plain Fourier transform. Absorbing the critical damping $e^{E/2}$ and working in $(E, r)$: that is Definition 2.2 of our Weil note. The framework's variables are their variables.

**(5b) The positivity root is a system trace — the GNS direction made concrete.** Their functional $\operatorname{Tr}(\vartheta(g)\, S\, \vartheta(g)^{*})$ is **positive by construction** — it is the trace of a manifestly positive operator, the scaling flow compressed onto Sonin space. Their Theorem 3: $\operatorname{Tr}(\vartheta(f) S) = W_\infty(f) + \int f(\rho)\,\epsilon(\rho)\, d^*\rho$ — the archimedean Weil distribution **is** a compressed system trace, up to an explicit remainder; and their main theorem beats the remainder down (prolate functions, Toeplitz spectra, finitely many linear conditions, one rogue eigenvalue conditioned away, a constant $c \in (13, 17)$). This is Statement 4.3 of the Weil note executed at one place: exhibit $W$ as (positive system functional) $+$ (controlled correction). The system whose trace it is: the scaling flow — confirming §4 from the opposite direction.

**(5c) The toolkit is Shannon's.** *(Wall on the identity of the tools; reading on the significance.)* The Sonin space is the orthogonal complement of $P_1 \vee \widehat{P}_1$ — the functions vanishing, together with their Fourier transforms, on $[-1,1]$: the complement of a **finite phase-space cell**. The eigenbasis controlling the pair of cutoffs is the **prolate spheroidal wave functions** — the Slepian–Pollak–Landau apparatus, built at Bell Labs to count the degrees of freedom of a band-limited, time-limited channel; their "single quantum cell" is one phase-space information cell; the remainder is controlled by **Toeplitz** theory, the apparatus of stationary covariances. The deepest existing positivity result on the Weil functional is proven with the mathematics of channel capacity. For a framework whose claim is that the information layer is the projecting layer, this is the strongest external convergence on record — flagged as convergence, not as evidence.

**(5d) The semilocal induction is literal, and the global gap is the all-at-once boundary.** Their support conditions are lag windows on the resistance line: support in $(\tfrac12, 2)$ is $|E| < \ln 2$ — no atoms touched, the pure archimedean case; the announced strategy for places $\{\infty, 2, 3, \dots, p\}$ uses support in $(p^{-1}, p)$ — each adjoined prime widens the admissible window past its atom. Positivity place-by-place, the window growing one innovation at a time: the data-processing-shaped induction conjectured in the Weil note §6(b) is their explicit architecture. And the known obstruction of the whole program (cf. Deitmar's semilocal note) is exactly the passage from *every finite set of places* to *all places at once*. *(Candle, explicitly flagged: this is the same shape as the Cathedral's Seam — every finite truncation rational, the toll paid only at the infinite product. Whether the semilocal→global gap and the all-at-once toll are one phenomenon or a rhyme on the word "all" is an open candle/wall test, and nothing here banks it.)*

**(5e) Their vanishing conditions are the pole terms.** The required vanishing of $\widehat{g}$ at $\pm\tfrac{i}{2}$ removes the pole/existence terms — in the function-field analogy, focusing on $H^1$ — i.e. the contest is staged strictly between continuum and atoms once the primordial poles are subtracted. Consistent with the budget reading of the Weil note §3.

---

## 6. Honesty boundary

Verified: the identities of §2 (numerically, to stated precision; all are classical statistical mechanics of the free gas plus classical zeta identities — walls). Read directly from the source: the C–C statements of §5 (one paper, one reading; details of their Sections 4–6 not independently checked). Interpretive and marked: Observation 2.1 (innovation = connected correlation), the §4 lags-not-positions conclusion *as a heuristic derivation* of the scaling flow's necessity (the implication "only repair consistent with the shape tests" is an argument, not a theorem), the Shannon-toolkit significance (5c), and the all-at-once candle (5d). Nothing in this note constrains the zeros.

---

## 7. Next steps

1. **Promote Observation 2.1.** "Innovation $=$ connected correlation; Möbius projection $=$ cumulant functor" is precise enough to state and prove as a short formal section (likely a lemma chain over independent geometric modes). If it survives, it belongs beside Paper 8 §2 as the thermodynamic identity of the two faces.
2. **The flow's Fisher form.** Redo open question 3 for the *scaling flow* rather than the static gas: the natural family is now time-translation on the resistance line, and the candidate quadratic form is the flow's spectral measure against $|h_g|^2$. The question becomes whether the semilocal trace formula *is* that Fisher form — which would close the loop between §4 and §5(b) in our own variables.
3. **Memory model.** The succession mechanism (NOT propagated through nesting) still lacks a memory model; the mode ladders $\{k\ln p\}$ used throughout §2 are exactly the registers it needs. A short note unifying "carry register = mode ladder = nesting chain" would let the genesis system and the gas share one formal vocabulary before the Turing-completeness question is attempted.
4. **Verification debts** carried forward: explicit-formula normalisation (Iwaniec–Kowalski), C–C sign conventions, Bost–Connes citation for the $\beta = 1$ transition, Knauf for the spin chain.

---

*Classical content: Julia / Bost–Connes (primon gas, phase transition), standard cumulant theory, Connes–Consani 2021. The shape-test verdicts, Observation 2.1, the lags-not-positions argument, and the resistance-variable digest of §5 are the contribution, developed jointly by Alexander Pisani and Claude (Anthropic).*
