class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l =0
        n = len(s)
        maxl = 0
        seen = set()
        for r in range(n):
            while s[r] in seen:
                seen.remove(s[l])
                l +=1
            seen.add(s[r])
            maxl = max(maxl, r - l +1)
        return maxl