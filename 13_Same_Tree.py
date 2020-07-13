# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        return self.helper(p, q)
    
    def helper(self, tree1, tree2):
        if (tree1 and not tree2) or (not tree1 and tree2):
            return False
        if not tree1 and not tree2:
            return True
        if tree1.val != tree2.val:
            return False
        return self.helper(tree1.left, tree2.left) and self.helper(tree1.right, tree2.right)