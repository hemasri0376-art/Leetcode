class Solution:
    def countIslands(self, grid: List[List[int]], k: int) -> int:
        m, n = len(grid), len(grid[0])
        ans = 0
        for i in range(m):
            for j in range(n):
                if not grid[i][j]:
                    continue
                total, grid[i][j], island = grid[i][j], 0, [(i, j)] 
                for x, y in island:  
                    for a, b in (x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1):
                        if 0 <= a < m and 0 <= b < n and grid[a][b]:
                            total += grid[a][b]
                            grid[a][b] = 0 
                            island.append((a, b))
                ans += total % k == 0
        return ans