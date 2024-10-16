class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # o(N)
        numSet = set(nums)
        longest = 0
        # o(N)
        for i in nums:
            l = 0
            # lookup is O(1)
            if(i-1) not in numSet:
                while(i + l  in numSet):
                    #inner loop O(N)
                    l +=1
                longest = max(l, longest)
        return longest
# tc   O(n) + O(n) + O(n) = O(n)
# sc O(N)