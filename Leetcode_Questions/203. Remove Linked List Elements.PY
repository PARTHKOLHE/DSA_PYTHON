from typing import Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
            new_node = ListNode(0)
            back = new_node
            back.next = head
            
            while head:
                if head.val == val:
                    back.next = head.next
                    head = head.next 
                else:
                    head = head.next   
                    back = back.next
                
            return new_node.next 
            