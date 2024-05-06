# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head :
            return head
        self.maxvalue = float('-inf')
        
        def traversal(node):
            if not node: 
                return None
            
            node.next = traversal(node.next)
            self.maxvalue = max(self.maxvalue, node.val)
            
            if  self.maxvalue > node.val:
                return node.next
            return node
        
        return traversal(head)
       