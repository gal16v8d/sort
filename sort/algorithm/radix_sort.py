"""Radix Sort Algorithm Implementation"""

from typing import List


class RadixSort:
    """
    A class that implements the radix sort algorithm.
    This algorithm sorts numbers by processing individual digits.
    Time Complexity: O(d * (n + k)), where d is the number of digits in the maximum number,
    n is the number of elements in the array, and k is the range of the input (0-9 for decimal).
    Space Complexity: O(n) for the output array.
    """

    def __counting_sort(self, arr: List[int], exp1: int) -> None:
        """
        A function to do counting sort of arr[] according to
        the digit represented by exp1 (10^i where i is the current digit number).
        :param arr: The array to be sorted.
        :param exp1: The exponent representing the current digit (1, 10, 100, etc.).
        """
        n = len(arr)
        output = [0] * (n)
        count = [0] * (10)
        # Storage of occurrences in count[]
        for i in range(0, n):
            index = arr[i] / exp1
            count[int((index) % 10)] += 1

        for i in range(1, 10):
            count[i] += count[i - 1]

        i = n - 1
        while i >= 0:
            index = arr[i] / exp1
            output[count[int((index) % 10)] - 1] = arr[i]
            count[int((index) % 10)] -= 1
            i -= 1

        i = 0
        for i in range(0, len(arr)):
            arr[i] = output[i]

    def radix_sort_console(self, arr: List[int]) -> List[int]:
        """
        Sorts an array using the radix sort algorithm.
        :param arr: List of numbers (can be int or float) to be sorted.
        :return: A new list containing the sorted numbers as integers.
        """
        int_arr = list(map(int, arr))
        max1 = max(int_arr)
        # Do counting sort for every digit. Note that instead
        # of passing digit number, exp is passed. exp is 10^i
        # where i is current digit number
        exp = 1
        val = max1 / exp
        while val > 0:
            self.__counting_sort(int_arr, exp)
            exp *= 10
        return int_arr
