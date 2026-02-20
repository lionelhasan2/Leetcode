# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        
        nodes = set()
        currA = headA
        currB = headB

        while currA or currB:
            if currA:
                if currA in nodes:
                    return currA
                nodes.add(currA)
                currA = currA.next

            if currB:
                if currB in nodes:
                    return currB
                nodes.add(currB)
                currB = currB.next
      
        return None