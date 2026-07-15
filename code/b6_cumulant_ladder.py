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

"""B6 — cumulant ladder (self-authored). Tests whether 'matching d cumulants' is
what depth-d hiding costs, and whether the erasure-cascade cost deviates from the
classical moment/support bound (promote) or tracks it (park)."""
import sympy as sp
import numpy as np
from fractions import Fraction
from math import comb, ceil

# ---------------- (1) EXACT cascade cumulants ----------------
# cascade firing count = sum of independent Bernoulli(2^-k), k>=1.
# kappa_j(cascade) = sum_k kappa_j(Bernoulli(2^-k)); kappa_j(Bernoulli(p)) is a
# polynomial in p with zero constant term; sum_k (2^-k)^j = 1/(2^j - 1).
t, p = sp.symbols('t p')
cgf = sp.log(1 - p + p*sp.exp(t))
def bern_cumulant_poly(j):
    return sp.expand(sp.diff(cgf, t, j).subs(t, 0))
def S(j):
    return Fraction(1, 2**j - 1)
def cascade_cumulant(j):
    poly = sp.Poly(bern_cumulant_poly(j), p)
    tot = Fraction(0)
    for (power,), coeff in poly.terms():
        c = Fraction(int(coeff))
        assert power >= 1, "unexpected constant term in a cumulant"
        tot += c * S(power)
    return tot

print("(1) EXACT cascade cumulants  (kappa_j, from sum_k Bernoulli(2^-k)):")
casc = {}
for j in range(1, 7):
    kj = cascade_cumulant(j)
    casc[j] = kj
    print(f"    kappa_{j} = {str(kj):>8}  = {float(kj):+.9f}")
LN2 = np.log(2)
print(f"    cross-check: kappa_1={float(casc[1]):.6f} (=1), "
      f"kappa_2*ln2^2 = {float(casc[2])*LN2**2:.9f}  (heat variance (2/3)ln2^2)")

# ---------------- cumulants from an exact pmf (rationals) ----------------
def cumulants_from_pmf(pmf, order):
    # raw moments about 0
    mu = [Fraction(0)]*(order+1)
    mu[0] = Fraction(1)
    for r in range(1, order+1):
        mu[r] = sum(Fraction(x)**r * w for x, w in pmf.items())
    kap = [None]*(order+1)
    for n in range(1, order+1):
        s = mu[n]
        for m in range(1, n):
            s -= comb(n-1, m-1) * kap[m] * mu[n-m]
        kap[n] = s
    return kap[1:]

# ---------------- (2) ladder EXISTS (exact, general distributions) ----------------
# finite-difference signed measure w_i = (-1)^i C(d+1,i) on {0..d+1} has vanishing
# moments 0..d and nonzero moment d+1. base = Binomial(d+1,1/2). P = base+eps*w, Q = base-eps*w.
print("\n(2) Ladder exists (EXACT, general distributions on {0..d+1}):")
for d in range(1, 5):
    n = d + 1
    base = {i: Fraction(comb(n, i), 2**n) for i in range(n+1)}
    w    = {i: Fraction((-1)**i * comb(n, i)) for i in range(n+1)}
    eps  = Fraction(1, 2**(n+1))   # < min base weight, keeps P,Q >= 0
    P = {i: base[i] + eps*w[i] for i in range(n+1)}
    Q = {i: base[i] - eps*w[i] for i in range(n+1)}
    assert all(v >= 0 for v in P.values()) and all(v >= 0 for v in Q.values())
    assert sum(P.values()) == 1 and sum(Q.values()) == 1
    kP = cumulants_from_pmf(P, d+1)
    kQ = cumulants_from_pmf(Q, d+1)
    match = all(kP[i] == kQ[i] for i in range(d))      # kappa_1..kappa_d
    diff  = kP[d] != kQ[d]                              # kappa_{d+1}
    print(f"    d={d}: kappa_1..kappa_{d} match: {match};  kappa_{d+1} differs: {diff}  "
          f"(kP[{d+1}]={str(kP[d]):>7}, kQ[{d+1}]={str(kQ[d]):>7})")

# ---------------- (3) COST discriminator: cascade stages vs free support ----------------
# free-support bound: s points -> 2s-1 params; distinct pair matching d moments needs 2s-1>d
#   => s_free(d) = ceil(d/2)+1
# cascade bound (independent Bernoulli stages): kappa_1..kappa_d <-> power sums P_1..P_d;
#   a size-s multiset is fixed by P_1..P_s (Newton), so distinct pair needs s>d => s_cascade(d)=d+1.
def cascade_cumulants_numeric(qs, order):
    pmf = {0: 1.0}
    for q in qs:                       # convolve Bernoulli(q)
        new = {}
        for x, wt in pmf.items():
            new[x]   = new.get(x, 0.0) + wt*(1-q)
            new[x+1] = new.get(x+1, 0.0) + wt*q
        pmf = new
    mu = [0.0]*(order+1); mu[0] = 1.0
    for r in range(1, order+1):
        mu[r] = sum((x**r)*wt for x, wt in pmf.items())
    kap = [0.0]*(order+1)
    for nn in range(1, order+1):
        s = mu[nn]
        for m in range(1, nn):
            s -= comb(nn-1, m-1)*kap[m]*mu[nn-m]
        kap[nn] = s
    return kap[1:]

def distinct_cascade_pair_at(d, s):
    """Try to build two distinct s-stage cascades matching kappa_1..kappa_d.
       Perturb the constant term of prod(x-b_i); roots share e_1..e_{s-1}? No —
       constant term is e_s, so P_1..P_{s-1} unchanged, P_s changes. Works only when
       s-1 >= d, i.e. s >= d+1."""
    b = np.linspace(0.2, 0.8, s)
    poly = np.poly(b)                       # monic, roots b
    for delta in (1e-2, 3e-3, 1e-3, 3e-4, 1e-4):
        p2 = poly.copy(); p2[-1] += delta   # shift constant term = e_s
        r = np.roots(p2)
        if np.max(np.abs(r.imag)) < 1e-9:
            rr = np.sort(r.real)
            if rr.min() >= 0.0 and rr.max() <= 1.0:
                k1 = cascade_cumulants_numeric(b, d+1)
                k2 = cascade_cumulants_numeric(rr, d+1)
                match = all(abs(k1[i]-k2[i]) < 1e-9 for i in range(d))
                differ = abs(k1[d]-k2[d]) > 1e-9
                distinct = np.max(np.abs(np.sort(b)-rr)) > 1e-9
                if match and differ and distinct:
                    return True, rr
    return False, None

print("\n(3) Cost of hiding depth d:  free-support bound  vs  cascade-stage bound")
print(f"    {'d':>2} {'s_free=ceil(d/2)+1':>18} {'s_cascade=d+1':>14}  {'distinct (d+1)-stage pair matches k1..kd?':>44}")
for d in range(1, 5):
    s_free = ceil(d/2) + 1
    s_casc = d + 1
    ok, rr = distinct_cascade_pair_at(d, s_casc)
    # also confirm a d-stage cascade CANNOT (Newton): try and expect failure
    ok_short, _ = distinct_cascade_pair_at(d, d) if d >= 2 else (False, None)
    print(f"    {d:>2} {s_free:>18} {s_casc:>14}  {str(ok):>10}   (d-stage pair exists: {ok_short})")
print("    minimality of s_cascade=d+1 is Newton's identities (size-s multiset fixed by P_1..P_s);")
print("    s_free=ceil(d/2)+1 is Gauss quadrature (s points fix 2s-1 moments). Both are classical.")
