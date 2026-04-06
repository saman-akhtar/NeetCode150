# Description
# Given a nested list of integers, return the sum of all integers in the list weighted by their depth.

# Each element is either an integer, or a list -- whose elements may also be integers or other lists.

# Different from the previous question where weight is increasing from root to leaf, now the weight is defined from bottom up. i.e., the leaf level integers have weight 1, and the root level integers have the largest weight."""
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation

# class NestedInteger(object):
#     def isInteger(self):
#         # @return {boolean} True if this NestedInteger holds a single integer,
#         # rather than a nested list.

#     def getInteger(self):
#         # @return {int} the single integer that this NestedInteger holds,
#         # if it holds a single integer
#         # Return None if this NestedInteger holds a nested list

#     def getList(self):
#         # @return {NestedInteger[]} the nested list that this NestedInteger holds,
#         # if it holds a nested list
#         # Return None if this NestedInteger holds a single integer
# """
# Example
# Example 1:

# Input: nestedList = [[1,1],2,[1,1]]
# Output: 8
# Explanation:
# four 1's at depth 1, one 2 at depth 2
# Example 2:

# Input: nestedList = [1,[4,[6]]]
# Output: 17
# Explanation:
# one 1 at depth 3, one 4 at depth 2, and one 6 at depth 1
# 1*3 + 4*2 + 6*1 = 17


class Solution:
    """
    @param nestedList: a list of NestedInteger
    @return: the sum
    """
    def depthSumInverse(self, nestedList):
        
        def maxdepth(nest, current_depth):
            max_d = current_depth
            for item in nest:
                if  not item.isInteger():
                   max_d = max(max_d, maxdepth(item.getList(), current_depth + 1))
            return max_d
        max_depth = maxdepth(nestedList, 1)
        def dfs(elm, depth):

            cur_sum = 0
            for i in range(len(elm)):
                if elm[i].isInteger():
                    cur_sum+= elm[i].getInteger() * (max_depth - depth +1)
                else:
                    cur_sum += dfs(elm[i].getList(), depth +1)
            return cur_sum
        total = dfs(nestedList, 1)
        return total

# TC O(N) => in two pass
# SC O(D)

        # WEIGHT 1
        def dfs(elm, depth):

            cur_sum = 0
            for i in range(len(elm)):
                if elm[i].isInteger():
                    cur_sum+= elm[i].getInteger()* depth
                else:
                    cur_sum += dfs(elm[i].getList(), depth +1)
            return cur_sum
        print("whi,",nestedList)
        total = dfs(nestedList, 1)
        return total

        # TC O(N) => each elemnet visited oly once
        # SC O(D) +> depth can be each item ie list isnide another list =>0(N)

        # Write your code here.
