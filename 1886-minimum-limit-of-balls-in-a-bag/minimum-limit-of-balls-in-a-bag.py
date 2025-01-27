class Solution:
    def minimumSize(self, nums: List[int], maxOperations: int) -> int:

        #TC O(log(max(nums))⋅len(nums))
        # SC O(1)
        def can_divide(max_balls):
            ops = 0
            for n in nums:
                # if total no of operation is aplicable
                ops += ceil(n/max_balls) -1
                if ops > maxOperations:
                    return False
            return True

        max_no = max(nums)

        # 1st divide from small no , is the minimu ball required
        l = 1
        r = max(nums)
        while l < r: # as we r = m
            m = (l + r)//2
            if can_divide(m):
                r = m
            else:
                l = m +1
        return l



        # APPROACH 1
        # def can_divide(max_balls):
        #     ops = 0
        #     for n in nums:
        #         # if total no of operation is aplicable
        #         print("N",n, " :::  ", max_balls)
        #         ops += ceil(n/max_balls) -1
        #         if ops > maxOperations:
        #             print("N1 Fals",ops,False)
        #             return False
        #     print("N1 Fals",ops,False)
        #     return True

        # max_no = max(nums)

        # # 1st divide from small no , is the minimu ball required
        # for i in range(1,max_no):
        #     if can_divide(i):
        #         return i
        # TC O(N * M) m is no of op
        # SC # O(1)

        