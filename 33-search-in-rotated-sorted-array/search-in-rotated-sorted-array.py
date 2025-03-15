class Solution:
    def search(self, nums: List[int], target: int) -> int:
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
        