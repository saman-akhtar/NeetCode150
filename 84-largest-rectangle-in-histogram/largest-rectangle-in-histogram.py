class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []  # To store (index, height)
        max_area = 0  # To keep track of the maximum area

        # Iterate through each bar in the histogram
        for i in range(len(heights)):
            # While the stack is not empty and the current height is less than the height at the top of the stack
            while stack and heights[stack[-1]] > heights[i]:
                h = heights[stack.pop()]  # Height of the rectangle
                width = i if not stack else i - stack[-1] - 1  # Calculate the width
                max_area = max(max_area, h * width)  # Update the maximum area

            stack.append(i)  # Push the current index onto the stack

        # Process any remaining heights in the stack
        while stack:
            h = heights[stack.pop()]  # Height of the rectangle
            width = len(heights) if not stack else len(heights) - stack[-1] - 1  # Calculate the width
            max_area = max(max_area, h * width)  # Update the maximum area

        return max_area
