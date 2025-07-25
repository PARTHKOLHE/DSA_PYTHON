class MinHeap:
    def __init__(self):
        self.heap = []

    def _left_child(self, index):
        return 2 * index + 1

    def _right_child(self, index):
        return 2 * index + 2

    def _parent(self, index):
        return (index - 1) // 2

    def _swap(self, index1, index2):
        self.heap[index1], self.heap[index2] = self.heap[index2], self.heap[index1]

    def insert(self, value):
        self.heap.append(value)
        current = len(self.heap) - 1

        while current > 0 and self.heap[current] < self.heap[self._parent(current)]:
            self._swap(current, self._parent(current))
            current = self._parent(current)

    def _sink_down(self, index):
        curr = index

        while True:
            left_index = self._left_child(curr)
            right_index = self._right_child(curr)

            if (left_index < len(self.heap) and
                    self.heap[curr] > self.heap[left_index]):
                curr = left_index
            
            if (right_index < len(self.heap) and
                    self.heap[curr] > self.heap[right_index]):
                curr = right_index
                
            if curr != index:
                self._swap(curr,index)
                index = curr
            else:
                return
                    

    def remove(self):
        if len(self.heap) == 0:
            return None

        if len(self.heap) == 1:
            return self.heap.pop()

        min_value = self.heap[0]
        self.heap[0] = self.heap.pop()
        self._sink_down(0)

        return min_value


myheap = MinHeap()
myheap.insert(12)
myheap.insert(10)
myheap.insert(8)
myheap.insert(6)
myheap.insert(4)
myheap.insert(2)

print(myheap.heap)  # [2, 6, 4, 12, 8, 10]

removed = myheap.remove()
# Removed: 2, Heap: [4, 6, 10, 12, 8]
print(f'Removed: {removed}, Heap: {myheap.heap}')

removed = myheap.remove()
# Removed: 4, Heap: [6, 8, 10, 12]
print(f'Removed: {removed}, Heap: {myheap.heap}')

removed = myheap.remove()
# Removed: 6, Heap: [8, 12, 10]
print(f'Removed: {removed}, Heap: {myheap.heap}')


"""
    EXPECTED OUTPUT:
    ----------------
    [2, 6, 4, 12, 8, 10]
    Removed: 2, Heap: [4, 6, 10, 12, 8]
    Removed: 4, Heap: [6, 8, 10, 12]
    Removed: 6, Heap: [8, 12, 10]

"""
