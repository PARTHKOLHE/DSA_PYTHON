# Definition of singly linked list:
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def findLengthOfLoop(self, head):
        fast = head
        slow = head
        
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            
            if slow == fast:
                count = 1
                curr = slow.next
                while curr != slow:
                    count += 1
                    curr = curr.next
                return count
                
        return 0
        