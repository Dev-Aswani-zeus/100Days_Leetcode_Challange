class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # initilize new array
        # Traverse all the elements len(nums) to 0 (basicaly start from end)
        # Numbers of k time elements from start will be appended to new array
        # And remaning elements will be appened from back to new array
        # Return new array
        
        n = len(nums)

        k = k % n
        new_array = []
        for i in range(n - k, n):
            new_array.append(nums[i])
        for i in range(0, n - k):
            new_array.append(nums[i])
        for i in range(n):
            nums[i] = new_array[i]