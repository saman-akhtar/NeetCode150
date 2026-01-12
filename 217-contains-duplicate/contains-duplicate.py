class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        dicts = {}
        for i in nums:
            if i in dicts:
                return True
            else:
                dicts[i] = 1


        return False
        