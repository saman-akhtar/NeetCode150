class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        # APPROCH 1 :
#         Merging Backward Strategy:
# Recognize that some problems are best solved from the end of the array rather than the beginning. This is a common technique to avoid additional space

        # CAN negative no?
        # can 0 be there ?

        # since cant have temp space, make use of
        # extra space in nums1
        # arrange form hieght to lowest
        i = m -1
        j = n - 1
        start = m + n -1
        while j >= 0:
            # edge case , check if i goes out of bound, then no comparision for i needed
            if i < 0 or nums2[j] >= nums1[i]:
                nums1[start] = nums2[j]
                j -= 1
            else:
                nums1[start] = nums1[i]
                i -= 1
        start -=1

    # TC O(N)
    # SC O(1)


# ARPPROACH 2
        if m < 1 and n < 1:
            return 
        if m < 1:
            nums1[:]= nums2
            # CANT DO  nums1 = nums2, as The line nums1 = nums2 only reassigns the local variable nums1 to point to nums2 and does not modify the original list in-plac
            return 
        if n < 1:
            return
        total = len(nums1)
        # 1 2 3 4 5 0 0.  7 -5 = 2
        diff = total -m
        nums1[diff:] = nums1[0:m] # SC  (because of the temporary copy generated during slicing)
        i = diff
        j = 0
        start = 0
        while i < total:
            if j < n and nums2[j] < nums1[i]:
                nums1[start]= nums2[j]
                j += 1
            else:
                nums1[start]= nums1[i]
                i += 1
            start += 1
        while j < n:
            nums1[start]= nums2[j]
            j += 1
            start += 1
            # cond for n
        # 1 2 3
                            # i
        # [1, 2, 3, 1, 2, 3]
            #  j
        # [2,5,6]
        # [1, 2, 2, 3]
        # start  3


        # TC O(M + N)
        # SC O(m) due to slicing

                
           

        