class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool: 

        rows = len(matrix)
        cols = len(matrix[0])
        top = 0
        bot = rows - 1

        # Binary search to find the correct row
        while top <= bot:
            mid = (top + bot) // 2
            if target > matrix[mid][-1]:
                top = mid + 1
            elif target < matrix[mid][0]:
                bot = mid - 1
            else:
                break
        
        # If no valid row was found
        if not (top <= bot):
            return False

        # Binary search within the identified row
        row = (top + bot) // 2
        l = 0
        r = cols - 1
        while l <= r:
            m = (l + r) // 2
            if matrix[row][m] == target:
                return True
            elif matrix[row][m] < target:
                l = m + 1
            else:
                r = m - 1
        
        return False