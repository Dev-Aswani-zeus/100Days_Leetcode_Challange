class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        n = len(grid)
        freq = {}
        for row in grid:
            for num in row:
                if num in freq:
                    freq[num] += 1
                else:
                    freq[num] = 1
        repeated = 0
        missing = 0

        for num in range(1, n*n + 1):
            if num not in freq:
                missing = num
            elif freq[num] == 2:
                repeated = num
        return [repeated, missing]