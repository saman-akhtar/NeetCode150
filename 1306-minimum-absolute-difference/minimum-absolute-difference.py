class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr.sort()
        min_d = float('inf')
        res = []
        for i in range(len(arr)-1):
            diff = arr[i+1] - arr[i]
            if diff < min_d:
                res = []
                res.append([arr[i],arr[i+1]])
                min_d =diff
            elif diff == min_d:
                res.append([arr[i],arr[i+1]])

        return res
        # TC O(NlogN)
        # SC O(N)