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

"""Z2 — arithmetic structure in the primon cumulants? (self-authored)
Tests whether any cumulant-LEVEL property is prime-specific, or whether the arithmetic
is entirely in the spectrum {ln p} with the cumulant algebra generic.
 (1) independent-prime-mode decomposition: kappa_j = sum_p (ln p)^j g_j(p^-s), g_j = geometric cumulant.
 (2) CGF = shift of log zeta: K(t) = log zeta(s-t) - log zeta(s).
 (3) universal pole: kappa_j(s) (s-1)^j -> (j-1)!  as s->1+.
 (4a) subleading constant: kappa_1(s) - 1/(s-1) -> -gamma (Euler-Mascheroni).
 (4b) null comparison: standardized cumulants of primon vs fake-prime vs all-integer mode gases.
Promote iff a cumulant-level RELATION holds for primes but not the generic null. Expect: park."""
import mpmath as mp
import math
mp.mp.dps = 40

def sieve_primes(n):
    s=bytearray([1])*(n+1); s[0]=s[1]=0
    for i in range(2,int(n**0.5)+1):
        if s[i]:
            for j in range(i*i,n+1,i): s[j]=0
    return [i for i in range(2,n+1) if s[i]]
PRIMES = sieve_primes(2_000_000)

# geometric-distribution cumulants g_j(x), x = p^-s  (occupation ~ Geometric(x))
def g(j,x):
    o=1-x
    if j==1: return x/o
    if j==2: return x/o**2
    if j==3: return x*(1+x)/o**3
    if j==4: return x*(1+4*x+x*x)/o**4
    raise ValueError
def kappa_modes(j, s, modes):
    tot=0.0
    for e in modes:                       # e = ln(mode)
        x=math.exp(-s*e)
        if x<=0 or x>=1: continue
        tot += (e**j)*g(j,x)
    return tot
def kappa_true(j, s):                      # ground truth = (-1)^j (log zeta)^(j)(s)
    return ((-1)**j)*mp.diff(lambda x: mp.log(mp.zeta(x)), s, j)

# ---------------- (1) decomposition vs ground truth ----------------
print("(1) Independent-prime-mode decomposition  kappa_j = sum_p (ln p)^j g_j(p^-s)")
logp=[math.log(p) for p in PRIMES]
for s in (2.0,3.0):
    print(f"    s={s}")
    for j in range(1,5):
        km=kappa_modes(j,s,logp); kt=float(kappa_true(j,s))
        print(f"      kappa_{j}: mode-sum={km:.10f}  truth={kt:.10f}  |diff|={abs(km-kt):.2e}")

# ---------------- (2) CGF = shift of log zeta ----------------
print("\n(2) CGF = shift:  kappa_j = j! * [t^j]( log zeta(s-t) - log zeta(s) )   at s=2")
s=mp.mpf(2)
K = lambda t: mp.log(mp.zeta(s-t)) - mp.log(mp.zeta(s))
for j in range(1,5):
    coeff = mp.diff(K, mp.mpf(0), j)          # d^j K/dt^j at 0 = kappa_j
    print(f"      kappa_{j} via CGF = {mp.nstr(coeff,10)}   truth = {mp.nstr(kappa_true(j,2.0),10)}")

# ---------------- (3) universal pole ----------------
print("\n(3) Universal pole:  kappa_j(s) * (s-1)^j  ->  (j-1)!   as s->1+")
import math as _m
fact=[_m.factorial(j-1) for j in range(1,5)]
for s in (mp.mpf('1.1'), mp.mpf('1.01'), mp.mpf('1.001')):
    row=[]
    for j in range(1,5):
        val=kappa_true(j,float(s))*(s-1)**j
        row.append(mp.nstr(val,8))
    print(f"    s={mp.nstr(s,5):>7}:  " + "   ".join(f"j={j}:{row[j-1]}(target {fact[j-1]})" for j in range(1,5)))

# ---------------- (4a) subleading constant = -gamma ----------------
print("\n(4a) Subleading constant:  kappa_1(s) - 1/(s-1)  ->  -gamma")
for s in (mp.mpf('1.01'), mp.mpf('1.001'), mp.mpf('1.0001')):
    val=kappa_true(1,float(s)) - 1/(s-1)
    print(f"    s={mp.nstr(s,6):>8}:  kappa_1 - 1/(s-1) = {mp.nstr(val,10)}   (-gamma = {mp.nstr(-mp.euler,10)})")

# ---------------- (4b) null comparison: standardized cumulants at s=2 ----------------
print("\n(4b) Null comparison — standardized cumulants at s=2 (skew=k3/k2^1.5, exkurt=k4/k2^2)")
# fake primes q_k ~ k ln k, forced strictly increasing integers >=2
fake=[]; prev=1
for k in range(2, 300000):
    q=int(round(k*math.log(k)))
    if q<=prev: q=prev+1
    if q<2: q=2
    fake.append(q); prev=q
fake_modes=[math.log(q) for q in fake]
int_modes=[math.log(m) for m in range(2, 2_000_001)]
prime_modes=logp
for name,modes in [("primon (primes)",prime_modes),("fake-primes k ln k",fake_modes),("all-integers m>=2",int_modes)]:
    k2=kappa_modes(2,2.0,modes); k3=kappa_modes(3,2.0,modes); k4=kappa_modes(4,2.0,modes)
    skew=k3/k2**1.5; exk=k4/k2**2
    print(f"    {name:<22} k2={k2:.5f}  skew={skew:.5f}  exkurt={exk:.5f}")
print("    (all three are generic geometric-mode shapes; no primon-specific cumulant relation.)")
