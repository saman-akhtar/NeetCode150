class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        stack = []

        def backtrack( oc, cc):
            if oc == 0 and cc == 0:
                s = "".join(stack)
                res.append(s)
                return
            if oc > 0:
                stack.append("(")
                backtrack( oc-1,cc+1)
                stack.pop()

            if cc > 0:
                stack.append(")")
                backtrack(  oc,cc-1)
                stack.pop()

        backtrack(n,0)
        return res


# TC no of valid ways * no of time
# TC= O (4^n) * O(N)

# SC
#  recursiv stack of func + space to store data
# O(n) + 4^n combon & each tale O(n) stack used
# O(4^n +n)
        