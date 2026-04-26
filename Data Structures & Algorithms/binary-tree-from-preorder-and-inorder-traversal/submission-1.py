# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        indices = {}
        for i, x in enumerate(inorder):
            indices[x] = i
        
        preorder = deque(preorder)
        
        def dfs(inorder, l, r):
            if l > r or not preorder:
                return None
            x = preorder.popleft()
            root = TreeNode(x)
            idx = indices[x]
            root.left = dfs(inorder, l, idx - 1)
            root.right = dfs(inorder, idx + 1, r)
            return root
        
        return dfs(inorder, 0, len(inorder) - 1)