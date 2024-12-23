class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for bracket in s:
            if ( bracket not in [")","]","}"]):
                stack.append(bracket)
            else:
                if(stack):
                    old_bracket = stack.pop()
                    if( bracket == ")" and old_bracket == "(" or bracket == "}" and old_bracket == "{" or  bracket == "]" and old_bracket == "["):
                        continue
                    return False
                else:
                    return False
        return not stack
