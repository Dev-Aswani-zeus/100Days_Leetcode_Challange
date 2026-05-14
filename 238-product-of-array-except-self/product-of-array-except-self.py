class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # this was my Approach but timeout error occured so now coping a random code
        # so could comment this code and submit it
        # array = []
        
        # for i in range(len(nums)):
            
        #     product = 1
            
        #     for j in range(len(nums)):
                
        #         if i != j:
        #             product = product * nums[j]
            
        #     array.append(product)
        
        # return array

        n = len(nums)
        
        ans = [1] * n
        
        
        prefix = 1
        
        for i in range(n):
            
            ans[i] = prefix
            
            prefix = prefix * nums[i]
        
        
        suffix = 1
        
        for i in range(n-1, -1, -1):
            
            ans[i] = ans[i] * suffix
            
            suffix = suffix * nums[i]
        
        return ans
        