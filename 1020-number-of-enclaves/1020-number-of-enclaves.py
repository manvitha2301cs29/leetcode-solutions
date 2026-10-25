from collections import deque

class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        total_ones = sum(cell for row in grid for cell in row)

        def bfs(i, j):
            q = deque()
            q.append((i, j))
            grid[i][j] = 0  # Mark visited
            count = 1

            while q:
                x, y = q.popleft()
                for dx, dy in [(-1,0), (1,0), (0,-1), (0,1)]:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < m and 0 <= ny < n and grid[nx][ny] == 1:
                        grid[nx][ny] = 0
                        q.append((nx, ny))
                        count += 1
            return count

        boundary_ones = 0

        for i in range(m):
            for j in range(n):
                if (i == 0 or i == m - 1 or j == 0 or j == n - 1) and grid[i][j] == 1:
                    boundary_ones += bfs(i, j)

        return total_ones - boundary_ones

 

