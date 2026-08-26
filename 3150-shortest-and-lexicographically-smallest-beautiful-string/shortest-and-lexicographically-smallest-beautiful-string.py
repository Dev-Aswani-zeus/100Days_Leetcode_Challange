class Solution:
    def shortestBeautifulSubstring(self, s: str, k: int) -> str:

        left = 0
        ones = 0
        answer = ""

        for right in range(len(s)):

            # Add current character
            if s[right] == '1':
                ones += 1

            # We have exactly k ones
            while ones == k:

                # Current substring
                current = s[left:right + 1]

                # Check if this is better
                if answer == "" or len(current) < len(answer):
                    answer = current
                elif len(current) == len(answer) and current < answer:
                    answer = current

                # Move left forward
                if s[left] == '1':
                    ones -= 1

                left += 1

        return answer