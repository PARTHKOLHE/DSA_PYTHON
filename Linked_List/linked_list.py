class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next

    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            return new_node

        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1
        return True

    def pop(self):
        if self.head is None:
            return None

        if self.length == 1:
            popped = self.head
            self.length = 0
            self.head = None
            self.tail = None
            return popped

        else:
            temp = self.head
            pre = self.head
            while temp.next is not None:
                pre = temp
                temp = temp.next
        self.tail = pre
        self.tail.next = None
        self.length -= 1
        return temp

    def prepend(self, value):
        new_node = Node(value)
        if self.tail is None:
            self.head = new_node
            self.tail = new_node
            self.length += 1
            return new_node

        else:
            temp = self.head
            new_node.next = temp
            self.head = new_node
            self.length += 1
            return True

    def pop_first(self):
        if self.head is None:
            return None

        if self.length == 1:
            popped = self.head
            self.head = None
            self.tail = None
            self.length = 0
            return popped
        else:
            temp = self.head
            self.head= self.head.next            
            self.length -= 1
            return temp


my_linked_list = LinkedList(4)
my_linked_list.append(5)
my_linked_list.pop()
my_linked_list.prepend(5)
my_linked_list.pop_first()

# my_linked_list.pop()
print('Head:', my_linked_list.head.value)
print('Tail:', my_linked_list.tail.value)
print('Length:', my_linked_list.length)


print("\nMy_linked_list")
my_linked_list.print_list()
