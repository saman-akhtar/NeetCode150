class Solution:
    def trap(self, height: List[int]) -> int:
        l = 0
        r = len(height)-1
        maxl= [0] * len(height)
        maxr = [0] * len(height)
        ll = height[l]
        for i in range(1,len(height)):
            ll = max(ll, height[i-1])
            maxl[i] = ll
        print("maxl",maxl)
        rr = height[r]
        for i in range(len(height)-2,-1,-1):
            rr = max(rr, height[i+1])
            maxr[i] = rr
        trap =0
        print("maxl",maxr)
        for i in range(len(height)):
            cur =  min(maxl[i],maxr[i]) - height[i]
            if cur > 0:
                trap += cur
        return trap
