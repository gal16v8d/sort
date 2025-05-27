"""Binary Insertion Sort Algorithm"""

from builtins import map
from algorithm.sort_types import Number


class BinSort:
    """
    This class implements the binary insertion sort algorithm.
    It provides a method to sort an array using binary search
    to find the correct position for each element.
    """

    def __binary_search(
        self, arr: list[Number], val: float, start: int, end: int
    ) -> int:
        """
        This function performs a binary search to find the
        position where the value `val` should be inserted
        in the sorted array `arr` between indices `start` and `end`.
        It returns the index where `val` can be inserted
        while maintaining the sorted order of the array.
        """
        if start == end:
            if arr[start] > val:
                return start
            else:
                return start + 1

        # this occurs if we are moving beyond left\'s boundary
        # meaning the left boundary is the least position to
        # find a number greater than val
        if start > end:
            return start

        mid = int((start + end) / 2)
        if arr[mid] < val:
            return self.__binary_search(arr, val, mid + 1, end)
        elif arr[mid] > val:
            return self.__binary_search(arr, val, start, mid - 1)
        else:
            return mid

    def insertion_sort_console(self, arr: list[Number]) -> list[float]:
        """
        This method sorts an array using the binary insertion sort algorithm.
        It converts the input array to a list of floats, then iteratively
        finds the correct position for each element using binary search,
        and inserts it into the sorted portion of the array.
        :param arr: The input array to be sorted.
        :return: A sorted list of floats.
        """

        float_arr = list(map(float, arr))
        for i in range(1, len(float_arr)):
            val = float_arr[i]
            j = self.__binary_search(float_arr, val, 0, i - 1)
            float_arr = float_arr[:j] + [val] + float_arr[j:i] + float_arr[i + 1 :]
        return float_arr
