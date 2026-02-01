import operator
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:

        stack = [] 
        i = 0
        op = {
        "+": operator.add,
        "-": operator.sub,
        "*": operator.mul,
        "/": lambda a,b :int(a/b)  # or floordiv for LeetCode
        }
        res = ""
        for token in tokens:
            if token in op:
                b = stack.pop()
                a = stack.pop()
                stack.append(op[token](a, b))
            else:
                stack.append(int(token))

        return stack[0]

        # TC O(N)
        #      SC O(N)