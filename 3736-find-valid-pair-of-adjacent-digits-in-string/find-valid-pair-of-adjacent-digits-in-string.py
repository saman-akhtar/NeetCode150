class Solution:
    def findValidPair(self, s: str) -> str:
        if len(s) < 2:
            return ""
        res = ""
        # O(N)
        map = Counter(s)
        # O(N)
        for r in range(len(s)-1):
            if s[r] == s[r + 1]:
                continue
            if map[s[r]] == int(s[r]) and  map[s[r+ 1]] == int(s[r+ 1]):
                res = s[r] + s[r+1]
                return res
        return res
        # TC O(N)
        # SC O(N)
        