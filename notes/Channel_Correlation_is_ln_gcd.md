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

# Channel Correlation: the Connected Correlation is ln gcd

## The first relational quantity, and it lands on the resistance isomorphism's lattice core

**Alexander Pisani & Claude (Anthropic)** · June 2026 · companion note

**Framing.** The catalog mapped single operations, each an `ln(fan-in)` — a single-integer resistance. The first *relational* question — how much do two modulo channels share — produces the first two-variable quantity. Erasure-only discipline, claims graded Fact / Reading / Lead, verified by `channel_correlation.py`.

---

## 1. The result

Run `a mod m₁` and `a mod m₂` on the same `a`, uniform over one full joint period `N = lcm(m₁, m₂)`. Then

$$I(a \bmod m_1 \,;\, a \bmod m_2) \;=\; \ln \gcd(m_1, m_2),$$

confirmed numerically across all pairs `2..8` to machine precision (`max |I − ln gcd| = 2×10⁻¹⁶`). The Chinese Remainder structure makes it exact: both channels determine `a mod gcd` and nothing more, and `I = ln m₁ + ln m₂ − ln lcm = ln gcd`. *(Fact.)*

## 2. Coprimality is zero correlation

The `gcd` matrix is the coprimality lattice; the correlation is `ln` of each cell. Coprime pairs carry `I = 0`. **Two number-channels share information iff they share a prime**, and exactly `ln(shared part)` of it. The multiplicative core has become a thermodynamic signal. *(Fact.)*

## 3. It is the `Ω_gcd` term of the resistance isomorphism

`ln gcd` is still a resistance value — the resistance of the integer `gcd` — so this is not an escape from `ln(integer)`. It is sharper than that: it is `Ω_gcd`, the subtracted correlation term in Paper 1's union law

$$\Omega_{\mathrm{lcm}} = \Omega_a + \Omega_b - \Omega_{\gcd}.$$

The mutual information of two modulo channels landed exactly on that term. So the relational question reached the **lattice core** of the resistance isomorphism (the `gcd`/`lcm` structure), not a single-integer rung. The project's *Innovation = Connected Correlation* finding now has its arithmetic face: the connected correlation between two number-channels is `ln gcd`. *(Identification with `Ω_gcd`: Fact. "Relational core, not single-integer ladder": Reading.)*

## 4. The honest boundary, and the direction it opens

Coprimality *emerges* as zero correlation but is not *derived*: `m₁, m₂` are still inputs, so this is correlation-as-divisibility-test, not primes-from-nothing — the same standing problem the modulo gateway named. What is new is that the test is now *relational*: it reads the shared prime structure of a pair, which single-integer resistance cannot express, and the whole coprimality lattice (`6/π²` density of coprime pairs, Paper 1 Appendix A) is reproduced as a correlation pattern.

**Next-direction flag (deep, speculative, later).** The resistance isomorphism's zeta reading (Paper 8) is already a superposition/interference story: each integer is a phasor of amplitude `n^{−σ}` and phase `−t ln n`, the nontrivial zeros are total destructive interference of the whole phasor bouquet on the critical line `σ = 1/2`, and the amplitude-decay and phase rates are locked by `−i` (Cauchy–Riemann). That `−i` is the same `i` we *generated* discretely from succession and the probe (`[S,D] = −iσ_y` at the genesis bit). The avenue: whether the continuous critical-line cancellation is the shadow of a discrete proto-phase structure, with the generated `i` as the bridge. Held as a direction only — the corpus is explicit that the zeta work gives no leverage on the location of the zeros, and this claims none. *(Lead.)*

---

*Originating direction (the gcd as native to information systems and central to the resistance isomorphism; the relational channel-correlation test; the proto-phase / critical-line connection as a later thread) is Alexander Pisani's; the test and this compilation were developed jointly with Claude (Anthropic). June 2026.*
