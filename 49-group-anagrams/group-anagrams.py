class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        map = defaultdict(list)
        # TC  O(N)
        for st in strs:
            nst = [0] * 26
            # O(26)
            for s in st:
                index = ord(s)- ord('a')
                nst[index] = nst[index] + 1
            map[tuple(nst)].append(st)
        res = []
        return list(map.values())
            
        
     
        