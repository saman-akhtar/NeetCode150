class Solution:
    def countVowelPermutation(self, n: int) -> int:
        MOD = 10**9 + 7
        vowels = {'a': ['e'],'e':['a','i'],'i':['a','e','o','u'],'o':['i','u'],'u':['a']}
        memo = {}
        
        def dp(cur_str, length):
            if (length == n):
                return 1

            if (cur_str, length) in memo:
                return memo[(cur_str, length)]
            count = 0
            
            if cur_str == "":
                for key,val in vowels.items():
                    count =( count + dp(key ,1)) % MOD
            else:
                for s in vowels[cur_str]:
                        count =( count + dp(s, length + 1 )) % MOD
            memo[(cur_str, length)] =count
            return memo[(cur_str, length)]

        return dp("", 0)
        # MOD = 10**9 + 7
        # vowels = {'a': ['e'],'e':['a','i'],'i':['a','e','o','u'],'o':['i','u'],'u':['a']}
        
        # def dp(cur_str, length):
        #     if (length == n):
        #         return 1
        #     count = 0
            
        #     if cur_str == "":
        #         for key,val in vowels.items():
        #             count =( count + dp(key ,1)) % MOD
        #     else:
        #         for s in vowels[cur_str]:
        #                 count =( count + dp(s, length + 1 )) % MOD

        #     return count

        # return dp("", 0)
        # TC (O(5ⁿ)) + strig concation is N ^2 => 5 vowel 5 branch is each leve
        # # Total Worst-Case Space Complexity (O(5ⁿ) ×N)+O(N)



        # MOD = 10**9 + 7
        # vowels = {'a': ['e'],'e':['a','i'],'i':['a','e','o','u'],'o':['i','u'],'u':['a']}
        # res = set()
        # self.count = 0
        # memo = {}
        # def createVowel( cur_len,prev):
        #     if(cur_len ==n):
              
        #         return 1
        #     if (cur_len, prev) in memo:
        #         return memo[(cur_len, prev)]
        #     count = 0
        #     if prev == "":
        #         for key in vowels:
        #             count = (count + createVowel(cur_len + 1, key)) % MOD
        #     else:
        #         for nextV in vowels[prev]:
        #                 count = (count + createVowel(cur_len + 1, nextV)) % MOD
        #     memo[(cur_len, prev)] = count
        #     return count


        # return createVowel( 0, "")

        # TC O(N * 5) = O(N)
        # SC O(N * 5) = O(N)
         

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