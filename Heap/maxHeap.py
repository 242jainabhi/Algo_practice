class Heap():
    def __init__(self, arr):
        self.heap = arr
        self.heap_size = len(self.heap)

    def parent(self, i):
        return i//2

    def left_child(self, i):
        return 2*i+1

    def right_child(self, i):
        return 2*i+2

    def max_heapify(self, i):
        l = self.left_child(i)
        r = self.right_child(i)
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

    def insert(self, x):
        i = self.heap_size
        self.heap.insert(i, x)
        while i != 0 and self.heap[i] > self.heap[self.parent(i)]:
            self.heap[i], self.heap[self.parent(i)] = self.heap[self.parent(i)], self.heap[i]
            i = self.parent(i)

    def get_max(self):
        self.build_max_heap()
        return self.heap[0]

    def extract_max(self):
        self.build_max_heap()
        max = self.heap[0]
        self.heap[0] = self.heap[-1]
        self.heap.pop()
        self.max_heapify(0)
        self.heap_size -= 1
        return max

if __name__ == "__main__":
    A = [4, 1, 3, 2, 16, 9, 10, 8, 14, 7]
    h = Heap(A)
    h.insert(100)
    print(h.get_max())
    print(h.heap)