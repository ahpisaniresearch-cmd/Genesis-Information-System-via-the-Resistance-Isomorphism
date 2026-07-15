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

# Erasure as the Carrier of Mathematics

## A New Reading: the Shadows as the Trace of Irreversibility

**Alexander Pisani & Claude (Anthropic)** · June 2026 · side document · DRAFT — direction, not result

**Status.** A new reading, opened this cycle. One pillar is a **Fact** (resistance $=$ the Landauer erasure cost); the central claim — that what we read as number theory is the *shadow of erasure* — is a **Lead**, attractive and corpus-consistent, with a concrete kill-or-promote test stated in §6. Nothing here is promoted to the spine beyond the Fact (master §3.1) and the flagged direction (master §9). Written to be resumable cold.

**Role.** The next major direction for the programme. It re-reads the framework's central quantity (resistance) thermodynamically and proposes that the observable structure of number theory is the permanent record left by the only costly information-processing step — erasure. It sits downstream of, and connects, three things already in the corpus: resistance $=$ code length (Paper 3), the dissipative/storage split of the resistance plane (master §4), and the two-slit erasure result (*Probe* §7).

---

## 1. The hypothesis (Lead)

The genesis system processes information — an *encoding*, an "invisible language." Reversible processing leaves no permanent trace; it can be undone. The **only** information-processing step with an energy requirement is **erasure** (Landauer; more precisely, any logically irreversible operation, of which erasure is the minimal and canonical one). So the only permanent record a genesis computation leaves in its environment is its erasure-heat. **The hypothesis: the shadows we read as number theory are cast by erasure** — number theory is the structure of that record, and the probe's specific function casts a shadow precisely where it erases.

## 2. The pillar: resistance is the erasure cost (Fact)

The corpus already has resistance $=$ code length (Paper 3). Landauer supplies the missing leg: erasing $H$ nats of information costs $kT\cdot H$. Composing,
$$\Omega(n) = \ln n = \frac{\text{(energy to forget the integer } n)}{kT},$$
the Landauer cost, in units of $kT$, of erasing the state. **The framework's entire central quantity is a thermodynamic erasure cost.** Consequence: the resistance-based reading of number theory has *been* an erasure-ledger all along — this is recognition of what resistance thermodynamically is, not a new construction. *(Fact, given resistance $=$ code length $+$ Landauer; ⚠ Landauer classical.)*

This snaps onto two existing pieces:
- **Master §4** — the real (resistance) axis *dissipates*; the imaginary (phase) axis *stores rather than dissipates*. Dissipation is irreversibility is energy spent is erasure: **the resistance axis is the erasure axis; the phase axis is the reversible/storage axis.**
- **Probe §7** — "ignorance is free, forgetting is not"; the erase step paid exactly $\ln$ of the marker. Forgetting costs $\ln$ — costs resistance. The same identity, already measured.

## 3. Erasure and the probe are one mechanism (Reading)

The probe's *reading* is free (probe §7: a blind probe costs nothing). Its only fundamental cost is the moment of commitment — actualising one branch, which **erases the virtuality of the alternatives**. That is Axiom 5's "conversion of virtual to actual is never free," and the "never free" is precisely an erasure. So the probe casts a shadow exactly where it erases: "erasure" and "the probe's specific function" are one thing, not two. *(Well-grounded Reading: Axiom 5 + probe §7.)*

## 4. What casts shadows: visible vs inferred (Lead)

Because reversible processing leaves no record and erasure leaves heat, the hypothesis predicts a split in how number theory is *accessed*, and the split is already visible:

- The **magnitude / density** structure (resistance — dissipative, erasure) is the **directly-measured** part. We measure prime densities.
- The **fluctuation** structure (the zeros — the reversible phase axis, §4) is the **inferred** part, reconstructed from the explicit formula, never directly weighed. We infer zeros.

We measure densities; we infer zeros. That this matches is the first non-trivial sign the reading is more than re-description — but see §6: it must *predict where energy is spent*, not merely re-label.

