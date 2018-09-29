class MinHeap():
    def __init__(self, arr):
        self.heap = arr
        self.heap_size = len(self.heap)

    def parent(self, i):
        return i//2

    def left_child(self, i):
        return 2*i+1

    def right_child(self, i):
        return 2*i+2

    def min_heapify(self, i):
        l = self.left_child(i)
        r = self.right_child(i)
        if l < self.heap_size and self.heap[l] < self.heap[i]:
            largest = l
        else:
            largest = i
        if r < self.heap_size and self.heap[r] < self.heap[largest]:
            largest = r
        if largest != i:
            self.heap[i], self.heap[largest] = self.heap[largest], self.heap[i]
            self.min_heapify(largest)

    def build_min_heap(self):
        for i in range(self.heap_size//2, -1, -1):
            self.min_heapify(i)

    def insert(self, x):
        i = self.heap_size
        self.heap.insert(i, x)
        while i != 0 and self.heap[i] < self.heap[self.parent(i)]:
            self.heap[i], self.heap[self.parent(i)] = self.heap[self.parent(i)], self.heap[i]
            i = self.parent(i)

    def get_min(self):
        self.build_min_heap()
        return self.heap[0]

    def extract_min(self):
        self.build_min_heap()
        min = self.heap[0]
        self.heap[0] = self.heap[-1]
        self.heap.pop()
        self.min_heapify(0)
        self.heap_size -= 1
        return min

if __name__ == "__main__":
    A = [4, 1, 3, 2, 16, 9, 10, 8, 14, 7]
    h = MinHeap(A)
    h.build_min_heap()
    print('Min Heap: ', h.heap)
    print(h.get_min())