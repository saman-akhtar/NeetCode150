class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        path = []
        def dfs (i, sums):
            print("for i",i, "sums:",sums, "path :",path)
          
            if sums == target:
                res.append(path[:])
                return
            if i >= len(candidates) or sums > target:
                return 
            
            path.append(candidates[i ])
            print(sums + candidates[i],"sums pa")
            dfs(i , sums + candidates[i])
            # sums = sums - candidates[i + 1]
            path.pop()

            # inclue
            # if ( i + 1)< len(candidates):
                # sums =  sums + candidates[i + 1]
            # path.append(candidates[i + 1])
            dfs(i + 1, sums )
                
             
            return res
            
            
           
        
        dfs( 0, 0)
        return res

           
            