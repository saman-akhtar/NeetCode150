class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        nums.sort()
        res = []
        for i in range(n):
            if i >0 and nums[i] == nums[i-1]:
                # skip i
                continue
            target = -nums[i]
            l = i + 1
            r = n - 1
            while l < r:
            
                    sums = nums[l] + nums[r]
                
                    if sums == target:
                        arr= [ nums[i], nums[l], nums[r]]
                        res.append(arr)
                        l += 1
                        r -= 1
                        # imp
                        # avoid duplicate
                        while l < r and nums[l]== nums[l-1]:
                            l +=1
                        while l < r and nums[r] == nums[r+1]:
                            r -= 1

                    elif sums > target:
                        r -=1
                    else:
                        l +=1
  
        return res
           

        