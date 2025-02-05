class Solution:
    def longestSubstring(self, s: str, k: int) -> int:

        # claryfing sorted ?
        # substri : contiguous ?
        # logic if any freq of ch < k , that wont be included in part of substring
        # so start new substring
        
        # l = 0 
        # # The Counter(s) operation takes O(N).

        # chMap = Counter(s)
        # maxLen = 0
        # valid = True
        # # O(N)
        # for r in range(len(s)):
        #     # In the worst case, each recursive call operates on roughly half the original input (T(N) ≈ 2T(N/2) + O(N)), leading to O(N log N).
        #     if chMap[s[r]] > 0 and chMap[s[r]] < k:
        #         substring = s[l:r]
        #         maxLen = max(maxLen, self.longestSubstring(substring, k))
        #         valid = False
        #         l = r + 1
        # if (valid):
        #     return len(s)
        # else:
        #     return max(maxLen,self.longestSubstring(s[l:], k))

        # def helper(left, right):
        #     if right - left < k:
        #         return 0
            
        #     chMap = Counter(s[left:right])
        #     for mid in range(left, right):
        #         if chMap[s[mid]] > 0 and chMap[s[mid]] < k:
        #             return max(helper(left, mid), helper(mid + 1, right))
                    
        #     return right - left
        
        # return helper(0, len(s))
#         Time Complexity	O(N log N)	O(N log N)
# Space Complexity	O(N) (due to slicing)	O(N) (due to Counter, but no slicing overhead)

        maxLen = 0
        # Try to find valid substrings with exactly `uniqueTarget` unique characters
        for uniqueTarget in range(1, 27):  # Since there are at most 26 letters
            wordMap = {}
            l = r = 0
            have = 0  # Count of characters occurring at least `k` times
            need = 0  # Count of unique characters in the window
            
            while r < len(s):
                # Expand the window
                if s[r] in wordMap:
                    wordMap[s[r]] += 1
                else:
                    wordMap[s[r]] = 1
                    need += 1  # New unique character added
                
                if wordMap[s[r]] == k:
                    have += 1  # This character now meets the k requirement
                
                r += 1
                
                # Shrink the window if there are too many unique characters
                while need > uniqueTarget:
                    if wordMap[s[l]] == k:
                        have -= 1  # This character no longer meets the k requirement
                    wordMap[s[l]] -= 1
                    if wordMap[s[l]] == 0:
                        del wordMap[s[l]]
                        need -= 1  # Remove a unique character
                    l += 1
                
                # Update max length if all `need` characters meet the `k` condition
                if have == need:
                    maxLen = max(maxLen, r - l)
        
        return maxLen
