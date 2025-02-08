class Solution:
    def decodeString(self, s: str) -> str:
        stack =[]
        word =""
        num = 0
        res = ""
        for i in s:
            if i.isdigit():
                num = num * 10 + int(i)
            elif i == "[":
                stack.append((word,num))
                # reset
                num = 0
                word = ""


            elif i == "]":
                stored_str, store_num = stack.pop()
                word = stored_str + word * store_num

            else:
                word += i
        return word


#  "3[a2[c]]"
#         c
#         a  2. acc
#         "" 3


#  "3[a]2[bc]"

#         3abcbc
#         bc    ].    3abcbc
#         3a 2
#         a     ].  3a
#         "" 3

         
        

     


