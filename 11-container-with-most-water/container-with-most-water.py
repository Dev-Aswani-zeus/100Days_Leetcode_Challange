class Solution:
    def maxArea(self, height: List[int]) -> int:
        water_store = 0
        l = 0
        r = len(height)-1
        

        while l<r:
            width = r-l
            h = min(height[l], height[r])
            area = width * h
            if area > water_store:
                water_store = area
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
        return water_store