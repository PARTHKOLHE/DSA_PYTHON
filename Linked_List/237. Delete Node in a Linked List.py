from typing import Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def deleteNode(self, node):
        curr = node
        
        temp = node
        curr.val = curr.next.val
        curr.next.val = temp
        
        curr.next = curr.next.next
        
            
        
        
        
        