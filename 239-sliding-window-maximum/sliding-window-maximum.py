class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        q = deque() # store indices
        output = []
        l =r = 0
        while r < len(nums):
            # before adding, chck if q is in motonice decre
            while q and nums[q[-1]] < nums[r]:
                q.pop()

             

            # add indices
            q.append(r)

            # if out of bound ,remove
            if l > q[0]:
                q.popleft()
            
            # edge case
            if ( r +1) >= k:
                output.append(nums[q[0]])
                l += 1
            r += 1
        return output

        # tC O(n)
        # Sc O(n) beacuse of deque
        