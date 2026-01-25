class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l =0
        n = len(s)
        if n < 1:
            return 0
        seq = set(s[l])
        maxl = 1
        for r in range(1,n):
            if s[r] in seq:
                maxl= max(maxl, len(seq))
                while s[r] in seq:
                    seq.remove(s[l])
                    l +=1
                
                    

            seq.add(s[r])
        maxl= max(maxl, len(seq))
        return maxl