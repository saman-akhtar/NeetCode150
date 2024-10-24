# class Solution:
#     def checkInclusion(self, s1: str, s2: str) -> bool:
#         #approch 2
#         map1 = {}
#         map2 = {}
#         l,have = 0, 0
#         for i in s1:
#             map1[i] = 1 + map1.get(i , 0)
#         need = len(map1)
#         r =0
#         # for r in range(len(s2)):
#         while r < len(s2):
#             c = s2[r]
            
#             if c in map1 :
#                 l = r
#                 while l < len(s2) and  s2[l] in map1 :
#                     map2[s2[l]] = 1 + map2.get(s2[l],0)
#                     if map2[s2[l]]== map1[s2[l]]:
#                         have += 1
#                     elif map2[s2[l]] > map1[s2[l]]:
#                         # break
#                         map2 = {}
#                         map2[s2[l]] = 1 + map2.get(s2[l],0)
#                         have = 1
#                     if have == need:
#                         return True
#                     l += 1
#                 r = l
#                 map2 = {}
#                 have = 0
#             r += 1
#         return False
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        map1, map2 = {}, {}
        have, l = 0, 0
        
        # Fill map1 with the frequency of each character in s1
        for i in s1:
            map1[i] = 1 + map1.get(i, 0)
        need = len(map1)  # Number of distinct characters we need to match

        # Slide the window over s2
        for r in range(len(s2)):
            c = s2[r]
            
            # Add the current character to map2
            if c in map1:
                map2[c] = 1 + map2.get(c, 0)
                if map2[c] == map1[c]:
                    have += 1
            
            # If the window size exceeds the size of s1, shrink it from the left
            if r - l + 1 > len(s1):
                left_char = s2[l]
                if left_char in map1:
                    if map2[left_char] == map1[left_char]:
                        have -= 1
                    map2[left_char] -= 1
                l += 1
            
            # If we have matched all needed characters, return True
            if have == need:
                return True
        
        return False
                
# # tle : as restarting check from r
       
