class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        #BrutForce
        # temp = 0
        # for i in range(0,len(nums)-1):
        #     for j in range(i+1,len(nums)):
        #         if nums[i] == nums[j]:
        #             return nums[i]

        seen = {}

        for i in range(0, len(nums)):
            if nums[i] in seen:
                return nums[i]
            seen[nums[i]] = 1


