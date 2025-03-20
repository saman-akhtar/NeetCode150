class Solution:
    def countSubstrings(self, s: str) -> int:
        # n  =len(s)
        # s2 = s[::-1]
        # # dp[i][j] does NOT store the count of palindromic substrings.

        # #dp[n][n] will only store the length of the longest matching substring (
        # dp = [[0] * (n+1) for _ in range(n+1)]
        # count = 0
        # for i in range(1, n+1):
        #     for j in range(1, n+1):
        #         if s[i-1] == s2[j-1]:
        #             dp[i][j] = dp[i-1][j-1] +1
        #             L = dp[i][j]
        #             # if alignment 
        #             if ( i - L) ==(n- j):
        #                 count += 1 #imp to sum all len
        # # print(d)
        # return count
        # DOESNT WORK up


# this works with DP but not on top of LCS logic
        # n = len(s)
        # dp = [[False] * n for _ in range(n)]
        # count = 0
        
        # # Every single character is a palindrome.
        # for i in range(n):
        #     dp[i][i] = True
        #     count += 1
            
        # # Check substrings of length 2 and above.
        # for L in range(2, n + 1):
        #     for i in range(n - L + 1):
        #         j = i + L - 1
        #         if s[i] == s[j]:
        #             if L == 2 or dp[i + 1][j - 1]:
        #                 dp[i][j] = True
        #                 count += 1
        # return count
        #TC O(n^2)
        #SC O(n^2)
        
        #In summary:

# Maximum Palindrome Substring:
# You’re after a single value (the longest length) and its position. The LCS approach works well because a valid palindrome appears as a contiguous block that satisfies the alignment condition, and you just take the maximum.

# Counting Palindromic Substrings:
# You must enumerate every valid occurrence—even overlapping ones. The LCS method gives you blocks, but it doesn’t naturally separate overlapping counts. This makes it non-intuitive and error-prone to adapt the LCS DP for counting.

# That’s why the LCS-based method is more naturally suited for finding the longest palindromic substring, while counting all palindromic substrings is best done using a DP method or center expansion approach that directly deals with overlaps and enumerates every palindromic substring.

# better to use TWO pointer here
        
        n = len(s)
        count = 0
        def is_palin(i,j):
            res = 0
            while i >=0 and j < len(s) and  s[i] == s[j]:
                    i -=1
                    j +=1
                    res += 1
            return res


        for i in range(n):
            count += is_palin(i,i)
            count += is_palin( i,i+1)
        return count
        # tc O(n ^2 )
        # Sc O(1)
