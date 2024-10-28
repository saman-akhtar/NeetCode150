class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for i in range(len(tokens)):
            ch = tokens[i]
            if ch in ['*','/','+','-']:
                if len(stack) < 2:
                    print("wrong operation")
                    return None
                op1 = int(stack.pop())
                op2= int(stack.pop())
                
                    
                if ch == '*':
                    cal = op1 * op2
                elif ch == '/':

                    # note do truee divsion instead of float division
                    cal = op2 / op1
                elif ch == '+':
                    cal = op1 + op2
                elif ch == '-':
                    cal = op2 - op1

                stack.append(int(cal))
            else:
                stack.append(ch)
        if len(stack) > 1:
            print("wrong operation")
        else:
            return int(stack.pop())
