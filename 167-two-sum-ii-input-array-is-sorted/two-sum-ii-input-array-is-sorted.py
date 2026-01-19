class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        n = len(numbers)
        l = 0
        r = n -1
        while l < r:
            sums = numbers[l] + numbers[r]
            if sums == target:
                return[l+1, r+ 1]
            if sums > target:
                r -=1
            else:
                l +=1
        return [-1.-1]
