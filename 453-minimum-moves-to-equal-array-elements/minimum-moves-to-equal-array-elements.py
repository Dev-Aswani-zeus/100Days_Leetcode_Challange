class Solution:
    def minMoves(self, nums: list[int]) -> int:
        minimum = min(nums)
        answer = 0
        for num in nums:
            answer += num - minimum
        return answer