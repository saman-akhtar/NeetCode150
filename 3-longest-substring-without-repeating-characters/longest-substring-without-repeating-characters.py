class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        windL = 0
        wind = set()
        for r in range(len(s)):
            while s[r] in wind:
                wind.remove(s[l])
                l += 1
            wind.add(s[r])
            windL = max(windL, len(wind))
        return windL


    # APROACH 1
    # def lengthOfLongestSubstring(self, s: str) -> int:
    #     windLen = 0
    #     l = 0
    #     r = 0
    #     wind = set()
    #     while r < len(s):
    #         while s[r]  in wind:
    #                 wind.remove(s[l])
    #                 l +=1
    #         wind.add(s[r])
    #         r += 1
    #         windLen = max(windLen, r -l )
    #     return windLen
# TC outher O(N) for r & inner while lloop ch character is added and removed from the wind set only once  O(N) => O(N) + O(N) = 0(N)

#SC O(min(n,a)) a is no of ch .. where n is the length of the string and a is the size of the character set (e.g., 26 for low
    
    # APproach 2
    # def lengthOfLongestSubstring(self, s: str) -> int:
    #     windLen = 0
    #     l = 0
    #     charIndex = {}

    #     for r in range(len(s)):
    #         if s[r] in charIndex and charIndex[s[r]] >= l:
    #             # Update left pointer to skip duplicate
    #             l = charIndex[s[r]] + 1
            
    #         # Update the character's most recent index
    #         charIndex[s[r]] = r

    #         # Calculate the current window length
    #         windLen = max(windLen, r - l + 1)

    #     return windLen
