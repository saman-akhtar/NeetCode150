class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        # here focu on subproblem
        # for [1, 2, 3]
        # if nothig perm is [[]]
        # for 3 [[3]]
        # for 2,3 [[2,3],[3,2]]

        path = []
        if len(nums)==0:
            return [[]]
        perms = self.permute(nums[1:])
        res = []
        # inssert nums[0]
        for p in perms:
            for i in range(len(p)+ 1):
                p_copy = p.copy()
                p_copy.insert(i, nums[0])
                res.append(p_copy)
        return res

#   Time complexity: 

# )
# O(n!∗n 
# 2
#  )
# Space complexity: 

# O(n!∗n)