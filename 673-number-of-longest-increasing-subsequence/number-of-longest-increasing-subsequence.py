class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:

        # appoahc 4 optimze bottom up

        if not nums:
            return 0
        
        n = len(nums)
        lengths = [1] * n  # lengths[i] = length of LIS ending at index i
        counts = [1] * n   # counts[i] = number of LIS ending at index i
        
        for i in range(n):
            for j in range(i):
                if nums[i] > nums[j]:  # nums[i] can extend LIS ending at nums[j]
                    if lengths[j] + 1 > lengths[i]:
                        lengths[i] = lengths[j] + 1
                        counts[i] = counts[j]
                    elif lengths[j] + 1 == lengths[i]:
                        counts[i] += counts[j]
        
        # Find the maximum length of LIS
        max_length = max(lengths)
        
        # Count the number of LIS with the maximum length
        return sum(c for l, c in zip(lengths, counts) if l == max_length)
        # TC O(n^2)
        # SC o(N)

        # approach 3
        # memmoization
        # memo = {}
        # def dp (index, prev_index):
        #     if index == len(nums):
        #         return (0,1)

        #     if (index, prev_index) in memo:
        #         return memo[(index,prev_index)]

        #     # exclude
        #     l_ex, c_ex = dp(index + 1, prev_index)

        #     #inc;ud
        #     l_inc, c_inc = 0, 0
        #     if prev_index == -1 or nums[index] > nums[prev_index] :
        #         next_l, next_c = dp( index + 1, index)
        #         l_inc = next_l + 1
        #         c_inc = next_c
            
        #     # combinc
        #     if l_ex > l_inc:
        #         result = (l_ex, c_ex)
        #     elif l_inc > l_ex:
        #         result = (l_inc, c_inc)
        #     else:
        #         result = (l_inc, c_inc + c_ex)
            
        #     memo[(index, prev_index)] = result
        #     return result


        # max_length, count = dp(0,-1)
        # return count

        # TC o(n^2)
        # S c O(N)+ O(n^2)

        # # apprach 2 
        # if not nums:
        #     return 0
        # res = []
        # self.count = 0
        # self.max_len = 0
        
        # def generateLIS(index, last_num, length):
        #     if index == len(nums):
        #         if ( length > self.max_len):
        #             self.max_len = length
        #             self.count = 1
        #         elif (self.max_len == length):
        #             self.count += 1

                
        #         return
            
        #     # Include nums[index] if it's greater than the last element of cur
        #     if nums[index] > last_num:
        #         generateLIS(index + 1, nums[index], length + 1)
            
        #     # Exclude nums[index]
        #     generateLIS(index + 1, last_num, length)

        # generateLIS(0, float('-inf'), 0)
        # return self.count

        #TC O (2^n)
        # Sc O(n)

        #APPROACH 1
        # if not nums:
        #     return 0
        # res = []
        # def generateLIS(index, cur):
        #     if index == len(nums):
        #         res.append(cur[:])
                
        #         return
            
        #     # Include nums[index] if it's greater than the last element of cur
        #     if not cur or nums[index] > cur[-1]:
        #         generateLIS(index + 1, cur + [nums[index]])

        #     # not includ
        #     generateLIS(index + 1, cur)

        # generateLIS(0, [])
        # max_len = 0
        # count = 0
        # for seq in res:
        #     l = len(seq)
        #     if l == max_len:
        #         count += 1
        #     elif l > max_len:
        #         count = 1
        #         max_len = l
        # return count


        