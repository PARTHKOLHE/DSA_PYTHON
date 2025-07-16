class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addOne(self, head):
        prev = None
        curr = head
        
        while curr:
            after = curr.next
            curr.next = prev
            prev = curr
            curr = after
            
        curr = prev
        carry = 1
        last = None
        
        while curr:
            sum_val = carry + curr.val
            carry = sum_val // 10
            curr.val = sum_val % 10
            last = curr
            curr = curr.next
            
        if carry:
            last.next = ListNode(carry)

        prev2 = None
        curr2 = prev
        
        while curr2:
            after2 = curr2.next
            curr2.next = prev2
            prev2 = curr2
            curr2 = after2
        return prev2       
            
            
        