import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().split())
adj = [[] for _ in range(n + 1)]
indeg = [0] * (n + 1)

for _ in range(m):
    a, b = map(int, input().split())
    adj[a].append(b)
    indeg[b] += 1

q = deque(i for i in range(1, n + 1) if indeg[i] == 0)
res = []

while q:
    u = q.popleft()
    res.append(u)
    for v in adj[u]:
        indeg[v] -= 1
        if indeg[v] == 0:
            q.append(v)

if len(res) != n:
    print(-1)
else:
    print(*res)
