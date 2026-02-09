class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
       

        # 1 2 3 4 5 
        # hr      h lenght
        # 5   5  same -max
        # 3   5  <.  - max
        #        >
        #     1

        # given third condition
        # i.e h > piles lenght

        #brute force -- 1 - max(op)
        # O(max(p) * p[len of pile])


        # Binary searc
        # TC O(log(max(p)) * p)
        import math
        maxb = max(piles)
        min_res = maxb
        l = 1
        r = maxb

        def time_consumed(mid):
            tc =0
            for n in piles:
                tc +=   math.ceil( n /mid)
            return tc


        while l <= r:
         
            mid = (l +r)//2
            tc = time_consumed(mid)
           
            if  tc <= h:
                res = mid
                min_res = min(mid, min_res) #

                r = mid - 1 # # try smaller
            else:
                # tc > h:
                l = mid + 1# need bigger speed

           
        
        return min_res

         # Time complexity: 
# O
# (
# n
# ∗
# log
# ⁡
# m
# )
# O(n∗logm)
# Space complexity: 
# O
# (
# 1
# )
# O(1)
   