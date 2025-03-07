class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        resArr = []
        # O(n log n)
        nums = sorted(nums)
        n = len(nums)
        print("nums:: ",nums)
        # edge case dupli set ?
        # O(N)
        for i in range(n-2):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            j = i + 1
            k = n -1
            # O(n => O(n ^2))
            while j < k:
                sums = nums[j] + nums[k] + nums[i]
                if( sums  == 0):
                   
                        resArr.append([nums[i], nums[j], nums[k]])
                        j +=1
                        while j < k and nums[j] == nums[j-1]:
                            j += 1
           
                elif sums > 0:
                    k -= 1
                else:
                    j += 1
        return resArr


            


        #TC O (N^2) + O(nlogn)
        # SC O(k) k unique 

        
        #approach1
        # for i in range(len(nums)):
        #     for j in range(i+1,len(nums)):
        #         for k in range(j+1,len(nums)):
                    
        #             if(nums[i]+ nums[j]+ nums[k] == 0):
        #                 temp = sorted([nums[i], nums[j], nums[k]])
        #                 if (temp) not in soln:
        #                     soln.append(temp)
        # return soln

# TC N^3 * O(3log3) => O(1)
# SC O(N)
        