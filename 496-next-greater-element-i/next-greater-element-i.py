class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:         
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
        