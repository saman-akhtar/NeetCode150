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
            stack.append((temperatures[i], i))
        return res


        # TC O(N)
#          Time Complexity (TC) Analysis
# Each temperature is processed once (loop iterates N times).
# Each index is pushed onto the stack at most once (O(N)).
# Each index is popped from the stack at most once (O(N)).
# Thus, the worst-case scenario is that each element is pushed once and popped once, leading to:

# O(N)

        # SC O(N)
#         Result array (res) → O(N) (stores answers for each day).
# Monotonic stack (stack) → Worst case O(N) (if temperatures are strictly decreasing, all elements go on the stack).
# Other auxiliary variables → O(1), which is negligible.
# currentl storing O(2N) as storing tuples
# we can also stor only index to make it O(N)

        # 1 1 4 2 1 1 0 0
