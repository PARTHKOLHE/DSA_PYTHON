from typing import Optional
# Definition for singly-linked list.


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        temp1 = l1
        temp2 = l2

        dummy_node = ListNode(0)
        curr = dummy_node
        carry = 0

        while temp1 or temp2:
            sum = carry
            if temp1:
                sum = sum + temp1.val
                temp1 = temp1.next
            if temp2:
                sum = sum + temp2.val
                temp2 = temp2.next

            new_node = ListNode(sum % 10)
            carry = sum // 10

            curr.next = new_node
            curr = curr.next

        if carry > 0:
            curr.next = ListNode(carry)

        return dummy_node.next
