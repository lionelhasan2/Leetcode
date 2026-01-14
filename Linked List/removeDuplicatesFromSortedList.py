class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummyNode = ListNode()
        dummyNode.next = head
        prev = dummyNode
        curr = head
        
        while curr:
            # Skip all nodes with the same value
            while curr.next and curr.val == curr.next.val:
                curr = curr.next
            # If we skipped any duplicates, remove them but keep the first one
            if curr != prev.next:
                prev.next = curr
            prev = curr
            curr = curr.next
        
        return dummyNode.next