from typing import Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> 0:  
        slow = list1
        for _ in range(a - 1):
            slow = slow.next
        
        curr = slow.next
        for _ in range(b - a + 1):
            curr = curr.next
        
        slow.next = list1
        
        tail = list2
        while tail.next:
            tail = tail.next
            
        tail.next = curr
        return list1
            
        
        
                   
            
        