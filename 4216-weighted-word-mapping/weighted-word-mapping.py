class Solution:
    def mapWordWeights(self, words: list[str], weights: list[int]) -> str:
        ans = ""

        for word in words:
            total = 0

            for ch in word:
                index = ord(ch) - ord('a')
                total += weights[index]

            value = total % 26

            letter = chr(ord('z') - value)

            ans += letter

        return ans