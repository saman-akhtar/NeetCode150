class Solution:
    def isValid(self, s: str) -> bool:
        brackets = {"}":"{",")":"(","]":"["}
        stack = []
        for ch in s:
            if ch not in brackets:
                stack.append(ch)
            else:
                if stack:
                   cur_ch = stack.pop()
                   expected_ch = brackets[ch]
                   print(expected_ch)
                   if expected_ch != cur_ch:
                        return False
                else:
                    return False
        if stack:
            return False
        return True








        # stack = []
        # for bracket in s:
        #     if ( bracket not in [")","]","}"]):
        #         stack.append(bracket)
        #     else:
        #         if(stack):
        #             old_bracket = stack.pop()
        #             if( bracket == ")" and old_bracket == "(" or bracket == "}" and old_bracket == "{" or  bracket == "]" and old_bracket == "["):
        #                 continue
        #             return False
        #         else:
        #             return False
        # return not stack
# TC O(N)
# SC O(N)