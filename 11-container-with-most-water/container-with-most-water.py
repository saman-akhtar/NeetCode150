class Solution:
    def maxArea(self, height: List[int]) -> int:
        r = len(height) -1
        l =0
        maxl = 0
        maxr = r
        vol = 0
        while l < r:
            area = (r - l) * min(height[l] ,height[r])  
            vol = max(area, vol)  
            if (height[l]> height[r]):
                r -= 1
            else:
                    l += 1

        
        return vol
