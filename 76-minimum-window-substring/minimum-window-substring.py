class Solution:
    def minWindow(self, s: str, t: str) -> str:
        l1 = len(s)
        l2 = len(t)
        res =""
        if l2 > l1:
            return res
        minlen = l1 +1
        minl =0
        count2 = Counter(t)
        count1 = {}
        l = 0
        r =0
        need = len(count2)
        have = 0
        # for r in range(l1):
        for r in range(l1):
            count1[s[r]]= count1.get(s[r], 0) + 1
            if s[r] in count2 and count1[s[r]] == count2[s[r]]:
                have += 1

            # start sliding
            while have == need:
                # find min wind
                if minlen > r - l + 1:
                    minl = l
                    minlen =  r - l + 1


                #slide
                count1[s[l]] -= 1
                if s[l] in count2 and count1[s[l]]  == count2[s[l]] -1:
                    have -= 1
                l += 1
        
        if minlen != l1 + 1 :
            return s[minl: minl + minlen]
        return ""


        