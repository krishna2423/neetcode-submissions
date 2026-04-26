# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def validate(node, lower, upper):
            if not node:
                return True
            else:
                if node.val <= lower or node.val >= upper:
                    return False
                else:
                    return validate(node.left, lower, node.val) and validate(node.right, node.val, upper)
        if not root:
            return True
        else:
            return validate(root.left, float('-inf'), root.val) and validate(root.right, root.val, float('inf'))

        