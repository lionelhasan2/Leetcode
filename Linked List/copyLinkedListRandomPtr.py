class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        dummyNode, curr = Node(0), head
        nodeMap = {}
        origRanMap = {}
        i = 0
        prevNew = dummyNode
        
        # First pass: create all nodes and map original nodes to indices
        while curr:
            newNode = Node(curr.val)
            prevNew.next = newNode
            origRanMap[curr] = i                
            nodeMap[i] = newNode
            prevNew = newNode
            curr = curr.next 
            i += 1
        
        # Second pass: set random pointers
        curr = head
        curr_new = dummyNode.next 
        while curr:
            if curr.random:
                random_index = origRanMap[curr.random]
                curr_new.random = nodeMap[random_index]
            curr = curr.next
            curr_new = curr_new.next
        
        return dummyNode.next