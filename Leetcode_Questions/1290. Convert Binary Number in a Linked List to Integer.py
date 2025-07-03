from typing import Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def getDecimalValue(self, head: Optional[ListNode]) -> int:   
        if head is None:
            return None
        temp = head
        store = temp.val
        
        while head.next:
            store = (store*2) + temp.val
            temp =temp.next
        
        return store 
            
        
        