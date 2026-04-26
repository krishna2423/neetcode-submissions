# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        def findAncestors(node, target, ancestors):
            if not node:
                return None
            ancestors.append(node)
            if node.val == target:
                return ancestors
            elif node.val < target:
                return findAncestors(node.right, target, ancestors)
            else:
                return findAncestors(node.left, target, ancestors)
        p_ancestors = findAncestors(root, p.val, [])
        q_ancestors = findAncestors(root, q.val, [])

        intersection = [x for x in p_ancestors if x in q_ancestors]
        return intersection[-1]