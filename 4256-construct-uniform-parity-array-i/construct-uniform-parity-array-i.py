class Solution:
    def uniformArray(self, nums1: list[int]) -> bool:
        n = len(nums1)
        can_make_even = True
        can_make_odd = True
        for i in range(n):
            even_possible = False
            odd_possible = False
            if nums1[i] % 2 == 0:
                even_possible = True
            else:
                odd_possible = True
            for j in range(n):
                if i == j:
                    continue
                value = nums1[i] - nums1[j]
                if value % 2 == 0:
                    even_possible = True
                else:
                    odd_possible = True
            if not even_possible:
                can_make_even = False
            if not odd_possible:
                can_make_odd = False
        return can_make_even or can_make_odd