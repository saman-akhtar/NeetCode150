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
        
        len_r =-1
        prev = 0
        cur = 0
    
        while len_r < ind :
            prev = cur
            if i < n and ((j >=m) or nums1[i] < nums2[j]) :
                
                cur = nums1[i]
                i += 1
                
            else:
                    cur = nums2[j]
                    j += 1
            len_r += 1
      
        if is_even :
            return (prev + cur)/2
        else:
            return cur
            
            
#. TC O(n + M)
# SC O(1)


        
