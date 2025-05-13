class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        l = 0
        r = 0
        res = 0
        cur = set()
        while r < len(s):
            while s[r]  in cur:
                cur.remove(s[l])
                l += 1
            cur.add(s[r])      #  z a 
            if len(cur) == 3:
                res += 1
                cur.remove(s[l])
                l += 1
            r += 1
        return res
    # TC O(N)
    # Sc O(1) ste conatin 3 ch
            

        