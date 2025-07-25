from typing import Optional
# Definition for singly-linked list.


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy_node = ListNode(0)
        dummy = dummy_node

        while list1 and list2:
            if list1.val < list2.val:
                dummy.next = list1
                list1 = list1.next

            else:
                dummy.next = list2
                list2 = list2.next

            dummy = dummy.next
        if list1:
            dummy.next = list1
        else:
            dummy.next = list2
        return dummy_node.next
