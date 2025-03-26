class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # unique 
        result = {}
        for i,num in enumerate(nums):
            diff = target - num
            if  diff in result:
                index = result[diff]
                return [index, i ]
            else:
                result[num] = i
        
        # TC O(N)
        # SC  O(N)
        
        
