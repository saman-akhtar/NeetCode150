class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        n,m = len(word1), len(word2)
        dp =[[0] * (m +1) for i in range(n +1)]
         # Base cases
        for i in range(n + 1):
            dp[i][0] = i  # delete all characters from word1
        for j in range(m + 1):
            dp[0][j] = j  # insert all characters to word1

        for i in range(1, n +1):
            for j in range(1, m + 1):
                if word1[i-1]== word2[j-1]:
                    dp[i][j]=  dp[i-1][j-1]
                else:
                    dp[i][j]=  1 + min(
        dp[i-1][j],    # delete
        dp[i][j-1],    # insert
        dp[i-1][j-1]   # replace
    )


        return dp[n][m]
        