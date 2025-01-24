class Solution:
    def minTaps(self, n: int, ranges: List[int]) -> int:
        intervals = []

        for i in range(len(ranges)):
            left = max(0, i - ranges[i] )
            right = min( ranges[i]+ i , n)
            intervals.append([left,right])
            
        intervals.sort(key = lambda x: x[0])

        start = 0
        taps = 0
        end = 0
        i = 0
        while start < n:
            
            while i < len(intervals) and intervals[i][0] <= start:
                end = max( end, intervals[i][1])
                i += 1
            if start == end:
                return -1
            start = end
            taps += 1


        return taps


