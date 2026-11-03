class Solution:
    def minMoves(self, nums: list[int]) -> int:
        maximum = max(nums)
        answer = 0
        for num in nums:
            answer += maximum - num
        return answer