class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # O(N logN)
        intervals.sort(key= lambda x:x[0])
        res = [intervals[0]]
        # ON
        for i in range(1,len(intervals)):
            cur_int = intervals[i]
            if(cur_int[0] <= res[-1][1]):
                res[-1][1] = max(cur_int[1], res[-1][1] )
            else:
                res.append(cur_int)

        return res

        # TC O(N Log N)
        # SC O(N)
        