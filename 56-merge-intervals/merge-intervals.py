class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:

        #CLARYIFNg : is it sorted
        intervals.sort(key= lambda x : x[0])
        res = []
        # for i in range(len(intervals)-1):
        i = 0
        while i < len(intervals): 
            if i == len(intervals)-1:
                # res.append(intervals[i])
                break
            end_cur = intervals[i][1]
            start_next = intervals[i+ 1][0]
            if ( end_cur >= start_next):
                intervals[i][1] = max(end_cur,intervals[i+ 1][1])
                del intervals[i+1]
                # res.append([intervals[i][0],max(end_cur,intervals[i+ 1][1])])
                # i += 1
            else:
                # res.append(intervals[i])
                i += 1
        return intervals


        