# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        
        #For this solution the Time Com = O(n + logn + n) and space com = O(n)
        
#         list_s = []
#         temp = head
        
#         while temp != None:
#             list_s.append(temp.val)
#             temp = temp.next
            
#         list_s.sort()
#         i = 0
#         temp = head
#         while temp != None:
#             temp.val = list_s[i]
#             i+=1
#             temp= temp.next
            
#         return head



# So in the previous code we use extra space where the interviewer are not happy so let's slove that using Merge sort

        if not head or not head.next:
            return head
        
        # Find the middle of the list
        mid = self.findMiddle(head)
        
        # Split the list into two halves
        left_half = head
        right_half = mid.next
        mid.next = None
        
        # Recursively sort each half
        left_sorted = self.sortList(left_half)
        right_sorted = self.sortList(right_half)
        
        # Merge the sorted halves
        return self.merge(left_sorted, right_sorted)
    
    def findMiddle(self, head):
        slow = head
        fast = head.next
        
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        return slow
    
    def merge(self, left, right):
        dummy = ListNode()
        current = dummy
        
        # Merge the two sorted lists
        while left and right:
            if left.val < right.val:
                current.next = left
                left = left.next
            else:
                current.next = right
                right = right.next
            current = current.next
        
        # Append any remaining nodes
        if left:
            current.next = left
        if right:
            current.next = right
        
        return dummy.next


        
        
