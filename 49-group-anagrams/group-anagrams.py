class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        alpha = {}
        for w in strs:
            arr = [0]*26
            for l in w:
                arr[ord(l) - ord('a')] += 1
            key = tuple(arr)
            alpha.setdefault(key,[]).append(w)
        return list(alpha.values())