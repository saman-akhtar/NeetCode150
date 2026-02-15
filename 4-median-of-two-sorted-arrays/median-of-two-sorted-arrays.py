class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:  
        A, B = nums1, nums2
        if len(A) > len(B):
            A, B = B, A

        n = len(A)
        m = len(B)

        total = n + m
        half = total // 2
        even = (total % 2 == 0)

        l = -1
        r = n - 1

        while True:
            i = (l + r) // 2
            j = half - i - 2

            Aleft  = A[i]   if i >= 0 else float("-inf")
            Aright = A[i+1] if i+1 < n else float("inf")
            Bleft  = B[j]   if j >= 0 else float("-inf")
            Bright = B[j+1] if j+1 < m else float("inf")

            if Aleft <= Bright and Bleft <= Aright:
                if even:
                    return (max(Aleft, Bleft) + min(Aright, Bright)) / 2
                else:
                    return min(Aright, Bright)

            elif Aleft > Bright:
                r = i - 1
            else:
                l = i + 1

            


                








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


        
