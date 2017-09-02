"""
    Module that contains implementation of Heap
"""


import time
import random


class BinaryHeap:
    """
        Binary heap data structure
    """

    def __init__(self, arr):
        self.heap = arr
        self.heap_size = None
        self._build_binary_heap()

    def _build_binary_heap(self):
        """ Private method that rearranges data in array to represent binary
            heap """
        try:
            self.heap_size = len(self.heap)
            i = len(self.heap) // 2 + 1
            while i >= 0:
                self._maxify_heap(i)
                i -= 1
        except TypeError:
            print(i)

    def get_item(self, i):
        """ Return item """
        if i < self.heap_size and i >= 0:
            return self.heap[i]

    def left_child(self, i):
        """ Return position of left child if exists """
        if (2 * i + 1) < self.heap_size and i >= 0:
            return 2 * i + 1
        return None

    def right_child(self, i):
        """ Return position of right child if exists """
        if (2 * i + 2) < self.heap_size and i >= 0:
            return 2 * i + 2
        return None

    def _maxify_heap(self, i):
        """
            Replace elements in array for representing a correct binary heap
        """
        largest = i
        if self.left_child(i):
            if self.get_item(self.left_child(i)) > self.get_item(largest):
                largest = self.left_child(i)
        if self.right_child(i):
            if self.get_item(self.right_child(i)) > self.get_item(largest):
                largest = self.right_child(i)
        if largest != i:
            self.heap[largest], self.heap[i] = \
                    self.heap[i], self.heap[largest]
            self._maxify_heap(largest)

    def sort(self):
        """
            Sort heap using heapsort
        """
        i = len(self.heap) - 1
        while i >= 1:
            self.heap[0], self.heap[i] = self.heap[i], self.heap[0]
            self.heap_size -= 1
            self._maxify_heap(0)
            i -= 1

    def rebuild_heap(self):
        """
            Recreate proper heap
        """
        self._build_binary_heap()

    def add(self, data):
        """
            Add element to the heap
        """
        # TODO: optimize alghorithm
        self.heap.append(data)
        self.heap_size += 1
        self._build_binary_heap()

    def __str__(self):
        return str(self.heap)


def measure(func, *args):
    """
        Measure clock time of the function
    """
    start = time.perf_counter()
    result = func(*args)
    stop = time.perf_counter()
    return (stop - start) * 100000000, result


def generate_random_input(size, elements_range):
    """
        Generate random array with given size and elements within range
        from 0 to elements_range
    """
    in_arr = []
    for _ in range(size):
        in_arr.append(random.randint(0, elements_range))
    return in_arr


class PriorityQueue:
    pass


def main():
    """
        Module entry point
    """
    in_array = [5, 7, 2, 4, 1, 6, 7, 8, 3]

    temp_heap = BinaryHeap(in_array)
    temp_heap.add(500)
    print(temp_heap)

    for _ in range(3):
        in_array = generate_random_input(random.randint(9, 20), 150)
        print("Initial array: ", in_array)
        cpu_time, heap = measure(BinaryHeap, in_array)
        print("Initial heap: ", heap, "   Time: ", cpu_time)
        cpu_time, _ = measure(heap.sort,)
        print("Heapsort: ", heap, "    Time: ", cpu_time)
        cpu_time, _ = measure(heap.rebuild_heap,)
        print("Rebuilded heap: ", heap, "   Time: ", cpu_time)
        print("\n\n\n")


if __name__ == '__main__':
    main()
