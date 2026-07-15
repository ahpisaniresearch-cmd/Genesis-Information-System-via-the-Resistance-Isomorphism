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
Genesis Information Project - Stage 1, the stream over time
===========================================================
A bank of succession-clocks {g_1,...,g_N} ticks off one shared succession.
At each step the destructive meet-atom probe reads one bit per clock:
    bit_i(t) = 1 if the clock is home (g_i | t) else 0.
The readout B(t) is the bitstring the system emits from its current state.

We separate the TWO erasure interfaces and confirm they sum to the resistance:
    coarsening  (observation side)  = ln L - H(B)   destroyed at the measurement
    reset       (Maxwell's-demon)   = H(B)          record cleared to read again
    total per read-reset cycle      = ln L

and we decompose the recorded information H(B) across channels:
    sum of marginals  Sum_i H(1/g_i)
    joint             H(B)
    redundancy        Sum_i H(1/g_i) - H(B)   = connected correlation
                                                (zero iff channels independent / coprime)
"""

from math import log, gcd
from functools import reduce


def lcm(a, b):
    return a * b // gcd(a, b)


def lcm_list(gs):
    return reduce(lcm, gs, 1)


def H_binary(p):
    if p <= 0.0 or p >= 1.0:
        return 0.0
    return -(p * log(p) + (1 - p) * log(1 - p))


def entropy(weights):
    tot = sum(weights)
    h = 0.0
    for w in weights:
        if w > 0:
            pr = w / tot
            h -= pr * log(pr)
    return h


def bitstream(gs):
    """B(t) over one full period L = lcm(gs)."""
    L = lcm_list(gs)
    return L, [tuple(1 if t % g == 0 else 0 for g in gs) for t in range(L)]


def joint_HB(gs):
    L, stream = bitstream(gs)
    counts = {}
    for b in stream:
        counts[b] = counts.get(b, 0) + 1
    return L, entropy(list(counts.values())), counts


def analyze(gs):
    L, HB, _ = joint_HB(gs)
    lnL = log(L)
    sum_marg = sum(H_binary(1.0 / g) for g in gs)
    return {
        "gs": gs, "L": L, "lnL": lnL, "sum_marg": sum_marg, "HB": HB,
        "redundancy": sum_marg - HB,
        "coarsen": lnL - HB,   # observation-side erasure (expected)
        "reset": HB,           # demon record reset (expected)
    }


def show_stream(gs):
    """Concrete bitstream + per-readout information texture."""
    L, stream = bitstream(gs)
    counts = {}
    for b in stream:
        counts[b] = counts.get(b, 0) + 1
    print(f"\n=== Bank {gs} : period L = {L}, ln L = {log(L):.4f} ===")
    print(f"{'t':>2} | {'B(t)':>9} | {'P(b)':>5} | "
          f"{'resolved -lnP':>13} | {'residual ln|S|':>14} | {'sum':>6}")
    print("-" * 64)
    for t, b in enumerate(stream):
        P = counts[b] / L
        resolved = -log(P)          # info this readout pins down  (-> reset cost)
        residual = log(counts[b])   # ambiguity it leaves          (-> coarsened)
        print(f"{t:>2} | {str(b):>9} | {P:>5.2f} | "
              f"{resolved:>13.4f} | {residual:>14.4f} | {resolved+residual:>6.4f}")
    a = analyze(gs)
    print(f"averaged over the period:  reset H(B) = {a['reset']:.4f}   "
          f"coarsen = {a['coarsen']:.4f}   total = {a['lnL']:.4f}")


def compare(banks):
    print("\n=== Bank comparison (averaged per read-reset cycle) ===")
    print(f"{'bank':>12} | {'L':>3} | {'ln L':>6} | {'Sum Hi':>6} | {'H(B)':>6} | "
          f"{'redund':>6} | {'coarsen':>7} | {'reset':>6} | {'total':>6} | indep?")
    print("-" * 92)
    for gs in banks:
        a = analyze(gs)
        indep = "yes" if abs(a["redundancy"]) < 1e-12 else "no"
        print(f"{str(gs):>12} | {a['L']:>3} | {a['lnL']:>6.3f} | {a['sum_marg']:>6.3f} | "
              f"{a['HB']:>6.3f} | {a['redundancy']:>6.3f} | {a['coarsen']:>7.3f} | "
              f"{a['reset']:>6.3f} | {a['lnL']:>6.3f} | {indep}")


if __name__ == "__main__":
    show_stream((2, 3))    # coprime pair
    show_stream((2, 4))    # shared-factor pair
    compare([(2, 3), (2, 4), (2, 3, 5), (2, 4, 8), (2, 3, 4), (3, 5, 7)])
