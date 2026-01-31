# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        prev1, curr1 = None,  l1 
        curr2 = l2
    
        carry = 0 
        while curr1 or curr2 or carry != 0:

            val1 = curr1.val if curr1 else 0 
            val2 = curr2.val if curr2 else 0 
            sumNode = val1 + val2 + carry
            carry = (sumNode//10)

            if curr1:
                curr1.val = sumNode % 10 
                prev1 = curr1 
                curr1 = curr1.next
            else:
                newNode = ListNode(val = sumNode % 10 ) 
                prev1.next = newNode
                prev1 = prev1.next
            curr2 = curr2.next if curr2 else None 
        return l1


