class MinStack:

# invariant: Design stack so that each opertaion 
# retunr value as if it is actuall a stakc
    def __init__(self):
        self.stack = []
        

    def push(self, val: int) -> None:
        prev= None
        if self.stack:
            prev= self.stack[-1]
        if prev and val >= prev[1]:
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
 

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
