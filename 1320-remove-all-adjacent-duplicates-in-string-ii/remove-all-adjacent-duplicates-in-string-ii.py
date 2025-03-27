class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        n = len(s)
        if n < 2:
            return s
        stack = []
        i = 0
        for ch in s:
            if stack and stack[-1][0] == ch:
                stack[-1][1] +=1
                if stack[-1][1] == k:
                    stack.pop()
            else:
                stack.append([ch,1])
        return "".join( ch * count for ch,count in stack)
        # TC O(N)
        # SC O(N)

                
       

        
        # d 
        # d 2
        # d 1
        
        