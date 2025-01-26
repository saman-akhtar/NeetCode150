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
            if preMap[crs] == []:
                order.append(crs)
                return True
            cycle.add(crs)
            
            

            for c in preMap[crs]:
                if not dfs(c):
                    return False
            preMap[crs]= []
            order.append(crs)
            cycle.remove(crs)
            return True


        for crs in preMap:
            if not dfs(crs):
                return []
        return order
        