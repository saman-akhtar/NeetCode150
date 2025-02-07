class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        numMap = Counter(nums)

        sorted_list =sorted(nums, key=lambda x: (numMap[x], -x) )
        return sorted_list

        # TC O(NLOGN)
        # SC O(N)

        