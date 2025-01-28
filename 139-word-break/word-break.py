class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # cats and og
        # cat sandog. sand i

        # APPROACH 2:
        memo = {}
        def canBreak(s):
            # base case
            if not s:
                return True
            if  s in memo:
                return memo[s]
            for word in wordDict:
                if s.startswith(word):
                    if canBreak(s[len(word):]):
                        memo[s] = True
                        return True
            memo[s] = False
            return False
        return canBreak(s)
    # TC O(k.n)
    # SC O(n)

        # APPROACH 1
        # def canBreak(s):
        #     # base case
        #     if not s:
        #         return True
        #     for word in wordDict:
        #         if s.startswith(word):
        #             if canBreak(s[len(word):]):
        #                 return True
        #     return False
        # return canBreak(s)

        # TC k branch & depth n = > o(k ^N) k words in the dictionary, n characters in the string 
        # SC depth n=> O(N)
        
