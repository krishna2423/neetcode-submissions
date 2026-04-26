# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        def minValueNode(root):
            curr = root
            while curr and curr.left:
                curr = curr.left
            return curr
        def dfs(root, val):
            if not root:
                return None
            
            if val > root.val:
                root.right = dfs(root.right, val)
            elif val < root.val:
                root.left = dfs(root.left, val)
            else:
                if not root.left:
                    return root.right
                elif not root.right:
                    return root.left
                else:
                    minNode = minValueNode(root.right)
                    root.val = minNode.val
                    root.right = dfs(root.right, minNode.val)
            return root
        return dfs(root, val)
