class Solution:
    def findMin(self, nums: List[int]) -> int:
        min_res = float("inf")
        l = 0
        n = len(nums)
        r = n-1
        while l <= r:
       
            mid = (l + r)//2
            min_res= min(min_res,nums[mid])
            left_r = (nums[l], nums[mid-1])
            l1 = mid +1
            if  l1 >= n:
                l1 = mid


            right_r = (nums[l1], nums[r])

            if left_r[0] < right_r[1] or left_r[1] < right_r[1] :
        
                r = mid -1
            else:
                l = mid +1
        return min_res


   # TC O(logN)   
   # SC O(n)  

    # 7 8  9   10 11  13. 14. 15 0 1 2 3 4 5 6

    # sorted
    # 3 5 1 2   
    # 5 2 6 8
    # 4 8 9 1
    #   2.6. 9 10