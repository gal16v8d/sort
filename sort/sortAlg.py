# -*- coding: utf-8 -*-

class BubbleSort:
    def bubble_sort_console(self, arr):
        float_arr = list(map(float, arr))
        n = len(arr)

        # Traverse through all array elements
        for i in range(n-1):
            # range(n) also work but outer loop will repeat one time more than needed.

            # Last i elements are already in place
            for j in range(0, n-i-1):
                # traverse the array from 0 to n-i-1
                # Swap if the element found is greater
                # than the next element
                if float_arr[j] > float_arr[j+1]:
                    float_arr[j], float_arr[j+1] = float_arr[j+1], float_arr[j]
        return float_arr


class HeapSort:
    # To heapify subtree rooted at index i.
    # n is size of heap
    def __heapify(self, arr, n, i):
        largest = i  # Initialize largest as root
        l = 2 * i + 1     # left = 2*i + 1
        r = 2 * i + 2     # right = 2*i + 2
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

    # The main function to sort an array of given size
    def heap_sort_console(self, arr):
        float_arr = list(map(float, arr))
        n = len(float_arr)
        # Build a maxheap.
        # Since last parent will be at ((n//2)-1) we can start at that location.
        for i in range(n // 2 - 1, -1, -1):
            self.__heapify(float_arr, n, i)
        # One by one extract elements
        for i in range(n-1, 0, -1):
            float_arr[i], float_arr[0] = float_arr[0], float_arr[i]   # swap
            self.__heapify(float_arr, i, 0)
        return float_arr


class RadixSort:
    # Una función para contar una especie de arr [] según
    # el dígito representado por exp.
    def __counting_sort(self, arr, exp1):
        n = len(arr)
        output = [0] * (n)
        count = [0] * (10)
        # Almacenamiento de ocurrencias en count[]
        for i in range(0, n):
            index = (arr[i]/exp1)
            count[int((index) % 10)] += 1
        # Cambia count[i] para que count[i] ahora contiene la
        #  posicion de ese digito en el array output
        for i in range(1, 10):
            count[i] += count[i-1]
        # Construye el array output
        i = n-1
        while i >= 0:
            index = (arr[i]/exp1)
            output[count[int((index) % 10)] - 1] = arr[i]
            count[int((index) % 10)] -= 1
            i -= 1
        # Copia output en arr[],
        # so that arr now contains sorted numbers
        i = 0
        for i in range(0, len(arr)):
            arr[i] = output[i]

    def radix_sort_console(self, arr):
        int_arr = list(map(int, arr))
        # Encuentra el valor maximo para saber el numero de digitos
        max1 = max(int_arr)
        # Do counting sort for every digit. Note that instead
        # of passing digit number, exp is passed. exp is 10^i
        # where i is current digit number
        exp = 1
        val = max1/exp
        while val > 0:
            self.__counting_sort(int_arr, exp)
            exp *= 10
        return int_arr


class BinSort:
    def __binary_search(self, arr, val, start, end):
        # we need to distinugish whether we should insert
        # before or after the left boundary.
        # imagine [0] is the last step of the binary search
        # and we need to decide where to insert -1
        if start == end:
            if arr[start] > val:
                return start
            else:
                return start+1

        # this occurs if we are moving beyond left\'s boundary
        # meaning the left boundary is the least position to
        # find a number greater than val
        if start > end:
            return start

        mid = int((start+end)/2)
        if arr[mid] < val:
            return self.__binary_search(arr, val, mid+1, end)
        elif arr[mid] > val:
            return self.__binary_search(arr, val, start, mid-1)
        else:
            return mid

    def insertion_sort_console(self, arr):
        float_arr = list(map(float, arr))
        for i in range(1, len(float_arr)):
            val = float_arr[i]
            j = self.__binary_search(float_arr, val, 0, i-1)
            float_arr = float_arr[:j] + [val] + \
                float_arr[j:i] + float_arr[i+1:]
        return float_arr


class ShellSort:
    def shell_sort_console(self, arr):
        float_arr = list(map(float, arr))
        # Empieza con una gran brecha y luego va reduciendola
        n = len(float_arr)
        gap = n//2

        # Realice una ordenación por inserción con huecos para este tamaño de hueco.
        # Los primeros elementos de espacio a [0..gap-1] ya están en espacio
        # orden sigue agregando un elemento más hasta que la matriz completa
        # está ordenado por espacios
        while gap > 0:

            for i in range(gap, n):

                # agrega a[i] a los elementos que han sido ordenados
                # guarda a[i] en temp y deja un agujero en la pos i
                temp = float_arr[i]

                # desplazar elementos anteriores ordenados por espacios hasta el correcto
                # Se encontró ubicación para una [i]
                j = i
                while j >= gap and float_arr[j-gap] > temp:
                    float_arr[j] = float_arr[j-gap]
                    j -= gap

                # pone el temp (el original a[i]) en la ubicacion correcta
                float_arr[j] = temp
            gap //= 2
        return float_arr


class QuickSort:
    # This function takes last element as pivot, places
    # the pivot element at its correct position in sorted
    # array, and places all smaller (smaller than pivot)
    # to left of pivot and all greater elements to right
    # of pivot
    def __partition(self, arr, low, high):
        i = (low-1)         # index of smaller element
        pivot = arr[high]     # pivot

        for j in range(low, high):
            # If current element is smaller than or
            # equal to pivot
            if arr[j] <= pivot:
                # increment index of smaller element
                i = i+1
                arr[i], arr[j] = arr[j], arr[i]

        arr[i+1], arr[high] = arr[high], arr[i+1]
        return (i+1)

    # The main function that implements QuickSort
    # arr[] --> Array to be sorted,
    # low  --> Starting index,
    # high  --> Ending index
    # Function to do Quick sort
    def quick_sort_console(self, arr, low, high):
        float_arr = list(map(float, arr))
        if len(float_arr) == 1:
            return float_arr
        if low < high:
            # pi is partitioning index, arr[p] is now
            # at right place
            pi = self.__partition(float_arr, low, high)
            # Separately sort elements before
            # partition and after partition
            self.quick_sort_console(float_arr, low, pi-1)
            self.quick_sort_console(float_arr, pi+1, high)
        return float_arr
