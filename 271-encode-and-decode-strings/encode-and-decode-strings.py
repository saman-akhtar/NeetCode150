class Codec:
    def encode(self, strs: List[str]) -> str:
        """Encodes a list of strings to a single string.
        """
        res = ""
        for n in strs:
            l=len(n)
            res += str(l) + "#" + n
    
        return res

        

    def decode(self, s: str) -> List[str]:
        """Decodes a single string to a list of strings.
        """
        res = []
        i = 0
        l = len(s)
        while i < l:
            j = i
            while s[j] != '#':
                j += 1
                print(j)
            print(i, j-1)
            no_len= int(s[i:j])
            j = j+ 1
            new_str = s[j: j+ no_len]
            res.append(new_str)
            i =  j + no_len


        return res




# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(strs))