class Solution:
    def trap(self, height: List[int]) -> int:
        water = 0
# 1.            0  2  1  0  1  3. 2
#         0  0  1  1  2  2  2  2  2
#         3  3  3  3  3  3  3  3  0
#         0. 0  1  0. 1  2  1  -1. 0
        maxl = []
        maxr = [0] * len(height)
        curl = 0
        for i in range( len(height)):
            maxl.append(curl)
            curl = max(height[i], curl)
        curr = 0
        for i in range( len(height)-1,-1,-1):
            maxr[i] = curr
            curr = max(height[i], curr)
        for i in range( len(height)):
            cur_w = min(maxl[i], maxr[i]) - height[i]
            if cur_w > 0:
                water += cur_w

        return water


        
        
