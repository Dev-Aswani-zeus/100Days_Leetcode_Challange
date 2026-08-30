class Solution:
    def minimumDeletions(self, nums: List[int]) -> int:
        n = len(nums)
        min_pos = nums.index(min(nums))
        max_pos = nums.index(max(nums))
        left = min(min_pos, max_pos)
        right = max(min_pos, max_pos)
        option1 = right + 1
        option2 = n - left
        option3 = (left + 1) + (n - right)
        return min(option1, option2, option3)