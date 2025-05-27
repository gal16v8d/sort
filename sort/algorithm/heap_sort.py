"""Heap Sort Algorithm Implementation"""

from builtins import map
from algorithm.sort_types import Number


class HeapSort:
    """
    A class that implements the heap sort algorithm.
    This algorithm builds a max heap from the input data and then
    repeatedly extracts the maximum element from the heap to build the sorted array.
    Time Complexity: O(n log n) in the worst case.
    Space Complexity: O(1) as it sorts the list in place.
    """

    def __heapify(self, arr: list[Number], n: int, i: int) -> None:
        """
        Maintains the heap property for a subtree rooted at index i.
        :param arr: The array representing the heap.
        :param n: The size of the heap.
        :param i: The index of the root of the subtree.
        """
        largest = i  # Initialize largest as root
        l = 2 * i + 1  # left = 2*i + 1
        r = 2 * i + 2  # right = 2*i + 2
        # See if left child of root exists and is
        # greater than root
        if l < n and arr[i] < arr[l]:
            largest = l
        # See if right child of root exists and is
        # greater than root
        if r < n and arr[largest] < arr[r]:
            largest = r
        # Change root, if needed
        if largest != i:
            arr[i], arr[largest] = arr[largest], arr[i]  # swap
            # Heapify the root.
            self.__heapify(arr, n, largest)

    def heap_sort_console(self, arr: list[Number]) -> list[float]:
        """
        Sorts an array using the heap sort algorithm.
        :param arr: List of numbers (can be int or float) to be sorted.
        :return: A new list containing the sorted numbers as floats.
        """
        float_arr = list(map(float, arr))
        n = len(float_arr)
        # Build a maxheap.
        # Since last parent will be at ((n//2)-1) we can start at that location.
        for i in range(n // 2 - 1, -1, -1):
            self.__heapify(float_arr, n, i)
        # One by one extract elements
        for i in range(n - 1, 0, -1):
            float_arr[i], float_arr[0] = float_arr[0], float_arr[i]  # swap
            self.__heapify(float_arr, i, 0)
        return float_arr
