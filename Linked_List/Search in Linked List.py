class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class Solution:
    def searchKey(self, head, key):
        current = head
        while current:
            if current.value == key:
                return True
            current = current.next
        return False