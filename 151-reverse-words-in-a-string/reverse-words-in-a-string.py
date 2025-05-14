class Solution:
    def reverseWords(self, s: str) -> str:
        s = s.strip()
        s += " "
        l,r = 0 , len(s)-1
        i = 0
        prev = " "
        arr = []
        while i < len(s):
            
            if prev == " " and s[i]!= " ":
                l = i
            
            elif prev != " " and s[i]== " ":
                arr.append(s[l:i])
            prev = s[i]
            i += 1
        return " ".join(arr[::-1])

        