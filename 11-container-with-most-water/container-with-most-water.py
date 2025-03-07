class Solution:
    def maxArea(self, height: List[int]) -> int:
        l,r = 0 ,len(height)-1
        maxA = 0

        while l < r:
            dist = r - l
            maxA = max(maxA, dist *  min(height[l],height[r]))
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
            
        return maxA

# 1,8,6,2,5,4,8,3,7
# 0 1 1 1 1 1 1 1 1
    
    

# TC O(N)
# SC O(1)


        