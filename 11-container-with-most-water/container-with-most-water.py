class Solution:
    def maxArea(self, height: List[int]) -> int:
        l, r = 0, len(height)-1
        maxv = 0
        while l < r:
            d = abs(r-l)
            maxv = max(maxv, d * min(height[l],height[r]))
            if height[l] > height[r]:
                r -= 1
            else:
                l +=1
        return maxv

    
    

# TC O(N)
# SC O(1)


        