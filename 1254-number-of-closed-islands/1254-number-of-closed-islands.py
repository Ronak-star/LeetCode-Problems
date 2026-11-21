from collections import deque
from typing import List

class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])

        visit = [[False] * n for _ in range(m)]
        count = 0

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0 and not visit[i][j]:
                    if self.bfs(i, j, m, n, grid, visit):
                        count += 1

        return count

    def bfs(self, x: int, y: int, m: int, n: int,
            grid: List[List[int]], visit: List[List[bool]]) -> bool:

        q = deque([(x, y)])
        visit[x][y] = True
        is_closed = True

        dirx = [0, 1, 0, -1]
        diry = [-1, 0, 1, 0]

        while q:
            r, c = q.popleft()

            for i in range(4):
                nr = r + dirx[i]
                nc = c + diry[i]

                if nr < 0 or nr >= m or nc < 0 or nc >= n:
                    is_closed = False

                elif grid[nr][nc] == 0 and not visit[nr][nc]:
                    visit[nr][nc] = True
                    q.append((nr, nc))

        return is_closed