class Solution:
    def search(self, nums: List[int], target: int) -> int:

        l, r = 0 , len(nums)-1
        while l <= r:
            mid = (l + r) // 2
            print("mid tar", mid, target)
            if nums[mid] == target:
                return mid
            # sorted
            # logic is search in sorted half
            if nums[l] <= nums[mid]:
                if nums[l]<= target < nums[mid]:
                    r   = mid -1
                else:
                    l = mid + 1
            else:
                if nums[mid] < target <= nums[r]:
                    
                    l = mid + 1
                else:
                    r = mid -1
            # elif nums[r] > nums[mid]:
            #     if target > nums[mid]:
            #         l = mid + 1
                    
            #     else:
            #         r   = mid -1
                    
            # # if nums[r] > nums[mid]:
            # #  / unsorted ??
            # else:
            #     if target > nums[mid]:

            #             l = mid + 1
            #     else:
            #         r = mid -1
        return -1
        # 3 4 5 6 7 0 1 2

        # TC O(logn)
        # SC O(1)


        l = 0
        h = len(nums) -1
        while l <= h:
            m = (l +h)//2
            if nums[m]== target:
                    return  m
            elif nums[m] >= nums[l]:
                if target < nums[l] or target > nums[m]:
                    l = m + 1 # if not found in sorted
                else:
                    h = m -1
                # sorted part
            else:
                if target > nums[h] or target < nums[m]:
                    h = m - 1 # if not found in sorted
                else:
                    l = m + 1

            
                
        return -1
                

# trick .. find which is sorted part , check target exist there in sorted part,else belong to undotred part

# 4 5 6 0 1 2 3
# O (Logn )
# O(1)
        