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
GIP - Experiment 1: the lattice information suite
=================================================
Section 14 established the PAIR result: I(a mod m1; a mod m2) = ln gcd(m1,m2),
landing on the union law's single correlation term. If that is not a coincidence,
the ENTIRE inclusion-exclusion of the gcd/lcm lattice should be realised by the
multivariate information measures. Predictions (derived from CRT + the max/min
inclusion-exclusion on exponent vectors, then verified empirically):

  (a) TOTAL CORRELATION of k channels:
      TC = sum_i H_i - H(joint) = sum_i ln m_i - ln lcm(all)
         = sum_{pairs} ln gcd - sum_{triples} ln gcd + ...  (alternating, full I-E)
  (b) CONDITIONAL mutual information:
      I(X1; X2 | X3) = ln gcd(m1,m2) - ln gcd(m1,m2,m3)   (the relative meet)
  (c) CO-INFORMATION (interaction information):
      I(X1; X2) - I(X1; X2 | X3) = ln gcd(m1,m2,m3)       (the triple meet)

All entropies computed empirically: a uniform over one joint period L = lcm.
"""
from math import log, gcd
from itertools import combinations
from functools import reduce
from collections import Counter


def lcm(*ms):
    return reduce(lambda a, b: a * b // gcd(a, b), ms)


def gcd_all(*ms):
    return reduce(gcd, ms)


def H_of(cols):
    """Empirical joint entropy (nats) of the listed residue columns."""
    L = lcm(*[m for m, in cols]) if False else None  # placeholder


def joint_entropy(ms, which):
    """H of the joint readout of channels ms[i] for i in `which`, a uniform over lcm(ms)."""
    L = lcm(*ms)
    counts = Counter(tuple(a % ms[i] for i in which) for a in range(L))
    return -sum((c / L) * log(c / L) for c in counts.values())


def TC(ms):
    """Total correlation = sum of marginal entropies - joint entropy."""
    return sum(joint_entropy(ms, (i,)) for i in range(len(ms))) - joint_entropy(ms, tuple(range(len(ms))))


def IE_gcd(ms):
    """The alternating inclusion-exclusion sum over ln gcd of all subsets of size >= 2."""
    total, k = 0.0, len(ms)
    for r in range(2, k + 1):
        sgn = 1 if r % 2 == 0 else -1
        for sub in combinations(ms, r):
            total += sgn * log(gcd_all(*sub))
    return total


print("(a) Total correlation = full lattice inclusion-exclusion over ln gcd")
print(f"{'bank':>16} {'TC (measured)':>14} {'I-E over gcds':>14} {'|diff|':>10}")
banks = [(2, 4, 8), (6, 10, 15), (4, 6, 10), (2, 3, 5), (12, 18, 30),
         (2, 4, 6, 8), (6, 10, 15, 21), (4, 6, 8, 12)]
worst = 0.0
for b in banks:
    tc, ie = TC(list(b)), IE_gcd(list(b))
    worst = max(worst, abs(tc - ie))
    print(f"{str(b):>16} {tc:>14.8f} {ie:>14.8f} {abs(tc - ie):>10.2e}")
print(f"  max |TC - inclusion-exclusion| = {worst:.2e}\n")

print("(b) Conditional MI: I(X1;X2|X3) = ln[ gcd(m1,m2) / gcd(m1,m2,m3) ]")
print(f"{'(m1,m2,m3)':>14} {'I(X;Y|Z)':>10} {'ln(g12/g123)':>13} {'|diff|':>10}")
worst = 0.0
for m1, m2, m3 in [(4, 6, 2), (12, 18, 6), (12, 18, 4), (8, 12, 3), (6, 10, 15), (9, 12, 6)]:
    ms = [m1, m2, m3]
    # I(X;Y|Z) = H(XZ) + H(YZ) - H(Z) - H(XYZ)
    i_cond = (joint_entropy(ms, (0, 2)) + joint_entropy(ms, (1, 2))
              - joint_entropy(ms, (2,)) - joint_entropy(ms, (0, 1, 2)))
    pred = log(gcd(m1, m2)) - log(gcd_all(m1, m2, m3))
    worst = max(worst, abs(i_cond - pred))
    print(f"{str((m1,m2,m3)):>14} {i_cond:>10.6f} {pred:>13.6f} {abs(i_cond - pred):>10.2e}")
print(f"  max deviation = {worst:.2e}")
print("  -> conditioning on a third channel divides out the shared part: the relative meet.\n")

print("(c) Co-information I(X;Y) - I(X;Y|Z) = ln gcd(m1,m2,m3)  (the triple meet)")
print(f"{'(m1,m2,m3)':>14} {'co-info':>10} {'ln gcd123':>10} {'|diff|':>10}")
worst = 0.0
for m1, m2, m3 in [(4, 6, 2), (12, 18, 6), (6, 10, 15), (12, 18, 4), (30, 42, 70)]:
    ms = [m1, m2, m3]
    i_pair = joint_entropy(ms, (0,)) + joint_entropy(ms, (1,)) - joint_entropy(ms, (0, 1))
    i_cond = (joint_entropy(ms, (0, 2)) + joint_entropy(ms, (1, 2))
              - joint_entropy(ms, (2,)) - joint_entropy(ms, (0, 1, 2)))
    co = i_pair - i_cond
    pred = log(gcd_all(m1, m2, m3))
    worst = max(worst, abs(co - pred))
    print(f"{str((m1,m2,m3)):>14} {co:>10.6f} {pred:>10.6f} {abs(co - pred):>10.2e}")
print(f"  max deviation = {worst:.2e}")
print("  -> the multivariate interaction is ln of the triple gcd: the whole meet-lattice")
print("     is realised in the information measures, not only the pair term.")
