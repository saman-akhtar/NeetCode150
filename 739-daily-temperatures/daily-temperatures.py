class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:

        # MONOTONIC stack
        # ie it keeps growing in 1 direction
        n = len(temperatures)
        res = [0]* n
        stack = [(temperatures[0], 0)]
        for i in range (1, n):
            
            cur_temp = temperatures[i]
            while  stack and temperatures[i] > stack[-1][0]:
                old_temp, old_index = stack.pop()
                res[old_index]= i - old_index
                # cur_temp = old_temp
                # cur_index = old_index

            stack.append((temperatures[i], i))
        # if stack:
        #     print("stac",stack)
        #     while ( stack ):
        #         cur_temp, cur_index = stack.pop()
        #         if( stack and cur_temp > stack[-1][0]):
        #             prev_index =stack[-1][1]
        #             res[prev_index]= cur_index - prev_index
        return res


        # TC O(N)
        # SC O(N)
        # 1 1 4 2 1 1 0 0
