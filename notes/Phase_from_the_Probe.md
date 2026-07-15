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

# Phase from the Probe

## The Genesis Heisenberg Pair, $XZ = \sqrt{\mathrm{NOT}}$, and the Information Shadow

**Alexander Pisani & Claude (Anthropic)** · June 2026 · companion note · DRAFT

**Status.** Companion to *The Genesis Information Project* (§2.5, which carries the headline). Shows that $\sqrt{\mathrm{NOT}}$ — taken as primitive in §4 ("$i$ is the square root of NOT") — is *constructed* from the two genesis operations failing to commute. The algebra is classical (the clock–shift / Weyl / generalised-Pauli operators on $\mathbb{Z}/p$; ⚠ Weyl); the contribution is reading the genesis probe and dynamics as that pair, the $XZ=\sqrt{\mathrm{NOT}}$ genesis-prime observation, and the information shadow. All computational claims verified by execution this session (`probe_dynamics.py`, archived).

**Role.** This is the first place in the corpus where **phase is built rather than assumed**. It deepens §2.1/§4 (NOT primitive; $i=\sqrt{\mathrm{NOT}}$) by handing $\sqrt{\mathrm{NOT}}$ a derivation, and it supplies the information-shadow that links to the next direction (erasure; *Erasure as the Carrier of Mathematics*).

---

## 1. The two operations, as operators

A computation state is one integer (§2.3). Represent it in the number basis $\{\lvert n\rangle\}$.

- **Succession** $S$ — the dynamics (NOT propagated through nesting, §2.2): $S\lvert n\rangle = \lvert n+1\rangle$, the shift.
- **The genesis probe** $D_p$ — the meet-atom "does $p$ divide $n$" (§2.3, §5.3) as a yes/no operator: $D_p\lvert n\rangle = \lvert n\rangle$ if $p\mid n$, else $0$. A projection (eigenvalues $0,1$), as a binary probe must be.

## 2. The disturbance is real and structured (Fact)

The commutator $[D_p, S]$ acts as
$$[D_p,S]\,\lvert n\rangle = \bigl(\,[\,p\mid n{+}1\,] - [\,p\mid n\,]\,\bigr)\,\lvert n+1\rangle .$$
Consecutive integers are coprime, so the coefficient is $\pm1$ or $0$: **$+1$ just before each multiple of $p$** (gaining divisibility), **$-1$ just after** (losing it), zero elsewhere — nonzero, periodic with period $p$. Testing-for-$p$ and stepping do not commute: stepping moves the answer. (Verified for $p=3$: nonzero at $n = 2,3,5,6,8,9,11$ with the predicted signs.)

## 3. Mod $p$, it is the discrete Heisenberg pair (Fact; prior art)

Reduce to the residues. Succession becomes the **shift** $X:\lvert r\rangle\mapsto\lvert r+1 \bmod p\rangle$; the probe becomes a spectral projection of the **clock** $Z:\lvert r\rangle\mapsto \omega^r\lvert r\rangle$, $\omega = e^{2\pi i/p}$ — indeed $D_p = \tfrac1p\sum_{k=0}^{p-1} Z^k$ is the projection onto $Z$'s eigenvalue-$1$ (residue-$0$) space. They obey the **Weyl relation**
$$ZX = \omega\,XZ,\qquad \omega = e^{2\pi i/p}.$$
So the obstruction to "measure then step" versus "step then measure" is a **phase** — a root of unity (verified for $p=3$). This is a third, sharper origin of phase: not $\sqrt{\mathrm{NOT}}$ postulated (§4), not phase-as-NOT's-generator, but **phase as the price the probe pays to disturb the dynamics**, quantised in roots of unity (proto-phase units). The clock–shift / Weyl / generalised-Pauli operators are classical (⚠ Weyl; the basis of the finite Fourier transform and mutually-unbiased bases); the reading of the genesis probe and dynamics as that pair is the contribution.

## 4. The genesis prime $p=2$: $XZ = \sqrt{\mathrm{NOT}}$ (Fact, verified)

