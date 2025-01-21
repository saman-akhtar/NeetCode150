class Solution:
    def isHappy(self, n: int) -> bool:
        sums = 0

        def findHappy(n):
            sums = 0
            while n > 0 :
                rem = n % 10
                sums = sums + rem ** 2
                n = n // 10
            return sums
        
        seen = set()
        while n != 1 and n not in seen:
            seen.add(n)
            n  = findHappy(n)
        return n ==1
        
        