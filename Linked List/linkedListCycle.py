class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        nodeSet = set()
        node = head
        while node:
            if node in nodeSet:
                return True
            else:
                nodeSet.add(node)
                node = node.next
        return False