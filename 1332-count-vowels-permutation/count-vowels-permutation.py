class Solution:
    def countVowelPermutation(self, n: int) -> int:
        MOD = 10**9 + 7
        vowels = {'a': ['e'],'e':['a','i'],'i':['a','e','o','u'],'o':['i','u'],'u':['a']}
        res = set()
        self.count = 0
        memo = {}
        def createVowel( cur_len,prev):
            if(cur_len ==n):
              
                return 1
            if (cur_len, prev) in memo:
                return memo[(cur_len, prev)]
            count = 0
            if prev == "":
                for key in vowels:
                    count = (count + createVowel(cur_len + 1, key)) % MOD
            else:
                for nextV in vowels[prev]:
                        count = (count + createVowel(cur_len + 1, nextV)) % MOD
            memo[(cur_len, prev)] = count
            return count


        return createVowel( 0, "")
         

        # brute force
    #     class Solution:
    # def countVowelPermutation(self, n: int) -> int:
    #     vowels = {'a': ['e'],'e':['a','i'],'i':['a','e','o','u'],'o':['i','u'],'u':['a']}
    #     res = set()
    #     self.count = 0
    #     def createVowel( cur,prev):
    #         if(cur and len(cur) ==n):
    #             res.add(cur) # store permautatiom
    #             self.count += 1
    #             return 
    #         for key, val in vowels.items():
    #             if prev == "":
    #                 createVowel( key ,key)
    #             else:
    #                 allowedVal = vowels[prev]
    #                 for nextV in allowedVal:
    #                     nw_str = cur + nextV
    #                     if ( nw_str not in res):
    #                         createVowel( nw_str ,nextV)
    #         return


    #     createVowel( "", "")
    #     return self.count

        # TC (O(5ⁿ)) + strig concation is N ^2 => 5 vowel 5 branch is each leve
        # SC  (O(5ⁿ)):= for storing all combe , then string contin is O(N) &  call stack O(N)
#         Component	Space Complexity
# Recursive Stack Depth	O(N)
# Set res storing all sequences	O(5^N * N)
# Temporary String Concatenation (cur + nextV)	O(N) per call
# Total Worst-Case Space Complexity (O(5ⁿ) ×N)+O(N)