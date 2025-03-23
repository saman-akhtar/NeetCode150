class Solution:
    def numDistinct(self, s: str, t: str) -> int:

        # q?? HOW MANY path ?
        # not 
        # abc
        # abbc  

        n = len(s)
        m = len(t)
        dp = [[0]* (m +1) for _ in range(n +1)]
        # how may way u can create empt strimg ""
        #  from i 0 - n ??there is 1 way
        for i in range(n+1):
            dp[i][0] = 1

        for i in range(1, n +1):
            for j in range(1, m + 1):
                if s[i-1] == t[j-1]:

                    dp[i][j]= dp[i-1][j-1]+ dp[i-1][j] #dp[i - 1][j]	❌ Skip: We ignore s[i-1] and try to match t[j-1] from earlier s

                else:
                    dp[i][j]=  dp[i-1][j]
        return dp[n][m]

