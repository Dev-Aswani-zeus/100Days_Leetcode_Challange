class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left = 0
        total = 0
        answer = len(nums) + 1
        for right in range(len(nums)):
            total += nums[right]
            while total >= target:
                length = right - left + 1
                if length < answer:
                    answer = length
                total -= nums[left]
                left += 1
        if answer == len(nums) + 1:
            return 0

        return answer
            

        