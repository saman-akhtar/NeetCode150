class Solution:
    def trap(self, height: List[int]) -> int:
        # APPROACH 2

        water = 0
        l = 0
        r = len(height) -1
        maxl, maxr = height[0], height[r]
        while l < r:
            if maxl < maxr:
                cur_w = maxl - height[l]
                if cur_w > 0:
                    water += cur_w
                l += 1
                maxl = max(maxl, height[l])
            else:
                # maxr 
                cur_w = maxr - height[r]
                if cur_w > 0:
                    water += cur_w
                r -= 1
                maxr = max(maxr, height[r])

        return water


        # APPROACH 1

        # use maxl
        # & maxr 
        # for cur i water trapped = min(maxl[i], maxr[i]) - height[i]


        
# 1.            0  2  1  0  1  3. 2
#         0  0  1  1  2  2  2  2  2
#         3  3  3  3  3  3  3  3  0
#         0. 0  1  0. 1  2  1  -1. 0
        # water = 0
        # maxl = []
        # maxr = [0] * len(height)
        # curl = 0
        # for i in range( len(height)):
        #     maxl.append(curl)
        #     curl = max(height[i], curl)
        # curr = 0
        # for i in range( len(height)-1,-1,-1):
        #     maxr[i] = curr
        #     curr = max(height[i], curr)
        # for i in range( len(height)):
        #     cur_w = min(maxl[i], maxr[i]) - height[i]
        #     if cur_w > 0:
        #         water += cur_w

        # return water

        # TC O(n)= (N)+ N +N
        # SC O(N) = N + N


        
        
