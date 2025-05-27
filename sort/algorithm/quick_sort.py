"""QuickSort Algorithm Implementation"""

from typing import List
from algorithm.sort_types import Number


class QuickSort:
    """QuickSort is a divide-and-conquer algorithm that sorts an array by
    selecting a 'pivot' element and partitioning the other elements into two
    sub-arrays, according to whether they are less than or greater than the pivot.
    The sub-arrays are then sorted recursively.
    """

    def __partition(self, arr: List[Number], low: Number, high: Number) -> int:
        """This function takes last element as pivot, places
        the pivot element at its correct position in sorted
        array, and places all smaller (smaller than pivot)
        to left of pivot and all greater elements to right
        of pivot.
        Args:
            arr (List): The array to be sorted.
            low (Number): The starting index of the array.
            high (Number): The ending index of the array.
        Returns:
            int: The index of the pivot element after partitioning.
        """
        i = low - 1  # index of smaller element
        pivot = arr[high]  # pivot

        for j in range(low, high):
            # If current element is smaller than or
            # equal to pivot
            if arr[j] <= pivot:
                # increment index of smaller element
                i = i + 1
                arr[i], arr[j] = arr[j], arr[i]

        arr[i + 1], arr[high] = arr[high], arr[i + 1]
        return i + 1

    def quick_sort_console(
        self, arr: List[Number], low: Number, high: Number
    ) -> List[float]:
        """The function to sort an array using quick sort algorithm.
        Args:
            arr (List): The array to be sorted.
            low (Number): The starting index of the array.
            high (Number): The ending index of the array.
        Returns:
            list: The sorted array.
        """
        float_arr = list(map(float, arr))
        if len(float_arr) == 1:
            return float_arr
        if low < high:
            # pi is partitioning index, arr[p] is now
            # at right place
            pi = self.__partition(float_arr, low, high)
            # Separately sort elements before
            # partition and after partition
            self.quick_sort_console(float_arr, low, pi - 1)
            self.quick_sort_console(float_arr, pi + 1, high)
        return float_arr
