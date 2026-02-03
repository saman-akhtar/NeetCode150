class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stack = []
        pair = [[p,s] for p,s in zip(position,speed)]
        for p,s in sorted(pair,reverse= True):
            stack.append((target-p)/s)
      
            if len(stack) >=2 and stack[-1] <= stack[-2]:
                    stack.pop()# merge fleet

        return len(stack)
        
# TC O(nlogn)
# SC ON

        #         2, 4,12,7,9
        # 2  4 1 1. 3
        # 1  1 12 7 3
        # 1  4 12 

        # 3 5 7.   10
        # 7     5    3
        # 3     2    1
        # 2.3  2.5.  3
   

        