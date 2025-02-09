class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        maxArea = 0
        for i, h in enumerate(heights):
            start = i
            while stack and stack[-1][0] >= h:
                old_h,old_i = stack.pop()
                area = old_h * (i -old_i)
                maxArea = max(maxArea, area)
                start = old_i
            stack.append((h,start))
        for  h, i in stack:
            area = h * (len(heights) - i)
            maxArea = max(maxArea, area)
        return maxArea






        # TC O(N)
        # SC O(N)


        # COmplute maxleft & maxright

    #     maxA = 0

    #     for i in range(len(heights)):
    #         h = heights[i]
    #         rightMost = i + 1
    #         while rightMost < len(heights) and heights[rightMost] >= heights[i]:
    #             rightMost += 1
    #         leftMost = i -1 
    #         while leftMost >=0 and heights[leftMost] >= heights[i]:
    #             leftMost -= 1

    #         maxA = max(maxA, heights[i] * (rightMost - leftMost -1))
    #     return maxA

    # # TC O(n^2)

    # # SC O(1)
            



        