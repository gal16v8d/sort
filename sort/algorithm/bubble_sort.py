"""Bubble Sort Algorithm Implementation"""

from typing import List
from algorithm.sort_types import Number


class BubbleSort:
    """
    A class that implements the bubble sort algorithm.
    This algorithm repeatedly steps through the list, compares adjacent elements,
    and swaps them if they are in the wrong order. The pass through the list is repeated
    until the list is sorted.
    Time Complexity: O(n^2) in the worst case.
    Space Complexity: O(1) as it sorts the list in place.
    """

    @staticmethod
    def bubble_sort_console(arr: List[Number]) -> List[float]:
        """
        Sorts an array using the bubble sort algorithm.
        :param arr: List of numbers (can be int or float) to be sorted.
        :return: A new list containing the sorted numbers as floats.
        """
        float_arr = list(map(float, arr))
        n = len(arr)

        # Traverse through all array elements
        for i in range(n - 1):
            # range(n) also work but outer loop will repeat one time more than needed.

            # Last i elements are already in place
            for j in range(0, n - i - 1):
                # traverse the array from 0 to n-i-1
                # Swap if the element found is greater
                # than the next element
                if float_arr[j] > float_arr[j + 1]:
                    float_arr[j], float_arr[j + 1] = float_arr[j + 1], float_arr[j]
        return float_arr
