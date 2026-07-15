# E8 Results — The Two-Path Merge: State, Process, and the Interference Gate

**Madness in the Probe sub-programme · design experiment, two stages · July 2026**
**Alexander Pisani & Claude (Anthropic)**

---

## Status

**STAGE A: ALL 26 COMMITTED/STRUCTURAL CHECKS PASSED. Exact enumeration; no Monte Carlo. Banking run complete.**

**STAGE B: GATE SUBMISSION ONLY — no Stage B code was written (the gate is mandatory and blocking). The submission below carries the lawful phase-assignment rule, the two null families it produces, the instantiated discriminator, the classical-mixture statement, and a self-audit. The self-audit finds that every null the lawful rule can reach hits a register KILL condition, and the one *forced* coherent object provably does not cancel. The recommended register verdict is therefore PARK, with the obstruction mapped precisely. Stage B results, if the lead signs off on a construction I have not found (a multi-merge escape), would follow in a second part after sign-off.**

The Stage A pre-registered prediction — *all committed measures pass, with MA3(c) held as a hypothesis whose failure would itself be the finding* — held in full. No committed bar was moved; no result was patched. MA3(c) is **confirmed**: the balanced split attains the enumerated maximum of S_p at every m ≤ 8 (with ties, as permitted). No survivor appeared: no tree violated the floor theorem, no prime-swap changed the ledger's integer structure, and no squarefree record carried tree information.

**The result, in one line (Stage A).** *Build the same integer two ways and the value is identical while the overlap ledger is not — and the ledger's structure is a function of multiplicity alone, blind to which primes carry it; where multiplicity is absent (squarefree), the assembly leaves no trail at all, and erasing the record returns exactly the integer.*

Implemented fresh for E8 only. No prior script was consulted or reused; the corpus documents were read for context, not copied into the implementation. The §5 pre-run derivation check (the (2m−3)!! counts, the 3/15 balanced fraction, H(3/15) = 0.500402, the floor theorem, the additive replication values) was performed before any check was written and is honoured exactly; it surfaced no discrepancy to escalate.

---

## Reproducibility block

| Item | Value |
|---|---|
| Script | `523_e8_twopath.py` (fresh; PID-prefixed) |
| Recorded seed | `20260710` (form only; **no sampling occurs** — Stage A is exact enumeration) |
| Runtime PID (this run) | `523` |
| Exit code | `0` (all committed checks passed) |
| Python | 3.12.3 |
| mpmath | 1.3.0 (dps=50 cross-check of the two float-sensitive quantities) |
| Precision | float64 + integer arithmetic throughout; one **mpmath dps=50** recomputation of H(3/15) and the MA2a decomposition residual |
| Enumeration | full leaf-labelled binary-tree enumerations, count `(2m−3)!!` asserted for m = 2..8; **no Monte Carlo anywhere** |
| Multisets | pure powers p^m (p ∈ {2,3,5}, m = 4..8); mixed {p,p,q},{p,p,q,q},{p,p,p,q,q}; squarefree {p,q},{p,q,r},{p,q,r,s} |

**Precision justification (the E3/E7 convention, carried).** Every Stage A quantity is either an integer (S_p, E, D, tree counts — exact) or a small entropy/log in nats (H(3/15) ≈ 0.5; overlaps ≤ ~5). float64 carries ~15–16 significant digits, so absolute error is ≲10⁻¹⁴ at this scale; the (E−D)/2 identity is pure integer arithmetic (residual **exactly 0.0**). The tightest float bar (MA2a at 10⁻¹²) clears by ~1000×, and the **mpmath dps=50** recomputation confirms the residuals are honest float artefacts, not masked violations: H(3/15) agrees to **2.0×10⁻¹⁷**, and the MA2a decomposition residual is **1.1×10⁻⁵⁰** at dps=50 (float64 reported a worst-case 1.78×10⁻¹⁵ over all trees). E4's ≥800-digit regime was continued-fraction-specific and does not transfer here (E3 ratification, carried).

**Pre-registered bars** are copied verbatim into the script header (before any check was written) and are reproduced with actuals below.

### Implementation choices (documented, within remit)

- **Canonical unordered tree enumeration.** Trees are leaf-labelled binary trees with unordered children, de-duplicated by the rule "the child containing the smallest leaf-label is *left*." This yields exactly `(2m−3)!!` trees (asserted for m = 2..8), and each tree is enumerated once. Leaves are indices into the actual prime multiset.
- **The record is the ordered (post-order, canonical-left) sequence of per-merge overlaps.** Because pure-power leaves are structurally identical, all labelled trees of one shape yield the *same* ordered record; the multiset of overlaps gives the identical shape partition, so MA4's mutual-information results are invariant to the ordered/multiset choice. The ordered form is reported (it is what a real ledger would emit).
- **S_p and (E,D) computed by independent routes.** S(T) is computed via integer `gcd` of the two subtree product-values; S_p via per-prime `min(v_p(left), v_p(right))` sums; E and D via the branch-node `(L_p+R_p)` and `|L_p−R_p|` on the p-projected tree. The three are separate enumerations, so MA2a and MA3b are measured coincidences, not restated definitions.
- **Balanced/caterpillar/smallest-first constructed independently.** The balanced tree (ceil/floor split), the caterpillar, and the smallest-first (heap-Huffman) build order are each constructed directly and compared to the *enumerated* max/min, so MA3(c) and MA5's minimiser claims are checks against the full enumeration, not against themselves.

