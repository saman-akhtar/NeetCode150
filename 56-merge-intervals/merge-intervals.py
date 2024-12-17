class Solution:

    # will interval sorted?
    # will overlap of 1st takeover? [[1,4],[2,3]]? edge case
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        res = [intervals[0]]
        for i in range(1,len(intervals) ):
            if(res[-1][1] >= intervals[i][0]):
                end = max(res[-1][1], intervals[i][1])
                res[-1]= [res[-1][0], end]
            else:
                res.append(intervals[i])
        return res
        