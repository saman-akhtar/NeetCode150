class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """

        # CAN negative no?
        # can 0 be there ?

        # since cant have temp space, make use of
        # extra space in nums1
        # arrange form hieght to lowest
        k =  m + n - 1
        i = m -1
        j = n -1
        while  i > -1 and j > -1:
            if(nums1[i] > nums2[j]):
                nums1[k]= nums1[i]
                i -=1
            else:
                nums1[k]= nums2[j]
                j -=1
            k -= 1
        # edge cae

        while j > -1:
            nums1[k] = nums2[j]
            k, j = k-1, j-1

           
        return nums1


                
           

        