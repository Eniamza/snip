import sys
from collections import deque

MAXN = 5000

def build_prime_factors_upto(n=MAXN):
    spf = [0] * (n + 1)
    for i in range(2, n + 1):
        if spf[i] == 0:
            spf[i] = i
            if i * i <= n:
                for j in range(i * i, n + 1, i):
                    if spf[j] == 0:
                        spf[j] = i


    pf = [[] for _ in range(n + 1)]
    for x in range(2, n + 1):
        v = x
        last = 0
        while v > 1:
            p = spf[v]
            if p != last:
                if p < x:            
                    pf[x].append(p)
                last = p
            v //= p
    return pf

PF = build_prime_factors_upto(MAXN)

def min_steps(s, t):
    if s == t:
        return 0
    if s > t:
        return -1

    dist = [-1] * (t + 1)
    q = deque([s])
    dist[s] = 0

    while q:
        cur = q.popleft()
        for p in PF[cur]:
            nxt = cur + p
            if nxt <= t and dist[nxt] == -1:
                dist[nxt] = dist[cur] + 1
                if nxt == t:
                    return dist[nxt]
                q.append(nxt)
    return dist[t]

def main():
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    T = int(next(it))
    out = []
    for _ in range(T):
        s = int(next(it)); t = int(next(it))
        out.append(str(min_steps(s, t)))
    print("\n".join(out))

if __name__ == "__main__":
    main()
