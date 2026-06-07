class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        # count = len(nums)
        # for in range(0,len(nums)):
        #     if nums[i] == val:
        #         count -= 1
        # return count

        k = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[k] = nums[i]
                k += 1
        return k

        