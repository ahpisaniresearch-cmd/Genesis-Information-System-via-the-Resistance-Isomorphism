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
GIP - modulo: the multiplicative gateway
a -> a mod m forgets the QUOTIENT floor(a/m) and keeps the remainder.
fan-in of a residue = how many inputs share it = the quotient (M+1)/m.
This is the first operation whose fan-in is a DIVISION, not a count or sum.
"""
from math import log
from collections import defaultdict

M = 11                       # inputs a in 0..M, M+1 = 12 (divisors 1,2,3,4,6,12)
vals = list(range(M + 1))

print(f"modulo a -> a mod m,  a in 0..{M}  (M+1 = {M+1});  erasure = ln(fan-in)")
print("fan-in(r) = #{a : a = r mod m} = the quotient; modulo forgets floor(a/m)\n")
print(f"{'m':>3} | {'#residues':>9} | {'fan-in per residue':>18} | {'erasure':>12} | note")
print("-" * 66)
for m in [1, 2, 3, 4, 6, 12, 5, 7]:
    counts = defaultdict(int)
    for a in vals:
        counts[a % m] += 1
    fans = sorted(set(counts.values()))
    if len(fans) == 1:
        f = fans[0]
        fan_str = f"{f} = (M+1)/{m}"
        eras = "0" if f == 1 else f"ln {f}"
        note = "reset" if m == 1 else ("identity" if m == M + 1 else "m | 12, uniform")
    else:
        fan_str = f"{fans[0]} or {fans[1]}"
        eras = f"ln {fans[0]} / ln {fans[1]}"
        note = "m does not divide 12: near-uniform"
    print(f"{m:>3} | {m:>9} | {fan_str:>18} | {eras:>12} | {note}")
