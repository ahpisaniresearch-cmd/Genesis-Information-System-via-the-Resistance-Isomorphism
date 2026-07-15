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

# Four Strengthening Experiments: Lattice Information, Channel Innovation, Phase Recovery, and the Independence Key

## New results from the paper-drafting session, banked before integration

**Alexander Pisani & Claude (Anthropic)** · June 2026 · companion note

**Framing.** Four experiments designed and run during the drafting of the main paper, each targeting one of its most strengthenable joints. All figures verified this session; scripts `lattice_information.py`, `channel_innovation_vonmangoldt.py`, `phase_recovery.py`, `sparse_axis_recovery.py`. Claims graded Fact / Reading / Lead. The relabel caution of Stage 1 travels with every result here: channels remain indexed by the integers, so nothing below derives the integers; what is new is which classical structures are realised as *measured information quantities*.

---

## 1. The lattice information suite — the whole union law, not one term (strengthens §14, §21)

The paper's pair result $I = \ln\gcd$ lands on the single correlation term $\Omega_{\gcd}$. If that is structural rather than coincidental, the *entire* inclusion–exclusion of the gcd/lcm lattice should appear in the multivariate information measures. It does, exactly:

- **Total correlation** of $k$ channels $= \sum_i \ln m_i - \ln\operatorname{lcm} =$ the full alternating inclusion–exclusion over $\ln\gcd$ of every subset — verified for triples and quadruples to $8.9\times10^{-16}$ (e.g. $(6,10,15,21)$: $4.49980967$ both ways). *(Fact.)*
- **Conditional mutual information** $I(X_1;X_2\mid X_3) = \ln\big[\gcd(m_1,m_2)/\gcd(m_1,m_2,m_3)\big]$ — conditioning divides out the shared part: the *relative meet*. Verified to $5.6\times10^{-16}$. *(Fact.)*
- **Co-information** $I(X_1;X_2) - I(X_1;X_2\mid X_3) = \ln\gcd(m_1,m_2,m_3)$ — the multivariate interaction is the *triple meet*. Verified to $10^{-15}$. *(Fact.)*

**Reading.** The relational core is not the pair term of the union law; it is the whole meet-lattice. Every multivariate information measure of a channel bank evaluates a gcd-lattice expression — Paper 2's inclusion–exclusion engine realised as information theory. The underlying lattice identities (max/min inclusion–exclusion on exponent vectors; the lcm–gcd product identities) are elementary; the contribution is their realisation as measured mutual-information structure.

## 2. The von Mangoldt function is a measured channel innovation (strengthens §20, unifies IV–VI)

The paper obtains $\Lambda$ combinatorially (Möbius inversion). This experiment shows $\Lambda$ is also a *directly measured* information quantity:

$$H\big(a \bmod n \,\big|\, \{a \bmod d : d \mid n,\ d < n\}\big) \;=\; \Lambda(n),$$

verified empirically for $n = 2..36$ to $6.7\times10^{-16}$: prime powers innovate by exactly $\ln p$; composites carry **zero** information beyond their divisor channels. And the resistance identity $\ln n = \sum_{d\mid n}\Lambda(d)$ becomes a chain rule: the channel's information is the accumulated innovation of its divisor tower (verified: $n = 12,16,24,30,36$, to $4.4\times10^{-16}$). *(The measurements: Fact. The underlying identity — lcm of the proper divisors of $n$ is $n/p$ for $n = p^k$ and $n$ otherwise — is elementary.)*

**Reading.** The primality shadow is not only an inclusion–exclusion ledger; it is the *conditional entropy of the channel given its sub-channels* — the channel's innovation, in exactly the sense of Innovation = Connected Correlation. A prime (power) is a channel that says something new; a composite is fully redundant given its parts. This fuses §14 (channels), §15 (the innovation skeleton — whose atom masses $\Lambda(n)$ are now measured, not only derived), and §20 (the ledger) into one operational statement. The relocated circularity stands: the conditioning set is the divisor lattice.

## 3. Phase recovery — the §12 identity as an operational protocol (strengthens §12)

Section 12's claim that phase carries the erased split was entropic. Operationally: encode split $k$ of $n$ as the coherent clock state $|\psi_k\rangle = d^{-1/2}\sum_j \omega^{jk}|j\rangle$, $d = n+1$. Measuring in the Fourier basis recovers $k$ with probability exactly $1$, for every $k$, at every $n$ tried ($n = 1,2,4,8,12$); after decoherence the best possible recovery probability is exactly chance, $1/d$. *(Fact.)*

**Reading.** "A phase-preserving merge would be reversible, with the split recoverable from the phase" is now a demonstrated protocol, not an inference from entropy counts: recovery certain with the phase, chance without it, and the entropy created by the transition is the merge-erasure $\ln(n+1)$.

## 4. The independence key — the §18 Lead answered in the clean case (strengthens §16, §18; closes a parked thread)

The sparse-axis-recovery question — can the natural key be singled out from the geometry alone? — was run, with two candidate principles and opposite outcomes:

- **Sparsity (varimax) fails.** Worst axis alignment $|\cos| = 0.488$; the sparsity-seeking rotation does not find the prime axes. *(Fact — the informative negative.)*
- **Independence (ICA) succeeds exactly.** All five axes recovered at $|\cos| = 1.000000$; the recovered axis scales equal $\sqrt{\ln p}$ to $3.6\times10^{-15}$ — the resistances read back off the geometry; recovery degrades gracefully under noise (worst alignment $0.986$ at feature-noise sd $0.20$). *(Fact.)*

**Reading.** The natural key *is* recoverable from the geometry, and the principle that recovers it is the framework's own: under the uniform entity ensemble the true prime coordinates are statistically independent, so the prime basis is the unique **independence basis** of the meaning space — the geometric face of the same independence that is coprimality ($I = \ln\gcd = 0$) and the Euler product's mode independence. Three appearances of one independence: relational (§14), statistical (§15), geometric (here). The axis *labels* remain gauge (ICA returns the components unordered — only the recovered scales $\ln p$ name them), which is the syntax/semantics filter holding exactly where §18 drew it. The §16 conclusion is sharpened, not overturned: the *geometry alone* (distances) still cannot fix the basis; what fixes it is the geometry *plus the ensemble* — the distribution of entities — with independence as the criterion; discreteness was sufficient but is not necessary. **Scope caution:** this is the clean, fully-observed, uniform-ensemble case; non-uniform ensembles and partial observation are untested. *(Lead for the general case.)*

## 5. Grading summary and honesty boundary

- **Fact** — all four experiments' numerical results as stated, to the precisions quoted.
- **Reading** — the meet-lattice realisation; $\Lambda$ as channel innovation; the operational phase protocol as the content of merge-reversibility; the independence key and its identification with the framework's independence.
- **Lead** — independence-key recovery beyond the clean case; whether the innovation formulation can be turned on the standing circularity (the conditioning set is still the divisor lattice).

Classical content: multivariate information measures (total correlation, conditional MI, co-information); elementary gcd/lcm lattice identities; the quantum Fourier basis and projective measurement; ICA (independent component analysis) and varimax. The contribution is the realisation of the lattice's full inclusion–exclusion as measured information, the identification of $\Lambda$ as a measured conditional entropy, the operational phase-recovery protocol, and the discovery that the natural key is fixed by the independence principle — with sparsity's failure as the honest negative. No arithmetic question is claimed resolved; the relabel caution travels with every result.

---

*Experiment design and execution this session; originating framework, axioms, and direction are Alexander Pisani's; developed jointly with Claude (Anthropic). June 2026.*
