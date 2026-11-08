class Solution:
    def countServers(self, grid: list[list[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        row_count = [0] * rows
        col_count = [0] * cols
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    row_count[i] += 1
                    col_count[j] += 1
        answer = 0
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    if row_count[i] > 1 or col_count[j] > 1:
                        answer += 1

        return answer