from collections import deque
    
def solve():
    size = int(input())
    sx, sy, tx, ty = map(int, input().split())
    sx -= 1; sy -= 1; tx -= 1; ty -= 1
    
    if sx == tx and sy == ty:
        print(0)
        return
    
    knight_moves = [
        (2, 1), (1, 2), (-1, 2), (-2, 1),
        (-2, -1), (-1, -2), (1, -2), (2, -1)
    ]
    
    total_squares = size * size
    visited = [False] * total_squares
    
    start_idx = sx * size + sy
    target_idx = tx * size + ty
    visited[start_idx] = True
    
    queue = deque([start_idx])
    steps = 0
    
    while queue:
        steps += 1
        for _ in range(len(queue)):
            current = queue.popleft()
            cx, cy = divmod(current, size)
            for dx, dy in knight_moves:
                nx, ny = cx + dx, cy + dy
                if 0 <= nx < size and 0 <= ny < size:
                    next_idx = nx * size + ny
                    if not visited[next_idx]:
                        if next_idx == target_idx:
                            print(steps)
                            return
                        visited[next_idx] = True
                        queue.append(next_idx)
    
    print(-1)
    
if __name__ == "__main__":
    solve()