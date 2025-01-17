class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        windLen = 0
        l = 0
        r = 0
        wind = set()
        # wind.add(s[0])
        while r < len(s):
            while s[r]  in wind:
                    wind.remove(s[l])
                    l +=1
            # if s[r] not in wind:
            wind.add(s[r])
            r += 1
            windLen = max(windLen, r -l )
        return windLen

        