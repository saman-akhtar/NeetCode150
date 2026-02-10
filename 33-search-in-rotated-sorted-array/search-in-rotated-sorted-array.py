class Solution:
    def search(self, nums: List[int], target: int) -> int:

        # So your thinking should be:

        #     Which half is sorted?

        #     Is target inside that sorted half?

        #     If yes → go there

        #     If no → go to the other half
        index = -1
        l = 0
        r = len(nums)-1
        while l <= r:
            mid = (l + r)//2
            if nums[mid]== target:
                return mid
            # sorted
            lsort = False 
            rsort = False

            if nums[mid] <= nums[r]:
                rsort = True
            if nums[mid] >= nums[l]  :
                lsort = True
            
            
            if (lsort ):
                if nums[l]<= target <nums[mid]:
                    r = mid -1
                else:
                    l = mid + 1
 
           # rsort
            else:
                if nums[mid]< target <= nums[r]:
                    l = mid + 1
                    
                else:
                    r = mid -1


        return index
        
        # 6 7 1 2 3 4 5
        # 1