class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        arr = []
        for i in range(0, len(nums)):
            arr.append(nums[i] * nums[i])

        arr.sort()
        return arr

            

        