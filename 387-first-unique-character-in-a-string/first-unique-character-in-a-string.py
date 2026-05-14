class Solution:
    def firstUniqChar(self, s: str) -> int:
        # for i in range(0,len(s)):
        #     count = 0
        #     for j in range(0, len(s)):
        #         if s[i] == s[j]:
        #             count += 1
        #     if count ==1:
        #         return i
        # return -1

        d = {}
        
        for i in range(0, len(s)):
            
            if s[i] in d:
                d[s[i]] += 1
            else:
                d[s[i]] = 1
        
        
        for i in range(0, len(s)):
            
            if d[s[i]] == 1:
                return i
        
        
        return -1
