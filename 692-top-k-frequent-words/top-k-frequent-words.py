class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        # freqMap = {}
        # for word in words:
        #     freqMap[word] = freqMap.get(word, 0) + 1
        freqMap = Counter(words) # O (N)
        print("freqMap",freqMap)
        heap = []
        heap = [(-freq, word) for word, freq in freqMap.items()] # O (N)
        heapq.heapify(heap)  # Convert list into a heap # O (N)

        # Extract top K frequent words, the smallest lexicographically comes first for ties
        res = [heapq.heappop(heap)[1] for _ in range(k)]  # O k log(N) # pop max elemnt
        
        return res

        #Total Complexity: O(N + K log N),
        # for key, value in freqMap.items():
        #     heapq.heappush(heap, (value,key))
        #     if len(heap) > k:
        #         heapq.heappop(heap)
        # print('heappq', heap)
        # # res = [ value for value_k, value in heap]
        # res = []
        # res = [heapq.heappop(heap)[1] for _ in range(k)]
        # return res
        