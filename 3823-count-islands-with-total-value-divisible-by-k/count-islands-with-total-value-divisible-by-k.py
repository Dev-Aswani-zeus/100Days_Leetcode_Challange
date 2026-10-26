class Solution:
    def countIslands(self, grid: list[list[int]], k: int) -> int:
        rows = len(grid)
        cols = len(grid[0])
        def dfs(r, c):
            if r < 0 or r >= rows or c < 0 or c >= cols:
                return 0
            if grid[r][c] == 0:
                return 0
            value = grid[r][c]
            grid[r][c] = 0
            value += dfs(r - 1, c)
            value += dfs(r + 1, c)
            value += dfs(r, c - 1)
            value += dfs(r, c + 1)
            return value
        answer = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] > 0:
                    island_sum = dfs(r, c)
                    if island_sum % k == 0:
                        answer += 1
        return answer