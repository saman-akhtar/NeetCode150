class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        l, r = 0 , len(nums)-1
        while l <= r:
            mid = (l + r)//2
            if nums[mid] == target:
                return True
            # EDGE case for duplicates
             # If we can't tell which half is sorted due to duplicates
       
            if nums[l] == nums[mid]== nums[r]:
                l += 1
                r -= 1
            # check sorted
            elif nums[l] <= nums[mid]:
                # if target on sorted half
                if nums[l] <= target < nums[mid]:
                    r = mid -1
                else:
                    l = mid + 1
            else:
                # if in other sorted half
                if nums[mid] < target <= nums[r]:
                    l = mid + 1
                else:
                    r = mid -1


        return False
        # TC O(logn)
        # SC O(1)