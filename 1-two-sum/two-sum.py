class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #clarify can 1 no exist twice ?
        numMap = {}
        for i, num in enumerate(nums):
            diff = target - num
            if diff in numMap:
                return [numMap[diff], i]
            else:
                numMap[num] = i
        
        
