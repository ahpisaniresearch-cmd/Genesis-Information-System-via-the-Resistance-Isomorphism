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
GIP - Experiment 5: ordinal innovation - weakening the circularity
==================================================================
The standing circularity: extracting the prime signal has always required the
divisor lattice (Stage 1's Z/g indexing; the modulo gateway's clean-split pattern;
the Mobius inversion's divisor sums; and Experiment 2's conditioning set
{a mod d : d | n}).

This experiment replaces the divisor conditioning set with a set defined purely
by SUCCESSION ORDER - all predecessors:

    innovation(n) = H( a mod n | { a mod k : 2 <= k <= n-1 } ).

The procedure references only: the succession-cycle family (Stage 1's clocks),
the ordinal sweep (condition on everything BEFORE n), the shared stream (one a
read by all clocks), and Shannon conditional entropy. Divisor knowledge appears
NOWHERE in the extraction.

Empirical method: exact enumeration of a over one full period L = lcm(1..n),
residue tuples encoded by Horner keys (an encoding of observed data, not an
assumption); entropies from counts. Lambda(n) computed independently by trial
division for comparison only.
"""
import numpy as np
from math import log, gcd

def lcm_upto(n):
    L = 1
    for k in range(2, n + 1):
        L = L * k // gcd(L, k)
    return L

def Lambda(n):
    if n < 2: return 0.0
    m, p = n, None
    for q in range(2, n + 1):
        if m % q == 0:
            p = q
            while m % q == 0: m //= q
            break
    return log(p) if m == 1 else 0.0

def entropy_of_key(key):
    _, counts = np.unique(key, return_counts=True)
    p = counts / counts.sum()
    return float(-(p * np.log(p)).sum())

def joint_entropy_channels(n_max, upto):
    """H of the joint readout of channels 2..upto, over one period of lcm(1..n_max)."""
    L = lcm_upto(n_max)
    a = np.arange(L, dtype=np.int64)
    key = np.zeros(L, dtype=np.int64)
    for k in range(2, upto + 1):
        key = key * k + (a % k)
    return entropy_of_key(key)

print("Ordinal innovation: H(a mod n | ALL predecessor channels 2..n-1)")
print(f"{'n':>3} {'innovation':>12} {'Lambda(n)':>10} {'|diff|':>9} {'novelty ratio inn/ln n':>23}")
prev = 0.0
results = []
for n in range(2, 19):
    Hn = joint_entropy_channels(n, n)
    inn = Hn - (joint_entropy_channels(n, n - 1) if n > 2 else 0.0)
    lam = Lambda(n)
    ratio = inn / log(n)
    results.append((n, inn, lam, ratio))
    tag = ("PRIME (ratio = 1)" if abs(ratio - 1) < 1e-12 else
           ("prime power" if inn > 1e-9 else "composite: zero"))
    print(f"{n:>3} {inn:>12.8f} {lam:>10.6f} {abs(inn-lam):>9.1e} {ratio:>23.10f}  {tag}")
print(f"\nmax |innovation - Lambda| over n = 2..18: {max(abs(i-l) for _,i,l,_ in results):.2e}")
print("-> the ORDER-based conditioning set reproduces the von Mangoldt function exactly;")
print("   no divisor knowledge is used in the extraction. A PRIME is a channel whose")
print("   innovation over all predecessors equals its ENTIRE content (novelty ratio 1);")
print("   prime powers innovate partially (1/k); composites innovate zero.")

print("\nCumulative innovation of the ordinal sweep = the total information of the bank:")
print(f"{'n':>3} {'sum of innovations':>18} {'ln lcm(1..n)':>13} {'psi(n) [Chebyshev]':>18} {'psi(n)/n':>9}")
cum = 0.0
for n, inn, lam, _ in results:
    cum += inn
    psi = sum(Lambda(m) for m in range(2, n + 1))
    print(f"{n:>3} {cum:>18.8f} {log(lcm_upto(n)):>13.6f} {psi:>18.6f} {cum/n:>9.4f}")
print("-> cumulative channel innovation = ln lcm(1..n) = the second Chebyshev function")
print("   psi(n). (Classical identity; flagged.) The prime number theorem psi(n) ~ n then")
print("   reads: the ordinal channel bank gains ASYMPTOTICALLY ONE NAT PER STEP.")

print("\nInnovation decay profile: I_m(n) = H(a mod n | channels 2..m), m sweeping")
for n in [13, 12, 16]:
    prof = []
    for m in range(1, n):
        L = lcm_upto(max(m, 1))
        Lj = L * n // gcd(L, n)
        a = np.arange(Lj, dtype=np.int64)
        key = np.zeros(Lj, dtype=np.int64)
        for k in range(2, m + 1):
            key = key * k + (a % k)
        Hc = entropy_of_key(key)
        Hj = entropy_of_key(key * n + (a % n))
        prof.append(Hj - Hc)
    steps = " ".join(f"{v:.3f}" for v in prof)
    print(f"  n={n:>2}: {steps}")
print("-> a prime's profile stays FLAT at ln n through the whole sweep (nothing before it")
print("   explains any of it); a composite's profile steps DOWN as each prime-power part")
print("   is covered by the sweep - the factorisation, read as an order-indexed decay.")
