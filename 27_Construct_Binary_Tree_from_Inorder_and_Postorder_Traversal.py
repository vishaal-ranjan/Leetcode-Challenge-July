# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        # Inorder --> Left, Node, Right
        # Postorder --> Left, Right, Node
        
        if not inorder or not postorder:
            return None
        
        val = postorder.pop()
        root = TreeNode(val)
        i = inorder.index(val)
        root.left = self.buildTree(inorder[:i], postorder[:i])
        root.right = self.buildTree(inorder[i+1:], postorder[i:])
        return root