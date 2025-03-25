class Solution:
    def isScramble(self, s1: str, s2: str) -> bool:
        n = len(s1)
        m = len(s2)
        if n != m:
            return False
        if n == m == 0:
            return True
        memo ={}
        def scramble(a,b):
            if a == b:
                return True
                # great and "" is wrong
            if len(a) <= 1:
                return False

            if (a,b) in memo:
                return memo[(a,b)]
            # for partinion count space after word for greta can be partiona at 4 places      
            # Prune: if sorted chars don't match, can't be scramble
            if sorted(a) != sorted(b):
                memo[(a, b)] = False
                return False
            n = len(a)
            flag = False
            for i in range(1,n):
                # No swap
                cond1 = scramble(a[:i], b[:i]) and scramble(a[i:], b[i:])
                # Swap
                cond2 = scramble(a[:i], b[-i:]) and scramble(a[i:], b[:-i])
                if cond1 or cond2:
                    memo[(a,b)] =True
                    return True
            memo[(a,b)] =False
            return False
                
        return scramble(s1,s2)
#         Time: O(n⁴)
# Space: O(n³)

        # great
    # g        reat        reat g
    #                     r.  eat.   g            eat.  r    g
    #         r.    