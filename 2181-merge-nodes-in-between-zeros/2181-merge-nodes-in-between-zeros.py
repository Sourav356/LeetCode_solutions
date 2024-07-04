# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)  # Dummy node to simplify result list construction
        current = dummy
        sum_value = 0
        node = head.next  # Skip the initial 0
        
        while node:
            if node.val == 0:
                if sum_value != 0:
                    current.next = ListNode(sum_value)
                    current = current.next
                    sum_value = 0
            else:
                sum_value += node.val
            node = node.next
        
        return dummy.next
        
        