"""Shell Sort Algorithm Implementation"""

from builtins import map
from algorithm.sort_types import Number


class ShellSort:
    """ShellSort is an in-place comparison-based algorithm that generalizes
    insertion sort to allow the exchange of items that are far apart.
    It starts by sorting pairs of elements far apart from each other,
    then progressively reduces the gap between elements to be compared.
    The algorithm uses a gap sequence to determine which elements to compare
    and sort, which allows it to move elements closer to their final position
    more quickly than a simple insertion sort.
    """

    @staticmethod
    def shell_sort_console(arr: list[Number]) -> list[float]:
        """Sorts an array using the Shell Sort algorithm.
        Args:
            arr (List): The array to be sorted.
        Returns:
            List[float]: The sorted array.
        """
        float_arr = list(map(float, arr))
        # Starts with a large gap and then reduces it
        n = len(float_arr)
        gap = n // 2

        while gap > 0:

            for i in range(gap, n):
                temp = float_arr[i]
                # Shift elements of arr[0..i-gap] that are
                # greater than temp to their new position
                # in the gap-sorted array
                j = i
                while j >= gap and float_arr[j - gap] > temp:
                    float_arr[j] = float_arr[j - gap]
                    j -= gap

                # put the temp (the original float_arr[i]) in the correct location
                float_arr[j] = temp
            gap //= 2
        return float_arr
