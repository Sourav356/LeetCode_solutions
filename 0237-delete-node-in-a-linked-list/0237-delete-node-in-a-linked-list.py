# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def __init__(self):
        self.head = None
        
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
#         if self.head == node:
#             self.head = self.head.next
#             return
        
#         temp = self.head
#         while temp.next is not None and temp.next != node:
#             temp = temp.next
#         if temp is not None and temp.next is not None:
#             temp.next = temp.next.next
            
#         else:
#             return
            
        node.val = node.next.val
        node.next = node.next.next
            
        
        