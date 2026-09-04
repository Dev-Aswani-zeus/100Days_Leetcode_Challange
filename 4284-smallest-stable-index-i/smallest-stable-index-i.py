class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        n = len(nums)
        for i in range(n):
            left_max = max(nums[0:i+1])
            right_min = min(nums[i:n])
            if left_max - right_min <= k:
                return i

        return -1