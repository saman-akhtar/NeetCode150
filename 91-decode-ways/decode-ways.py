class Solution:
    def numDecodings(self, s: str) -> int:

        # Memoization

        res = []
        memo = {}
        count = 0
        def dfs(i):
            if  i == 0:
                return 1
            idx = n - i
            if s[idx] == '0':
                return 0
            if i in memo:
                return memo[i]
            # if s[-1] == '0':
            #     return 0
            # Option 1: Decode one digit
            count = dfs(i-1)
             # Option 2: Decode two digits (if possible)
           # Option 2: Decode two digits (if possible)
            
            if i >= 2 and 10 <= int(s[idx: idx+2]) <= 26:
                count += dfs(i - 2)
            memo[i] = count
            return memo[i]
        n = len(s)
        return dfs(n) 


        # recursion
        res = []
        count = 0
        def dfs(i):
            if  i == 0:
                return 1
            idx = n - i
            if s[idx] == '0':
                return 0
            # if s[-1] == '0':
            #     return 0
            # Option 1: Decode one digit
            count = dfs(i-1)
             # Option 2: Decode two digits (if possible)
           # Option 2: Decode two digits (if possible)
            
            if i >= 2 and 10 <= int(s[idx: idx+2]) <= 26:
                count += dfs(i - 2)
            return count
        n = len(s)
        return dfs(n) 
        # TC O(2 ^ n)
        # Sc (On)
