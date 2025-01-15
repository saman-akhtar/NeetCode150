class Solution:
    def longestPalindrome(self, s: str) -> int:
        letter = Counter(s)
        count = 0
        odd_found = False
        for v in letter.values():
           
                if v % 2 == 0:
                    count += v
                    
                else:
                    if v > 1:
                        count += v-1
                    odd_found = True 
        if odd_found:
            count += 1
        return count

# TC O(N)
# TC O(n)

        