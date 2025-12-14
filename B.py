import sys
from collections import deque
input = sys.stdin.readline
    
n, m = map(int, input().split())
adj = [[] for _ in range(n+1)]
for _ in range(m):
    u, v = map(int, input().split())
    adj[u].append(v)
    adj[v].append(u)
    
color = [-1] * (n+1)
ans = 0
    
for i in range(1, n+1):
    if color[i] == -1:
        dq = deque([i])
        color[i] = 0
        c0, c1 = 1, 0
        while dq:
            x = dq.popleft()
            for y in adj[x]:
                if color[y] == -1:
                    color[y] = color[x] ^ 1
                    if color[y] == 0:
                        c0 += 1
                    else:
                        c1 += 1
                    dq.append(y)
        ans += max(c0, c1)
    
print(ans)