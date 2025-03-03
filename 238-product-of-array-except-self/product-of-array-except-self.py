class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        # CAN it fit into 32 bit ?
        # can each element be negative positive
        # check 32 bit overflow python, how to resolve it
        # 1.  2. 3. 4. intial
        # 1   1  2    6 pre
        # 24  12  4   1  post
        # 24 12.  8   6

        # -1  1   0  -3    3
        # 1. -1  -1   0    0
        # 0   0   -9  3    1
        # 0   0.   9. 0.   0

        # 1.  -1. -1  0 

        prefic = 1
        postfix =1
        res= [1] * len(nums)
        for i in range(1, len(nums)):
            res[i]= res[i-1] * nums[i-1]
        
        for i in range(len(nums)-1,-1,-1):
            res[i] = postfix * res[i]
            postfix= postfix * nums[i]
        return res



        # n = len(nums)
        # res = [1] * n

        # # 1st compute prefix
        # for i in range(1, len(nums)):
        #     res[i] = res[i-1] * nums[i-1]
        # postfix = 1

        # # postfix is already 1 
        # # that mean calcu res = prefix * postfix
        # # then update postfix
        # for i in range(n -1 , -1,-1):
        #     res[i]= postfix * res[i]
        #     postfix = postfix * nums[i]
        # return res

    # TC O(N) + O(N)
    # SC O(1) as res is the o/p

        