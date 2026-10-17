class Solution:
    def minSwaps(self, nums: list[int]) -> int:

        def digit_sum(num):
            total = 0

            while num > 0:
                total += num % 10
                num //= 10

            return total

        # Make the array in the order we actually want
        sorted_nums = sorted(nums, key=lambda x: (digit_sum(x), x))

        # Remember where each number currently is
        position = {}

        for i in range(len(nums)):
            position[nums[i]] = i

        swaps = 0

        for i in range(len(nums)):

            # Already in correct position
            if nums[i] == sorted_nums[i]:
                continue

            j = position[sorted_nums[i]]

            nums[i], nums[j] = nums[j], nums[i]

            position[nums[i]] = i
            position[nums[j]] = j

            swaps += 1

        return swaps