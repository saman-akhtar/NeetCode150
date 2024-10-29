class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        # to form each valid bracktes
        stack = []

        # store all the brackets
        res = []
        def backtrack(openP, closeP):
            if openP == closeP == n:
                s = "".join(stack)
                res.append(s)
                return
            if openP < n:
                stack.append("(")
                backtrack(openP + 1, closeP)
                stack.pop()
            
            if closeP < openP:
                stack.append(")")
                backtrack(openP , closeP +1)
                stack.pop()
        backtrack(0,0)
        return res

        