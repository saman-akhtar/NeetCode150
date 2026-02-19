class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow = 0
        fast =0

        # find start if a cycke
        while True:
            slow = nums[slow] # travek 1 at a time
            fast = nums[nums[fast]] # go twice
            if slow == fast:
                break 
       # if two pointer pont to start of a cycle, tahts the answer
        slow2 = 0 # start from start
        while True:
            slow = nums[slow] # withing cycke , sl slow2& slwo are eqidistance for 
            slow2 = nums[slow2]
            if slow == slow2:
                return slow
