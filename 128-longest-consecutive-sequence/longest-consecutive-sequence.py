class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        # APPProach 2
        # optimized
        # check if num -1 doest exist, then calculates longest 
        # so that u vistit 1 item only ince in ineer loop
        longest = 0
        numSet = set(nums) # O(N)
        for num in numSet:
            streak = 1
            if num -1 not in numSet:
                cur_num = num
                while cur_num + 1 in numSet:
                    streak += 1
                    cur_num += 1
            longest = max(longest,streak)
        return longest

        # TC O(N) + O(n)+ O(N)
#         Creating the set: O(n)
# Iterating over the set: O(n)
# Inner while loops (across all iterations): O(n)
# SC O(N)






        # APProach 1 : TLE

        # logic: u loop through each item, if each ietm -1 exist ther is seq
        # keep incrementing longest
        longest = 0
        numSet = set(nums) # O(N)
        for i in range(len(nums)):
            cur_long = 0
            cur_num = nums[i]
            while cur_num in numSet:
                cur_long += 1
                cur_num -= 1
            longest = max(longest,cur_long)
        return longest

        # O(n ^2)
        # SC O(N)












        # # o(N)
        # numSet = set(nums)
        # longest = 0
        # # o(N)
        # for i in nums:
        #     l = 0
        #     # lookup is O(1)
        #     if(i-1) not in numSet:
        #         while(i + l  in numSet):
        #             #inner loop O(N)
        #             l +=1
        #         longest = max(l, longest)
        # return longest
# tc   O(n) + O(n) + O(n) = O(n)
# sc O(N)