
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
                
# # tle : as restarting check from r , when resetting map2 & have
# instead use sliding window, l=from left remove , right add


# Time Complexity: 
# O(∣s1∣+∣s2∣)

# Space Complexity: 
# \U0001d442(1)
# O(1), because we are only using fixed-size maps map1 and map2 that store the frequencies of the 26 possible lowercase characters.
       
