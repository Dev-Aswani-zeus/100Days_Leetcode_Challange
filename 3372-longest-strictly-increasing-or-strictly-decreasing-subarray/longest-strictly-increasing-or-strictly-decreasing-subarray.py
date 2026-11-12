class Solution:
    def longestMonotonicSubarray(self, nums: list[int]) -> int:
        increasing = 1
        decreasing = 1
        answer = 1
        for i in range(1, len(nums)):
            if nums[i] > nums[i - 1]:
                increasing += 1
                decreasing = 1
            elif nums[i] < nums[i - 1]:
                decreasing += 1
                increasing = 1
            else:
                increasing = 1
                decreasing = 1
            answer = max(answer, increasing, decreasing)
        return answer