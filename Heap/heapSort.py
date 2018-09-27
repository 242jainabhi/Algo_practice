class Heap():
    def __init__(self, arr):
        self.heap_size = len(arr)
        self.heap = arr

    def max_heapify(self, i):
        l = 2*i+1
        r = 2*i+2
        if l < self.heap_size and self.heap[l] > self.heap[i]:
            largest = l
        else:
            largest = i
        if r < self.heap_size and self.heap[r] > self.heap[largest]:
            largest = r
        if largest != i:
            self.heap[i], self.heap[largest] = self.heap[largest], self.heap[i]
            self.max_heapify(largest)

    def build_max_heap(self):
        for i in range(self.heap_size//2, -1, -1):
            self.max_heapify(i)

    def heap_sort(self):
        self.build_max_heap()
        for i in range(self.heap_size-1, 0, -1):
            self.heap[0], self.heap[i] = self.heap[i], self.heap[0]
            self.heap_size -= 1
            self.max_heapify(0)

if __name__ == "__main__":
    A = [4, 1, 3, 2, 16, 9, 10, 14, 8, 7]
    h = Heap(A)
    try:
        h.max_heapify(1)
        assert h.heap == [4, 16, 3, 2, 7, 9, 10, 14, 8, 1]
    except AssertionError:
        print('Could not Heapified!')
    try:
        h.build_max_heap()
        assert h.heap == [16, 14, 10, 8, 7, 9, 3, 2, 4, 1]
    except AssertionError:
        print('Not converted to Max Heap!')
    try:
        h.heap_sort()
        assert h.heap == [1, 2, 3, 4, 7, 8, 9, 10, 14, 16]
    except AssertionError:
        print('Not Sorted!')
