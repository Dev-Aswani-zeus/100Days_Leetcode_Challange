class Solution:
    def climbStairs(self, n: int, costs: list[int]) -> int:

        dp = [0] * (n + 1)

        for i in range(1, n + 1):

            one = float('inf')
            two = float('inf')
            three = float('inf')

            # Jump from previous step
            if i >= 1:
                one = dp[i - 1] + costs[i - 1] + 1

            # Jump from two steps before
            if i >= 2:
                two = dp[i - 2] + costs[i - 1] + 4

            # Jump from three steps before
            if i >= 3:
                three = dp[i - 3] + costs[i - 1] + 9

            dp[i] = min(one, two, three)

        return dp[n]