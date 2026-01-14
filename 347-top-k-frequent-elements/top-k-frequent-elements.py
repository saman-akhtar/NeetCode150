class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
     
        d = {}
        # O(N)
        for n in nums:
            d[n]= d.get(n,0) + 1
        count = defaultdict(list)
        #O(N)
        for key, v in d.items():
            count[v].append(key)
        res = []

        for i in range(len(nums),0,-1):
            if len(count[i]) > 0:
                    res.extend(count[i])
            if len(res) >=k:
                return res[0:k]
        return res[0:k-1]

