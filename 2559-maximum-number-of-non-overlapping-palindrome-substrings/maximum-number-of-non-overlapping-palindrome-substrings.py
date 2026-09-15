class Solution:
    def maxPalindromes(self, s: str, k: int) -> int:
        n = len(s)

        # dp[i][j] tells us whether s[i:j+1] is a palindrome
        dp = [[False] * n for _ in range(n)]

        # Every single character is a palindrome
        for i in range(n):
            dp[i][i] = True

        # Check substrings by their length
        for length in range(2, n + 1):
            for i in range(n - length + 1):
                j = i + length - 1

                if s[i] == s[j]:
                    if length == 2:
                        dp[i][j] = True
                    else:
                        dp[i][j] = dp[i + 1][j - 1]

        # Greedily choose palindromes
        ans = 0
        last_end = -1

        for end in range(n):
            for start in range(last_end + 1, end + 1):

                # Length must be at least k
                if end - start + 1 >= k and dp[start][end]:

                    ans += 1
                    last_end = end
                    break

        return ans