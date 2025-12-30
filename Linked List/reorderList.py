# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if not head:
            return
        node_list = []
        curr = head
        while curr:
            node_list.append(curr)
            curr = curr.next
        
        i = 0
        j = len(node_list) - 1
        while i<j:
            # Point to the end
            node_list[i].next = node_list[j]
            i += 1 
            if i>=j:
                break
            node_list[j].next = node_list[i]
            j-=1

        node_list[i].next = None
