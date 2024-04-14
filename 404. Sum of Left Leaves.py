# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorder(self, root, sum):
        if root:
            self.inorder(root.left, sum)
            if root.left:
                if not root.left.left and not root.left.right:
                    sum[0] += root.left.val
            self.inorder(root.right, sum)
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        sum = [0]
        self.inorder(root, sum)
        return sum[0]
