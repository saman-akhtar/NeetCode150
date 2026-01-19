class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
         # question
         #1 can no be negative 
       
       # METHOD 1 : TLE
        # l = len(nums)
        # pre =[1] * l
        # post =[1] * l
        # res =[1] * l
        # for i in range(l):
        #     j = i + 1
        #     total = 1
        #     while j < l:
        #         total *= nums[j]
        #         j+=1
        #     pre[i] = total

        # for i in range(l-1,-1,-1):
        #     j = i -1
        #     total = 1
        #     while j > -1:
        #         total *= nums[j]
        #         j-=1
        #     post[i] = total
        

        # for i in range(l):
        #     res[i] = pre[i] * post[i]
        # return res
            

        # TC O(n^2) + O(n^2) + O(n) = o(n^2)
        # SC O(n) + O(n)  = O(n)

        # METHOD 2 opmized
    
       
#         l = len(nums)
#         res =[1] * l
#         pre =[1] * l
#         post =[1] * l
# #         Prefix product: pref[i] = product of all elements to the left of i
# # potfix product: post[i] = product of all elements to the right of i
#         for i in range(1,l):
#             pre[i] =nums[i-1] * pre[i-1]

#         for i in range(l-2,-1,-1):
#             post[i]= nums[i+1] * post[i+1]
#         for i in range(l):
#             res[i] = pre[i] * post[i]
#         return res
            

        # TC O(n) + O(n) + O(n) = o(n)
        # SC O(n) + O(n)  = O(n)

      

       # Method 3 - fully optimized for space too
        l = len(nums)
        res =[1] * l
        postfix = 1
        prefix =1 
        for i in range(1,l):
            res[i] = prefix * nums[i-1]
            prefix = res[i]
        
        for i in range(l-2,-1,-1):
            postfix = postfix * nums[i+1]
            res[i] = postfix * res[i]

        return res


















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


        n = len(nums)
        res = [1] * n

        # 1st compute prefix
        for i in range(1, len(nums)):
            res[i] = res[i-1] * nums[i-1]
        postfix = 1

        # postfix is already 1 
        # that mean calcu res = prefix * postfix
        # then update postfix
        for i in range(n -1 , -1,-1):
            res[i]= postfix * res[i]
            postfix = postfix * nums[i]
        return res

    # TC O(N) + O(N)
    # SC O(1) as res is the o/p

        