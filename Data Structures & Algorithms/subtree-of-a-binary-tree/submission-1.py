# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def sameTree(node1, node2):
            if not node1 and not node2:
                return True
            elif not node1:
                return False
            elif not node2:
                return False
            elif node1.val != node2.val:
                return False
            else: 
                return sameTree(node1.right, node2.right) and sameTree(node1.left, node2.left)
        def dfs(node1, node2):
            if not node1:
                return False
            elif node1.val == node2.val:
                same = sameTree(node1, node2)
                if same:
                    return same
            return dfs(node1.left, node2) or dfs(node1.right, node2)
        return dfs(root, subRoot)