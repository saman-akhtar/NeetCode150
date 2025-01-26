class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        visit = set()
        preMap = {i:[] for i in range(numCourses)}
        # can same pre-re be there?
        for course in prerequisites:
            preMap[course[0]].append(course[1])

            # 1 2 3.     1 2 3
            #            2 1
            # 2 3
            # 3 []
        def dfs(crs):
            if crs in visit:
                return False
            if(preMap[crs] == []):
                    return True
            visit.add(crs)
            for c in preMap[crs]:
                
                
                if dfs(c)== False:
                    return False
            preMap[crs] = []
            visit.remove(crs)
            return True


        for crs in preMap:
            if dfs(crs) == False:
                return False
        return True


# TC O(c + p)
# O(c +p) = premAp o(c), visit O(N)


        