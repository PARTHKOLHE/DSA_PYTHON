from typing import Optional
import math
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head.next is None:
           return head
        curr = head
       
        while curr.next:
           gcd_val = math.gcd(curr.val,curr.next.val)
           
           new_node = ListNode(gcd_val)
           
           new_node.next = curr.next
           curr.next = new_node
           
           curr = new_node.next
        
        return head
           
       
        