class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        match = {')': '(', '}': '{', ']': '['}
        for ch in s:
            if ch in match:
                # closing brack
                if not stack or stack[-1] !=match[ch]:
                    return False
                stack.pop()
            # openini brac:
            else:
                stack.append(ch)

        return not stack



        
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
    
        if stack:
            return False
        return True
        