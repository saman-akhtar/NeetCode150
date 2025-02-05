class Solution:
    def longestSubstring(self, s: str, k: int) -> int:

        # claryfing sorted ?
        # substri : contiguous ?
        # logic if any freq of ch < k , that wont be included in part of substring
        # so start new substring
        
        l = 0 
        chMap = Counter(s)
        maxLen = 0
        valid = True
        for r in range(len(s)):
            if chMap[s[r]] > 0 and chMap[s[r]] < k:
                substring = s[l:r]
                maxLen = max(maxLen, self.longestSubstring(substring, k))
                valid = False
                l = r + 1
        if (valid):
            return len(s)
        else:
            return max(maxLen,self.longestSubstring(s[l:], k))


        # while l <= r:
        #     # r += 1
        #     if (r < len(s) ):
        #         if (s[r] in wordMap):
        #             wordMap[s[r]] =  wordMap[s[r]] + 1
        #             if( wordMap[s[r]] % k == 0):
        #                 have += 1
        #         else:
        #             wordMap[s[r]] =1
        #             need += 1
        #             if (wordMap[s[r]] == k):
        #                 have += 1
        #         r += 1
        #     if have == need:
        #         length = r - l
        #         maxLen =max(have,length)

        #     r- l
        #     l che k
        # return maxLen

# cabbc
# abbcabbc
        