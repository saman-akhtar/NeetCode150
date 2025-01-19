class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        
        res = []
        digitMap = {
        "2": ["a", "b", "c"],
        "3": ["d", "e", "f"],
        "4": ["g", "h", "i"],
        "5": ["j", "k", "l"],
        "6": ["m", "n", "o"],
        "7": ["p", "q", "r", "s"],
        "8": ["t", "u", "v"],
        "9": ["w", "x", "y", "z"]
    }
        def backtrack(i, curStr):
            if i == len(digits):
                res.append(curStr)
                return 
            val = digitMap[digits[i]]
            for v in val:
                backtrack(i + 1, curStr + v)
            
        if digits:  # Only start backtracking if digits is not empty
            backtrack(0, "")
        return res

# TC Therefore, there are 

#   combinations, and each combination requires O(n) to store (as strings are immutable in Python and must be copied).
# Overall Time Complexity:\U0001d442(\U0001d458 ^ \U0001d45b⋅\U0001d45b)

# Where: 
# k=3 or 4
# 4 (letters mapped to a digit, e.g., 7 maps to 4 letters, others map to 3).
# \U0001d45b
# n is the number of digits in the input.

# SCO(k ^n⋅n) == each stack if od dept n & store k ^ n combo