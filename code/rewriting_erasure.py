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
Genesis Information Project - the string-rewriting family (conditional erasure)
==============================================================================
Find-and-act operations: locate the first occurrence of a pattern B in A, then
truncate / delete / substitute. What's new versus the additive operations is that
the erasure is CONDITIONAL - gated by whether B matches - so the test and the
forgetting are fused. Inputs without B pass through unchanged (fan-in 1, zero
erasure); inputs with B are erased.

Same method as always: erasure = ln(fan-in), and the two-legged ledger
    system erasure H(input|output) + demon reset H(output) = H(input).
"""

from math import log
from collections import defaultdict

L = 5            # inputs are all binary strings of length L
B = "11"         # the pattern
C = "0"          # replacement for substitute


def all_strings(n):
    return [format(i, f'0{n}b') for i in range(2 ** n)]


def truncate(A):
    i = A.find(B)
    return A if i < 0 else A[:i]                      # keep prefix before first B


def delete(A):
    i = A.find(B)
    return A if i < 0 else A[:i] + A[i + len(B):]     # splice out first B


def substitute(A):
    i = A.find(B)
    return A if i < 0 else A[:i] + C + A[i + len(B):]  # replace first B with C


inputs = all_strings(L)
N = 2 ** L
with_B = sum(1 for A in inputs if B in A)
print(f"L={L}, B='{B}', C='{C}': {with_B}/{N} inputs contain B (erased); "
      f"{N - with_B}/{N} have no B and pass through unchanged.\n")
print("  -> non-matching inputs map to themselves: fan-in 1, zero erasure (CONDITIONAL).\n")


def analyze(op):
    pre = defaultdict(int)
    for A in inputs:
        pre[op(A)] += 1
    Hout, mean_sys = 0.0, 0.0
    for fan in pre.values():
        p = fan / N
        Hout -= p * log(p)
        mean_sys += p * log(fan)
    return pre, Hout, mean_sys, log(N), max(pre.values())


rows = [(truncate, "truncate (find-cut)", "suffix from B on"),
        (delete, "delete (find-splice)", "B's position"),
        (substitute, "substitute (B->C)", "that it was B")]

print(f"{'operation':>22} | {'forgets':>16} | {'mean erase':>10} | "
      f"{'reset H(out)':>12} | {'total':>7} | {'max fan-in':>10}")
print("-" * 94)
for op, name, forgets in rows:
    pre, Hout, mean_sys, Hin, maxfan = analyze(op)
    print(f"{name:>22} | {forgets:>16} | {mean_sys:>10.4f} | "
          f"{Hout:>12.4f} | {mean_sys + Hout:>7.4f} | {maxfan:>10}")
print(f"\n(total should equal H(input) = L*ln2 = {L * log(2):.4f} for every row)")

print("\nTruncate per-output - the graded, exponential collapse "
      "(shorter prefix = more free suffix):")
pre = defaultdict(int)
for A in inputs:
    pre[truncate(A)] += 1
for out in sorted(pre, key=lambda o: (-pre[o], o)):
    if pre[out] > 1:
        label = out if out else "(empty)"
        print(f"   '{label}' <- {pre[out]:>2} inputs, erasure ln {pre[out]} = {log(pre[out]):.4f}")
