class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        res = [0]*n
        stack =[]
        
        for i in range(n-1, -1,-1):
            t = temperatures[i]
            # remove from stakc if not in expected way ie. previo temp < old temp
            while stack and t  >= stack[-1][0]:
                stack.pop()
            if stack:
                res[i]= stack[-1][1] -i 
            # keep adding in stack 
            stack.append((t,i))

        return res     

                #no bigger
# TC O(N)
# SC O(N)
        # 0
        # 0 76
        # 1 72 76
        # 1 69 72 76
        # 2
        # 30
        # 40
        # 50    50,1
        # 60.  60,0`12
        
        
        # 60
        # 50 55,5
        # 4. 5,1
        # 5. 6,1
        # 6. 55,2
        # 6  55,1
        # 55 80,1
        # 80 80 0

        0
        0
        1
        1
