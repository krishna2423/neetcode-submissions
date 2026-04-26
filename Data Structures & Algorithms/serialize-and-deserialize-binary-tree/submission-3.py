# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque 
"""class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        # take the preorder traversal
        result = ""
        preorder = deque([])
        inorder = deque([])
        def dfs1(root):
            if not root:
                return
            preorder.append(root.val)
            dfs1(root.left)
            dfs1(root.right)
        
        def dfs2(root):
            if not root:
                return
            dfs2(root.left)
            inorder.append(root.val)
            dfs2(root.right)
        dfs1(root)
        dfs2(root)
        while preorder:
            result = result + str(preorder[0])
            result += ','
            preorder.popleft()
        result += '|'
        while inorder:
            result = result + str(inorder[0])
            result += ','
            inorder.popleft()
        return result
        



        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        def buildTree(preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
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
        
        i = 0 
        # find the index where the bar is at
        while data[i] != '|':
            i += 1
        pre = data[:i]
        in_ = data[i + 1:]
        preorder = pre.split(',')
        inorder = in_.split(',')
        inorder.pop()
        preorder.pop()
        preorder = [int(preorder[i]) for i in range(len(preorder))]
        inorder = [int(inorder[i]) for i in range(len(inorder))]

        return buildTree(preorder, inorder)
"""
class Codec:

    def serialize(self, root):
        vals = []

        def dfs(node):
            if not node:
                vals.append("N")
                return
            vals.append(str(node.val))
            dfs(node.left)
            dfs(node.right)

        dfs(root)
        return ",".join(vals)

    def deserialize(self, data):
        vals = deque(data.split(","))

        def dfs():
            val = vals.popleft()
            if val == "N":
                return None

            node = TreeNode(int(val))
            node.left = dfs()
            node.right = dfs()
            return node

        return dfs()