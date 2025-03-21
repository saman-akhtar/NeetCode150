class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]

        # top down
        def helper(newarr):
            prev1, prev2 = 0,0
            for arr in newarr:
                newRob = max(prev1 + arr, prev2)
                prev2,prev1 = newRob, prev2
            return prev2
        
        return max( helper(nums[1:]),helper(nums[:-1]))
    # tC O(n)
    # Sc O(1)



        #memoiztaion
        n = len(nums)
        memo = {}
        if n == 1:
            return nums[0]
        def dfs(i,flag):
            # If there are no houses left, return 0.
            # Also, if flag is True (last house robbed) and we've reached the first house (i == 1),
            # we cannot rob the first house.
            if (i == 1 and flag == True) or i <=0:
                return 0
            if (i,flag) in memo:
                return memo[(i,flag) ]
            # Option 1: Skip the current house i.
            # Option 2: Rob the current house i and then skip the next one (i-1), so move to i-2.
            # If we are at the last house (i == n-1) and we rob it, set flag to True.
            memo[(i,flag) ] = max(
                nums[i-1] + dfs(i-2, flag),
                 dfs(i-1,flag)
                 )
            return memo[(i,flag) ]
            
        
        return max(dfs(n, True), dfs(n-1, False))

        # TC O N ^ 2
        # SC  O(n) + o(n ^2)

        # RECURSION
        n = len(nums)
        if n == 1:
            return nums[0]
        def dfs(i,flag):
            # If there are no houses left, return 0.
            # Also, if flag is True (last house robbed) and we've reached the first house (i == 1),
            # we cannot rob the first house.
            if (i == 1 and flag == True) or i <=0:
                return 0
            # Option 1: Skip the current house i.
            # Option 2: Rob the current house i and then skip the next one (i-1), so move to i-2.
            # If we are at the last house (i == n-1) and we rob it, set flag to True.
           
            return max(
                nums[i-1] + dfs(i-2, flag),
                 dfs(i-1,flag)
                 )
            
        
        return max(dfs(n, True), dfs(n-1, False))

        # TC O(2 ^ n)
        # SC O(N)




        
    #      0 1 2 3 4
    #    0 1 2 3 1

    #    n   amt

    #    4.  3  1
    #    2.  1  2

    #    3   2. 3 
    #    1

        