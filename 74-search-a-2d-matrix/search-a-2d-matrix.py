class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        r = len(matrix)
        c = len(matrix[0])
        l = 0
        h = c-1
        r1 =0
        for i in range(r):
            if target <= matrix[i][c-1]:
                r1 = i
                break
     
        while l <= h:
            mid = (l + h)//2
            print(l, h, mid)
            if matrix[r1][mid]== target:
                return True
            elif matrix[r1][mid] > target:
                   h = mid - 1
                
            else:
                l = mid +1
             
        return False

# O log(M *n)
# O(1)

# noe have a test case of base case ie. [[1]]