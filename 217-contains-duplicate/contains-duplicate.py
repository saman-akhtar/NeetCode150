class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        map = {}
        for i, nums in enumerate(nums):
            if nums in map:
                return True
            else:
                map[nums] = 1
        return False
# TC O(N)
# SC O(N)