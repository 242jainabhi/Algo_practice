from maxHeap import Heap


def heap_sort(h):
	h.build_max_heap()
	for i in range(h.heap_size-1, 0, -1):
		h.heap[0], h.heap[i] = h.heap[i], h.heap[0]
		h.heap_size -= 1
		h.max_heapify(0)

if __name__ == "__main__":
    A = [4, 1, 3, 2, 16, 9, 10, 14, 8, 7]
    h = Heap(A)
    try:
        heap_sort(h)
        assert h.heap == [1, 2, 3, 4, 7, 8, 9, 10, 14, 16]
    except AssertionError:
        print('Not Sorted!')
    else:
	    print('Sorted Array: ', h.heap)

