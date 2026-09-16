class Solution:
    def numberOfSets(self, n: int, k: int) -> int:
        MOD = 10**9 + 7
        ans = 1
        a = n + k - 1
        b = 2 * k
        for i in range(1, b + 1):
            ans = ans * (a - i + 1) // i
        return ans % MOD