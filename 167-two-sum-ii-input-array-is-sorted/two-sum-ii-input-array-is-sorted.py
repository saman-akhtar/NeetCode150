class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        map = {}
        for i,num in enumerate(numbers):
            if target - num in map:
                return [map[target - num]+1, i + 1]
            else:
                map[num]=i
        return [-1,-1]
    # TC O(N)
    # SC O(N)