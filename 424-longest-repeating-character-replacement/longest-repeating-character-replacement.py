class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        # approach 2
        l = 0
        map = {}
        res =0
        maxf = 0
        for r, ch in enumerate(s):
            map[ch]= map.get(ch, 0) + 1
            maxf= max(maxf,map[ch] )
            while( r- l + 1 - maxf > k):
                map[s[l]] -= 1
                l +=1
            res = max(res, r-l +1)
        return res
        #APPparoch 1
        # l = 0
        # map = {}
        # res =0
        # for r, ch in enumerate(s):
        #     map[ch]= map.get(ch, 0) + 1
        #     while( r- l + 1 - max(map.values()) > k):
        #         map[s[l]] -= 1
        #         l +=1
        #     res = max(res, r-l +1)
        # return res
            

        # #approch 1
        # count = {}
        # l = 0
        # res = 0
        # maxf = 0
        # #O(N)
        # for r in range(len(s)):
        #     count[s[r]] = 1 + count.get(s[r], 0)
        #     #Optimization
        #     maxf = max(maxf,  count[s[r]])
            
        #     # while not valid 
       
        #     while (r -l +1 - maxf) > k:
        #         count[s[l]] -= 1
        #         l += 1
        #     res = max(r-l +1,res)
        # return res

#        Time Complexity: O(N)
#        Space Complexity: O(1) (if character set is fixed, like English alphabet), otherwise O(C) where C is the number of distinct characters.

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
        