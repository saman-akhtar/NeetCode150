class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        winL = 0
        l = 0
        win = set()
        for r in range(len(s)):
            if (s[r] in win):
                while(s[r] in win and l < r):
                    win.remove(s[l])
                    l += 1
                win.add(s[r])
            else:
                win.add(s[r])
                winL = max(len(win), winL)
        return winL
