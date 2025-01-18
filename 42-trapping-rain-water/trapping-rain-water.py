class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        maxl = height[0]
        maxr = height[n-1]
        l,r = 0, n-1
        vol = 0
        while l < r:
            if maxl < maxr:
                cur_water = maxl-height[l]
                if (cur_water > 0):
                    vol += cur_water
                l +=1
                maxl = max(height[l],maxl)
                
            else:
                cur_water = maxr-height[r]
                if (cur_water > 0):
                    vol += cur_water
                r -=1
                maxr = max(height[r],maxr)
                
        return vol

       
    # TC O(N)
    # SC (O(1))
            
        
