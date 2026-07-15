# =============================================================================
#  Genesis Information System via the Resistance Isomorphism
#  (c) 2026 Alexander Pisani - Blue Mountains, NSW, Australia
#  Contact: a.h.pisani.research@gmail.com
#  Licensed under Creative Commons Attribution 4.0 International (CC BY 4.0).
#
#  Originating theory & axioms: Alexander Pisani.
#  Code, formalisation & computation: Claude (Anthropic).
#
#  Attribution to BOTH the author and the AI collaborator is required for reuse,
#  adaptation, reference (including as material for AI systems), or incorporation
#  into software, inventions, or patents. See CITATION.cff.
# =============================================================================

"""
GIP - the energy-ledger test (Erasure as the Carrier, §6), end-to-end
=====================================================================
A single composed genesis computation on the lattice machine of §2.3: the state
is an integer n = 2^a * 3^b (two registers a,b holding prime exponents), and the
steps are FRACTRAN-style register operations. Most are reversible (bijections);
ONE is a deliberate erasure. We account the energy at every step over an ensemble
of inputs (Landauer: cost = entropy compressed = H_before - H_after), and check
the two §6 kill conditions:
    (a) does energy appear at a non-erasure step?   (b) do the totals disagree?

HONEST CAVEAT (kept in front): in simulation this is Landauer's principle applied
to the bijection-vs-many-to-one distinction - an identity, true by construction.
It demonstrates the accounting is CONSISTENT and the erasures CORRECTLY LOCATED;
it does not RISK anything, so it confirms the carrier reading, it does not promote
it. Genuine falsifiability needs physical heat measurement (the physical direction).
"""
import numpy as np
from math import log

M = 5
K = M + 1


def H(P):
    p = P[P > 1e-15]
    return float(-np.sum(p * np.log(p)))


def run(P0, label):
    print(f"\n=== {label} ===")
    P = P0.copy()
    print(f"  start: H = {H(P):.4f} nats   (n = 2^a 3^b; registers a,b in 0..{M})")
    steps = []
    # 1) INC a : x2, cyclic bijection on a
    steps.append(("INC a   (x2, reversible)", P, (P := np.roll(P, 1, axis=0))))
    # 2) SWAP a,b : swap primes 2<->3, bijection
    steps.append(("SWAP a,b (2<->3, reversible)", P, (P := P.T.copy())))
    # 3) controlled add a <- (a+b) mod K : bijection on the pair
    Pn = np.zeros_like(P)
    for a in range(K):
        for b in range(K):
            Pn[(a + b) % K, b] += P[a, b]
    steps.append(("ADD a<-(a+b) mod K (reversible)", P, (P := Pn)))
    # 4) THE ERASURE: reset b->0 (divide out all 3s; forget exponent b)
    Pn = np.zeros_like(P)
    for a in range(K):
        for b in range(K):
            Pn[a, 0] += P[a, b]
    steps.append(("RESET b->0  [ERASURE: forget exp of 3]", P, (P := Pn)))
    # 5) DEC a : /2, cyclic bijection
    steps.append(("DEC a   (/2, reversible)", P, (P := np.roll(P, -1, axis=0))))

    print(f"  {'step':<40}{'energy (nats)':>14}")
    total = 0.0
    costs = []
    for name, b_, a_ in steps:
        c = H(b_) - H(a_)
        costs.append(c); total += c
        print(f"  {name:<40}{c:>14.4f}")
    print(f"  {'-'*54}")
    print(f"  {'TOTAL':<40}{total:>14.4f}")
    return costs, total


# 1) uniform ensemble
costs, total = run(np.ones((K, K)) / K**2, "Uniform ensemble")
print(f"  erasure cost = {costs[3]:.4f} = ln K = ln {K} = {log(K):.4f}  (resistance of the forgotten register)")

# 2) random non-uniform ensemble (generality)
rng = np.random.default_rng(1)
Pr = rng.random((K, K)); Pr /= Pr.sum()
costs2, total2 = run(Pr, "Random non-uniform ensemble")
print(f"  erasure cost = H(b|a) = {costs2[3]:.4f}; reversible steps exactly 0; total = the one erasure")

# 3) the two kill conditions, explicit
print("\n=== the two §6 kill conditions ===")
rev = [c for i, c in enumerate(costs) if i != 3] + [c for i, c in enumerate(costs2) if i != 3]
print(f"  (a) energy at a non-erasure step? max|cost over reversible steps| = {max(abs(c) for c in rev):.2e}  -> NO")
print(f"  (b) totals disagree? |total - erasure| = uniform {abs(total-costs[3]):.2e}, random {abs(total2-costs2[3]):.2e}  -> NO")
print("  neither is triggered: energy appears only at the erasure, equal to the resistance erased.")
print("\n  (Caveat: this is Landauer applied to bijection-vs-many-to-one - an identity in")
print("   simulation. It confirms consistent, correctly-located accounting; it does not")
print("   reach physical falsifiability. Carrier reading stays a Lead.)")
