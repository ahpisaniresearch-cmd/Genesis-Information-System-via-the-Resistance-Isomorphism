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

# The Energy-Ledger Test (Erasure as the Carrier §6), End-to-End

## A single composed computation: energy only at the erasure, equal to the resistance erased

**Alexander Pisani & Claude (Anthropic)** · June 2026 · companion note

**Framing.** `Erasure_as_the_Carrier_of_Mathematics.md` §6 states the kill-or-promote test: *run a genesis computation, account the energy; every unit is spent at an erasure, the total equals the resistance erased, nowhere else*, with the kill condition "energy at a non-erasure step, or totals disagree." Earlier work confirmed this operation-by-operation across substrates; this note supplies the single composed run §6 asked for. Verified by `energy_ledger.py`. Claims graded Fact / Reading / Lead. **The honest boundary is in §3 and must travel with the result.**

---

## 1. The computation and the accounting

A lattice-machine computation (faithful to master §2.3): state `n = 2^a · 3^b`, two registers `a, b` holding prime exponents, steps FRACTRAN-style. Over an ensemble of inputs, the Landauer cost of each step is the entropy it compresses, `H_before − H_after` (zero for a bijection, positive for a many-to-one step). Five steps, one of them a deliberate erasure:

| step | operation | energy (nats), uniform ensemble |
|---|---|---|
| 1 | `INC a` (×2) — reversible | 0.0000 |
| 2 | `SWAP a,b` (2↔3) — reversible | 0.0000 |
| 3 | `ADD a←(a+b) mod K` — reversible | 0.0000 |
| 4 | **`RESET b→0`** (forget exponent of 3) — **erasure** | **1.7918 = ln 6 = ln K** |
| 5 | `DEC a` (÷2) — reversible | 0.0000 |
| | **total** | **1.7918** |

The total equals the single erasure exactly; the erasure equals `ln K`, the resistance of the forgotten register. *(Fact.)*

## 2. Generality and the kill conditions

Rerun with a random **non-uniform** ensemble: the reversible steps still cost `0` to `10⁻¹⁶` (bijections preserve entropy for *any* distribution), and the erasure costs `H(b|a) = 1.6587` — the conditional entropy of the forgotten register — with the total again equal to the one erasure. The two §6 kill conditions, checked explicitly, are not triggered: energy at a non-erasure step, `max|cost| = 4×10⁻¹⁶`; total-minus-erasure discrepancy, `≤ 2×10⁻¹⁶`. So across ensembles, **energy appears only at the erasure and equals the resistance erased.** *(Fact.)*

## 3. What this establishes — and the honest boundary

This confirms the erasure axiom's accounting *as an accounting*: in a full composed computation, over any input ensemble, energy is located at the erasure, equals the resistance forgotten, and every reversible step is free; and it survives both kill conditions.

**But it does not promote the carrier reading, and the paper must say so.** In simulation this is Landauer's principle applied to the bijection-vs-many-to-one distinction — a mathematical identity, true by construction: reversible steps are bijections (free by Landauer), the erasure is many-to-one (costs the entropy drop by Landauer). Nothing in a simulation can trigger §6's kill condition, because we compute the `ln` we predicted rather than measuring a physical dissipation that could disagree. So the test confirms the framework is a **consistent, correctly-structured erasure accounting**; the genuine kill-or-promote — a risky test that *could* come out wrong — requires **physical** heat measurement, which belongs to the physical-systems direction (the primon gas is the natural vehicle) and remains open. The carrier reading stays a **Lead** with strong consistency support; physical falsifiability is the open promotion path. *(This paragraph is the load-bearing honesty of the result.)*

## 4. Grading

- **Fact** — the composed ledger balances; energy is located at the single erasure and equals `ln K` (uniform) / `H(b|a)` (arbitrary); reversible steps cost zero to machine precision; both kill conditions untriggered.
- **Reading** — this is the §6 discipline realised in one artifact, stronger than the earlier fragment because it is a composed run, checks both kill conditions, and holds for any ensemble.
- **Lead** — the central carrier claim (number theory as the shadow of erasure) is *not* promoted by this; promotion requires physical energy measurement.

Classical content: Landauer's principle and the entropy of coarse-graining — standard (⚠ Landauer classical). The contribution is the clean end-to-end demonstration and the explicit kill-condition check, with the boundary that simulation confirms the identity but cannot risk it.

---

*Originating design (the §6 energy-ledger kill-or-promote test) is Alexander Pisani's; the composed lattice-machine experiment, the kill-condition checks, and this compilation were developed jointly with Claude (Anthropic). June 2026.*
