class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for ch in s:
            if ch in ["}",")","]"]:
                if stack:
                    old_ch = stack.pop()
                    if ch == "}" and old_ch != "{":
                        return False
                    elif ch == ")" and old_ch != "(":
                        return False
                    elif ch == "]" and old_ch != "[":
                        return False
                    
                    
                else:
                    return False
            else:
                stack.append(ch)
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