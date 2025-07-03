from typing import Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        if not head or not head.next:
            return True    
        fast = head
        slow = head
        
        
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        
        prev = None
        while slow:
            nn = slow.next
            slow.next = prev
            prev = slow
            slow = nn
            
        first = head
        last = prev
        while last:
            if first.val == last.val:
                first = first.next
                last = last.next
                
            else:
                return False
        return True
        