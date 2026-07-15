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

# A Catalog of Erasure Operations

## Mapping the genesis system's discrete operations by their fan-in

**Alexander Pisani & Claude (Anthropic)** · June 2026 · companion note (extensible)

**Framing.** Erasure-only cartography: map values, note where they line up, assert no mechanism of the genesis system. The organising fact is that **every irreversible operation's erasure is `ln(fan-in)`** — the log of how many inputs collapse onto the output. The `ln` is the generic Landauer signature; the **fan-in is the content**. So to map an operation is to count its fan-in. Tables lead with the **per-output fan-in** (which carries clean closed forms); the prior-dependent *mean* erasure is a secondary thermodynamic summary, shown only where illuminating. Every operation also carries the same two-legged ledger that held for the merge:

$$\underbrace{H(\text{input}\mid\text{output})}_{\text{system erasure}} \;+\; \underbrace{H(\text{output})}_{\text{demon reset}} \;=\; H(\text{input}) \quad\text{(chain rule).}$$

Claims graded Fact / Reading / Lead. Verified by `erasure_operations.py`, `rewriting_erasure.py`, `modulo_erasure.py`.

---

## 1. The additive batch (proto-integers `0..M`, uniform; here `M = 8`)

| operation | forgets | per-output fan-in | erasure |
|---|---|---|---|
| add / merge ✓ | the split | `n+1` (output `n`) | `ln(n+1)` |
| projection `(a,b)→a` | `b` entirely | `M+1` (flat) | `ln(M+1) = ln 9` |
| reset `a→0` | `a` entirely | `M+1` (flat) | `ln(M+1) = ln 9` |
| max `(a,b)` | smaller + which | `2m+1` (output `m`) | `ln(2m+1)` |
| min `(a,b)` | larger + which | `2(M−m)+1` (output `m`) | `ln(2(M−m)+1)` |

**Flat vs graded.** Projection and reset are *flat* — constant fan-in `M+1`, forgetting a whole register at a cost independent of its value (reset is the limit: forget everything, record nothing, so demon reset `= 0`). Max, min, and the merge are *graded* — fan-in varies with the output (`max`: larger max forgot more; `min`: the mirror; merge: `n+1`). Operations differ only in their fan-in *profile*; the `ln` wrapper and the two-legged structure are common to all. *(Counts and the flat/graded split: Fact. "Fan-in is the signature": Reading.)*

## 2. The string-rewriting family (conditional erasure; length-`L` strings, `L = 5`, pattern `B = "11"`)

Find the first occurrence of `B`, then act. The erasure is **conditional** — gated by the match, so the test and the forgetting are fused. Of the 32 length-5 inputs, 13 contain no `B` and pass through unchanged (fan-in 1, zero erasure); the other 19 are erased.

| operation | forgets | top per-output fan-in | erasure |
|---|---|---|---|
| truncate (find-cut) `A → prefix before first B` | suffix from `B` on | empty prefix `← 8 = 2³` | up to `ln 8` |
| delete (find-splice) `A → A without first B` | `B`'s position | `≤ 4` | up to `ln 4` |
| substitute `A → A with first B → C` | that it was `B` | `≤ 4` | up to `ln 4` |

**Conditional / bimodal cost.** Per-input erasure is zero for non-matching inputs and positive for matching ones, so the *expected* cost depends on how often the pattern occurs — a dependence with no analogue in the additive family. **Fan-in ranks the family** by how much it discards: truncate (the whole suffix, exponential collapse — shorter prefix, more free suffix) > delete (only *where* `B` was) > substitute (only *that* it was `B`). All totals equal `L·ln 2 = H(input)`. A Turing-complete discrete substrate (Markov / Post / Thue) with no quantum shadow, and the ledger is unchanged. *(Conditional/bimodal structure, ranking, exponential profile: Fact. "Test and forget fused": Reading.)*

## 3. Modulo — the multiplicative gateway (inputs `0..M`, `M+1 = 12` for its divisors)

`a → a mod m` keeps the remainder `r = a mod m` and forgets the quotient `q = ⌊a/m⌋`. The fan-in of each residue is the quotient `(M+1)/m`.

| m | per-residue fan-in | erasure | note |
|---|---|---|---|
| 1 | `(M+1)/1 = 12` | `ln 12` | = reset (all → 0) |
| 2 | `(M+1)/2 = 6` | `ln 6` | `m ∣ 12`, uniform |
| 3 | `(M+1)/3 = 4` | `ln 4` | `m ∣ 12`, uniform |
| 4 | `(M+1)/4 = 3` | `ln 3` | `m ∣ 12`, uniform |
| 6 | `(M+1)/6 = 2` | `ln 2` | `m ∣ 12`, uniform |
| 12 | `(M+1)/12 = 1` | `0` | = identity |

