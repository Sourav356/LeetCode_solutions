# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        dummy.next = head
        prev = dummy
        current = head
        
        while current and current.next:
            if current.val == current.next.val:
                while current.next and current.next.val == current.val:
                    current = current.next
                prev.next = current.next
            else:
                prev = prev.next
            current = current.next
            
        return dummy.next
                
                