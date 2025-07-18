from typing import Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        fast = head
        slow = head
        temp = head
        
        
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            
        before = None
        while slow:
            after = slow.next
            slow.next = before
            before = slow
            slow = after
        sum_val1 = 0
        while before:
            sum_val2 = temp.val + before.val
            if sum_val2 > sum_val1:
                sum_val1 = sum_val2
        return sum_val1
            
            
        
        