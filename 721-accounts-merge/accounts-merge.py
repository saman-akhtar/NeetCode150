class UnionFind:
    def __init__(self, n):
        self.par = list(range(n))
        self.rank = [1] * n

    def find(self, cur):
        while cur != self.par[cur]:
            self.par[cur] = self.par[self.par[cur]]
            cur = self.par[cur]
        return cur

    def union(self, u, v):
        p1 = self.find(u)
        p2 = self.find(v)

        if p1 == p2:
            return 0
        if(self.rank[p2] > self.rank[p1]):
            self.par[p1]=  p2
            self.rank[p2] += self.rank[p1]
        else:
            self.par[p2] = p1
            self.rank[p1] += self.rank[p2]

        return 1
class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        uf = UnionFind(len(accounts))
        emailToAcc = {}

        for i, email in enumerate(accounts):
            for e in email[1:]:
                if  e in emailToAcc:
                    uf.union(i, emailToAcc[e])
                else:
                    emailToAcc[e] = i
        print("emailToAcc Map:", emailToAcc)
        # {
        #     johnsmith@mail.com: 0
        #     john_newyork@mail.com: 0,
        #     john00@mail.com: 1,
        #     mary@mail.com: 2,
        #     johnnybravo@mail.com: 3
            
        # }
        emailGroups = defaultdict(list)
        for e, i in emailToAcc.items():
            leader = uf.find(i)
            emailGroups[leader].append(e)
        res = []
        for i , email in emailGroups.items():
            name = accounts[i][0]
            res.append([name] + sorted(email))


        return res

# TC 
# 1 O (A * E)
# UNION & find  O (A* E *alpha(A))
# GROUP O(E)
# O(ElogE)
# TC O(A×E×α(A)) + O(ElogE)

# SC Union find O(A)
# GROUP & emailtoACC O(E)
# SC = O(A+E).

# SC O()