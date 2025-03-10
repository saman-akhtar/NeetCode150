class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "":
            return ""
        # res = "" optimized to store indice ,as it creates new string everytime
        res  = [-1,-1]
        l = 0
        have = 0
        smap = {}
        tmap = Counter(t)
        need = len(tmap)
        minLen = float('inf')
        for r,ch in enumerate(s):
            if ch in tmap:
                smap[ch] = smap.get(ch,0) + 1
                if smap[ch] == tmap[ch]:
                    have += 1
            while have == need:
                windLen = r - l + 1
                if windLen < minLen:
                    res = [l, r]
                    minLen = windLen
                left_ch = s[l]
                if left_ch in tmap:
                    if smap[left_ch] == tmap[left_ch]:
                        have -= 1
                    smap[left_ch] -= 1
                l += 1
        l,r = res
        return s[l:r+1]
        # TC O(N)
        #  ✅ O(N) means you touch each item a limited number of times.
        # ❌ O(N²) means you keep checking the same items again and again.
        # SC O(M), m is len of t
        # smap: Stores characters found in s that match t, using O(M) space in the worst case.



















        # if t == "":
        #     return ""
        # have, need ,l = 0,0, 0
        # map1 = {}
        # map2 = {}
        # res = [-1,-1]
        # rlen = float("infinity")
        # # O(M)
        # for i in t :
        #     map1[i]= 1 + map1.get(i,0)
        # need = len(map1)
        # # O(N)
        # for r in range(len(s)):
        #     c = s[r]
        #     map2[c] = 1 + map2.get(c,0)
        #     if c in map1 and map1[c]== map2[c]:
        #         have += 1
        #    # amortized O(∣n∣) 
        #     while( have == need):
        #         if ( r-l + 1 ) < rlen:
        #             rlen =  r - l + 1
        #             res= [l, r]
        #         #pop from left
                
        #         map2[s[l]] -= 1
        #         if s[l] in map1 and map1[s[l]] > map2[s[l]]:
        #             have -= 1
        #         l += 1
        # l,r = res
        # return s[l:r+1]
            
#TC O(N + m)= O(N)
# SC = o(N + m) = O(N)
 
        