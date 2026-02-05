class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:    
        # invarianrt: Stack stores a decreasing sequence of numbers whose next greater element is not yet found.

        # MEthod 2 TC O(n) SC O(n)

        # find global next > of all element in num2
        # create dict 0f  num2
        nxt_great = {}
        stack=[]
        # 4 3 2
        # 1 2 3 1
        for n in nums2:
            while stack and n > stack[-1]:
                prev = stack.pop()
                nxt_great[prev]= n

            stack.append(n)
    
        return [nxt_great.get(n,-1) for n in nums1]
       
# SC = O(n) due to stack & dict



        # MEthod 1 no t optimized     
        res = [-1] * len(nums1)
        for i, n1 in enumerate(nums1):
            search_idx = -1
            for j,n2 in enumerate(nums2):
                if n1 == n2:
                    search_idx = j
                
                elif search_idx != -1 and j > search_idx and n2 > n1:
                        res[i]= n2
                        break

        return res
        # TC = O(n²).
        # SC = O(n) due to stack
