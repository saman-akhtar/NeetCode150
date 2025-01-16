class Solution:
    def calculate(self, s: str) -> int:
        stack = []
        cur = 0
        sign = 1
        res = 0
        for i in s:
            if i.isdigit():
                cur = cur * 10 + int(i)
            elif i in ["+", "-"] :
                res += cur * sign
                if i == "+":
                    sign = 1
                else:
                    sign = -1
                cur = 0
        
            elif i == "(":
                stack.append(res)
                stack.append(sign)
                sign = 1
                res = 0
            elif i == ")":
                res += sign * cur
                # sign
                res *= stack.pop()

                #no
                res += stack.pop()
                cur = 0

        return  res + cur * sign

        