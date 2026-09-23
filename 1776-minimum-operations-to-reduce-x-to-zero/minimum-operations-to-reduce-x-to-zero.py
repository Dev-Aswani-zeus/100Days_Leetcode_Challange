class Solution:
    def minOperations(self, nums: list[int], x: int) -> int:

        total = sum(nums)
        target = total - x

        if target < 0:
            return -1

        left = 0
        window_sum = 0
        max_length = -1

        for right in range(len(nums)):

            window_sum += nums[right]

            while window_sum > target:
                window_sum -= nums[left]
                left += 1

            if window_sum == target:
                length = right - left + 1
                max_length = max(max_length, length)

        if max_length == -1:
            return -1

        return len(nums) - max_length