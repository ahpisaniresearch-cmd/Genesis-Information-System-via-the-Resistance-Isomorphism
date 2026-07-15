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

# The Primality Shadow as a Signed Inclusion-Exclusion Ledger

## Pisani's primality-shadow formula is the von Mangoldt function — and it is the Euler product

**Alexander Pisani & Claude (Anthropic)** · June 2026 · companion note

**Framing.** Pisani's proposal: the primality shadow of `p` is the ON state, minus the erasure of everything but the unique row, plus the nats that certify primality (the irreversibility test). This note formalises that ledger and verifies it. Verified by `primality_shadow_ledger.py`. Claims graded Fact / Reading / Lead.

---

## 1. The ledger is the von Mangoldt function via Möbius inversion of the resistance

Two identities, both verified:

$$\ln n = \sum_{d\mid n} \Lambda(d) \qquad\text{(resistance built from innovations)},$$
$$\Lambda(n) = -\sum_{d\mid n} \mu(d)\,\ln d \qquad\text{(the irreversibility test: invert it)},$$

where `Λ(n) = ln p` if `n = pᵏ` and `0` otherwise. The second is a signed inclusion–exclusion over the divisor lattice — Paper 2's Möbius engine — that pulls the prime-signal back out of the resistance. *(Both identities classical; verified to `10⁻¹²`. Fact.)*

## 2. Mapping the three terms (the prime is the clean case)

For a prime `n = 5` the ledger has two rows only:
- `d = 1`: the **ON state** — `μ(1) = +1`, contributing `ln 1 = 0`, the identity always present.
- `d = 5`: the **certificate** — `+ln 5`.
- no composite divisor → **no erasure term** → the full `ln 5` survives. `Λ(5) = ln 5`. The prime *locks up*: nothing to reduce.

For a composite `n = 6` the erasure appears: `+ln 2 + ln 3` certify the prime parts, the `−ln 6` term cancels them exactly, and `Λ(6) = 0`. The composite *reduces away*. **The erasure is the inclusion–exclusion cancellation that annihilates everything not irreducible; a prime is exactly a number with an empty erasure column.** *(Recognising the classical identity as the data-structure ledger — primes as the rows with nothing to cancel: Reading.)*

## 3. This is the Euler product — and the coprimality result — and Paper 2

The von Mangoldt series is the log-derivative of the Euler product:

$$-\frac{\zeta'}{\zeta}(s) = \sum_n \frac{\Lambda(n)}{n^{s}}, \qquad \zeta(s) = \prod_p \left(1 - p^{-s}\right)^{-1}.$$

So `Λ` is the prime-signal the product hands back when differentiated — the bridge between the additive sum over integers and the multiplicative product over primes, in resistance variables. The product factorises **because** divisibility by distinct primes is independent, and that independence is the coprimality measured earlier: `I(a mod p ; a mod q) = ln gcd(p,q) = 0`. Three things are one: Paper 2's Euler product, the `ln gcd` coprimality, and the primality-shadow ledger are three faces of unique factorisation written in information. The product factorises because the prime channels are uncorrelated; its log-derivative is the von Mangoldt; and the von Mangoldt is the ON − erasure + certificate ledger, with primes the irreducible survivors. *(The synthesis across the three: Reading.)*

## 4. Grading and honesty boundary

- **Fact** — `ln n = Σ_{d|n} Λ(d)`, `Λ(n) = −Σ_{d|n} μ(d) ln d`, and `Λ` as the Euler product's log-derivative (all classical, verified).
- **Reading** — the identification of Pisani's ON/erasure/certificate ledger with the von Mangoldt inclusion–exclusion (primes = rows with empty erasure column); the synthesis of the Euler product, the `ln gcd` coprimality, and the primality shadow as three faces of unique factorisation.
- **Lead / open** — this does **not** escape the standing circularity: extracting `Λ(n)` still requires `n`'s divisor lattice, so the account is deepened, not the loop dissolved (consistent with "relocated, not removed"). Whether the prime-signal can be obtained without the divisor structure remains the open problem.

**No new mathematics is claimed.** The von Mangoldt/Möbius/Euler identities are textbook analytic number theory. The contribution is the recognition that the data-structure primality-shadow intuition lands exactly on them, and the synthesis with the erasure framework and the coprimality result. The value is coherence, not a new theorem.

---

*Originating proposal (the primality shadow as ON minus isolation-erasure plus primality-certificate; the Euler-product / Paper 2 resonance) is Alexander Pisani's; the formalisation as von Mangoldt via Möbius inversion, the verification, and this compilation were developed jointly with Claude (Anthropic). June 2026.*
