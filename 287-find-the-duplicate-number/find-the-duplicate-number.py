class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        map1 = {}
        for i in range(len(nums)):
            map1[nums[i]] =  map1.get(nums[i], 0) + 1
            if map1[nums[i]] > 1:
                return nums[i]
        #     cur = cur.next


        # while cur:
        #     map1[cur.val] = map1.get(cur.val, 0) + 1
        #     if map1[cur.val] > 1:
        #         return cur.val
        #     cur = cur.next
        