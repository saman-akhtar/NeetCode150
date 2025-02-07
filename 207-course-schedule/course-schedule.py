class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        visit = set()
        preMap = {i:[] for i in range(numCourses)}
        for courses in prerequisites:
            crs, pre = courses[0], courses[1]
            preMap[crs].append(pre)
        print(preMap)
        def dfs(crs):
            if crs in visit:
                return False
            if preMap[crs] == []:
                return True
            visit.add(crs)
            for preqs in preMap[crs]:
                if not dfs(preqs):
                    return False
                    
            preMap[crs] = []
            visit.remove(crs)
            return True

        for crs, pre in preMap.items():
                if not dfs(crs):
                    return False
        return True

# TC O(P + C)
# SC 