---

## Stage A — pre-registered bars vs actuals

| Check | Bar | Actual | Verdict |
|---|---|---|---|
| counts (2m−3)!! m=2..8 | len == (2m−3)!! | `[1,3,15,105,945,10395,135135]` | **PASS** |
| **MA1** root value = n *(structural)* | root == n every tree | all equal | **PASS** |
| **MA1** resistance conservation *(structural)* | \|ln(ab)−ln a−ln b\| ≤ 1e-12 | **1.78e-15** | **PASS** |
| **MA1** additive merge creates ln(m+1) *(contrast)* | min created > 0 | **1.6094** | **PASS** |
| **MA2a** decomposition S = Σ_p ln p·S_p | \|·\| ≤ 1e-12 | **1.78e-15** | **PASS** |
| **MA2b** prime-swap: {S_p} identical over p∈{2,3,5} *(exact-by-constr.)* | vectors identical, m=4..8 | all True | **PASS** |
| **MA3a** floor S_p ≥ m_p−1 | no tree below floor | min at/above floor | **PASS** |
| **MA3a** equality IFF caterpillar-in-p | at_floor ⇔ singleton p-side every uniting merge | IFF holds | **PASS** |
| **MA3a** anchors p⁴ bal=4 cat=3 | bal==4 and cat==3 | bal=4 cat=3 | **PASS** |
| **MA3b** identity S_p = (E−D)/2 | \|·\| ≤ 1e-12 | **0.00e+00** | **PASS** |
| **MA3c** balanced attains max S_p (m≤8, ties ok) | balanced == enumerated max each m | `{4:(4,4),5:(5,5),6:(7,7),7:(9,9),8:(12,12)}` | **PASS** |
| **MA4a** p⁴: 3 balanced-shaped of 15 | count == 3 | 3 of 15 | **PASS** |
| **MA4a** H(shape\|record) = 0 | == 0 | **0.00e+00** | **PASS** |
| **MA4a** I(record;shape) = H(3/15) | \|·−0.5004024\| ≤ 1e-6 | **0.500402** | **PASS** |
| **MA4b** squarefree: gcd=1, record constant, I(record;tree)=0 | all three families | all True, I=0.0 | **PASS** |
| **MA4c** value = n for every tree *(structural)* | single value == n | constant | **PASS** |
| **MA5** eight-1s chain = 12.11 | \|·−12.11\| ≤ 1e-2 & == enum max | **12.1087** | **PASS** |
| **MA5** eight-1s balanced = 9.81 | \|·−9.81\| ≤ 1e-2 | **9.8105** | **PASS** |
| **MA5** eight-1s smallest-first == enum min | sf == min(costs) | 9.8105 == 9.8105 | **PASS** |
| **MA5** eight-1s balanced == smallest-first | bal == sf | 9.8105 == 9.8105 | **PASS** |
| **MA5** {2,2,2} sf = 3.56 | \|·−3.56\| ≤ 1e-2 | **3.5553** | **PASS** |
| **MA5** {1,2,3} sf = 3.33 | \|·−3.33\| ≤ 1e-2 | **3.3322** | **PASS** |
| **MA5** {1,1,4} sf = 3.04 | \|·−3.04\| ≤ 1e-2 | **3.0445** | **PASS** |
| **MA5** ordering {2,2,2}>{1,2,3}>{1,1,4} | 3.56>3.33>3.04 | 3.555>3.332>3.045 | **PASS** |
| **MA5** smallest-first == enum min (each 3-piece) | sf == min all three | residuals 0.0 | **PASS** |
| **MA5** floor = ln(N+1) at single merge (N=8) | single==ln9 & < any ≥3-part build | single=2.1972, best finer=3.2958 | **PASS** |

**26/26 committed/structural checks passed.**

---

## Stage A — per-measure detail

### MA1 — the state function (wiring, structural)

The multiplicative merge conserves resistance at every step: `ln(ab) = ln a + ln b` to 1.78×10⁻¹⁵ on every merge of every tree, and the root value equals n on every tree. So the multiplicative register **creates no resistance at any step** — the root's ln n is exactly the sum of the leaves' resistances, independent of the merge tree. This is the isomorphism as a consistency check, and it is the contrast object for the additive register, where every merge *creates* ε(m) = ln(m+1) > 0 (checked: minimum created = 1.6094 > 0). The arithmetic value is a **state function**; the heat is not. *(Structural flag: the conservation is a float identity, not a measured surprise; the root=n check is a genuine wiring test that a summing-instead-of-multiplying bug would fail.)*

