class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:

        # Step 1: Count frequencies
        numMap = Counter(nums)  # O(N)

        # Step 2: Create buckets (index = frequency, values = numbers with that frequency)
        max_freq = max(numMap.values())  # Get max frequency in O(N)
        buckets = [[] for _ in range(max_freq + 1)]  

        # Step 3: Fill buckets
        for num, freq in numMap.items():
            buckets[freq].append(num)

        # Step 4: Build result from bucket (descending order of freq)
        res = []
        for freq in range(len(buckets)):  
            for num in sorted(buckets[freq], reverse=True):  # Sorting within small buckets
                res.extend([num] * freq)  # Extend the list instead of using a loop

        return res


        # #APPRIACh 2
        # numMap = Counter(nums)

        # #
        # sorted_list =sorted(nums, key=lambda x: (numMap[x], -x) )
        # return sorted_list

        # # TC O(NLOGN)
        # # SC O(N)

        # numMap = Counter(nums)

        # sorted_list =sorted(numMap.items(), key=lambda x: (x[1], -x[0]) )
        # res = [num for num, count in sorted_list for _ in range(count)]
        # return res

        # # TC O(N) + O(NLOGN) + o(N)= O(N log N).
        # # SC O(N)

        