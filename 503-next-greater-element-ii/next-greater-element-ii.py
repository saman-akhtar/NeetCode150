class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
#         Stack stores indices of elements whose next greater element has not yet been found.
# Stack is monotonically decreasing (values).
        # DUPLicate - index   
        stack = []
        n1 = len(nums)
        res= [-1]* n1
        for i in range(n1*2):
            idx = i % n1
            while stack and nums[idx] > nums[stack[-1]]:
                ind =stack.pop()
                res[ind] = nums[idx]
            if i < n1:
                stack.append(i)

        return res



        
        
        