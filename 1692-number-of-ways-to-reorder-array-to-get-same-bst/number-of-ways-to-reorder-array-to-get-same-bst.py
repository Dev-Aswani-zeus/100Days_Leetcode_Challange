class Solution:
    def numOfWays(self, nums: list[int]) -> int:
        MOD = 10**9 + 7
        def combination(n, r):
            if r == 0 or r == n:
                return 1
            result = 1
            for i in range(1, r + 1):
                result = result * (n - r + i) // i
            return result
        def solve(arr):
            if len(arr) <= 2:
                return 1
            root = arr[0]
            left = []
            right = []
            for num in arr[1:]:
                if num < root:
                    left.append(num)
                else:
                    right.append(num)
            left_ways = solve(left)
            right_ways = solve(right)
            ways_to_mix = combination(
                len(left) + len(right),
                len(left)
            )
            return (ways_to_mix * left_ways * right_ways) % MOD
        return (solve(nums) - 1) % MOD