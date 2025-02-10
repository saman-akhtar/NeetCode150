class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        l =0
        h = len(nums) -1
        while l <= h:
            m = (l + h)//2
            if(nums[m]== target):
                return m
            if (nums[m] < target):
                l = m +1
            else:
                h = m - 1
        return l

    # Throughout the loop, all elements at indices less than l are guaranteed to be less than the target, and all elements at indices greater than h are guaranteed to be greater than the target.
    # so as  sson as l > h , we can add new elemnt at l as it will be = taget & it wont effect
    # so in worst case l = len(nums) = end of array, so item instred there

    # TC O(Log n)
    # SC O(1)