from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        current = head   
        while current is not None:
            runner = current
            while runner.next is not None:
                if current.val == runner.next.val:
                    runner.next = runner.next.next

                else:
                    runner = runner.next

            current = current.next
        return head