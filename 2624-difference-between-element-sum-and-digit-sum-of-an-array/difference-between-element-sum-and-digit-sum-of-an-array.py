class Solution:
    def differenceOfSum(self, nums: List[int]) -> int:
        difference = 0
        total_element = 0
        total_digit = 0

        for i in range(0,len(nums)):
            total_element = nums[i] + total_element 

        for j in range(0,len(nums)):
            num = nums[j]
            while num > 0:
                digit = num % 10
                total_digit = total_digit + digit
                num = num // 10



        return abs(total_element - total_digit)

        