from math import gcd

class Solution:
    def subsequencePairCount(self, nums: List[int]) -> int:
        MOD = 10**9 + 7
        memo = {}
        def dfs(i, g1, g2):
            if i == len(nums):
                if g1 == 0 or g2 == 0:
                    return 0
                return 1 if g1 == g2 else 0
            if (i, g1, g2) in memo:
                return memo[(i, g1, g2)]

            ans = dfs(i + 1, g1, g2)

            new_g1 = nums[i] if g1 == 0 else gcd(g1, nums[i])
            ans += dfs(i + 1, new_g1, g2)

            new_g2 = nums[i] if g2 == 0 else gcd(g2, nums[i])
            ans += dfs(i + 1, g1, new_g2)

            memo[(i, g1, g2)] = ans % MOD
            return memo[(i, g1, g2)]

        return dfs(0, 0, 0)