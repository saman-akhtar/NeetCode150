class Solution:
    def decodeString(self, s: str) -> str:
        def parseData(j):
            stack = []
            rep = 0
            end_index = j
            str_res = ""
            
            while j < len(s) and s[j] != "]":
                if s[j].isdigit():
                    rep = rep * 10 + int(s[j])
                elif s[j] == "[":
                    tmp_res, end_index = parseData(j + 1)
                    # Apply repetition immediately when getting result from nested call
                    str_res += tmp_res * rep
                    rep = 0
                    j = end_index  # Skip the processed substring
                    continue
                else:
                    str_res += s[j]
                j += 1
                
            return str_res, j + 1  # Return the processed string and the position after ']'
        
        # Main function logic
        rep = 0
        res = ""
        i = 0
        while i < len(s):
            if s[i].isdigit():
                rep = rep * 10 + int(s[i])
            elif s[i] == "[":
                new_str, j = parseData(i + 1)
                res += new_str * rep
                rep = 0
                i = j - 1
            else:
                res += s[i]
            i += 1
            
        return res