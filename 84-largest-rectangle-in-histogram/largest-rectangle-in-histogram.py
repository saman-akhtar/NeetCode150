class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:

        # The stack stores increasing bars with their leftmost reach; popping finalizes area.”
# optimized Method 2
        stack = []
        max_vol = 0
        n = len(heights)
        for i,h in enumerate(heights):
            start = i
            while stack and stack[-1][1] > h:
                idx, prev = stack.pop()
                max_vol =max(max_vol, prev * (i - idx))
                start = idx
            
            stack.append((start,h))
        for i,h in stack:
            
            max_vol = max(max_vol, h * (n - i))  
        return max_vol

       # TC O(N)
       # SC O(N)



        # metho1 1 two pad
        stack = []
        max_area = 0
        n = len(heights)
        left =[0 ]*n
        for i in range(n):
            h = heights[i]
            while stack and stack[-1] >= h:

                    old_h  = stack.pop()
                    left[i] +=1
            stack.append((h))
        stack = []
        right =[0 ]*n
        for i in range(n-1,-1,-1):
            h = heights[i]
            
            while stack and stack[-1] >= h:

                    old_h  = stack.pop()
                    right[i] +=1
            stack.append((h))
        print("left",left)   
        print("right",right)
        for i in range(n):
            max_area = max(max_area, heights[i]* (left[i]+right[i]+1))
        return max_area





        #     while stack and stack[-1] >= h:

        #             idx , old_h = stack.pop()
        #             max_area =max(max_area, h * ( i - idx))
        #             start = idx
        #     stack.append((start,h))

        # stack = []
        # max_area = 0
        # n = len(heights)
        # for i in range(n):
        #     h = heights[i]
        #     start = i
        #     # left side, pop >=
        #     while stack and stack[-1][1] > h:

        #             idx , old_h = stack.pop()
        #             max_area =max(max_area, old_h * ( i - idx))
        #             start = idx
        #     stack.append((start,h))
        # # clean up rem
        # for i, h in stack:
        #     max_area = max(max_area, h * (n -i))


        # return max_area

#TC O(N^2)
# SC O(N)
     