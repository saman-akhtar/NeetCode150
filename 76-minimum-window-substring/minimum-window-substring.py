class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "":
            return ""
        have, need ,l = 0,0, 0
        map1 = {}
        map2 = {}
        res = [-1,-1]
        rlen = float("infinity")
        # O(M)
        for i in t :
            map1[i]= 1 + map1.get(i,0)
        need = len(map1)
        # O(N)
        for r in range(len(s)):
            c = s[r]
            map2[c] = 1 + map2.get(c,0)
            if c in map1 and map1[c]== map2[c]:
                have += 1
           # amortized O(∣n∣) 
            while( have == need):
                if ( r-l + 1 ) < rlen:
                    rlen =  r - l + 1
                    res= [l, r]
                #pop from left
                
                map2[s[l]] -= 1
                if s[l] in map1 and map1[s[l]] > map2[s[l]]:
                    have -= 1
                l += 1
        l,r = res
        return s[l:r+1]
            
#TC O(N + m)= O(N)
# SC = o(N + m) = O(N)
 
        