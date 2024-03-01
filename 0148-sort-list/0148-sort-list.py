# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        list_s = []
        temp = head
        
        while temp != None:
            list_s.append(temp.val)
            temp = temp.next
            
        list_s.sort()
        i = 0
        temp = head
        while temp != None:
            temp.val = list_s[i]
            i+=1
            temp= temp.next
            
        return head