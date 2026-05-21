class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        sum = 0
        max_sum = nums[0]

        for num in nums:
            sum += num 
            if sum > max_sum:
                max_sum = sum
            if sum < 0:
                sum = 0
        return max_sum

        
        