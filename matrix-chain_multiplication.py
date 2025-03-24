class Solution:
    def matrixMultiplication(self, arr):
        # code here

        # memoization
        memo = {}
        n = len(arr)
        i = 1
        
        
        def dfs(i,j):
            if i >= j:
                return 0
            if (i,j) in memo:
                return memo[(i,j)]
            min_cost= float('inf')
            # i to j-1 
            for k in range(i, j):
                cost = dfs(i, k) + dfs(k+1, j) + arr[i-1]* arr[k] *arr[j]
                min_cost = min(min_cost, cost)
            memo[(i,j)] = min_cost
            return memo[(i,j)]
        # as there is 1 less mtahn len of arr matirx     
        return dfs(i,n-1)

  # TC O(n²) subproblems × O(n) work per subproblem = O(n³)
# Space = O(n²) (memo) + O(n) (recursion stack) = O(n ^2)
