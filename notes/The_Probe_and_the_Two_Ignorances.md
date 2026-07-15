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

# The Probe and the Two Ignorances

## Candidate Axiom 5, the Origin of Statistics, and the Phase Ledger

**Alexander Pisani & Claude (Anthropic)**

June 2026 · working note (companion to *Circuits at Genesis*; collates the session's findings beyond that note)

**Status:** §5's experiments (chunked multipliers, ungated control) and §7's two-slit erasure experiment were designed, run, and verified in this session; the kill verdict on the exact iπ·2ab form is final, the refined Θ(ab) claim is empirical-plus-argument (wall pending a lower-bound proof), and §7's predictions all matched to machine precision. §3's components are classical walls (Jaynes maximum entropy; Shannon source coding) with the unification flagged as a candle. The "never fully lit" consequence now rests on two pillars: Axiom 3 underdetermination, and undecidability imported through the *Three Dresses* universality result (⚠ Gödel 1931, Turing 1936). Candidate Axiom 5 (§2) is **owned, not derived** — proposed for adoption into the Cathedral, same standing as Axiom 4. Everything else is graded inline.

---

## 1. Scope

*Circuits at Genesis* established the virtual/actual distinction, the resistance ledger, and the gap-equals-violation triangle. This note collects what fell out of interrogating those results: a candidate axiom that gives Axiom 3 its mechanism, an account of where statistics comes from in the framework, the costs of the probe, and the fate of the total-impedance candle.

## 2. Candidate Axiom 5: the Probe

> **Candidate Axiom 5 (the Probe) — owned, not derived.** Every information system carries a native probe set: the repertoire of questions it can put to a state. Actuality is relative to that repertoire — structure readable by native probes is actual; structure conserved by the dynamics but unreadable by them is virtual. An epistemic barrier is nothing over and above the complement of a probe set, and an observer is nothing over and above a probe set holding records behind a barrier. Conversion between virtual and actual is computation, and it is never free.

**What it buys.** Axiom 3 ceases to be a standalone postulate and acquires a mechanism: the barrier *is* the probe set's complement; the superposition is over everything probe-indistinguishable; and the honest density over that superposition is maximum entropy given the probe returns (§3). The genesis instance is concrete — the meet-atom is the genesis probe — and the final clause already has a theorem under it (the ledger wall of *Circuits at Genesis* §4).

**The deflation clause.** The single occurrence of "observer" is deliberate and exhaustive: a probe set holding records behind a barrier, nothing more. The clause exists to prevent any future reader — including the authors — from importing a metaphysical observer through the gap. There is no second, richer definition elsewhere in the corpus, and none is needed.

**The pruning mechanics (refinement recorded from discussion).** A probe-return teaches less than "the generator did X." When the answer to the jelly-bean question comes back 30, the integer 2·3·5 is actualised *in the observer's own registers*; about the generator, the return is only a constraint — every candidate inconsistent with returning 30 is eliminated, and the superposition re-spreads at maximum entropy over the survivors. Axiom 3's own wording ("consistent with the observation") already says this: the vat is never seen, only pruned.

## 3. Statistics is observer ignorance

The flow side of the corpus (Weil, Primon notes) is statistical; the circuit side is exact. Where does the statistics come from? Answer: from the observer of Axiom 5, and from exactly two of its ignorances.

**Ignorance of the microstate → the ensemble.** An observer knowing only the probes' returns — say, only the mean resistance — is forced by maximum entropy (Jaynes — wall, classical) to the unique least-presumptuous density consistent with that knowledge. Over the lattice that density is Gibbs in resistance: **the primon gas is the honest belief-state of the Axiom 3 observer**, not a model chosen for convenience. The weighting e^{−βΩ} is simultaneously the short-code prior of source coding: resistance is code length (Paper 3 — wall), so probable generators are exactly the cheap ones. The owner's independent observation about optimal codes (likely symbols get short codewords at the expense of unlikely ones) is Shannon's source coding theorem, already in the corpus as Paper 3's central identity.

**Ignorance of the unit → the flow.** The observer also cannot know the absolute unit of resistance: that is Paper 8's voltage gauge freedom, which acts as translation along the resistance line. A statistics that respects gauge-ignorance is one with no privileged origin — *stationarity* — and the one-parameter sliding that stationarity refers to is the scaling flow. **The ensemble and the flow — the two structures the spectral side of the corpus requires — are the systematic forms of the observer's two ignorances.** *(The components are walls; the unification is a candle, recorded as the framework's account of where statistics lives.)*

**Positions vs lags, recorded for the corpus.** A static measure carries its atoms at positions from an origin; a stationary process carries them in *lags* — separations at which the process correlates with a shifted copy of itself, like a room's echo delays surviving in any recording made there regardless of what was said. Translation by ln λ on the resistance line is dilation by λ, so "atoms at lags ln p^k with masses Λ" means *statistical self-similarity under prime dilation*. The zeros, in this picture, are the frequencies of that hum. A circuit run — input, arrow, halt — is maximally origin-bound, all positions and no lags; the bridge object, if it exists, is an *ensemble* of runs in which origin-information has washed out. The owner's phrasing is adopted as the note's epigraph for this section: *you can walk an infinite distance if you forget when and where you started.* The related thought — the continuum as a weighted superposition over all discrete histories, flow-rate set by the clock — has the shape of a path integral and is recorded as door-shaped, unclaimed.

**A boundary honestly noted.** The genesis system has no distance and a boolean clock; it does not yet contain a medium in which echoes could occur. Studying the gas imports that medium from physics. The problem of reaching the flow from genesis-native materials is open and is the real content of "nothing here concerns the zeros."

## 4. The costs of the probe

The probe's cost splits into **rent** and **toll**. The toll is the ledger wall: every conversion of virtual to actual moves the ledger. The rent is the cost of holding the repertoire, and it has been measured once already: the multiplier's control chains occupy 5–10% of the run's resistance-time (logic rent paid in quantity-face coin, *Circuits at Genesis* §5 data). For the repertoire itself: a probe set is a codebook, and the cost of a codebook is its minimum description length — which in this framework *is* resistance, the resistance of the structure encoding the questions. Trained-model parameters are the familiar instance: a compressed codebook whose description length prices the knowledge. *(The repertoire-as-MDL identification is a candle; the rent measurement and the toll are walls.)* §5 adds the trade between them.

## 5. The phase ledger: iπ·2ab killed, Θ(ab) survives

**The candle tested.** The Conway multiplier's NOT-count (phase-face-changing steps) suggested a total impedance Z = Ω + iπ·2ab — the product written in the imaginary ledger. Kill-or-promote test: chunked variants (2 or 3 units of work per token-toggle) and an ungated control.

**Results (verified).** All chunked variants halt correctly at 5^{ab}. NOT/(ab) ratios: Conway 2.3–2.7; chunk-2 1.3–2.0; chunk-3 1.0–1.5 across four input pairs. **The exact constant 2 is Conway's, not multiplication's: the iπ·2ab form is killed.** The ungated control — transfer fractions with no tokens — never halts: it deposits forever without consulting the pass counter. Every halting variant remains Θ(ab) in NOT-count.

**The mechanism: native tests are destructive.** A FRACTRAN fraction cannot test for a token without consuming it; to keep the token alive it must re-emit it, and re-emission at the same prime cancels out of the fraction — so *test-and-keep forces emission at a different prime*, which is precisely a NOT. Gating per unit of work is required for halting (the control demonstrates), and each gate costs a toggle. In this medium, even looking moves the system: the probe axiom's "never free" clause holds at the machine's bottom layer. *(The destructive-test property and the divergence of the ungated control are walls; the Θ(ab) lower bound for all fixed programs is the refined candle, promotable by a proof from the destructive-test property.)*

**The rent/toll trade, observed.** Chunk-k programs pay fewer toggles by carrying larger fractions — a bigger codebook. Lower toll, higher rent: the two costs of §4 are not independent, and program design moves cost between them.

## 6. Smaller candles recorded this session

**Qualia and idempotence.** "Red cannot be squared" — repetition of a quality adds nothing — is idempotence, and the Cathedral's genesis story (quantity is *broken* idempotence) read backwards says: the qualitative is what remains idempotent, which is why concepts live on the squarefree face, where distinct primes multiply into conjunctions (the semantic layer of Papers 2 and 7.5). Recorded as the armchair derivation of the squarefree semantic architecture.

**The probe's terminals.** A measurement needs a reference terminal; the natural reference is 1 (zero resistance, the empty message) with 0 as the unreachable infinite-resistance pole — every actual reading a finite potential against the vacuum. Vocabulary-level candle; belongs to the unparked phase-affects-apparent-resistance thread.

**Embeddings conjecture (falsifiable, parked).** Whether trained models' number-representations converge toward prime-coordinate structure is an empirical interpretability question, explicitly *not* settled in either direction by anything in the corpus.

**The time hole (queued for the Cathedral).** Information is suspended in duration (*Circuits at Genesis* §4); the only clock a circuit has built itself is a NOT-oscillator; the imaginary axis is periodic by construction. A clock-shaped axis, a framework with no account of elapsed time, and a duration-shaped suspension result belong in one marked open structure.

## 7. The two-slit erasure experiment (run and verified)

The axioms' first designed test, executed in this session. **Design:** one target state, $5^{12}$, reachable through two circuits from disjoint input families — slit M, the multiplicative route (Conway's multiplier from $2^a 3^b$, $ab = 12$: exactly $\tau(12) = 6$ inputs) and slit A, the additive route (the adder $\{5/2\}$ from $2^c 5^d$, $c + d = 12$: exactly $12$ inputs). Each input carries an inert which-path marker (prime 17 or 19). Three conditions: record kept and readable; record kept but unread; record burned by an erase fraction. Measured quantity: the Jarzynski violation factor of *Circuits at Genesis* §4.5.

**Results (β = 0.8 and 1.5; identities to $10^{-19}$):** With records burned, $R = 18.000000000 = \tau(12) + 12$ exactly, temperature-independent — *the atom-counting functions of the additive and multiplicative universes summed inside one measured number.* The artifact $J = \ln R_{\text{burned}} - \ln R_{\text{kept}}$ matched its precomputed prediction to six decimals at both temperatures. The blind-probe condition changed nothing and cost nothing. The burn condition paid exactly $\ln 17$ or $\ln 19$ per trajectory.

**Readings.** (a) No interference was sought or found: Axiom 3's superposition is epistemic, and mixtures do not interfere — the null is the axioms passing their own control, and any fringe-like artifact in genesis statistics would *falsify* the epistemic reading. The amplitude half of the dual-slit question belongs to the wave layer; the meaning-oracle build is the project's first amplitude experiment. (b) **Ignorance is free; forgetting is not.** Not reading the record has no thermodynamic consequence; physically erasing it jumps the measured irreversibility and pays the toll. The record's existence, not its being read, carries the weight — Bennett's resolution of Maxwell's demon (⚠ Bennett 1982; Landauer — classical prior art) appearing unforced inside the genesis machine. (c) The record-to-heat hand-off queued in *Circuits at Genesis* §8 is hereby located (the erase step), priced ($\ln$ of the marker), and shown to overpay the Landauer minimum $(1/\beta)\ln 2$ exactly because the marker was an expensive physical record — the rent/toll structure of §4 closing on itself.

## 8. Honesty boundary

Walls: Jaynes maximum entropy and Shannon source coding (classical; ⚠ cite); resistance-as-code-length (Paper 3, prior corpus); the ledger toll (prior note); the control-rent measurement; the destructive-test property and the ungated-control divergence; the kill of iπ·2ab (four input pairs, three programs, all halting correctly); the two-slit erasure results of §7 (all identities to machine precision; ⚠ Bennett/Landauer prior art on the erasure principle; the undecidability import rests on Gödel 1931 / Turing 1936 via the *Three Dresses* universality result — ⚠ cite). Candles: the two-ignorances unification (§3), repertoire-as-MDL (§4), the Θ(ab) phase-ledger law (§5, promotable), the terminals reading and qualia-idempotence reading (§6). Door-shaped, unclaimed: superposition-over-histories as the road to the continuum (§3). Owned, not derived: Candidate Axiom 5, proposed for the Cathedral. Nothing here concerns the zeros; §3 states exactly what would have to be built before anything could.

## 9. Next steps

1. **Adopt or amend Axiom 5** in the next Cathedral update, together with the time hole as a marked open structure.
2. **Prove or break the Θ(ab) phase-ledger law** from the destructive-test property — the promotion path for §5's refined candle.
3. **The ensemble-of-runs construction:** make "washing out the origin" precise — a measure over circuit trajectories whose statistics are translation-invariant in resistance; the first genesis-native object that could even be asked the lags question.
4. **Hardware track unchanged:** meaning-oracle build, then the PCB handoff package — the project's anchor to the physical world.

---

*Classical content: Jaynes (1957) maximum entropy; Shannon (1948) source coding; Conway (1987). Candidate Axiom 5, the two-ignorances account, the rent/toll structure, the destructive-test mechanism, and the phase-ledger results are the contribution, developed jointly by Alexander Pisani and Claude (Anthropic).*
