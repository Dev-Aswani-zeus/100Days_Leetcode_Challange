class Solution:
    def maxAlternatingSum(self, nums: list[int]) -> int:
        nums.sort(key=abs, reverse=True)
        positive_count = (len(nums) + 1) // 2
        answer = 0
        for i in range(len(nums)):
            value = nums[i] * nums[i]
            if i < positive_count:
                answer += value
            else:
                answer -= value
        return answer