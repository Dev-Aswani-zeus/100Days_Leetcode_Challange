class Solution:
    def minWindow(self, s: str, t: str) -> str:
        need = {}
        for ch in t:
            need[ch] = need.get(ch, 0) + 1
        window = {}
        left = 0
        formed = 0
        required = len(need)
        answer = ""
        min_length = len(s) + 1
        for right in range(len(s)):
            ch = s[right]
            window[ch] = window.get(ch, 0) + 1
            if ch in need and window[ch] == need[ch]:
                formed += 1
            while formed == required:

                current_length = right - left + 1
                if current_length < min_length:
                    min_length = current_length
                    answer = s[left:right + 1]
                left_char = s[left]
                window[left_char] -= 1
                if left_char in need and window[left_char] < need[left_char]:
                    formed -= 1
                left += 1
        return answer