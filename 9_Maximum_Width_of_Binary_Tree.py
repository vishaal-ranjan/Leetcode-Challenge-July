# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution:
    def widthOfBinaryTree(self, root: TreeNode) -> int:
        if not root:
            return 0
        maxwidth = 0
        q = deque()
        q.append((root, 0))
        
        while q:
            level_length = len(q)
            _, level_head_index = q[0]
            
            for _ in range(level_length):
                node, col_index = q.popleft()
                
                if node.left:
                    q.append((node.left, 2 * col_index))
                if node.right:
                    q.append((node.right, 2 * col_index + 1))

            maxwidth = max(maxwidth, col_index - level_head_index + 1)
            
        return maxwidth