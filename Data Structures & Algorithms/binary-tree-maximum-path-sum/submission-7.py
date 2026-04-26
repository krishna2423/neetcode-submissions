# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        max_sum = root.val
        def dfs(root): # checks the paths between root and every node in the tree
            if not root:
                return 0
            else:
                l = max(dfs(root.left), 0)
                r = max(dfs(root.right), 0)
                nonlocal max_sum
                cur_sum = root.val + l + r
                if cur_sum > max_sum:
                    max_sum = cur_sum 
                return root.val + max(l, r)
        dfs(root)
        return max_sum
        
            
        