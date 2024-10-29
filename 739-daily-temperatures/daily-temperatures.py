class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        # imp to intitialize
        res = [0] * len(temperatures)
        for i,temp in enumerate(temperatures):
            while(stack and stack[-1][0] < temp):
                prev_temp, prev_i = stack.pop()
                # do not treat res as a stack , append answr in correct index
                res[prev_i] = i - prev_i
                
            stack.append([temp,i])
        return res
        