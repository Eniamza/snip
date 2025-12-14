import sys
from collections import deque

def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    it = iter(data)

    n = next(it); m = next(it); s = next(it); q = next(it)

    g = [[] for _ in range(n + 1)]
    for _ in range(m):
        u = next(it); v = next(it)
        g[u].append(v)
        g[v].append(u)

    dist = [-1] * (n + 1)
    dq = deque()

    for _ in range(s):
        x = next(it)
        if dist[x] == -1:
            dist[x] = 0
            dq.append(x)

    while dq:
        u = dq.popleft()
        du = dist[u] + 1
        for v in g[u]:
            if dist[v] == -1:
                dist[v] = du
                dq.append(v)

    ans = []
    for _ in range(q):
        d = next(it)
        ans.append(str(dist[d]))

    sys.stdout.write(" ".join(ans))

if __name__ == "__main__":
    main()
