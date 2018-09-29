from maxHeap import MaxHeap
from minHeap import MinHeap


def heap_sort_increasing(h):
	h.build_max_heap()
	for i in range(h.heap_size-1, 0, -1):
		h.heap[0], h.heap[i] = h.heap[i], h.heap[0]
		h.heap_size -= 1
		h.max_heapify(0)

def heap_sort_decreasing(h):
	h.build_min_heap()
	for i in range(h.heap_size-1, 0, -1):
		h.heap[0], h.heap[i] = h.heap[i], h.heap[0]
		h.heap_size -= 1
		h.min_heapify(0)

if __name__ == "__main__":
    A = [4, 1, 3, 2, 16, 9, 10, 14, 8, 7]
    h = MaxHeap(A)
    try:
        heap_sort_increasing(h)
        assert h.heap == [1, 2, 3, 4, 7, 8, 9, 10, 14, 16]
    except AssertionError:
        print('Not Sorted!')
    else:
	    print('Sorted in increasing order: ', h.heap)

    h = MinHeap(A)
    try:
        heap_sort_decreasing(h)
        assert h.heap == [16, 14, 10, 9, 8, 7, 4, 3, 2, 1]
    except AssertionError:
        print('Not Sorted!')
    else:
	    print('Sorted in decreasing order: ', h.heap)

