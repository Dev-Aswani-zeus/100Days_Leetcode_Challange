class Solution:
    def minMoves2(self, nums: list[int]) -> int:
        nums.sort()
        median = nums[len(nums) // 2]
        answer = 0
        for num in nums:
            answer += abs(num - median)
        return answer