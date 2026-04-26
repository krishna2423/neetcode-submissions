# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        def dfs(node, currSum):
            if not node:
                return False
            if not node.right and not node.left:
                if currSum + node.val == targetSum:
                    return True
                else:
                    return False
            if dfs(node.left, currSum + node.val):
                return True
            if dfs(node.right, currSum + node.val):
                return True
            return False
        return dfs(root, 0)