# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        
        q = deque()
        q.append(root)
        sol = []
        cnt = 0
        
        while q:
            currentlevel = []
            for i in range(len(q)):
                curr = q.popleft()
                currentlevel.append(curr.val)
                if curr.left:
                    q.append(curr.left)
                if curr.right:
                    q.append(curr.right)
            if cnt%2 == 0:
                sol.append(currentlevel)
            else:
                sol.append(currentlevel[::-1])
            cnt += 1
            
        return sol