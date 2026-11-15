
class Solution:
    def numOfSubarrays(self, arr: list[int]) -> int:

        MOD = 10**9 + 7

        even = 1
        odd = 0

        total = 0
        answer = 0

        for num in arr:

            total += num

            if total % 2 == 0:
                answer += odd
                even += 1
            else:
                answer += even
                odd += 1

        return answer % MOD
