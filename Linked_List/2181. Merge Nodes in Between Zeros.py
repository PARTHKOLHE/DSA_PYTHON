from typing import Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head.next is None:
            return None
        curr = head.next
        sum_val = 0
        dummy_node = ListNode(0)
        dummy = dummy_node
        while curr:
            while curr.val != 0:
                sum_val = curr.val + sum_val
                curr = curr.next
            
            new_node = ListNode(sum_val)
            dummy.next = new_node
            dummy = dummy.next
            sum_val = 0
            curr = curr.next
        return dummy_node.next
            
            