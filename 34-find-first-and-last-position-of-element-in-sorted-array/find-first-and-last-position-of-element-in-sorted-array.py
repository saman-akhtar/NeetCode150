class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        l = 0 
        h = len(nums) -1
        while l <= h:
            mid = (l+ h)//2
            print(mid)
            if (nums[mid]== target):
                i = mid
                j = mid
                while( i >=0 and nums[i]== target):
                    i -= 1
                while( j <len(nums) and nums[j]== target):
                    j += 1
                i = i + 1
                j = j -1
                return [i,j]
            elif (nums[mid] > target):
                h = mid -1
            else:
                l = mid + 1
        return [-1,-1]


