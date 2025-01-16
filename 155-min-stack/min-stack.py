class MinStack:
 # claryfing : if uniqye item added ?
    def __init__(self):
        self.stack = []
        self.minStack = []
        

    def push(self, val: int) -> None:
        self.stack.append(val)
        if self.minStack:
            min_val = self.minStack[-1]
        else:
            min_val = float('inf')
        self.minStack.append(min(val, min_val))
        

    def pop(self) -> None:
        if self.stack:
            self.minStack.pop()
            last = self.stack.pop()
            return last
        print("Wrong operation")
        

    def top(self) -> int:
        if self.stack:
            return self.stack[-1]
        print("Wrong operation")

    def getMin(self) -> int:
        if self.stack:
            return self.minStack[-1]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()