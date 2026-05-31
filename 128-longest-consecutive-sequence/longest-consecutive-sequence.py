class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        count = 0
        nSet = set(nums)
        for item in nSet:
            if (item + 1) not in nSet:
                #start of 
                cur_count = 1
                newval = (item - 1)
                while  newval in nSet:
                    cur_count +=1
                    newval -= 1
                count = max(cur_count, count)

        return count