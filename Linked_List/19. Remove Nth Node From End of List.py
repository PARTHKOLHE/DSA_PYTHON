from typing import Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if head == None:
            return head
        
        fast = head
        new_node = ListNode(0)
        slow = new_node
        slow.next = head
        
        while n != 0:
            fast = fast.next
            n -= 1
            
        while fast:
            fast = fast.next
            slow = slow.next
        
        slow.next = slow.next.next
        
        return new_node.next
        
        
        