## 5. The ontology it requires: memory, and the lattice as shadow (Reading + open)

Erasure operates on *stored* bits — you can only erase what is held. So this direction lives at the **storage / memory** level, one step past the pre-memory floor the corpus has worked at:

- **Counting** is succession *as a process* — a flow, nothing stored.
- **Storage** is a register *holding* a configuration — memory. Memory is the lattice read as held state (master §2.3, the carry register).
- A lattice point is a register configuration — the exponent vector $(e_2, e_3, e_5, \dots)$, bits held. **The integer $n = \prod p^{e_p}$ is the multiplicative readout — the shadow — of that configuration.** "The integers we see could just be shadows; the lattice could be unique states storing bits" (owner, this cycle) is exactly this: the primitive is the stored register-state; $n$ is its readout.

So the instinct to "settle what a stored integer is first" and the erasure hypothesis are the **same step**: studying erasure *is* stepping into the register layer, which is where the stored-integer ontology must be pinned. *(The register-as-primitive reading is consistent with §2.3; the full ontology is the open object to settle before the test.)*

## 6. The kill-or-promote test (the energy-ledger experiment)

The reading is a Lead, and could be mere re-description unless it predicts where energy is spent — which it does, testably, in the corpus's experimental style:

> **Run any genesis computation, account the energy. The claim is that every unit of energy is spent at an erasure, and the total energy equals the resistance erased — nowhere else.**

The probe §7 two-slit experiment already verified a *fragment*: the marker-erase paid exactly $\ln$ marker, and ignorance (reading) cost nothing. The full ledger — energy-in $=$ resistance-forgotten, with reversible steps costing zero — is the promotion path. A clean first instance: a small reversible genesis computation (FRACTRAN-style, on the lattice machine of §2.3) with a single deliberate erasure, measuring whether the energy equals $\ln$ of the forgotten state and whether every other step is free. If energy appears at non-erasure steps, or the totals disagree, the carrier reading is killed (down to the standing Fact of §2).

## 7. Grading and honesty boundary

- **Fact:** resistance $=$ ln $=$ the Landauer erasure cost of the state (given Paper 3 $+$ Landauer; ⚠ Landauer/Bennett classical).
- **Reading (well-grounded):** the probe's only fundamental cost is the erasure of alternatives (Axiom 5 $+$ probe §7); the resistance/phase axes are the dissipative/reversible (erasure/storage) axes (master §4).
- **Lead (the central claim):** number theory is the shadow of erasure; the magnitude structure is the visible (erasure) part, the phase/zero structure the reversible inferred part. Promotable only by the §6 ledger test.
- **Open before the test:** the stored-register ontology of §5 — what a held configuration is, and how it differs from the integer it shadows.

No claim is made that this resolves any open arithmetic question. It re-reads what is already in the corpus and proposes a testable mechanism; the discipline is the same as the rest of the programme — refuse to claim a breakthrough where only an established fact has been found.

## 8. Next steps

1. **Settle the stored-state ontology** (§5): pin what a register configuration is, and confirm $\Omega =$ erasure cost on a concrete held state.
2. **Run the ledger experiment** (§6): a small reversible computation with one erasure; check energy $=$ resistance forgotten, and zero elsewhere.
3. **Map the visible/inferred split** (§4): make precise that the directly-measurable structure is the resistance (erasure) face and the inferred structure is the phase face — and whether that distinction is forced or a re-description.
4. **Bridge from *Phase from the Probe*:** the genesis-prime probe is the $1$-bit measurement whose irreversible commitment is an erasure — the information–disturbance peak at $p=2$ is the same fact as the erasure cost being maximal there.

---

*Originating observation (erasure as the carrier; the invisible-encoding reading) is Alexander Pisani's; the formalisation, the resistance $=$ erasure-cost identification, the experimental design, and this compilation were developed jointly with Claude (Anthropic). June 2026. Direction, not result — graded throughout.*
