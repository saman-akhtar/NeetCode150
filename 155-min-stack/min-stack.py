class MinStack:

# Invariant:
# For every index i, stack[i][1] is the minimum of stack[0..i] values.

# Striucture stack - sWe carry forward min

# No recomputation needed

# O(1) getMin

    def __init__(self):
        self.stack = []
        

    def push(self, val: int) -> None:
        prev= None
        if self.stack:
            prev= self.stack[-1]
        if prev is not None and val >= prev[1]:
            self.stack.append([val, prev[1]])
            
        else:    
            self.stack.append([val,val])
        

    def pop(self) -> None:
        val = "Stack is empty"
        if self.stack:
            combined_val = self.stack.pop()
            val = combined_val[0]
        return val
        

    def top(self) -> int:
        val = ""
        if self.stack:
            combined_val =self.stack[-1]
            val = combined_val[0]
     
        return val

    def getMin(self) -> int:
        val = ""
        if self.stack:
            combined_val =self.stack[-1]
            val = combined_val[1]
     
        return val
 
# TC O(1)
# SC O(N)
# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
