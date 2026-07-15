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
Genesis Information Project - Stage 1, build paths (storage in action)
=====================================================================
Storing a merged tally and reusing it makes addition repeatable. A stored
intermediate is a BARE proto-integer - it remembers its length, not how it was
composed - so the next merge forgets its split again. Under the max-ignorance
(superposition) merge, a merge whose output has length m forgets ln(m+1).

    total build-erasure = sum over merges of ln(output_of_merge + 1)

We build the SAME proto-integer several ways and compare:
  - single merge vs finer decompositions (granularity)
  - balanced vs linear merge order (does order matter?)
  - repeated-same vs different piece values (at fixed piece count)

State function vs path function: if the total depends only on N it is a state
function (like energy); if it depends on the build it is a path function (heat).

Proto-integer hygiene: tallies are additive lengths; no factorization is
referenced; primality is neither presupposed nor sought.
"""

from math import log


def build_erasure(merge_outputs):
    """Total erasure = sum of ln(output+1) over the merges in the build."""
    return sum(log(m + 1) for m in merge_outputs)


def show(label, pieces, merge_outputs):
    e = build_erasure(merge_outputs)
    print(f"{label:>34} | {str(pieces):>14} | {len(merge_outputs):>6} | "
          f"{str(merge_outputs):>20} | {e:>8.4f}")


def header(title):
    print(f"\n{title}")
    print(f"{'build':>34} | {'pieces':>14} | {'merges':>6} | "
          f"{'merge outputs':>20} | {'erasure':>8}")
    print("-" * 96)


if __name__ == "__main__":
    # ---- Builds of N = 8 : granularity and order ----
    header("Builds of N = 8")
    show("single merge (2 pieces)", "4+4", [8])
    show("2+2+2+2  balanced", "2,2,2,2", [4, 4, 8])
    show("2+2+2+2  linear", "2,2,2,2", [4, 6, 8])
    show("1x8  balanced (binary tree)", "1x8", [2, 2, 2, 2, 4, 4, 8])
    show("1x8  linear", "1x8", [2, 3, 4, 5, 6, 7, 8])
    show("1+3+4  small-first", "1,3,4", [4, 8])
    show("1+3+4  large-first", "1,3,4", [7, 8])
    print(f"\n  floor (single merge) = ln(N+1) = ln 9 = {log(9):.4f}  "
          f"-- the cheapest way to reach 8; every finer build costs more.")

    # ---- Builds of N = 6 : repeated-same vs different, at 3 pieces ----
    header("Builds of N = 6  (3 pieces: same vs different values)")
    show("2+2+2  (same)  linear", "2,2,2", [4, 6])
    show("1+2+3  (different)  small-first", "1,2,3", [3, 6])
    show("1+2+3  (different)  large-first", "1,2,3", [5, 6])
    show("1+1+4  (two same)  small-first", "1,1,4", [2, 6])

    # ---- the additive ledger across N=6 builds, sorted ----
    print("\nWhat sets the cost is the profile of partial sums, not whether the "
          "pieces are equal.\nCombining the smallest pieces first keeps the "
          "intermediate sums - and the erasure - lowest.")
