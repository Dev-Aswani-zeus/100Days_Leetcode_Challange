class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        str1 = s.lower()
        str2 = t.lower()

        if sorted(str1) == sorted(str2):
            return True
        else:
            return False
        