At $p=2$ the pair is the Pauli algebra:
- succession $= X = \bigl[\begin{smallmatrix}0&1\\1&0\end{smallmatrix}\bigr]$ — Pauli $X$, the bit-flip (swap even↔odd), which is the **Boolean** NOT ($X^2 = I$; §2.1's intuitionistic negation);
- probe $= Z = \bigl[\begin{smallmatrix}1&0\\0&-1\end{smallmatrix}\bigr]$ — Pauli $Z$, the parity-sign, which is the **proto-phase mark** for $p=2$;
- they anticommute, $ZX = -XZ$ (commutator-phase $\omega = -1 =$ the phase NOT);
- and their product is
$$XZ = \bigl[\begin{smallmatrix}0&-1\\1&0\end{smallmatrix}\bigr] = J = \sqrt{\mathrm{NOT}},\qquad (XZ)^2 = -I.$$

So the proto-phase generator $J$ — the real $2\times2$ rotation that §2.5/§4 identify as the genesis-native object beneath the complex numbers — is **manufactured as the product of the two genesis operations.** Not circular: $X$ is a real permutation (stepping), $Z$ is the real $\pm$ sign of the $2$-residue (the proto-phase mark) — neither contains $i$; the property $J^2=-I$ *emerges* from composing two real, order-2 operations that fail to commute, the anticommutation being exactly what lifts order 2 to order 4. This realises "$4 = 2\times 2 = \mathrm{order}(\sqrt{\mathrm{NOT}}) = 2\cdot\mathrm{order}(\mathrm{NOT})$" (master §2.1/§2.5) concretely, and both of the two NOTs appear in the one construction: the bit-flip is a factor, the phase NOT is the square of the product.

## 5. The information shadow: Shannon's 1 bit (Fact + Reading)

The parity probe ("is $n$ even?") cuts the integers into two halves of density $\tfrac12$ — Shannon's **1 bit**, the maximum-entropy split $p=\tfrac12$. This is special to $p=2$: a general prime's probe splits $\{1/p,\,1-1/p\}$, worth $H(1/p) < 1$ bit ($\approx 0.92$ at $p=3$, decreasing). Therefore **information and disturbance peak together at the genesis prime**: $p=2$ extracts the most ($1$ full bit) and disturbs the most (phase $\pi$), each falling off for larger primes — $H(1/p)$ and $\arg\omega = 2\pi/p$ are co-monotone (peaking together, not proportional). Two different measures (entropy and commutator-phase) landing on the same prime: the information-shadow and the algebra-shadow of one fact, that the genesis prime is the maximal one. This is the information–disturbance tradeoff in shadow form, the same family as the probe note's "ignorance is free, forgetting is not," and it connects to the corpus's existing Shannon seam (Paper 3: resistance $=$ code length). *(The $1$-bit and $H(1/p)$ facts are Fact; the "two shadows of one maximality" framing is the Reading.)*

## 6. Scope and what is promotable

**Scope.** The $\sqrt{\mathrm{NOT}}$ result lives at the **1-bit floor** — two states (parity), the flip, the sign — *not* the integer ladder. The full lattice operator of §§1–2 needs the successor operation (the carrier), but never the completed integers as a static set. So phase is manufactured the moment succession and the probe coexist and fail to commute, neither alone.

**Promotable.** The headline ($\sqrt{\mathrm{NOT}}$ manufactured; phase $=$ probe–dynamics non-commutativity) is promoted into the spine (§2.5). The general-$p$ structure — how the per-prime Heisenberg pairs combine (CRT/adele), and the infinite-dimensional limit whose generator is the scaling flow (the open §7.3 object whose spectrum would be the zeros) — is the natural continuation, deferred. The matrix group in play is $\mathrm{SL}(2,\mathbb{R})$, already the home of §7.1's two involutions (inversion and NOT), so this tool joins the spectrum programme when wanted.

## 7. Honesty boundary

Classical and cited: the clock–shift / Weyl / generalised-Pauli operators and their relation $ZX=\omega XZ$ (⚠ Weyl); the discrete uncertainty between a residue and its Fourier dual; Shannon entropy of a partition; Landauer/Bennett for the information–disturbance family. The contribution is the reading of the genesis probe and dynamics as the Weyl pair, the $XZ=\sqrt{\mathrm{NOT}}$ genesis-prime observation, and the two-shadows framing. No claim is made on the primes' distribution or the zeros: this is the genesis-native *seed* of measurement disturbance (a genuine residue/momentum uncertainty relation), the ancestor of the prime-distribution uncertainty, not that uncertainty — which requires the continuum medium the proto-level lacks (probe note §3). Verification archived (`probe_dynamics.py`).

## 8. Next steps

1. **Fold into the erasure direction.** The $1$-bit/parity probe is the information-shadow that bridges to *Erasure as the Carrier*: the genesis-prime probe is exactly the $1$-bit measurement whose irreversible commitment is an erasure.
2. **General-$p$ combination.** Work the per-prime Heisenberg pairs together (CRT); ask what the disturbance-phase pattern $2\pi/p$ says structurally.
3. **The infinite-dimensional generator.** Whether the scaling-flow generator (§7.3) is the continuum limit of these finite $J$'s — placed, not yet built.

---

*Originating observation (the probe/dynamics framing and the matrix reading) is Alexander Pisani's; the formalisation, the Weyl identification, the verification, and this compilation were developed jointly with Claude (Anthropic). June 2026.*
