class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:

        #CLARYIFNg : is it sorted
        # APproach 2
        intervals.sort(key= lambda x : x[0])
        res = []
        i = 0
        while i < len(intervals):
            # no overlapp  or no res
            if not res or res[-1][1] < intervals[i][0]:
                res.append(intervals[i])
            else:
                res[-1][1] = max(intervals[i][1],res[-1][1] )
            i += 1
        return res

        # TC  O(nlogn) + O(N))
        # SC O(N)




        # APproach 1
        # intervals.sort(key= lambda x : x[0])
        # res = []
        # i = 0
        # while i < len(intervals): 
        #     if i == len(intervals)-1:
        #         break
        #     end_cur = intervals[i][1]
        #     start_next = intervals[i+ 1][0]
        #     if ( end_cur >= start_next):
        #         intervals[i][1] = max(end_cur,intervals[i+ 1][1])
        #         del intervals[i+1]
        #     else:
        #         i += 1
        # return intervals
# TC  O(nlogn) +  O(N *N)

# SC O(1)

        