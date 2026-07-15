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
Genesis Information Project - a table of additive erasure operations
====================================================================
Every irreversible operation's erasure is ln(fan-in): the log of how many inputs
collapse onto the output. The ln is generic; the fan-in is the content. So
"mapping an operation" is counting its fan-in. We also check the two-legged
ledger that held for the merge:

    system erasure  = H(input | output)  = sum_out P(out) * ln(fan-in(out))
    demon reset     = H(output)
    total           = H(input)            (chain rule)

We map projection, reset, max, min on proto-integers 0..M (uniform). We STOP
before modulo, whose fan-in is the quotient - the multiplicative gateway - to be
crossed deliberately, not stumbled through.
"""

from math import log
from collections import defaultdict

M = 8
vals = list(range(M + 1))


def analyze(f, arity):
    pre = defaultdict(int)
    if arity == 2:
        N = (M + 1) ** 2
        for a in vals:
            for b in vals:
                pre[f(a, b)] += 1
    else:
        N = M + 1
        for a in vals:
            pre[f(a)] += 1
    Hout, mean_sys = 0.0, 0.0
    for fan in pre.values():
        p = fan / N
        Hout -= p * log(p)
        mean_sys += p * log(fan)            # = H(input|output), preimage uniform
    return pre, Hout, mean_sys, log(N)


ops = [
    ("projection (a,b)->a", "b entirely", (lambda a, b: a), 2),
    ("reset a->0", "a entirely", (lambda a: 0), 1),
    ("max(a,b)", "smaller + which", (lambda a, b: max(a, b)), 2),
    ("min(a,b)", "larger + which", (lambda a, b: min(a, b)), 2),
]

print(f"Additive erasure operations on proto-integers 0..{M} (uniform); erasure = ln(fan-in)\n")
print(f"{'operation':>20} | {'forgets':>16} | {'mean system erase':>17} | "
      f"{'demon reset H(out)':>18} | {'total = input info':>18}")
print("-" * 100)
for name, forgets, f, arity in ops:
    pre, Hout, mean_sys, Hin = analyze(f, arity)
    print(f"{name:>20} | {forgets:>16} | {mean_sys:>17.4f} | "
          f"{Hout:>18.4f} | {mean_sys + Hout:>10.4f}  (Hin {Hin:.3f})")

print("\nFan-in profile - flat vs graded:")
print("  projection, reset: fan-in is constant (M+1) - forgetting a whole register,")
print("                     cost independent of the value (FLAT).")
print("  max, min:          fan-in varies with the output (GRADED). For max, output m")
print("                     has 2m+1 preimages; larger max forgot more.\n")
print(f"{'output m':>9} | {'max fan-in 2m+1':>15} | {'erasure ln(2m+1)':>17} | "
      f"{'min fan-in 2(M-m)+1':>19}")
print("-" * 70)
for m in vals:
    print(f"{m:>9} | {2 * m + 1:>15} | {log(2 * m + 1):>17.4f} | {2 * (M - m) + 1:>19}")

# the gateway, named but not crossed
print("\nNEXT (multiplicative gateway, not computed here):")
print("  modulo a -> a mod m : fan-in is the quotient floor((M+1)/m) - division enters,")
print("  and division is where primality would eventually live. Cross deliberately.")
