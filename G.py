import sys
import heapq

def solve() -> None:
    input = sys.stdin.readline
    n = int(input().strip())
    words = [input().strip() for _ in range(n)]

    present = [False] * 26
    for w in words:
        for ch in w:
            present[ord(ch) - 97] = True

    adj = [[] for _ in range(26)]
    indeg = [0] * 26
    has_edge = [[False] * 26 for _ in range(26)]


    for i in range(n - 1):
        a, b = words[i], words[i + 1]
        m = min(len(a), len(b))
        j = 0
        while j < m and a[j] == b[j]:
            j += 1

        if j == m:

            if len(a) > len(b):
                print(-1)
                return
        else:
            u = ord(a[j]) - 97
            v = ord(b[j]) - 97
            if not has_edge[u][v]:
                has_edge[u][v] = True
                adj[u].append(v)
                indeg[v] += 1


    pq = []
    total = 0
    for i in range(26):
        if present[i]:
            total += 1
            if indeg[i] == 0:
                heapq.heappush(pq, i)

    ans = []
    while pq:
        u = heapq.heappop(pq)
        ans.append(chr(u + 97))
        for v in adj[u]:
            indeg[v] -= 1
            if indeg[v] == 0 and present[v]:
                heapq.heappush(pq, v)

    if len(ans) != total:
        print(-1)  # cycle
    else:
        print("".join(ans))

if __name__ == "__main__":
    solve()
