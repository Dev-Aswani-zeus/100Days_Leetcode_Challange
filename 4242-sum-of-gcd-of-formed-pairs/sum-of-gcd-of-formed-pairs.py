from math import gcd

class Solution:
    def gcdSum(self, nums: list[int]) -> int:
        prefixGcd = []

        current_max = 0
        for num in nums:
            current_max = max(current_max, num)
            prefixGcd.append(gcd(num, current_max))

        prefixGcd.sort()

        left = 0
        right = len(prefixGcd) - 1
        ans = 0

        while left < right:
            ans += gcd(prefixGcd[left], prefixGcd[right])
            left += 1
            right -= 1

        return ans