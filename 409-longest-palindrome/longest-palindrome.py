class Solution:
    def longestPalindrome(self, s: str) -> int:
        letter = {}
        for i in s:
            letter[i] = letter.get(i,0) + 1
        count = 0
        odd_found = False
        for v in letter.values():
           
                if v % 2 == 0:
                    count += v
                    
                else:
                    if v > 1:
                        count += v-1
                    odd_found = True 
                # del letter[k]
        if odd_found:
            count += 1
        return count



        