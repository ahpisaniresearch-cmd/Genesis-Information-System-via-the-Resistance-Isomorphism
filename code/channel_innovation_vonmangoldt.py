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
GIP - Experiment 2: the von Mangoldt function as measured channel innovation
============================================================================
Section 20 obtained Lambda(n) combinatorially (Mobius inversion of ln n over the
divisor lattice). This experiment asks whether Lambda is also a MEASURED
information quantity of the modulo channels themselves.

Claim under test:
    H( a mod n  |  { a mod d : d | n, d < n } )  =  Lambda(n).

Reading: the conditional entropy of channel n given all its divisor channels is
the channel's INNOVATION - the information it carries beyond everything its
sub-channels already said. Prediction: only prime powers innovate, and a prime
power innovates by exactly ln p. Then ln n = sum_{d|n} Lambda(d) becomes the
chain-rule statement that a channel's information is the accumulated innovation
of its divisor tower.

Underlying lattice identity (elementary): lcm(proper divisors of n) = n/p if
n = p^k, else n. The experiment MEASURES the conditional entropy empirically
(uniform a over one period), with no factorisation used in the measurement.
"""
from math import log, gcd
from functools import reduce
from collections import Counter


def lcm(a, b):
    return a * b // gcd(a, b)


def divisors(n):
    return [d for d in range(1, n + 1) if n % d == 0]


def Lambda(n):
    """von Mangoldt, computed independently (trial): ln p if n = p^k else 0."""
    if n < 2:
        return 0.0
    p = None
    m = n
    for q in range(2, n + 1):
        if m % q == 0:
            p = q
            while m % q == 0:
                m //= q
            break
    return log(p) if m == 1 else 0.0


def conditional_innovation(n):
    """H(a mod n | all proper-divisor channels), measured empirically."""
    props = [d for d in divisors(n) if d < n]
    L = n  # a mod n and a mod d (d|n) all have period n
    joint = Counter((tuple(a % d for d in props), a % n) for a in range(L))
    cond = Counter(tuple(a % d for d in props) for a in range(L))
    Hj = -sum((c / L) * log(c / L) for c in joint.values())
    Hc = -sum((c / L) * log(c / L) for c in cond.values())
    return Hj - Hc


print("H(a mod n | divisor channels)  vs  Lambda(n)")
print(f"{'n':>3} {'innovation (measured)':>22} {'Lambda(n)':>10} {'|diff|':>10}  note")
worst = 0.0
for n in range(2, 37):
    inn = conditional_innovation(n)
    lam = Lambda(n)
    worst = max(worst, abs(inn - lam))
    note = "prime" if lam > 0 and all(n % q for q in range(2, n)) else (
        "prime power" if lam > 0 else "composite -> zero innovation")
    print(f"{n:>3} {inn:>22.10f} {lam:>10.6f} {abs(inn - lam):>10.2e}  {note}")
print(f"\nmax |measured - Lambda| over n = 2..36: {worst:.2e}")

print("\nThe chain rule over the divisor tower:  ln n = sum of innovations of its divisors")
print(f"{'n':>3} {'sum_d innovation(d)':>20} {'ln n':>8} {'|diff|':>10}")
worst = 0.0
for n in [12, 16, 24, 30, 36]:
    s = sum(conditional_innovation(d) for d in divisors(n) if d >= 2)
    worst = max(worst, abs(s - log(n)))
    print(f"{n:>3} {s:>20.10f} {log(n):>8.4f} {abs(s - log(n)):>10.2e}")
print(f"  max deviation = {worst:.2e}")
print("\n-> the primality shadow is a MEASURED conditional entropy: a channel innovates")
print("   iff it is a prime power, by exactly ln p; composites are fully redundant")
print("   given their divisor channels; and the resistance ln n is the accumulated")
print("   innovation of the divisor tower (the two-legged ledger refined over the lattice).")
