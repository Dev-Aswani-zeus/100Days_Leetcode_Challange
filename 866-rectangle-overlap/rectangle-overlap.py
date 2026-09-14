class Solution:
    def isRectangleOverlap(self, rec1: List[int], rec2: List[int]) -> bool:
        x1, y1, x2, y2 = rec1
        a1, b1, a2, b2 = rec2
        if x1 >= a2 or a1 >= x2:
            return False
        if y1 >= b2 or b1 >= y2:
            return False
        return True