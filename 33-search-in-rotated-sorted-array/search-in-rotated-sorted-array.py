class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l,h = 0, len(nums)-1
        while l <=h:
            mid = (l + h)//2
            if ( nums[mid] == target):
                return mid
            # determin which is sorted
            if (nums[l] <= nums[mid]):
                if ( nums[l] <= target < nums[mid]):
                    h = mid -1
                else:
                    l = mid + 1
            else:
                # Target lies in the sorted right part
                if ( nums[mid] < target <= nums[h]):
                    l = mid +1
                else:
                    h = mid -1
        return -1
# O (Logn )
# O(1)
        