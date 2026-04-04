# Given an integer n, print all the n digit numbers in increasing order, such that their digits are in strictly increasing order(from left to right).

# Example 1:

# Input:
# n = 1
# Output:
# 0 1 2 3 4 5 6 7 8 9
# Explanation:
# Single digit numbers are considered to be 
# strictly increasing order.
# Example 2:

# Input:
# n = 2
# Output:
# 12 13 14 15 16 17 18 19 23....79 89
# Explanation:
# For n = 2, the correct sequence is
# 12 13 14 15 16 17 18 19 23 and so on 
# up to 89.
# Your Task:  
# You don't need to read input or print anything. Your task is to complete the function increasingNumbers() which takes an integer n as an input parameter and returns the list of numbers such that their digits are in strictly increasing order.

# Expected Time Complexity: O(9n)
# Expected Auxiliary Space: O(n)

# Constraints:
# 1 <= n <= 9


from typing import List


class Solution:
    def increasingNumbers(self, n : int) -> List[int]:
        # code here
        res = []
        if n== 1:
            return [i for i in range(10)]
        def solve(n, no,prev):
            # base case
            if n ==0 :
                res.append(no)
                return;
            
            for i in range(prev+1,10):
                    
                        new = no*10 + i
                        solve(n-1, new,i)
                
        solve(n, 0, 0)
        return res
        
        # TC & SC Reminder:TC: $O\binom{9}{n}$ — You are only visiting valid combinations.SC: $O(n)$ — The depth of your "shortcut" calls only goes as deep as the number of digits $n$.