### MA2 — kernel-blindness of the process ledger

**(a) Decomposition.** The overlap ledger S(T) = Σ_merges ln gcd(left,right), computed via integer gcd, equals Σ_p ln p · S_p(T) computed via per-prime min-sums, to 1.78×10⁻¹⁵ on every tree. Two independent routes agree.

**(b) Prime-swap invariance (exact-by-construction).** For each pure-power family p^m (m = 4..8), the integer vector {S_p(T)} over the tree enumeration is **identical** across p ∈ {2,3,5} — computed independently for each prime from its own exponent structure. The overlap ledger's integer skeleton is a function of the exponent pattern only; which prime carries the multiplicity enters S(T) *only* as the scalar ln p, never as structure. This is the register's **kernel-blindness**, now a check computed from the enumeration. *(Flagged exact-by-construction: the S_p integer is manifestly independent of the prime's value, so equality is structural; the computation is nonetheless run independently per prime, so a prime-asymmetric bug would break it.)*

### MA3 — the extremal structure of the process ledger

**(a) The floor theorem (exact, all enumerations m ≤ 8).** S_p(T) ≥ m_p − 1 on every tree, with **equality iff every p-uniting merge has a singleton p-side** (the caterpillar-in-p class). Both the inequality and the IFF are verified exhaustively. The two-line proof: the m_p p-atoms must be gathered into one subtree, which takes exactly m_p − 1 merges that unite p-content, and each such merge contributes min(L_p, R_p) ≥ 1; equality forces every one of those mins to be 1, i.e. one side a single p-atom. Anchors confirmed: p⁴ balanced S_p = 4, caterpillar S_p = 3.

**(b) The identity S_p = (E − D)/2 (exact, every tree, residual 0.0).** On the p-projected tree, overlap equals external path length minus imbalance, halved: min(L,R) = ½[(L+R) − |L−R|], summed over branch nodes gives ½(E − D). Computed with E and D from independent branch-node accumulations; the residual is **exactly zero** (pure integer arithmetic). Overlap is path length corrected for imbalance.

**(c) Balanced attains the maximum (hypothesis → confirmed, ties permitted).** The enumerated maximum of S_p is **4, 5, 7, 9, 12** for m = 4..8, and the balanced (ceil/floor) tree attains it at every m. For m a power of two the balanced tree is the unique-shape maximiser; for other m the maximum is attained by a *set* of shapes (e.g. m = 6: both the balanced (3,3) split and the (4,2)-with-balanced-4 split reach 7) — the ties the brief anticipated. The pre-registered hypothesis holds; had it failed at any m the true maximiser would have been reported as the finding.

### MA4 — the record and the quotient

**(a) The record determines the shape, and prices it.** For p⁴ under the uniform distribution on its 15 labelled trees, there are exactly **3 balanced-shaped** and 12 caterpillar-shaped trees. The record determines the shape class exactly (H(shape\|record) = 0.0), so I(record;shape) = H(shape) = **H(3/15) = 0.500402 nats**. The overlap ledger of a multiplicity-bearing assembly carries half a nat about how it was built.

**(b) Kernel anonymity (the paired Reading, exact).** For every squarefree multiset ({p,q}, {p,q,r}, {p,q,r,s}), every per-merge gcd is 1, the record is **constant across all trees** (a single distinct record per family), and I(record;tree) = **0 exactly**. Path memory lives in multiplicity; a kernel-only assembly leaves no trail. The value-plus-resistance quotient, path-erased, is exactly the multiplicative shadow — the record adds nothing, and erasing it returns n and only n.

**(c) The value carries zero tree information (structural).** The multiplicative value is n for every tree of every multiset — one distinct value per multiset, by construction — so I(value;tree) = 0 structurally. Stated, not presented as measured. This is the state/process split in one line: **all the path information the record carries is orthogonal to the value; erase the record and exactly the value survives.**

### MA5 — additive replication (ties E8 to the banked spoke)

The banked *Additive Merge* results reproduce exactly by full enumeration. Eight 1s building 8: linear chain **12.1087** (= the enumerated maximum), balanced **9.8105**. Three-piece builds of 6: {2,2,2} **3.5553** > {1,2,3} smallest-first **3.3322** > {1,1,4} smallest-first **3.0445**. The floor ln(N+1) = ln 9 = **2.1972** is attained only by the single 2-leaf merge; the cheapest ≥3-part build of 8 costs 3.2958 > 2.1972. Smallest-first is the enumerated minimiser for every multiset tested (residuals 0.0). Build-erasure is a path function with a state-function floor; the multiplicative register's conserved-per-merge resistance (MA1) is exactly the contrast that isolates the additive register's per-merge creation.

---

## Plain-language summary (Stage A)

Think of building a number by repeatedly gluing two smaller numbers together. There are many orders to glue in, and they form a tree.

- **The number you get is always the same; the "receipt" is not.** However you glue the prime factors of n together, the product is n — the value doesn't care about the order. But each gluing leaves a line on a receipt (how much the two pieces already had in common), and different gluing orders leave different receipts. Value is the destination; the receipt is the road.
- **The receipt only sees repetition, not identity.** If you build 2⁴ = 16 versus 3⁴ = 81, the *shape* of the receipt is identical — the only difference is a scale factor. The receipt records *how many* of each prime got stacked and in what order, never *which* prime. Kernel-blind.
- **If nothing repeats, the receipt is blank.** Build a product of *distinct* primes (say 2·3·5·7) any way you like, and every gluing joins two things with nothing in common — every line reads zero. All the orders leave the *same* (blank) receipt: with no repetition there is no trail. Tear up that blank receipt and you have lost nothing — the number is right there.
- **When there is repetition, the receipt is worth exactly half a nat.** For 2⁴ there are 15 ways to glue, falling into two shapes; the receipt tells you which shape you used, worth H(3/15) ≈ 0.50 nats of "how it was built."

Everything landed where it was predicted. The one open hypothesis — that the most-balanced gluing order leaves the *heaviest* receipt — came out true at every size (sometimes tied with a near-balanced order).

---

# PART 2 — Stage B gate submission

*Per §4 and §6.6 of the brief, this section is submitted to the lead **before any Stage B check is written**. It contains (i) the phase-assignment rule with a self-audit, (ii) the committed null family with derived phase differences, (iii) the discriminator instantiated, and (iv) the classical-mixture statement — followed by the register self-audit and the recommended verdict. No Stage B experiment code exists; the phase differences below are **derived**, and were confirmed arithmetically as part of constructing this submission (this is the "derived phase difference" the gate asks for, not a Stage B run).*

## B(i) — The lawful phase-assignment rule (audit-clean), with self-audit

**Object.** A build path to N is a **plane (ordered) additive merge tree**. Each merge has output size mᵢ and a **forced split index** kᵢ = the size of the left subtree — i.e. the ordered split (kᵢ, mᵢ−kᵢ) among the (mᵢ+1) preimages of the reverse-scattering. A *real* build has kᵢ ∈ {1,…,mᵢ−1} (both pieces nonempty).

**Phase.** At each merge, the clock Z — generated from {S, D} on the (mᵢ+1)-dim preimage space via |k⟩⟨k| = Sᵏ D S⁻ᵏ, Z = Σₖ ωᵏ|k⟩⟨k|, ω = e^{2πi/(mᵢ+1)} — acts on the split state |kᵢ⟩, giving phase ωᵢ^{kᵢ} = e^{2πi kᵢ/(mᵢ+1)}. This is the **phase-preserving (reversible) reading** of the merge: the coherent state Σₖ ωᵏ|k⟩ whose decoherence *is* the merge-erasure ln(mᵢ+1) (*Phase on the Merge* §2, banked).

**Path amplitude.** θ(P) = 2π Σᵢ kᵢ/(mᵢ+1) (product of per-merge clock phases); classical weight w(P) = Πᵢ 1/(mᵢ+1) = e^{−E(P)} (the reverse-scattering's uniform measure; E(P) the build-erasure of MA5). Amplitude **A(P) = √w(P)·e^{iθ(P)}**, so |A(P)|² = w(P) = the classical probability, and *all* interference lives in the cross terms — exactly the structure *Additive Merge* §3 anticipated ("order-dependence laid over amplitudes becomes interference").

**Self-audit against the audit list (exhaustive):**

| Ingredient used | On the audit list? |
|---|---|
| ω = e^{2πi/(mᵢ+1)} on the (mᵢ+1)-dim preimage (an erased multiplicity) | ✅ yes (roots of unity on erased-multiplicity spaces) |
| kᵢ = positional split index (left tally length), the only per-split label | ✅ yes (tally length is the additive layer's native quantity; no primality/multiplicative content imported) |
| Z generated from {S, D}; D = |0⟩⟨0|; S the succession shift | ✅ yes |
| No hand-painted continuous phases (all phases are roots of unity) | ✅ compliant |
| No per-split label carrying arithmetic content (kᵢ is positional, per *Phase on the Merge* §3) | ✅ compliant |

**One honest caveat on the rule.** Attaching Z-phase to the build is the phase-*preserving* reading; the merge dynamics *as run* **decohere** (that is their irreversibility — MA5 / *Phase on the Merge* §2). Whether the dynamics **force** this phased state, rather than merely permit it, is precisely the corpus's parked open question (*Additive Merge* §3, *Phase from the Probe* §6, *Phase on the Merge* §1, each stating it independently). The rule above is the **most-charitable lawful phase available**; I carry it forward and test whether, granted it, a *non-classical* null is forced.

## B(ii) — The committed null family (derived phase differences)

Under this rule, exactly two families of build-path cancellation exist. Both are single-merge (the atomic interference unit); the derived phase differences were confirmed arithmetically (values in the pre-run check).

**Family α — two-path mirror nulls.** A single merge to output m = 4k+1 has mirror splits (k, m−k) and (m−k, k) with phase difference 2π(m−2k)/(m+1) = **π** (since m = 4k+1 ⇒ m−2k = (m+1)/2). Equal weight (same output m). **Committed instance:** N = 5; P₁ = (1,4)→5 (k=1, θ₁ = π/3), P₂ = (4,1)→5 (k=4, θ₂ = 4π/3); Δθ = π; |A₁+A₂|² = 0 (|ω¹+ω⁴| = 4.6×10⁻¹⁶, ω = e^{2πi/6}).

**Family β — three-path cube-root nulls (genuinely complex).** A single merge to output m with m+1 = 3j has three splits k, k+j, k+2j at the cube roots of unity; all three are interior when j ≥ 3 (m ≥ 8). **Committed instance:** N = 8; P₁,P₂,P₃ = (1,7),(4,4),(7,1)→8 (k = 1,4,7); phases 2π/9·{1,4,7}, mutually 2π/3 apart; |A₁+A₂+A₃|² ≈ 3×10⁻³¹ (|ω¹+ω⁴+ω⁷| = 5.7×10⁻¹⁶, ω = e^{2πi/9}). Equal weight (all output 8).

## B(iii) — The discriminator, instantiated

- **Each path carries nonzero, equal classical weight:** Family α both w = 1/6; Family β all w = 1/9. ✅
- **|Σ amplitudes|² ≤ 10⁻⁹ × classical (probability-sum) value:**
  - Family α: |A₁+A₂|² = 0 vs classical sum w₁+w₂ = 1/3 → ratio 0 ≤ 10⁻⁹. ✅
  - Family β: |A₁+A₂+A₃|² ≈ 3×10⁻³¹ vs classical sum 1/3 → ratio ≈ 10⁻³⁰ ≤ 10⁻⁹. ✅

## B(iv) — The classical-mixture statement

A classical mixture of the same nonzero-weight paths is the probability sum Σᵢ wᵢ, **bounded away from zero** (both families: 1/3). So a null (|Σ amp|² → 0) at these fixed N is *not* something a mixture of the same ledgers can produce — the theorem that would make such a null non-classical, *if* the null itself were non-classical. The next section tests exactly that "if."

---

## Register self-audit and recommended verdict: **PARK (interference reading killed for every reachable null; the forced object provably does not cancel)**

The §4 KILL clause: *kill the interference reading if the null is reproducible by a signed classical ledger without the modulus-squared amplitude structure, or if the null depends on k-assignments chosen rather than forced by the construction.* Applied to the two families:

**Family α is killed as classical bookkeeping.** For any two paths of equal weight w, |A₁+A₂|² = 2w(1 + cos Δθ), which vanishes iff Δθ = π, i.e. A₂ = −A₁. A **signed classical ledger** reproduces this exactly: assign real signs (+,−) to the two equal weights, s₁√w + s₂√w = 0 — no complex phase, no modulus-of-a-sum. This is the genesis-bit NOT-cancellation 1 + (−1) = 0 (*Weyl-Clock* §1) in disguise. **Every** equal-weight two-path null is real-sign-reducible; the modulus-squared structure does no work. Interference reading: **killed**.

**Family β is genuinely complex — and killed as a chosen subset.** Three equal real signs cannot sum to zero (an odd sum), so no signed classical ledger with equal weights reproduces the cube-root null: Family β *is* non-classical. But it is killed by the second condition. The set {(1,7),(4,4),(7,1)} is a **chosen** sub-selection of the builds of 8 — the splits with k ≡ 1 (mod 3). The **forced** object — the coherent sum over *all* real (interior, both-pieces-nonempty) single-merge builds of output m — provably does **not** cancel:

$$\sum_{k=1}^{m-1}\omega^{k} \;=\; \underbrace{\sum_{k=0}^{m}\omega^{k}}_{=\,0}\;-\;\omega^{0}\;-\;\omega^{m}\;=\;-1-\omega^{-1},\qquad \bigl|{-1-\omega^{-1}}\bigr| \;=\; 2\cos\!\frac{\pi}{m+1}\;>\;0\quad(m\ge 2).$$

(Measured: 1.7321 at m = 5, 1.8794 at m = 8 — matching 2cos(π/6), 2cos(π/9).) The **only** exact single-merge cancellation is the full roots-of-unity sum Σ_{k=0}^{m} ωᵏ = 0, and that cancellation is carried **entirely by the two empty splits** k = 0 (=(0,m)) and k = m (=(m,0)) — "merge with a null tally," an operation the additive dynamics **never perform**. To recover the cube-root triple is to impose a residue-class (mod j) grouping that the audit list does not contain (it supplies ω and positional k, not a mod-j superselection). Interference reading: **killed** (chosen, not forced).

### The parking diagnosis, stated precisely

Proto-phase **does** couple to the merge lawfully — the rule of B(i) is audit-clean and reproduces the banked phase-cost = merge-erasure fact. What it does **not** do is force a *non-classical* null:

1. **The only forced coherent object cancels on the empty splits.** The reverse-scattering's uniform, clock-phased sum over a merge's (m+1) preimages cancels exactly (Σ all roots = 0) — but that cancellation lives on the two null-tally splits. Restricted to real builds (interior splits), the forced sum is 2cos(π/(m+1)) ≠ 0: it never vanishes.
2. **Every cancellation a real build can reach is either sign-reducible or cherry-picked.** Two-path mirror nulls reduce to the genesis-bit sign 1 + (−1) = 0 (classical bookkeeping); the one genuinely-complex null (the cube-root triple) requires selecting a residue class off the audit list.

So a *forced non-classical* two-path null requires an ingredient off the audit list — **the empty-tally merge** (an unphysical operation) or **a chosen residue-class grouping** (an unlicensed label). This is the corpus's open dynamics gap (*"whether the merge dynamics produce a definite phased state — open"*) **mapped to a precise obstruction**: the empty split is exactly the missing ingredient. The additive layer's phase is real, its cost is the merge-erasure, and its cancellations are genuine — but they are the **trivial (uniform, sign-reducible)** kind, not the **hard (logarithmic, phase-essential)** kind that *Weyl-Clock* distinguishes and that a surplus-structure result would need.

**Scope of the proof and the residual open piece.** The obstruction is **proven exactly at the single-merge level** (the atomic interference unit), and both general escape routes are off-audit. A *multi-merge* forced null — a coherent sum over all real multi-merge builds of a fixed N with fixed weight vanishing — is **not** ruled out by the single-merge proof alone; it would be a genuinely new construction, and it would still have to evade both off-audit ingredients. I did not find one, and the same empty-split mechanism governs each merge in any such sum, so my prior is that the obstruction is structural. This is the one place a determined construction could be attempted; it is flagged for the lead rather than claimed closed.

**Recommended verdict: PARK Stage B**, interference reading **killed** for every null the lawful rule reaches at the single-merge level, the forced object shown non-cancelling, and the multi-merge case mapped-but-open. Per §5 this is a full result: the dynamics gap the corpus itself flags is now mapped to a named missing ingredient, and §10's surplus-structure target (which lists E8 Stage B as its current best candidate) is sharpened — the reason Stage B does not yet deliver is identified, and *Phase on the Merge* §3's parked direction (coupling the additive layer to multiplicative structure, where phase could become *arithmetic*) is exactly the place the empty-split obstruction might be broken. That is off E8's remit.

---

## Implementer additions (labelled; separately graded; never substituting for a committed bar)

- **A1 (Stage A) — the exact maximal-overlap sequence and its tie structure.** The enumerated maximum of S_p is **{m: 4,5,7,9,12}** for m = 4..8. For m a power of two the maximiser shape is essentially unique; for other m the maximum is attained by a *set* of shapes (m = 6 by both the balanced (3,3) and the (4,2)-with-balanced-4 splits). *(Fact, elementary combinatorics; no novelty claimed. Reported because MA3(c)'s "ties permitted" is realised concretely, and the sequence is a clean pin for any successor.)*
- **A2 (Stage B) — the single-merge interference obstruction.** Σ_{k=1}^{m−1} ωᵏ = −1 − ω⁻¹ = −(1 + e^{−2πi/(m+1)}), of modulus 2cos(π/(m+1)) > 0 for all m ≥ 2; hence the forced interior sum never vanishes, and the only exact single-merge cancellation (the full roots-of-unity sum) is carried entirely by the two empty splits. *(The identity: Fact, elementary roots-of-unity. The Reading — the empty split as the off-audit ingredient a forced non-classical null would require, i.e. the precise technical core of the parking diagnosis — is the sub-programme's contribution.)*

---

## Non-vacuity (audit; honest flags)

Every committed bar can fail under an incorrect implementation, and no check compares a quantity to itself or restates a definition:

- **MA2a decomposition.** S(T) is the integer-`gcd` route; Σ_p ln p·S_p is the per-prime `min`-sum route — two independent computations of the same number. A mis-tallied exponent or a wrong gcd breaks the equality.
- **MA3a floor / equality.** S_p (min-sums) is checked against the floor m_p−1 (leaf counts) and, independently, the at-floor predicate is checked against a *structural* caterpillar-in-p test (every uniting merge has a singleton p-side). The IFF is two independent characterisations agreeing on every tree; a bug in either side breaks it.
- **MA3b identity.** E and D are computed at branch nodes from (L_p+R_p) and |L_p−R_p|; S_p from `min` at *all* nodes. A bug that included a non-branch node in E/D, or mis-signed the imbalance, would break the identity — which holds at residual **exactly 0.0** (integer arithmetic), the tightest possible demonstration.
- **MA3c maximiser.** The balanced tree is constructed independently and compared to the *enumerated* max over all (2m−3)!! trees; if a non-balanced tree exceeded it, the check would fail loudly (that would be the finding).
- **MA4a record→shape.** I(record;shape) uses two constructions — the record (post-order overlap tuple) and the shape (canonical bracket string) — and H(shape\|record) is computed by re-partitioning trees by record; a mis-built record or shape breaks the H(shape\|record)=0 result before it reaches the 0.500402 value.
- **MA4b squarefree.** Every per-merge gcd is checked == 1 explicitly; a wrong multiset or a factorisation bug that produced a shared prime would raise a gcd above 1 and make the record vary. The I=0 is then a consequence, not an assumption.
- **MA5 minimiser.** Smallest-first (independent heap-Huffman) is compared to the enumerated min over all trees; agreement (residual 0.0) is a check of both against each other, and the pinned values are compared to the banked note's printed constants.
- **Structural flags (not measured):** MA1's resistance conservation is a float identity (root=n is the genuine wiring test); MA2b's prime-swap is exact-by-construction (computed independently per prime nonetheless); MA4c's value-constancy is by construction. All three are flagged in the note and in the script header, so their near-zero/identical outcomes are not mistaken for tight statistical results.

---

## Notes for Alex (honest observations — none threaten a bar)

1. **The state/process split is the cleanest thing Stage A owns, and MA4(c) makes it exact.** Value carries zero tree information (structural); the record carries all of it; and the two are *orthogonal* — erase the record and precisely the value survives, with nothing of the path leaking into n and nothing of n leaking into the record. The squarefree case is the limiting demonstration: no multiplicity, no trail, blank receipt, value intact.

2. **Kernel-blindness and kernel-anonymity are two faces of one fact.** The ledger's integer skeleton depends on the *exponent pattern* only (blind to which primes — MA2b), and where the exponent pattern is flat (squarefree, all exponents 1) the skeleton is empty (anonymous — MA4b). Multiplicity is simultaneously *what the record can see* and *the only thing it can see*; remove it and the record goes dark. This is the same idempotence hinge the sub-programme keeps meeting (F1, E1's join, Q's double-negation), now on the merge ledger.

3. **Stage B's park is, I think, the honest and informative outcome — and it is sharper than a bare "cannot couple."** The lawful coupling *does* exist; what fails is that it forces nothing non-classical. The obstruction has a name: the empty split. The genuinely-complex null the layer *can* write (the cube-root triple) is exactly the one that needs cherry-picking, and the forced version needs a merge-with-nothing. If Stage B is ever revisited, the single-merge proof says the room to move is (a) a multi-merge forced construction (I could not find one and expect the same obstruction), or (b) *Phase on the Merge* §3's parked door — coupling to multiplicative structure so the phase becomes arithmetic, where "which split" could carry more than a position. Both are off E8's remit; I have left them as the mapped edges, not walked through them.

4. **A small structural pleasure worth recording.** The classical weight of a build path is e^{−(build erasure)} — the *same* ln-product MA5 measures — so |amplitude|² = the classical probability and the interference is entirely in the cross terms. The path-function heat of Stage A and the (would-be) interference of Stage B are the same object seen twice: the order-dependence that MA5 prices as excess heat is the order-dependence that, laid over amplitudes, *would* interfere — and the reason it doesn't (non-classically) is that the cross terms only cancel where the diagonal (empty-split) measure lives.

---

## The fence (mandatory)

E8 works ground the main corpus fences off, and the fence holds here. The Resistance Isomorphism forbids any contradiction of arithmetic; E8's novel content lives only in observables arithmetic declares meaningless — the *paths* (the overlap ledger, a path function) — and, in Stage B, in whether their amplitudes cancel. **No arithmetic question is claimed touched.** Stage A's identities (the floor theorem, (E−D)/2, the shape counts, gcd-of-coprimes, the additive replication) are elementary combinatorics and the banked note's Facts re-verified; Landauer/Huffman/Weyl attributions are carried. Stage B claims a **mapped obstruction**, not a resolution: the interference reading is killed for the reachable nulls and the dynamics gap is parked, not closed.

## Mandatory honesty caveat (transplanted from the corpus's energy-ledger discipline)

In simulation, Landauer accounting is an **identity true by construction** — bijections are free and erasures cost the entropy we compute because we compute the `ln` we predicted, not because we measured a physical dissipation that could disagree. E8 therefore confirms that the two-path ledger is a **consistent, correctly-structured accounting** and measures classical identities within it (the floor theorem, the path-length identity, mutual informations, the roots-of-unity obstruction); it does **not**, and cannot, *risk* the framework's carrier reading, which stays a **Lead pending physical measurement**. Nothing in Stage B changes this: the phase, its cost, and its (non-)cancellation are all computed identities, and the parking diagnosis is a statement about *which* identities the lawful ingredients can and cannot write — not a physical fact risked.

## Honesty boundary

The mathematics is classical and cited as such: **Landauer** (erasure = log multiplicity), **Shannon** (entropy, mutual information, the chain rule), the **Weyl/Pauli clock-shift algebra** and its relation ZX = ωXZ, **Huffman/optimal-merge order**, and the elementary combinatorics of leaf-labelled binary trees (the (2m−3)!! count, external path length, the roots-of-unity sum). **E8 adds no mathematics to these.** What belongs to the sub-programme is the reading *on the ledger*: the multiplicative register's **state/process split** (resistance conserved per-merge; the overlap ledger a path function — Reading); **kernel-blindness** of the process ledger (Reading); **kernel anonymity** — path memory lives in multiplicity, the Mad kernel is path-anonymous, the path-erased quotient is exactly the multiplicative shadow (Reading); and Stage B's **mapped obstruction** — proto-phase couples lawfully but forces no non-classical null, the missing ingredient being the empty split (Reading, with the roots-of-unity identity a labelled Fact). In simulation these are identities computed, not physical facts risked, so nothing here is — or can become — evidence that the genesis system holds beyond the axioms that posit it; the carrier reading is not promoted, and no leverage is claimed on any open problem. Boundary discipline inherited from the main spine, unamended.

*The master document has not been edited — banking edits to the spine (and any register update closing E8) are performed by the lead instance on return. The Stage B gate submission awaits the lead's sign-off or park.*

*Alexander Pisani & Claude (Anthropic) · Madness in the Probe sub-programme · E8 · July 2026.*

---

## Lead verification addendum (appended on return; original text above untouched)

**Stage A: independent rerun.** Exit 0, all checks reproduced to the printed digit (the (2m−3)!! counts; the max sequence {4,5,7,9,12}; I(record;shape) = 0.500402; the additive replication values; the integer-exact (E−D)/2 residual). Banking stands. The Weyl-Clock citation ("trivial and uniform vs hard and logarithmic"; the genesis-bit 1 + (−1) = 0) was checked against the note and is accurate.

**Stage B gate ruling: the submission is ratified at its full scope.** The Family-α kill (sign-reducibility of every equal-weight two-path null) and the Family-β kill (a residue-class selection the audit list does not license, with the three-equal-real-signs impossibility verified) are both endorsed; the single-merge obstruction identity Σ_{k=1}^{m−1} ω^k = −1 − ω^{−1}, |·| = 2cos(π/(m+1)), was independently recomputed (1.7321 at m=5, 1.8794 at m=8). The empty-split diagnosis — the only exact single-merge cancellation is carried entirely by the two null-tally splits the dynamics never perform — is adopted as the authoritative statement of the corpus's dynamics gap. The lawful phase rule of B(i) is a genuine contribution independent of the park: it is the first audit-clean, definite phase-assignment the programme possesses, and |A|² = classical weight makes Stage A's heat and Stage B's would-be interference one object seen twice, as the note's fourth observation records.

**The lead's scan of the mapped-open edge, with pre-committed criteria (sidecars `x520_e8_multimerge_scan.py`, `x520_e8_scan_controls.py`).** The submission flagged the multi-merge forced object as not ruled out by the single-merge proof. The lead scanned it: F(n) = the coherent sum over all plane build paths of n under the B(i) rule, against the classical total G(n), ratio r(n) = |F|²/G. Pre-committed: any r < 10⁻⁹ = candidate null, reopen; otherwise park stands. **The criterion fired in letter but not in anticipated shape:** there is **no null at any fixed n** — consistent with the submission's prior — but r(n) undergoes smooth **geometric extinction**, λ = 0.7225535(60) per step (sd 6×10⁻⁶ over n ∈ [250,300]), confirmed at mpmath dps 60 to 10⁻¹⁵ relative. Pre-committed controls: the **forced real-sign** ledger ((−1)^k) is *constructive* — r grows to 7.9×10¹⁰ by n = 300 — so the extinction is **not sign-reducible**; **seeded random phases** decay at the diffusive benchmark ≈ 0.79/step — ten orders of magnitude *slower* by n = 300 — so the forced clock's extinction **exceeds chance**; the flat control explodes (wiring). Ordering: flat ≫ sign ≫ random > clock. The forced clock is the most destructive object in its comparison class, systematically, at a clean constant.

**Ruling.** The exact-null interference reading remains killed/parked exactly per the submission. The gate **reopens on a different object**: the forced extinction rate λ — registered as **E8b** with pre-committed identify/discriminate/kill/park criteria and a boundary clause (no connection to any zeta object may be drawn). Excitement flag, recorded per protocol: the significance of λ is at present pattern-matched, not derived; the constant may have a mundane spectral identification, and E8b exists to decide that rather than assume it. Credit: the submission's A2 identity is the seed the scan grew from, and the flagged-not-claimed handling of the multi-merge edge is what made the scan a verification duty rather than a fishing trip.

*Lead instance, July 2026.*
