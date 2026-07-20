class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        rows = len(grid)
        cols = len(grid[0])

        for _ in range(k):
            last = grid[rows-1][cols-1]
            for i in range(rows-1, -1, -1):
                for j in range(cols-1, -1, -1):
                    if i == 0 and j == 0:
                        grid[0][0] = last
                    elif j == 0:
                        grid[i][0] = grid[i-1][cols-1]
                    else:
                        grid[i][j] = grid[i][j-1]
        return grid