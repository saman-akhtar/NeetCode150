class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False


        def createAnagram(word):
            dicts = {}
            for i in word:
                dicts[i]= 1 + dicts.get(i,0)
            return dicts

        if createAnagram(s) == createAnagram(t):
            return True
        return False

        