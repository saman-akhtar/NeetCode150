class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # maxl = 0
        # nset = set(nums)
        # for n in nums:
        #     cur_l = 0
        #     cur_n = n 
        # here we are check any no 
        # ie 321  thrice calcuation for lengh
        # this is repeatd .. how to optimzed?? find when the seq start so count 1
        #     while (cur_n -1) in nset:
        #         cur_l+=1
        #         cur_n -= 1
            
        #     maxl = max(maxl,cur_l)

        # return maxl
                  
     # TC O(n)[set creation] + O(n^2) (for & while]

     # Sc O(n) set


     ## Optimized
     # Crux find start of seq
     maxl = 0
     nset = set(nums)
     for n in nset:  #vvvv imp dont do for n in nums: reason is if duplicate no then that seq counted multiple times
        if n -1 not in nset:
            curl = 1
            while ( n + curl) in nset:
                curl += 1
            maxl = max(curl , maxl)
     return maxl

     # tc O(n) no repeated cal as finding start of seq
     # sc O(n)
    
