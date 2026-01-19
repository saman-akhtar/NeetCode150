class Solution:
    def isPalindrome(self, s: str) -> bool:
#         s = ''.join([ ch.lower() for ch in s if ch.isalnum()])
#         length = len(s)
#         if length < 2:
#             return True
#         l = 0
#         r = length -1
      


#         while l < r:
            
#             if s[l] != s[r]:
#                 return False
#             l +=1
#             r -= 1
            
#         return True
# # A man, a plan, a canal: Panama#
        

#         # TC O(N) + O(N)
#         # SC O(N) list comprehension

        # OPTIMZED
        length = len(s)
        l = 0
        r = length -1
        while l < r:
            while l < r and not s[l].isalnum():
                l +=1
            while l < r and not s[r].isalnum():
                r -=1
            if s[l].lower() != s[r].lower():
                return False
            l +=1
            r -=1
        return True
# TC O(N)
# SC O(1)