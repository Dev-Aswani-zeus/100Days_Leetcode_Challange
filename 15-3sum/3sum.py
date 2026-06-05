class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        # result = []
        # for i in range(len(nums)):
        #     for j in range(i + 1, len(nums)):
        #         for k in range(j + 1, len(nums)):
        #             if nums[i] + nums[j] + nums[k] == 0:
        #                 triplet = sorted([nums[i], nums[j], nums[k]])
        #                 if triplet not in result:
        #                     result.append(triplet)
        # return result

        # comenting my logic and pasting gpt logic because timeout occured

        nums.sort()

        result = []

        for i in range(len(nums)):

            if i > 0 and nums[i] == nums[i - 1]:
                continue

            left = i + 1
            right = len(nums) - 1

            while left < right:

                total = nums[i] + nums[left] + nums[right]

                if total == 0:

                    result.append(
                        [nums[i], nums[left], nums[right]]
                    )

                    left += 1
                    right -= 1

                    while left < right and nums[left] == nums[left - 1]:
                        left += 1

                elif total < 0:
                    left += 1

                else:
                    right -= 1

        return result