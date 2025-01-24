class Solution:
    def minTaps(self, n: int, ranges: List[int]) -> int:

        #APPROACH 2
        intervals = [0] * (n + 1)
        for i in range(len(ranges)):
            left = max(0, i - ranges[i] )
            right = min( ranges[i]+ i , n)
            intervals[left] = max(intervals[left], right) # this reduces sortimh
            # instead of interval at stat index store end index


        start = 0
        tap = 0
        i = 0
        while start < n:
            end = start
            while i < len(intervals) and i <= start:
                end = max(end, intervals[i])
                i += 1
            if end == start:
                return -1

            start = end
            tap += 1
        return tap




# APPROACH 1
#         intervals = []

#         for i in range(len(ranges)):
#             left = max(0, i - ranges[i] )
#             right = min( ranges[i]+ i , n)
#             intervals.append([left,right])
            
#         intervals.sort(key = lambda x: x[0])

#         start = 0
#         taps = 0
#         end = 0
#         i = 0
#         while start < n:
            
#             while i < len(intervals) and intervals[i][0] <= start:
#                 end = max( end, intervals[i][1])
#                 i += 1
#             if start == end:
#                 return -1
#             start = end
#             taps += 1


#         return taps

# Time Complexity:
# Convert to Intervals: 

# O(n), where 
# \U0001d45b
# n is the length of ranges.
# Sort Intervals: 

# O(nlogn).
# Find Minimum Taps: 

# O(n).
