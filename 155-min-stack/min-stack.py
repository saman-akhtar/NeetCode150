class MinStack:

    def __init__(self):
        self.stack = []
        self.min = []
        

    def push(self, val: int) -> None:
        self.stack.append(val)
        value = min (val, self.min[-1] if self.min else val)
        self.min.append(value)
        

    def pop(self) -> None:
        if self.stack:
            self.stack.pop()
            self.min.pop()
        else:
            print("wrong operation")

        

    def top(self) -> int:
        if self.stack:
            return self.stack[-1]
        
        print("wrong operation")
        return []
        

    def getMin(self) -> int:
        return self.min[-1]
#TC O(1)
# sc         
        
        
# class MinStack:

#     def __init__(self):
#         self.stack = []
#         self.min = float("infinity")
        

#     def push(self, val: int) -> None:
#         self.stack.append(val)
#         self.min = min(self.min, val)
        

#     def pop(self) -> None:
#         if len(self.stack) > 0:
#             # add logic for calculating min
#             ele = self.stack.pop()
#             if(ele == self.min ):
#                 if( len(self.stack) >0 ):
#                     self.min = min(self.stack)
#                 else:
#                     self.min = float("infinity")
#         else:
#             print("wrong operation")

        

#     def top(self) -> int:
#         le = len(self.stack)
#         if le > 0:
#             return self.stack[le-1]
        
#         print("wrong operation")
#         return []
        

#     def getMin(self) -> int:
#         return self.min
        
# in this approach, min is varible need to be updated whenever min item 
# is popped from stack
# so btter to have min as a stack

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
