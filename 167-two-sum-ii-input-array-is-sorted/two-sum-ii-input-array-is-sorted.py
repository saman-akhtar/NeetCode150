class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # approach 1
        l = 0
        r = len(numbers)-1
        while l < r:
            sums = numbers[l] + numbers[r]
            if sums == target:
                return [l+1,r+1]
            elif sums > target:
                r -=1
            else:
                l +=1
        return [-1,-1]
            


    # approach 2
    #     map = {}
    #     for i,num in enumerate(numbers):
    #         if target - num in map:
    #             return [map[target - num]+1, i + 1]
    #         else:
    #             map[num]=i
    #     return [-1,-1]
    # # TC O(N)
    # # SC O(N)