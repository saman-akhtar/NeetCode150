class Solution:
    def maxArea(self, height: List[int]) -> int:
        l,r =0, len(height)-1
        maxv = 0
        while l < r:
            dist  = abs(r- l)
            maxv = max(maxv, dist * min(height[l], height[r]))
            if height[l]< height[r]:
                l +=1
            else:
                r -= 1
        return maxv


        