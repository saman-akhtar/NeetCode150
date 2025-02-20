class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        map1 = Counter(s)
        map2 = Counter(t)
        return True if map1 == map2 else  False

        # TC O(N+ M)
        # SC O(N+ M)