class Solution:

   
    def canPartition(self, nums: List[int]) -> bool:

         # APPROACH 2 : Memoization TOp DOWN
         # can be browen in to target SUm

        # if total sum is odd cant be partion !!!
        totalSum = sum(nums)
        if totalSum % 2 != 0:
            return False
        target = totalSum//2
        memo = {}
        def canBreak(i, cur_sum):
            if cur_sum == 0:
                return True
            if i <= 0:
                return False
            if (i, cur_sum) in memo:
                return memo[(i, cur_sum)]
            if nums[i-1] <= cur_sum:
                memo[(i, cur_sum)] =canBreak(i-1, cur_sum- nums[i-1]) or canBreak(i-1, cur_sum)
            else:
                memo[(i, cur_sum)]  = canBreak(i-1, cur_sum)


            
            return memo[(i, cur_sum)]
        n = len(nums)
        return canBreak(n, target)

        # 5  3, 6 ||. 3,11
        # 11      ||  2 0
        