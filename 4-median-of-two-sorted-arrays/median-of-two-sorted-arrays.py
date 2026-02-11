class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:  
        n = len(nums1)
        m = len(nums2)
        is_even = True if (n + m ) % 2== 0 else False
        ind=(n+m)//2
        target = [ind]
        
        if is_even:
            target = [(ind - 1),ind]
            
        i = 0
        j = 0
        res = []
        len_r =-1
        median = 0
    
        while len_r < ind :
            if i < n and ((j >=m) or nums1[i] < nums2[j]) :
                
                res.append(nums1[i])
                i += 1
                len_r += 1
            else:
                if (j <m):
                    res.append(nums2[j])
                    j += 1
                    len_r += 1
            if len_r == target[0]:
                median = res[len_r]
            if is_even and len_r == target[1]:
                s =res[target[0]] +res[target[1]]
    
                median = s /2
                
                
        return median


        
