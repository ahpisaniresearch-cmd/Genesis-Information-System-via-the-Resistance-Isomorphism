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
Genesis Information Project - Stage 1
=====================================
Mapping the erasure math over a single succession-cycle channel under
superposition, read by the destructive meet-atom probe.

QUANTITY-FREE FRAMING (no number theory is used to build the channel):
  * A "channel" is the orbit of succession (NOT-propagated-through-nesting) that
    returns to its origin after g steps. g is the channel's GIRTH (return-time):
    a structural parameter, NOT a quantity we impose.
  * "Superposition" = the maximum-entropy belief state over the channel's g
    internal states (Axiom 3, state form): uniform, entropy ln g.
  * The genesis probe is the destructive meet-atom: the binary test
    "is the state the origin?". On a single channel this IS the divisibility atom.
    Being destructive, it records the partition and erases the rest.
  * PRIMALITY IS AN OUTPUT. A channel is irreducible ("prime") iff its succession
    cycle has no proper sub-period. Detected by RUNNING succession at every stride
    and looking for an early return - never by arithmetic factoring.

PER CHANNEL WE MEASURE (all in nats):
  ln g                            the conserved state-information (full forget cost)
  H(1/g)            [kept]        what the destructive probe records  (extracted)
  (1-1/g) ln(g-1)   [erased]      what the destructive probe coarsens away (dumped)
  kept + erased  == ln g          the chain rule / the conservation law
  reversible-run erasure          H(in)-H(out) for the advance permutation  -> 0
  overwrite erasure               H(in)-H(out) for the reset map            -> ln g
  efficiency = kept / ln g        extraction efficiency of the meet-atom probe

REFINEMENT UNDER TEST (from the direction note, sec 4):
  Are processing erasure and probe erasure two INDEPENDENT addends summing to ln g,
  or two FACES of one conserved quantity? Stage 1 answers it.
"""

from math import log


# ---------- information measures (nats) ----------

def H_binary(p):
    """Entropy of a two-outcome split {p, 1-p}."""
    if p <= 0.0 or p >= 1.0:
        return 0.0
    return -(p * log(p) + (1 - p) * log(1 - p))


def entropy(weights):
    """Entropy of a distribution given as unnormalised non-negative weights."""
    total = sum(weights)
    h = 0.0
    for w in weights:
        if w > 0:
            pr = w / total
            h -= pr * log(pr)
    return h


# ---------- the succession dynamics on a channel of girth g ----------

def advance_image(g):
    """Succession on the channel: state -> (state + 1) mod g.  Returns the image."""
    return [(x + 1) % g for x in range(g)]


def overwrite_image(g):
    """Reset / overwrite: every state -> origin (0)."""
    return [0 for _ in range(g)]


def is_permutation(image, g):
    return sorted(image) == list(range(g))


def map_erasure(image, g):
    """
    Landauer erasure of a deterministic map on the uniform (superposition) input:
        H(input ensemble) - H(output ensemble).
    A permutation -> 0 (reversible). A full reset -> ln g (everything dumped).
    """
    h_in = entropy([1] * g)                  # uniform over g states
    counts = {}
    for y in image:
        counts[y] = counts.get(y, 0) + 1     # preimage count per output value
    h_out = entropy(list(counts.values()))
    return h_in - h_out


# ---------- the destructive meet-atom probe ("is the state the origin?") ----------

def probe_split(g):
    """
    Partition the g superposed states into {origin} (1 state) and {rest} (g-1 states).
        kept   = I(state; outcome) = H(outcome)              = H(1/g)
        erased = H(state | outcome) (destroyed, probe is destructive)
               = (1/g)*0  +  ((g-1)/g)*ln(g-1)               = (1-1/g) ln(g-1)
    """
    kept = H_binary(1.0 / g)
    erased = ((g - 1) / g) * (log(g - 1) if g >= 2 else 0.0)
    return kept, erased


# ---------- structural primality test (OUTPUT), by running succession ----------

def orbit_length(stride, g):
    """Steps for the orbit 0, stride, 2*stride, ... mod g to return to 0.
       Genesis-native: we RUN succession at this stride, we do not factor."""
    x, steps = 0, 0
    while True:
        x = (x + stride) % g
        steps += 1
        if x == 0:
            return steps


def discovered_subperiods(g):
    """Proper sub-periods found by running succession at each stride (structural)."""
    periods = set()
    for stride in range(1, g):
        L = orbit_length(stride, g)
        if 1 < L < g:
            periods.add(L)
    return sorted(periods)


def is_prime_channel(g):
    """Irreducible iff NO stride produces a proper sub-period (no early return)."""
    return g >= 2 and len(discovered_subperiods(g)) == 0


# ---------- survey ----------

def report():
    hdr = (f"{'g':>3} {'prime?':>6} {'ln g':>8} {'kept':>8} {'erased':>8} "
           f"{'k+e':>8} {'chain':>6} {'runE':>5} {'ovrE':>8} {'eff':>6} {'subperiods':>14}")
    print(hdr)
    print("-" * len(hdr))
    for g in range(2, 13):
        lng = log(g)
        kept, erased = probe_split(g)
        chain = kept + erased
        chain_ok = abs(chain - lng) < 1e-12

        adv = advance_image(g)
        assert is_permutation(adv, g)               # succession is reversible
        runE = map_erasure(adv, g)                  # expect 0
        ovrE = map_erasure(overwrite_image(g), g)   # expect ln g

        eff = kept / lng
        prime = is_prime_channel(g)
        subs = discovered_subperiods(g)
        print(f"{g:>3} {str(prime):>6} {lng:>8.5f} {kept:>8.5f} {erased:>8.5f} "
              f"{chain:>8.5f} {str(chain_ok):>6} {runE:>5.2f} {ovrE:>8.5f} "
              f"{eff:>6.3f} {str(subs):>14}")

    # the conservation law, stated as one number reached two ways
    print("\nConservation check (one budget, two routes), sample g = 6:")
    k, e = probe_split(6)
    ovr = map_erasure(overwrite_image(6), 6)
    print(f"   probe:  kept {k:.5f} + erased {e:.5f} = {k+e:.5f}")
    print(f"   overwrite erasure                    = {ovr:.5f}")
    print(f"   ln 6                                 = {log(6):.5f}")
    print("   -> the SAME conserved ln g, partitioned by the probe vs dumped by overwrite.")

    # primality as an OUTPUT, collected over a wider range with no factoring
    primes_found = [g for g in range(2, 50) if is_prime_channel(g)]
    print("\nPrimality discovered structurally (running succession only), g = 2..49:")
    print("  ", primes_found)

    # the genesis bit
    k2, e2 = probe_split(2)
    print(f"\nGenesis bit g = 2:  kept = {k2:.6f}   erased = {e2:.6f}")
    print("  -> the unique channel whose destructive probe erases NOTHING (lossless).")

    # extraction efficiency falls from 1
    print("\nExtraction efficiency H(1/g)/ln g of the meet-atom probe:")
    for g in [2, 3, 5, 7, 11, 13]:
        k, _ = probe_split(g)
        print(f"   g={g:>2}:  {k/log(g):.4f}")


if __name__ == "__main__":
    report()
