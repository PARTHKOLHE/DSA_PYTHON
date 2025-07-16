from typing import Optional
# Definition of singly linked list:


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def sortList(self, head):
        # Brute Force:
        # temp1 = head
        # temp2 = head
        # count0 = 0
        # count1 = 0
        # count2 = 0

        # while temp1:
        #     if temp1.val == 0:
        #         count0 += 1
        #     elif temp1.val == 1:
        #         count1 += 1
        #     elif temp1.val == 2:
        #         count2 += 1
        #     temp1 = temp1.next
        # while temp2:
        #     if count0 > 0:
        #         temp2.val = 0
        #         count0 -= 1
        #     elif count1 > 0:
        #         temp2.val = 1
        #         count1 -= 1
        #     elif count2 > 0:
        #         temp2.val = 2
        #         count2 -= 1
        #     temp2 = temp2.next
        # return head

        # Optimal:
        if head == None or head.next == None:
            return head
        temp = head
        new_node0 = ListNode(0)
        zero = new_node0
        new_node1 = ListNode(0)
        one = new_node1
        new_node2 = ListNode(0)
        two = new_node2
        
        while temp:
            if temp.val == 0:
                zero.next = temp
                zero = temp
            elif temp.val == 1:
                one.next = temp
                one = temp
            elif temp.val == 2:
                two.next = temp
                two = temp
            
            temp = temp.next 
                
        if new_node1.next:
            zero.next = new_node1.next
        else:
            zero.next = new_node2.next
            
        one.next = new_node2.next
        two.next = None
        return new_node0.next