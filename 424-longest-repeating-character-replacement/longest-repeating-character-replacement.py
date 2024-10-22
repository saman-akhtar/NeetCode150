class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        #approch 1
        count = {}
        l = 0
        res = 0
        maxf = 0
        #O(N)
        for r in range(len(s)):
            count[s[r]] = 1 + count.get(s[r], 0)
            maxf = max(maxf,  count[s[r]])
            
            # while not valid 
       
            while (r -l +1 - maxf) > k:
                count[s[l]] -= 1
                l += 1
            res = max(r-l +1,res)
        return res

        #TC
        #SC 

        # Approch 2
        # count = {}
        # l = 0
        # res = 0
        # #O(N)
        # for r in range(len(s)):
        #     count[s[r]] = 1 + count.get(s[r], 0)
            
        #     # while not valid 
        #     # max fo count = 26
        #     while (r -l +1 - max(count.values())) > k:
        #         count[s[l]] -= 1
        #         l += 1
        #     res = max(r-l +1,res)
        # return res

        #TC O(26. N)
        #SC O(26)
        