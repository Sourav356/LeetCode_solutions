# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def doubleIt(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        curr = head
        while curr:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node
        
        # Double the linked list while considering carry
        carry = 0
        curr = prev
        while curr:
            total = curr.val * 2 + carry
            curr.val = total % 10
            carry = total // 10
            if not curr.next and carry:
                curr.next = ListNode(carry)
                break
            curr = curr.next
        
        # Reverse the linked list again
        new_head = None
        while prev:
            next_node = prev.next
            prev.next = new_head
            new_head = prev
            prev = next_node
        
        return new_head
        