(Non-divisor `m`: fan-in near-uniform, `⌊(M+1)/m⌋` or `⌈(M+1)/m⌉`.)

**The fan-in is a division — the first in the catalog.** Every prior fan-in was a count or sum; modulo's is a quotient `(M+1)/m`. It interpolates `reset` (`m=1`, fan-in `M+1`) to `identity` (`m=M+1`, fan-in `1`), the one-parameter bridge indexed by `m`.

**The ledger becomes a factorization.** For `m ∣ (M+1)`: `forgotten = ln((M+1)/m)`, `recorded = ln m`, `sum = ln(M+1)`, with `(M+1)/m` and `m` a factor pair of `M+1`. Where the merge split the ledger additively, modulo splits it *multiplicatively* — `ln(M+1)` along a factorization. The gateway is visible in the ledger itself.

**Reconnects to the Stage 1 channels.** `a mod m` is the position on the `m`-cycle — the succession-channel of girth `m`. Modulo `m` is the *full* readout of the `m`-clock (the Stage 1 probe read only "at origin?"), the quotient being how many full `m`-cycles fit the range.

**Honest gateway flag.** The clean factor-pair split occurs *exactly* when `m ∣ (M+1)`; the pattern of clean-splitting `m` across all `m` is the divisor structure of `M+1` (a prime `M+1` admits only `m=1`, `m=M+1`). But reading primality off "which `m` split cleanly" *imports* the divisor structure — the same circularity Stage 1 flagged. The gateway locates the multiplicative structure (the cross-`m` divisibility pattern = the channel-bank) and warns that getting primality as an *output*, not via the indexing, is the unsolved problem. The erasure values stay non-circular. *(Divisibility–cleanness equivalence: Fact. Circularity caution: methodological, from Stage 1.)*

## 4. The two-legged ledger is universal

Across every substrate mapped — additive operations, string rewriting, modulo — system erasure plus demon reset equals the input information exactly. Nothing about an operation alters the *structure* of the ledger; only the multiplicity inside the `ln`. For modulo this multiplicity becomes a factor pair. This is the through-line of the catalog and the discipline that keeps it honest: to map an operation is to count its fan-in. *(Fact — chain rule.)*

## 5. On the horizon

- **The cross-`m` divisibility pattern** — modulo opened the gateway; the multiplicative/prime structure lives in the divisibility pattern across all `m` (the Stage 1 channel-bank), not in any single modulo. The standing problem is to make primality emerge there as an *output* of a structural test, not smuggled in through the indexing (the Stage 1 circularity).
- **Parked beyond that** — whether Goldbach prime pairs are cost-extremal (needs arithmetic phase, which needs the multiplicative structure); *cheaper-to-generate ⇒ more probable to observe*.

## 6. Grading and honesty boundary

- **Fact** — the fan-in counts and erasures of every operation mapped; flat/graded and max–min mirror symmetry; conditional/bimodal cost and the truncate > delete > substitute ranking; modulo's quotient fan-in, reset↔identity interpolation, and factor-pair ledger; the divisibility–cleanness equivalence; the universal two-legged ledger.
- **Reading** — "fan-in profile is the operation's signature, `ln` the common wrapper"; "test and forget fused" in rewriting; modulo as the full readout of the Stage 1 `m`-channel; the ledger going additive → multiplicative as the visible gateway crossing.
- **Lead / open** — the cross-`m` divisibility pattern as the locus of prime structure; primality-as-output (unsolved, circularity to avoid); Goldbach and the observation-probability lead (parked).

Classical content is Landauer (erasure = log multiplicity), the chain rule of entropy, the standard string-rewriting models, and elementary modular arithmetic. The contribution is only the systematic fan-in mapping of these discrete operations across substrates, the flat/graded and conditional-erasure observations, and the additive→multiplicative ledger crossing at modulo. No arithmetic question is claimed resolved, and the genesis system's mechanism is not asserted — only erasure values, and where they line up.

---

*Originating direction (catalog the discrete operations beyond add/count/store; the conditional-truncation example; the deliberate approach to the modulo gateway) is Alexander Pisani's; the fan-in mapping and this compilation were developed jointly with Claude (Anthropic). June 2026.*
