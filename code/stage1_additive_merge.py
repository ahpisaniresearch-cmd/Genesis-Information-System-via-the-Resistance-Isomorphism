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
Genesis Information Project - Stage 1, the additive merge
=========================================================
The system's first IRREVERSIBLE operation. Two proto-integer tallies of lengths
a and b (unary strings, length only, NO multiplicity) are merged into one of
length n = a + b, forgetting the split (which a, which b).

Proto-integer hygiene: the merge references no factorization; primality is
neither presupposed nor sought. This step measures only the thermodynamics of
addition.

We separate the two legs and check the chain rule:
    system merge-erasure   = H(split | sum)        (the system's processing cost)
    demon read-reset       = H(sum) = H(n)         (recording the output, cleared)
    total per cycle        = H(a,b) = H(a)+H(b)     since (a,b) <-> (n, split)

and we read the per-merge law as a function of output size, plus its dependence
(or not) on the input prior.
"""

from math import log


def H(weights):
    """Shannon entropy (nats) of unnormalised weights (list or dict values)."""
    vals = list(weights.values()) if isinstance(weights, dict) else list(weights)
    tot = sum(vals)
    h = 0.0
    for w in vals:
        if w > 0:
            p = w / tot
            h -= p * log(p)
    return h


# ---------- Table 1 : the per-merge processing-erasure law ----------

def merge_law(nmax=10):
    print("Per-merge processing erasure as a function of output length n")
    print("(splits given the sum are uniform under both priors below):\n")
    print(f"{'n':>3} | {'#splits = n+1':>13} | {'merge-erasure  ln(n+1)':>22} | {'gas R = n+1':>11}")
    print("-" * 60)
    for n in range(nmax + 1):
        print(f"{n:>3} | {n + 1:>13} | {log(n + 1):>22.4f} | {n + 1:>11}")


# ---------- input priors over tally lengths ----------

def uniform_prior(M):
    return {a: 1.0 for a in range(M + 1)}                  # uniform on {0..M}


def geometric_prior(r, K=400):
    return {a: (1 - r) * r ** a for a in range(K + 1)}     # P(a) prop r^a


def split_and_output(prior):
    """Return (mean merge-erasure = E_n[H(split|sum=n)], output distribution P(n))."""
    tot = sum(prior.values())
    by_n = {}
    for a, wa in prior.items():
        for b, wb in prior.items():
            n = a + b
            by_n.setdefault(n, []).append((wa / tot) * (wb / tot))
    mean_merge = 0.0
    Pn = {}
    for n, ws in by_n.items():
        pn = sum(ws)
        Pn[n] = pn
        h_split = 0.0
        for w in ws:
            p = w / pn
            if p > 0:
                h_split -= p * log(p)
        mean_merge += pn * h_split
    return mean_merge, Pn


# ---------- Table 2 : the two-legged ledger under two priors ----------

def ledger_row(label, prior):
    input_info = 2 * H(prior)                 # H(a) + H(b), inputs independent
    mean_merge, Pn = split_and_output(prior)
    Hn = H(Pn)                                # output entropy = demon reset leg
    return label, input_info, Hn, mean_merge, mean_merge + Hn


if __name__ == "__main__":
    merge_law(10)

    print("\n\nTwo-legged ledger per merge-read-reset cycle (averaged over the prior):\n")
    print(f"{'prior':>20} | {'input H(a)+H(b)':>15} | {'demon reset H(n)':>16} | "
          f"{'mean merge-erase':>16} | {'reset+merge':>11}")
    print("-" * 90)
    for label, prior in [("uniform {0..8}", uniform_prior(8)),
                         ("geometric mean 4", geometric_prior(0.8))]:
        lab, inp, Hn, mm, tot = ledger_row(label, prior)
        print(f"{lab:>20} | {inp:>15.4f} | {Hn:>16.4f} | {mm:>16.4f} | {tot:>11.4f}")
    print("\nchain-rule check: reset + merge should equal input info, "
          "since H(a,b) = H(n) + H(split|n).")
