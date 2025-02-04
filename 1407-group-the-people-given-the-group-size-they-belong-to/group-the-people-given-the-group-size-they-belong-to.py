class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        # Better slicing techniqu
        n = len(groupSizes)
        groupMap = defaultdict(list)
        # O(N)
        res = []
        for i, size in enumerate(groupSizes):
            groupMap[size].append(i)
            if (len( groupMap[size]) == size):
                res.append(groupMap[size])
                groupMap[size] = []
        
        return res
        # TC O(N)
        # SC O(N)


        # n = len(groupSizes)
        # groupMap = defaultdict(list)
        # # O(N)
        # for i in range(n):
        #     group = groupSizes[i]
        #     groupMap[group].append(i)
        # res = []
        # # O(N)
        # for key, value in groupMap.items():
        #     if len(value) > int(key):
        #         for i in range(0, len(value), key ):
        #             res.append(value[i:i + key])

        #     else:
        #         res.append(value)
        # return res
        # TC O(N) + O(N).O(M)
        # SC O(N)
