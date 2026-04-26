# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        diameter = 0
        def dfs(node):
            if node is None:
                return 0
            else:
                l = 1 + dfs(node.left)
                r = 1 + dfs(node.right)
                nonlocal diameter 
                diameter = max(diameter, l + r - 2)
                return max(l, r)
        dfs(root)
        return diameter