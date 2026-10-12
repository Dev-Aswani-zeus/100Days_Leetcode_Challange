class Solution:
    def maxSum(self, nums: list[int], k: int) -> int:
        answer = [0] * k
        for bit in range(31):
            count = 0
            for num in nums:
                if num & (1 << bit):
                    count += 1
            for i in range(min(count, k)):
                answer[i] |= (1 << bit)
        result = 0
        for num in answer:
            result += num * num
        return result % (10**9 + 7)