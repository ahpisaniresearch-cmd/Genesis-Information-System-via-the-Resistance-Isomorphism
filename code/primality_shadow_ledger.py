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
GIP - the primality shadow as a signed inclusion-exclusion ledger
=================================================================
Pisani's proposal: the primality shadow of p is the ON state, minus the erasure
of everything but the row, plus the nats that certify primality (the irreversibility
test). Formalised: this is the von Mangoldt function as the Mobius inversion of the
resistance - a SIGNED inclusion-exclusion over the divisor lattice (Paper 2's engine).

  resistance built from innovations:  ln n = sum_{d|n} Lambda(d)
  the irreversibility test (invert):  Lambda(n) = - sum_{d|n} mu(d) ln d
  a prime SURVIVES (nothing to cancel); a composite REDUCES AWAY (Lambda = 0).
"""
from math import log


def factorize(n):
    f, m, d = {}, n, 2
    while d * d <= m:
        while m % d == 0:
            f[d] = f.get(d, 0) + 1; m //= d
        d += 1
    if m > 1:
        f[m] = f.get(m, 0) + 1
    return f


def divisors(n):
    ds = [1]
    for p, e in factorize(n).items():
        ds = [x * p**k for x in ds for k in range(e + 1)]
    return sorted(ds)


def mobius(n):
    if n == 1:
        return 1
    f = factorize(n)
    return 0 if any(e > 1 for e in f.values()) else (-1) ** len(f)


def Lambda(n):
    f = factorize(n)
    return log(next(iter(f))) if len(f) == 1 else 0.0


N = 12
print("1) resistance = sum of divisor innovations:  ln n = sum_{d|n} Lambda(d)")
ok = all(abs(sum(Lambda(d) for d in divisors(n)) - log(n)) < 1e-12 for n in range(2, N + 1))
print(f"   holds for all n in 2..{N}: {ok}\n")

print("2) the irreversibility test (Mobius inversion):  Lambda(n) = - sum_{d|n} mu(d) ln d")
for n in range(2, N + 1):
    val = -sum(mobius(d) * log(d) for d in divisors(n))
    tag = "prime-power -> SURVIVES (= ln p)" if Lambda(n) > 1e-12 else "composite -> cancels to 0"
    print(f"   n={n:2d}:  Lambda = {val:+.4f}   {tag}")

print("\n3) the signed ledger, a prime (5) vs a composite (6):")
for n in [5, 6]:
    parts = [f"[d={d}: mu={mobius(d):+d}, -mu*ln d = {-mobius(d)*log(d):+.3f}]" for d in divisors(n)]
    total = -sum(mobius(d) * log(d) for d in divisors(n))
    print(f"   n={n}:  " + "  ".join(parts))
    print(f"          -> Lambda({n}) = {total:+.4f}"
          + ("   (no composite divisor to cancel: the prime locks up)" if n == 5
             else "   (the ln6 term cancels ln2+ln3: the composite reduces away)"))
