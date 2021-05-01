# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    nTree = TreeNode()

    def mergeTrees(self, root1: TreeNode, root2: TreeNode) -> TreeNode:
        Solution.newTree(root1, root2)

        if not root1: root1 = root2

        return root1

    def newTree(t1, t2):

        if not t1 or not t2:
            return

        t1.val += t2.val

        if t1.left and t2.left:
            Solution.newTree(t1.left, t2.left)
        if not t1.left and t2.left:
            t1.left = t2.left

        if t1.right and t2.right:
            Solution.newTree(t1.right, t2.right)
        if not t1.right and t2.right:
            t1.right = t2.right









