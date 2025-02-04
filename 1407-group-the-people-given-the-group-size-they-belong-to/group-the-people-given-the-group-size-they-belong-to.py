class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        n = len(groupSizes)
        groupMap = defaultdict(list)
        for i in range(n):
            group = groupSizes[i]
            groupMap[group].append(i)
        res = []
        for key, value in groupMap.items():
            if len(value) > int(key):
                for i in range(0, len(value), key ):
                    res.append(value[i:i + key])

            else:
                res.append(value)
        return res
        
