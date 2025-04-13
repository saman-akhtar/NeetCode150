class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        x = str(x)
        l ,r = 0 , len(x)-1
        while l <= r:
            if x[l] == x[r]:
                l += 1
                r -= 1
            else:
                return False
        return True

        #TC O(N)
        # SC O(1)
        