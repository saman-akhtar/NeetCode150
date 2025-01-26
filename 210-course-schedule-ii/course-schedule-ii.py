class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        preMap = {i:[] for i in range(numCourses)}

        for crs , pre in prerequisites:
            preMap[crs].append(pre)
        
        order = []
        # viisited 
        # visiting
        #not visited
        visited = set()
        cycle = set()
        def dfs(crs):
            if crs in cycle:
                return False
            if crs in visited:
                return True
            visited.add(crs)
            cycle.add(crs)
            
            for c in preMap[crs]:
                if not dfs(c):
                    return False
            order.append(crs)
            cycle.remove(crs)
            return True


        for crs in preMap:
            if not dfs(crs):
                return []
        return order
        