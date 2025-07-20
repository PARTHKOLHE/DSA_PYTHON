class Solution:

    def initializeHeap(self):
        self.heap = []

    def _left_child(self, index):
        return 2 * index + 1

    def _right_child(self, index):
        return 2 * index + 2

    def _parent(self, index):
        return (index - 1) // 2

    def _swap(self, i, j):
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]

    def insert(self, key):
        self.heap.append(key)
        curr = len(self.heap) - 1
        while curr > 0 and self.heap[curr] > self.heap[self._parent(curr)]:
            self._swap(curr, self._parent(curr))
            curr = self._parent(curr)

    def changeKey(self, index, new_val):
        old_val = self.heap[index]
        self.heap[index] = new_val
        if new_val > old_val:
            # Bubble up
            while index > 0 and self.heap[index] > self.heap[self._parent(index)]:
                self._swap(index, self._parent(index))
                index = self._parent(index)
        else:
            # Sink down
            self._sink_down(index)

    def _sink_down(self, index):
        size = len(self.heap)
        curr = index
        while True:
            largest = curr
            left = self._left_child(curr)
            right = self._right_child(curr)

            if left < size and self.heap[left] > self.heap[largest]:
                largest = left
            if right < size and self.heap[right] > self.heap[largest]:
                largest = right

            if largest != curr:
                self._swap(curr, largest)
                curr = largest
            else:
                break

    def extractMax(self):
        if not self.heap:
            return None
        if len(self.heap) == 1:
            return self.heap.pop()
        max_val = self.heap[0]
        self.heap[0] = self.heap.pop()
        self._sink_down(0)
        return max_val

    def isEmpty(self):
        return 1 if len(self.heap) == 0 else 0

    def getMax(self):
        return self.heap[0] if self.heap else None

    def heapSize(self):
        return len(self.heap)
