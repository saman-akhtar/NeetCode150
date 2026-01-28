class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:

        # optimized
        # sliding window
        # 4 3 2 1.   0 1 2
        l = 0
        r = 0
        q = collections.deque()
        maxArr = []
        while r < len(nums):
            # remove samll                                                                 
            while q and nums[q[-1]] < nums[r]:
                q.pop()
            q.append(r)

            # remove left value from
            if l > q[0]:
                q.popleft()

            # adding of new
            if (r+ 1) >= k:
                maxArr.append(nums[q[0]])
                l+= 1
            r += 1
        return maxArr
# TC O(N) * O(1)
# SC
 # method 2 
# 4 3 2 1


        maxArr = []
        maxitem = max(nums[:k])
        maxArr.append(maxitem)
        l = 0

        for i in range(k,len(nums)):
            if nums[i] >= maxitem:
                maxitem = nums[i]
            else:
                # remove from left
                if nums[l] == maxitem:
                    maxitem = max(nums[l+1: i+1])
                
            maxArr.append(maxitem)  
            l += 1
        return maxArr


        # O(n * (k + k)) = O(n * 2k) = o(nk)
# 1 2 3 4
# 3 4



# 4 4 4 4
# [-6,-10,-7,-1,-9,9,-8,-4,10,-5,2,9,0,-7,7,4,-2,-10,8,7]
