class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        max = 0
        
        for i in range(len(accounts)):
            
            total = 0
            
            for j in range(len(accounts[i])):
                total = total + accounts[i][j]
            
            if total > max:
                max = total
        
        return max
        