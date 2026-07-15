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
Exponentials as Landauer licenses — A5 experiment (GIP, Note A)  [self-authored]

Linear-logic reading: linear logic removes weakening and contraction by default;
the exponential '!' licenses them back. You cannot DISCARD or COPY a formula
unless it sits under '!'. Section 4 established that DISCARD (weakening) is the
carrier of the priced erasure and COPY (contraction) is not. So the weakening
face of '!' is the license for the erasure the ledger prices.

This script does NOT assert that. It reuses the Section-4 simply-typed lambda
machinery VERBATIM (same gen/typable/normalize/is_linear, kinds included) so the
anchor numbers (N, #NF, forgotten leg) must reproduce Section 4 exactly. On top
it computes each term's STATIC exponential-license budget and tests whether it
lines up with the LEDGER structure.

Static license budget (typing-level, per term): walk every binder, count uses u
of its bound variable in the body:
   weakening licenses   w = # binders with u == 0
   contraction licenses c = sum over binders with u >= 2 of (u - 1)
   total ell = w + c ;  linear iff ell == 0.
STATIC, unlike Section 4's DYNAMIC step counts: K = \\x.\\y.x needs a weakening
license (y discarded) yet does zero reduction.

Prediction (from Section 4's weakening-vs-contraction asymmetry):
   ln(fan-in) rises with w but NOT with c, surviving a size control.
Entropies in nats.
"""

import math
from collections import defaultdict
import sys
sys.setrecursionlimit(100000)

# ================= Section-4 machinery, copied verbatim from structural_rules_ledger.py =================
_memo = {}
def gen(size, depth):
    key = (size, depth)
    if key in _memo:
        return _memo[key]
    out = []
    if size == 1:
        out = [('v', i) for i in range(depth)]
    else:
        out.extend(('l', b) for b in gen(size - 1, depth + 1))
        for s1 in range(1, size - 1):
            for f in gen(s1, depth):
                for x in gen(size - 1 - s1, depth):
                    out.append(('a', f, x))
    _memo[key] = out
    return out

def typable(term):
    subst = {}
    def prune(ty):
        while ty[0] == 'var' and ty[1] in subst:
            ty = subst[ty[1]]
        return ty
    def occurs(vid, ty):
        ty = prune(ty)
        if ty[0] == 'var':
            return ty[1] == vid
        return occurs(vid, ty[1]) or occurs(vid, ty[2])
    def unify(a, b):
        a, b = prune(a), prune(b)
        if a[0] == 'var':
            if b[0] == 'var' and b[1] == a[1]:
                return True
            if occurs(a[1], b):
                return False
            subst[a[1]] = b
            return True
        if b[0] == 'var':
            return unify(b, a)
        return unify(a[1], b[1]) and unify(a[2], b[2])
    nid = [0]
    def fresh():
        nid[0] += 1
        return ('var', nid[0])
    def go(t, env):
        if t[0] == 'v':
            return env[t[1]]
        if t[0] == 'l':
            tv = fresh()
            body = go(t[1], [tv] + env)
            if body is None:
                return None
            return ('fun', tv, body)
        f = go(t[1], env)
        if f is None:
            return None
        x = go(t[2], env)
        if x is None:
            return None
        r = fresh()
        if not unify(f, ('fun', x, r)):
            return None
        return r
    return go(term, []) is not None

def shift(t, d, c=0):
    if t[0] == 'v':
        return ('v', t[1] + d) if t[1] >= c else t
    if t[0] == 'l':
        return ('l', shift(t[1], d, c + 1))
    return ('a', shift(t[1], d, c), shift(t[2], d, c))

def subst_t(t, s, i=0):
    if t[0] == 'v':
        if t[1] == i:
            return shift(s, i)
        return ('v', t[1] - 1) if t[1] > i else t
    if t[0] == 'l':
        return ('l', subst_t(t[1], s, i + 1))
    return ('a', subst_t(t[1], s, i), subst_t(t[2], s, i))

def count_var(t, i=0):
    if t[0] == 'v':
        return 1 if t[1] == i else 0
    if t[0] == 'l':
        return count_var(t[1], i + 1)
    return count_var(t[1], i) + count_var(t[2], i)

def step(t):
    if t[0] == 'a' and t[1][0] == 'l':
        k = count_var(t[1][1])
        kind = 'K' if k == 0 else ('L' if k == 1 else 'C')
        return subst_t(t[1][1], t[2]), kind
    if t[0] == 'a':
        r = step(t[1])
        if r:
            return ('a', r[0], t[2]), r[1]
        r = step(t[2])
        if r:
            return ('a', t[1], r[0]), r[1]
        return None
    if t[0] == 'l':
        r = step(t[1])
        if r:
            return ('l', r[0]), r[1]
    return None

def normalize(t, fuel=2000):
    kinds = {'K': 0, 'L': 0, 'C': 0}
    while fuel > 0:
        r = step(t)
        if r is None:
            return t, kinds
        t = r[0]
        kinds[r[1]] += 1
        fuel -= 1
    raise RuntimeError("fuel exhausted")

def is_linear(t):
    if t[0] == 'l':
        return count_var(t[1]) == 1 and is_linear(t[1])
    if t[0] == 'a':
        return is_linear(t[1]) and is_linear(t[2])
    return True

def term_size(t):
    if t[0] == 'v':
        return 1
    if t[0] == 'l':
        return 1 + term_size(t[1])
    return 1 + term_size(t[1]) + term_size(t[2])

# ================= A5 addition: static exponential-license budget =================
def license_budget(t):
    w = 0
    c = 0
    def walk(node):
        nonlocal w, c
        if node[0] == 'v':
            return
        if node[0] == 'l':
            u = count_var(node[1], 0)   # uses of THIS binder's var (de Bruijn 0) in its body
            if u == 0:
                w += 1
            elif u >= 2:
                c += (u - 1)
            walk(node[1])
        else:  # 'a'
            walk(node[1])
            walk(node[2])
    walk(t)
    return w, c

# ================= statistics (pure python) =================
def pearson(xs, ys):
    n = len(xs)
    mx = sum(xs) / n
    my = sum(ys) / n
    cov = sum((x - mx) * (y - my) for x, y in zip(xs, ys))
    vx = sum((x - mx) ** 2 for x in xs)
    vy = sum((y - my) ** 2 for y in ys)
    if vx == 0 or vy == 0:
        return float('nan')
    return cov / math.sqrt(vx * vy)

def partial(xs, ys, zs):
    rxy = pearson(xs, ys)
    rxz = pearson(xs, zs)
    ryz = pearson(ys, zs)
    denom = math.sqrt(max(0.0, (1 - rxz ** 2) * (1 - ryz ** 2)))
    if denom == 0:
        return float('nan')
    return (rxy - rxz * ryz) / denom

# ================= run for a given cap =================
def run(SIZE_CAP):
    print("=" * 60)
    print(f"CAP {SIZE_CAP}")
    print("=" * 60)
    closed = []
    for s in range(2, SIZE_CAP + 1):
        closed.extend(gen(s, 0))
    terms = [t for t in closed if typable(t)]
    N = len(terms)
    print(f"Closed terms <= {SIZE_CAP}: {len(closed)};  typable proofs N = {N}")

    records = []
    nf_class = defaultdict(list)
    for t in terms:
        nf, kinds = normalize(t)
        records.append((t, nf, kinds))
        nf_class[nf].append((t, kinds))
    fanin_of = {}
    for nf, members in nf_class.items():
        for (t, kinds) in members:
            fanin_of[t] = len(members)

    # anchor check against Section 4
    H_forgot = sum((len(m) / N) * math.log(len(m)) for m in nf_class.values())
    print(f"ANCHOR vs Section 4: #NF = {len(nf_class)};  forgotten leg H(term|NF) = {H_forgot:.6f}")

    # per-term features
    W, C, L, SZ, LN = {}, {}, {}, {}, {}
    for t in terms:
        w, c = license_budget(t)
        W[t], C[t], L[t], SZ[t], LN[t] = w, c, w + c, term_size(t), math.log(fanin_of[t])

    # ---- (1) fragment coincidence + forgotten-leg attribution ----
    l0 = set(t for t in terms if L[t] == 0)
    lin = set(t for t in terms if is_linear(t))
    print("\n(1) Fragment coincidence  {ell==0}  vs  Section-4 is_linear")
    print(f"    |ell==0| = {len(l0)};  |is_linear| = {len(lin)};  EXACT MATCH: {l0 == lin}")
    if l0 != lin:
        print("    !! MISMATCH — static count disagrees with Section 4 — STOP")
        return
    fg_pos, fg_lin = 0.0, 0.0
    for nf, members in nf_class.items():
        k = len(members)
        contrib = (k / N) * math.log(k)
        if any(L[t] > 0 for (t, _) in members):
            fg_pos += contrib
        else:
            fg_lin += contrib
    print(f"    forgotten leg in classes touching ell>0 : {fg_pos:.4f} nats ({100*fg_pos/H_forgot:.2f}%)")
    print(f"    forgotten leg in purely-linear classes  : {fg_lin:.4f} nats ({100*fg_lin/H_forgot:.2f}%)")

    ys = [LN[t] for t in terms]
    zs = [SZ[t] for t in terms]

    def bin_table(KEY, name):
        by = defaultdict(list)
        for t in terms:
            by[KEY[t]].append(LN[t])
        for v in sorted(by):
            arr = by[v]
            print(f"    {name}={v}: n={len(arr):>6}   mean ln(fan-in) = {sum(arr)/len(arr):.4f}")

    # ---- (2) weakening license ----
    print("\n(2) Erasure vs weakening license w  (predict: RISES with w)")
    bin_table(W, "w")
    xs_w = [W[t] for t in terms]
    print(f"    r(w, ln fan-in) = {pearson(xs_w, ys):+.4f};  "
          f"size-controlled partial r(w, . | size) = {partial(xs_w, ys, zs):+.4f}")

    # ---- (3) contraction license ----
    print("\n(3) Erasure vs contraction license c  (predict: FLAT / no trend)")
    bin_table(C, "c")
    xs_c = [C[t] for t in terms]
    print(f"    r(c, ln fan-in) = {pearson(xs_c, ys):+.4f};  "
          f"size-controlled partial r(c, . | size) = {partial(xs_c, ys, zs):+.4f}")

    # ---- context ----
    print("\n    context: r(w,size)={:+.4f}  r(c,size)={:+.4f}  r(w,c)={:+.4f}  r(size,lnfan)={:+.4f}"
          .format(pearson(xs_w, zs), pearson(xs_c, zs), pearson(xs_w, xs_c), pearson(zs, ys)))
    print(f"    (w range {min(xs_w)}..{max(xs_w)}; c range {min(xs_c)}..{max(xs_c)})")

if __name__ == "__main__":
    run(9)
    run(11)
