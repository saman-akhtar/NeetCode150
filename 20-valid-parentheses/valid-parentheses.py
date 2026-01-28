class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        open_brac= ["(",'{', '[']
        close_brack =[")","}","]"]
        for b in s:
            if stack and stack[-1] in open_brac:
                prev_brack = stack[-1]
                if b in close_brack:
                    if prev_brack == "(" and b != ")":
                        return False
                    elif prev_brack == "{" and b != "}":
                        return False
                    elif prev_brack == "[" and b != "]":
                        return False
                    stack.pop()
                else:
                    stack.append(b)   
                        
            else:
                stack.append(b)
        print("stack",stack)
        if stack:
            return False
        return True
        