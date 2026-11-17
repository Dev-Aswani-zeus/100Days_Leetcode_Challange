
class Solution:
    def minimumChanges(self, s: str, k: int) -> int:
        n = len(s)
        INF = float('inf')
        cost = [[INF] * n for _ in range(n)]
        for left in range(n):
            for right in range(left + 1, n):
                length = right - left + 1
                for d in range(1, length):
                    if length % d != 0:
                        continue
                    group_size = length // d
                    changes = 0
                    for offset in range(d):
                        for t in range(group_size // 2):
                            first = left + offset + t * d
                            second = left + offset + (group_size - 1 - t) * d
                            if s[first] != s[second]:
                                changes += 1
                    cost[left][right] = min(cost[left][right], changes)
        dp = [[INF] * (n + 1) for _ in range(k + 1)]
        dp[0][0] = 0
        for parts in range(1, k + 1):
            for end in range(2 * parts, n + 1):
                for start in range(2 * (parts - 1), end - 1):
                    current = dp[parts - 1][start] + cost[start][end - 1]
                    dp[parts][end] = min(dp[parts][end], current)
        return dp[k][n]
