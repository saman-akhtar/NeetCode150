class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #bucket
        nMap = defaultdict(int)
        for n in nums:
            nMap[n] += 1
        bucket = [[] for i in range(len(nums)+1)]
        for key , freq in nMap.items():
            bucket[freq].append(key)
        res=[]
        for i in range(len(bucket) - 1, 0, -1):
            for num in bucket[i]:
                res.append(num)
                if len(res) == k:
                    return res
        

        # naive way
        nMap = defaultdict(int)
        for n in nums:
            nMap[n] += 1
        res = []
        for key , v in nMap.items():
            heapq.heappush(res,(-v,key))
        ans=[]
        for i in range(k):
            ans.append( heapq.heappop(res)[1])
        return ans
 #TC O(n) + n logn + klogN = N logN
 # SC O(N)