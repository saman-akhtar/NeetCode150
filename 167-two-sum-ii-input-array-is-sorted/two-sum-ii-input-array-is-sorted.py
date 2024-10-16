class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l = 0
        r = len(numbers)-1
        while l < r:
            sums =  numbers[r] + numbers[l]
            if(sums ==target):
                return [l+1,r+1]
            elif( sums > target):
                r -=1
            else:
                l += 1

