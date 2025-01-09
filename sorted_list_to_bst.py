"""
Thought process:
1. We need to create a binary search tree from a sorted list.
2. We can use the middle element of the list as the root of the tree.
3. We can then recursively build the left and right subtrees from the left and right halves of the list.
using the idea of binary search, we can find the middle element of the list and use it as the root of the tree. 
and from then use a recursive function to populate the left and right side of the tree
"""
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def sortedArrayToBST(self, nums):
        def helper(l,r):
            if l >r:return
            n = l+r
            mid = n//2

            node = TreeNode(nums[mid])
            node.left = helper(l, mid-1)
            node.right = helper(mid+1, r)
            return node
        return helper(0, len(nums)-1)


        