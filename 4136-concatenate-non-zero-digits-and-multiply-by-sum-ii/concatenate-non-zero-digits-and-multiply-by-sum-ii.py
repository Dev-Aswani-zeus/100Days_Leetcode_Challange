class Solution:
    def sumAndMultiply(self, s: str, queries: List[List[int]]) -> List[int]:
        MOD = 10**9 + 7
        n = len(s)

        # prefix sum of non-zero digits
        prefix_sum = [0] * (n + 1)

        # prefix number (ignoring zeros)
        prefix_num = [0] * (n + 1)

        # power of 10
        power = [1] * (n + 1)

        count = [0] * (n + 1)

        for i in range(n):
            prefix_sum[i + 1] = prefix_sum[i]
            prefix_num[i + 1] = prefix_num[i]
            count[i + 1] = count[i]

            if s[i] != "0":
                digit = int(s[i])
                prefix_sum[i + 1] += digit
                count[i + 1] += 1
                prefix_num[i + 1] = (prefix_num[i] * 10 + digit) % MOD

            power[i + 1] = (power[i] * 10) % MOD

        ans = []

        for l, r in queries:

            digit_sum = prefix_sum[r + 1] - prefix_sum[l]

            digits = count[r + 1] - count[l]

            if digits == 0:
                ans.append(0)
                continue

            number = (
                prefix_num[r + 1]
                - prefix_num[l] * power[digits]
            ) % MOD

            ans.append((number * digit_sum) % MOD)

        return ans