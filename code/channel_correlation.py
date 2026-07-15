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
GIP - correlation between two modulo channels
Run a mod m1 and a mod m2 on the same a (uniform over one full joint period,
N = lcm(m1,m2)). Prediction from the Chinese Remainder structure:

    I(a mod m1 ; a mod m2) = ln gcd(m1, m2)

Both channels pin down a mod gcd and nothing more, so what they SHARE is exactly
the gcd. Coprime channels (gcd = 1) share nothing: I = 0. This is the first
RELATIONAL quantity in the programme - a two-variable arithmetic function of the
shared prime structure, which single-integer resistance cannot express.
"""
from math import log, gcd
from collections import defaultdict


def lcm(a, b):
    return a * b // gcd(a, b)


def mutual_info(m1, m2):
    N = lcm(m1, m2)
    joint, p1, p2 = defaultdict(int), defaultdict(int), defaultdict(int)
    for a in range(N):
        r1, r2 = a % m1, a % m2
        joint[(r1, r2)] += 1
        p1[r1] += 1
        p2[r2] += 1
    I = 0.0
    for (r1, r2), c in joint.items():
        pj = c / N
        I += pj * log(pj / ((p1[r1] / N) * (p2[r2] / N)))
    return I


ms = list(range(2, 9))

# 1. exactness check
maxerr = max(abs(mutual_info(m1, m2) - log(gcd(m1, m2)))
             for m1 in ms for m2 in ms)
print(f"max |I - ln gcd(m1,m2)| over all pairs {ms[0]}..{ms[-1]}: {maxerr:.2e}")
print("  -> I(a mod m1 ; a mod m2) = ln gcd(m1, m2), exactly.\n")

# 2. the gcd matrix (I = ln of each cell)
print("gcd(m1, m2)  - and I = ln of each cell; cell 1 = coprime = zero correlation:")
print("       " + "".join(f"{m2:>4}" for m2 in ms))
for m1 in ms:
    print(f"  m={m1:>2}|" + "".join(f"{gcd(m1, m2):>4}" for m2 in ms))

# 3. the coprimality lattice as zero-correlation
print("\nzero-correlation (coprime) pairs, I = ln 1 = 0:")
cop = [(m1, m2) for m1 in ms for m2 in ms if m1 < m2 and gcd(m1, m2) == 1]
print("  " + ", ".join(str(p) for p in cop))
print("\nnonzero-correlation pairs share a prime; e.g.:")
for m1, m2 in [(2, 4), (3, 6), (4, 6), (4, 8), (6, 8)]:
    print(f"  ({m1},{m2}): share {gcd(m1,m2)}  ->  I = ln {gcd(m1,m2)}")
