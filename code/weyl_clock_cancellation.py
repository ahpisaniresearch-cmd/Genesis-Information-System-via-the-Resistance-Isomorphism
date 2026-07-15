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
GIP - the Weyl-clock-cancellation bridge (a careful first step)
================================================================
Honest framing up front. This DOES NOT touch the location of the zeros and claims
nothing about RH. It illustrates ONE thing: that the continuous critical-line
cancellation is the same MECHANISM as the discrete cancellation in our proto-phase
work - destructive interference of phasors - with the resistances ln n (the
forgetting-costs we cataloged) as the spin rates. The zeros are classical; the
resistance relabeling and the discrete-seed connection are the only framework content.

Part 1: our discrete proto-phase already has exact total cancellation -
        the d-th roots of unity sum to zero (uniform amplitudes, uniform phases).
        The genesis bit d=2 is 1 + (-1) = 0: the NOT cancellation.
Part 2: the zeta bouquet is the SAME idea with LOG-spaced phases t*ln n and
        amplitudes n^{-1/2}. It cancels only at special t - the zeros - which we
        confirm (as we must, since the bouquet IS the continued zeta function).
"""
import numpy as np
import mpmath as mp
mp.mp.dps = 30

# ---- Part 1: the discrete cancellation seed (exact) ----
print("Part 1 - discrete proto-phase cancellation seed: roots of unity sum to zero")
for d in [2, 3, 4, 5, 6]:
    w = np.exp(2j * np.pi / d)
    s = sum(w ** k for k in range(d))
    tag = "  <- genesis bit: 1 + (-1) = 0 (the NOT cancellation)" if d == 2 else ""
    print(f"  d={d}: |sum_k omega^k| = {abs(s):.1e}{tag}")
print("  uniform amplitudes, uniform phases -> exact cancellation for every d.\n")

# ---- Part 2: the resistance-phasor bouquet on the critical line ----
# eta(1/2+it) = sum_{n>=1} (-1)^{n-1} n^{-1/2} e^{-i t ln n}
# amplitude n^{-1/2}, phase -t*ln n (= -t * resistance), alternating sign (the 2-phase).
def bouquet(t, sigma=0.5):
    s = mp.mpc(sigma, t)
    return mp.nsum(lambda n: (-1) ** (int(n) - 1) * mp.e ** (-s * mp.log(n)), [1, mp.inf])

known = [14.134725, 21.022040, 25.010858, 30.424876]   # classical first zeros
print("Part 2 - the LOG-spaced bouquet |eta(1/2 + it)| at known zeros vs midpoints:")
print(f"{'t':>11} | {'|bouquet|':>11} | note")
pts = [(z, "known zero") for z in known] + \
      [((a + b) / 2, "midpoint") for a, b in zip(known, known[1:])]
for t, note in sorted(pts):
    print(f"{t:>11.4f} | {float(abs(bouquet(t))):>11.2e} | {note}")

# ---- a coarse scan: do the bouquet's nulls sit where the known zeros are? ----
print("\nCoarse scan of |bouquet| over t in [12, 32] (dips = interference nulls):")
ts = np.arange(12.0, 32.01, 0.5)
vals = [float(abs(bouquet(float(t)))) for t in ts]
for t, v in zip(ts, vals):
    bar = "#" * int(min(v, 2.0) / 2.0 * 40)
    near = "  <- near known zero" if any(abs(t - z) < 0.5 for z in known) else ""
    print(f"  t={t:5.1f} |{bar:<40}| {v:.3f}{near}")
