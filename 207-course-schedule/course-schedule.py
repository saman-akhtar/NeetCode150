class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        visit = set()
        preMap = {i:[] for i in range(numCourses)}
        for courses in prerequisites:
            crs, pre = courses[0], courses[1]
            preMap[crs].append(pre)
        print(preMap)
        def dfs(crs):
            if preMap[crs] == []:
                return True
            visit.add(crs)
            for preqs in preMap[crs]:
                if preqs in visit:
                    return False
                else:
                    if not dfs(preqs):
                        return False
                    
            preMap[crs] = []
            visit.remove(crs)
            return True

        for crs, pre in preMap.items():
            if crs not in visit:
                if not dfs(crs):
                    return False
        return True

        