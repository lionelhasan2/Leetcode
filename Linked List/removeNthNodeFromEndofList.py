# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummyNode = ListNode()
        dummyNode.next = head
        prev = dummyNode
        curr = head
        curr_ahead = head
        # Advance curr_head to n spots ahead of curr
        for i in range(n):
            curr_ahead = curr_ahead.next
        
        # Advance curr_ahead, curr, and prev until curr_ahead is None
        while curr_ahead:
            curr_ahead = curr_ahead.next
            curr = curr.next
            prev = prev.next
        
        # Point prev to curr.next
        if curr: 
            prev.next = curr.next

        return dummyNode.next
        