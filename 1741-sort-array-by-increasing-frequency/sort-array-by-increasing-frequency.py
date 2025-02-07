class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        numMap = Counter(nums)

        #
        sorted_list =sorted(nums, key=lambda x: (numMap[x], -x) )
        return sorted_list

        # TC O(NLOGN)
        # SC O(N)

        numMap = Counter(nums)

        sorted_list =sorted(numMap.items(), key=lambda x: (x[1], -x[0]) )
        res = [num for num, count in sorted_list for _ in range(count)]
        return res

        # TC O(N) + O(NLOGN) + o(N)= O(N log N).
        # SC O(N)

        