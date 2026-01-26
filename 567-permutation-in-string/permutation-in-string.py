class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        l1 = len(s1)
        l2 = len(s2)
        if l1 > l2:
            return False
        count1 = [0] * 26
        count2 = [0] * 26
      
        for i in range(len(s1)):
            count1[ord(s1[i]) - ord('a')] +=  1
            count2[ord(s2[i]) - ord('a')] += 1
        l = 0
        matches = 0
        for i in range(26):
            if count1[i] ==count2[i]:
                matches+= 1
        
        for r in range(len(s1),len(s2)):
            if matches == 26:
                return True
            
            idx = ord(s2[r]) - ord('a')
            count2[idx] += 1
            if  count2[idx] == count1[idx]:
                matches +=1
            elif count1[idx] + 1 == count2[idx]:
                matches -= 1
            
            idx = ord(s2[l]) - ord('a')
            count2[idx] -= 1
            if count2[idx] == count1[idx]:
                matches +=1
            # if mac=thes were equal but no become unequal
            # eg c for 4 in both, if l = c , then in count2 is 3 , count1 = 4
            elif count1[idx] - 1 == count2[idx]:
                matches -= 1
            l += 1
            
        return matches == 26
       
                
# a  a  a  b  e   b   b   c.  a

# 0 -1 -2 -2  -1  0   1

