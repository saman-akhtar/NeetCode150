class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        map = defaultdict(list)
        for st in strs:
            nst = [0] * 26
            for s in st:
                index = ord(s)- ord('a')
                nst[index] = nst[index] + 1
            map[tuple(nst)].append(st)
        res = []
        for key, val in map.items():
            if len(val) > 0:
                res.append(val)
        return res
            
        
     
        