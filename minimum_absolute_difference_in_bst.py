"""
Thought process:

Initially thought process was to use a bfs, since we were traversing in the end, but i realized
i did not understand the question by doing that, then I realized it was a bst and in a bst,
the left child is always less than the parent and the right child is always greater than the parent.
This led to my solution, 
1. Inorder traversal of BST will give us a sorted list
2. Find the minimum absolute difference between consecutive elements in the sorted list
"""
class Solution:
    def getMinimumDifference(self, root):
        first = float(inf)
        res = []

        def inorder(root):
            if root is None:
                return
            inorder(root.left)
            res.append(root.val)
            inorder(root.right)
        inorder(root)
        
        for i in range(1, len(res)):
            first = min(first, (res[i]-res[i-1]))
        return first
