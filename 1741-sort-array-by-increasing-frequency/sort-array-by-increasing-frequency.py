class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        numMap = Counter(nums)
        print("numMap",numMap)

        sorted_list =sorted(numMap.items(), key=lambda x: (x[1], -x[0]) )
        res = [num for num, count in sorted_list for _ in range(count)]
        # for freq in sorted_list:
        #     res.append()
        # for 
        return res
        # for k,v in numMap.items():

        