
class Solution:
    def maximumSubarraySum(self, nums: list[int], k: int) -> int:
        window = set()
        total = 0
        answer = 0
        left = 0
        for right in range(len(nums)):
            while nums[right] in window:
                window.remove(nums[left])
                total -= nums[left]
                left += 1
            window.add(nums[right])
            total += nums[right]
            if right - left + 1 > k:
                window.remove(nums[left])
                total -= nums[left]
                left += 1
            if right - left + 1 == k:
                answer = max(answer, total)
        return answer
