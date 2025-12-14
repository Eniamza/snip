

import sys
from collections import deque
    
read = sys.stdin.readline
n = int(read())
adj = [[] for _ in range(n + 1)]
for _ in range(n - 1):
    u, v = map(int, read().split()); adj[u].append(v); adj[v].append(u)
    
def bfs(s):
    dist = [-1] * (n + 1)
    q = deque([s])
    dist[s] = 0
    far = s
    while q:
        u = q.popleft()
        for v in adj[u]:
            if dist[v] == -1:
                dist[v] = dist[u] + 1
                q.append(v)
                if dist[v] > dist[far]:
                    far = v
    return far, dist
    
a, _    = bfs(1)
b, dist = bfs(a)
print(dist[b])
print(a, b)