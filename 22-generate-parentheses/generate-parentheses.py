class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        def backtrack(cur_str, oc, cc):
            if oc == 0 and cc == 0:
                res.append(cur_str)
                return
            if oc > 0:
                # cur_str += "("
                # oc -=1
                # cc +=1
                backtrack(cur_str + "(", oc-1,cc+1)

            if cc > 0:
                # cc -=1
                backtrack(cur_str + ")", oc,cc-1)

        backtrack("",n,0)
        return res

        