class Solution:
    def minOperations(self, s: str) -> int:
        if all(s[i] <= s[i + 1] for i in range(len(s) - 1)):
            return 0
        if len(s) == 2:
            return -1
        minimum = min(s)
        maximum = max(s)
        if s[0] == minimum or s[-1] == maximum:
            return 1
        for i in range(1, len(s) - 1):
            if s[i] == minimum or s[i] == maximum:
                return 2
        return 3