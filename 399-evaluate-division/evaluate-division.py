class Solution:

    # claryfig eg ARE valid? division by 0
    # will u/ v & v/u both be givem
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        adjMap = collections.defaultdict(list)
        for i in range(len(equations)) :
            eq = equations[i]
            val = values[i]
            adjMap[eq[0]].append([eq[1], val])
            adjMap[eq[1]].append([eq[0], 1/ val])
        res = []

        def bfs( src, target):
            visited = set()
            q = deque()
            q.append([src, 1])
            visited.add(src)
            while q:
                n, w = q.popleft()
                if(n == target):
                    return w
                for neig, weight in adjMap[n]:
                    if neig not in visited:
                        q.append( [neig,w * weight])
                        visited.add(neig)
            return -1


        for q in queries:
            n = q[0]
            d = q[1]
            ans = -1.0
            if(n not in adjMap or d not in adjMap):
                res.append(ans)
            else:
                res.append(bfs(n,d))
        return res

        



        