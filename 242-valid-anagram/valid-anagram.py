class Solution:
    def isAnagram(self, s: str, t: str) -> bool:


        def createAnagram(word):
            dicts = {}
            for i in word:
                dicts[i]= 1 + dicts.get(i,0)
            return dicts

        ana1 = createAnagram(s)
        ana2 = createAnagram(t)
        if ana1 == ana2:
            return True
        return False

        