class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # cats and og
        # cat sandog. sand i
        # n = len(s)
        # wordSet = set(wordDict)
        # dp = [True] * (n+1)
        # for i in range(1,n+1):
        #     for j in range(0, i):
                
        #         dp[i]= dp[i][j] and s[j: i] in wordSet
        # return dp[n]

        word ={}
        wordSet = set(wordDict)
        def cansegmentString(i ):
            if i== 0:
                # "" is semntable ?
                return True
            # check semnet s[o:i] ? chag is
            if (i) in word:
                return word[i]
            for j in range(i):
                # chekc if prefix is breakble & sufficx is breakable
                # why j notj - :beauc Can the part before j be broken into valid words?
                if cansegmentString(j) and s[j:i] in wordSet:
                    word[i] = True
                    return word[i]
            word[i] = False
            return word[i]
        n = len(s)
        return cansegmentString(n)







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
        
