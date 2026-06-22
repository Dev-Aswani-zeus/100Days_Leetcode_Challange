class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_length = 0
        for i in range(len(s)):
            current = ""
            for j in range(i, len(s)):
                if s[j] in current:
                    break
                current += s[j]
                if len(current) > max_length:
                    max_length = len(current)
        return max_length

        # d = {}
        # l = 0
        # count = 0
        # for r in range(0, len(s)):
        #     if s[r] in d:
        #         l = max(l, d[s[r]] +1)
        #     d[s[r]] = r
            
        #     length = r - l + 1
            
        #     if length > count:
        #         count = length

        # return count 
        
