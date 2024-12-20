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
        #O(E +V)
        def bfs(d):
            nonlocal total
            q.append(empMap[d])
            while q:
                node = q.popleft()
                if(node):
                    i, imp, sub = node.id, node.importance, node.subordinates
                    total += imp
                    for i in sub:
                        q.append(empMap[i])
                    
        # O(V)
        for emp in employees:
            empMap[emp.id] = emp
                
        bfs(id)
        return total

# TC O(V + E)
# SC: BFS & empMap =>. O(V).


# clarying willdata be given of 2 org?
        