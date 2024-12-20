"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        total = 0
        q = deque()
        empMap = {}
        def bfs(emp):
            nonlocal total
            q.append(emp)
            while q:
                node = q.popleft()
                print("node", node)
                if(node):
                    i, imp, sub = node.id, node.importance, node.subordinates
                    total += imp
                    for i in sub:
                        q.append(empMap[i])
                    
        
        for emp in employees:
            empMap[emp.id] = emp
                
        bfs(empMap[id])
        return total




# clarying willdata be given of 2 org?
        