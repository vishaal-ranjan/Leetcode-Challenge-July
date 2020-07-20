# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        tmp = []
        while head:
            if head.val != val:
                tmp.append(head.val)
            head = head.next
                
        res = res1 = ListNode(-1)
        
        for node in tmp:
            res1.next = ListNode(node)
            res1 = res1.next
        
        return res.next