class Solution:
    def sortPermutation(self, nums: list[int]) -> int:
        answer = -1
        for i in range(len(nums)):
            if nums[i] != i:
                answer = answer & nums[i]
        return max(answer, 0)