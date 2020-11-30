# -*- coding: utf-8 -*-
"""
Grupo 4 Programación avanzada

Nombres:
    Sebastian Potes Blandon
    Jessica M Jimenez Soto

Para resolver el método de ordenamiento ShellSort lee información
sobre el modo de uso e implementación, luego se usa como base
el código encontrado en l siguiente link.
https://www.geeksforgeeks.org/shellsort/ 
This code is contributed by Mohit Kumra

Para la actividad se solicita al usuario ingresar la cantidad de
números que desea ordenar, para luego ingresarlos y con un enter 
mostrar el resultado ordenado.
"""

#----------------librerias importadas------------------
import re
from tkinter import *
from tkinter import messagebox
from tkinter import ttk


#----------------variables globales------------------

OPTIONS = ['Burbuja', 'HeapSort', 'RadixSort', 'BinSort', 'ShellSort', 'QuickSort']
TITLE = 'Ordenamiento de datos'
arr = []

#----------------creación ventana------------------

root= Tk()
root.title(TITLE)

#----------------comienzo de funciones------------------

# Muestra para tests
#arr = [ 12, 34, 54, 2, 3, 10, 90, 12, 60, 100, 101, 205, 300, 500, 2, 5, 6, 15, 19, 2014, 0]

#--------- Inicio metodos bubbleSort ----------# 
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
                if float_arr[j] > float_arr[j+1] : 
                    float_arr[j], float_arr[j+1] = float_arr[j+1], float_arr[j] 
        return float_arr

#--------- Fin metodos bubbleSort ----------# 

#--------- Inicio metodos heapSort ----------# 

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
            arr[i],arr[largest] = arr[largest],arr[i]  # swap 
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

#--------- Fin metodos heapSort ----------# 

#--------- Inicio metodos radixSort ----------#
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
            count[int((index)%10)] += 1
        # Cambia count[i] para que count[i] ahora contiene la
        #  posicion de ese digito en el array output
        for i in range(1,10): 
            count[i] += count[i-1] 
        # Construye el array output 
        i = n-1
        while i>=0: 
            index = (arr[i]/exp1) 
            output[ count[ int((index)%10) ] - 1] = arr[i] 
            count[int((index)%10)] -= 1
            i -= 1
        # Copia output en arr[], 
        # so that arr now contains sorted numbers 
        i = 0
        for i in range(0,len(arr)): 
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
#--------- Fin metodos radixSort ----------#

#--------- Inicio metodos binSort ----------#

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
            float_arr = float_arr[:j] + [val] + float_arr[j:i] + float_arr[i+1:] 
        return float_arr 

#--------- Fin metodos binSort ----------#

#--------- Inicio metodos ShellSort ----------#
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
    
            for i in range(gap,n): 
    
                # agrega a[i] a los elementos que han sido ordenados
                # guarda a[i] en temp y deja un agujero en la pos i 
                temp = float_arr[i] 
    
                # desplazar elementos anteriores ordenados por espacios hasta el correcto
                # Se encontró ubicación para una [i]
                j = i 
                while  j >= gap and float_arr[j-gap] >temp: 
                    float_arr[j] = float_arr[j-gap] 
                    j -= gap 
    
                # pone el temp (el original a[i]) en la ubicacion correcta
                float_arr[j] = temp 
            gap //= 2
        return float_arr
#--------- Fin metodos ShellSort ----------#

#--------- Inicio metodos QuickSort ----------#

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

#--------- Fin metodos QuickSort ----------#

def print_console(arr, method): 
    n = len(arr)
    print('Array organizado usando: ' + method)
    for i in range(n): 
        print(arr[i]),

def sort_data():
    val = sort_combo.get()
    if val == OPTIONS[0]:
        bubble_sort()
    elif val == OPTIONS[1]:
        heap_sort()
    elif val == OPTIONS[2]:
        radix_sort()
    elif val == OPTIONS[3]:
        bin_sort()
    elif val == OPTIONS[4]:
        shell_sort()
    elif val == OPTIONS[5]:
        quick_sort()
    else:
        messagebox.showerror(TITLE,'Opcion de ordenamiento no soportada')

def show_result(sorted_arr, alg):
    print_console(sorted_arr, alg)
    show_in_text_field(result_text, sorted_arr)

def bubble_sort():
    print('BubleSort seleccionado')
    b_sort = BubbleSort()
    sorted_arr = b_sort.bubble_sort_console(arr)
    show_result(sorted_arr, 'BubleSort')

def heap_sort():
    print('HeapSort seleccionado')
    h_sort = HeapSort()
    sorted_arr = h_sort.heap_sort_console(arr)
    show_result(sorted_arr, 'HeapSort')

def radix_sort():
    print('RadixSort seleccionado')
    r_sort = RadixSort()
    sorted_arr = r_sort.radix_sort_console(arr)
    show_result(sorted_arr, 'RadixSort')

def bin_sort():
    print('BinSort seleccionado')
    bi_sort = BinSort()
    sorted_arr = bi_sort.insertion_sort_console(arr)
    show_result(sorted_arr, 'BinSort')

def shell_sort():
    print('ShellSort seleccionado')
    s_sort = ShellSort()
    sorted_arr = s_sort.shell_sort_console(arr)
    show_result(sorted_arr, 'ShellSort')

def quick_sort():
    print('QuickSort seleccionado')
    q_sort = QuickSort()
    sorted_arr = q_sort.quick_sort_console(arr, 0, len(arr) - 1)
    show_result(sorted_arr, 'QuickSort')

def regex_for_sort():
    val = sort_combo.get()
    regex_data = []
    if val == OPTIONS[2]:
        regex_data.append('^[0-9]+$')
        regex_data.append('Solo se permiten numeros enteros positivos')
        return regex_data
    elif val in OPTIONS:
        regex_data.append('^[0-9]*[.]{0,1}[0-9]*$')
        regex_data.append('Solo se permiten numeros/decimales con punto positivos')
        return regex_data
    else:
        messagebox.showerror(TITLE,'Opcion de ordenamiento no soportada')
        
# limpia los campos y el array para permitir re-iniciar el programa a 
# nuevos ordenamientos
def clear_fields():
    number_text.delete(1.0,END)
    result_text.delete(1.0,END)
    value_text.delete(1.0,END)
    arr.clear()

# mapea el contenido del array a un campo de texto, cada elemento es 
# separado por espacio
def show_in_text_field(field, arr):
    field.delete(1.0,END)
    field.insert(1.0, ' '.join(map(str, arr)))   

# Elimina el ultimo elemento del array y lo mapea a un campo de texto
def clear_last_value():
    if arr:
        arr.pop()
        show_in_text_field(value_text, arr)
  
# Agrega un nuevo valor al array y lo muestra en vista
# el valor nuevo debe ser un numero o decimal, el separador de
# decimal debe ser el punto (.)
def add_value():
    val = number_text.get('1.0', END).strip()
    regex_data = regex_for_sort()
    if regex_data:
        if re.match(regex_data[0], val):
            arr.append(val)
            show_in_text_field(value_text, arr)
        else:
            messagebox.showerror(TITLE, regex_data[1])

# Destruye la ventana (root)
def exit_app():
    valor = messagebox.askokcancel("Salir", "¿Deseas salir de la aplicación?") #devuelve True or False
    if valor== True:
        root.destroy()
        
def more_info():
    messagebox.showinfo("Taller3", "Sort")

def show_licence():
    messagebox.showinfo("Licencia","producto bajo licencia GNU - Software libre")


#----------------comienzo barra Menu------------------

menu_bar=Menu(root)
root.config(menu=menu_bar, width=300,height=300)

exit_menu=Menu(menu_bar, tearoff=0)
exit_menu.add_command(label="Salir", command=exit_app)

help_menu=Menu(menu_bar, tearoff=0)
help_menu.add_command(label="Licencia", command=show_licence)
help_menu.add_command(label="Acerca de...", command=more_info)

menu_bar.add_cascade(label="File",menu=exit_menu)
menu_bar.add_cascade(label="Ayuda",menu=help_menu)


#----------------textos y entradas------------------

frame1=Frame(root)
frame1.pack()

#----------------columna 1------------------

sort_label=Label(frame1, text="Tipo de ordenamiento: ")
sort_label.grid(row=0, column=0, sticky="e",padx=10,pady=10)

number_label=Label(frame1, text="Ingrese un número: ")
number_label.grid(row=1, column=0, sticky="e",padx=10,pady=10)

value_label=Label(frame1, text="Números ingresados: ")
value_label.grid(row=2, column=0, sticky="e",padx=10,pady=10)

#----------------columna 2------------------

sort_combo=ttk.Combobox(frame1, width=16, state='readonly', values=OPTIONS)
sort_combo.grid(row=0, column=1,padx=10,pady=10)
sort_combo.current(0)

number_text=Text(frame1,width=16,height=1)
number_text.grid(row=1, column=1,padx=10,pady=10)

value_text=Text(frame1,width=16,height=5)
value_text.grid(row=2, column=1,padx=10,pady=10)
scroll_vert=Scrollbar(frame1, command=value_text.yview)
scroll_vert.grid(row=2, column=2, sticky="nsew")
value_text.config(yscrollcommand=scroll_vert.set)

#----------------botones al final------------------

frame2=Frame(root)
frame2.pack()

add_button=Button(frame2,text="Agregar", width="10", height="1", command=add_value)
add_button.grid(row=0, column=0, padx=10, pady=10)
clear_last_button=Button(frame2,text="Borrar", width="10", height="1", command=clear_last_value)
clear_last_button.grid(row=0, column=1, padx=10, pady=10)
clear_all_button=Button(frame2,text="Limpiar", width="10", height="1", command=clear_fields)
clear_all_button.grid(row=0, column=2, padx=10, pady=10)
sort_button=Button(frame2,text="Ordenar", width="10", height="1", command=sort_data)
sort_button.grid(row=0, column=3, padx=10, pady=10)

#----------------Salida del shell sort------------------

frame3=Frame()
frame3.pack()

result_text=Text(frame3,width=40,height=3)
result_text.grid(row=0, column=1,padx=10,pady=10)
scroll_vert=Scrollbar(frame3, command=result_text.yview)
scroll_vert.grid(row=0, column=2, sticky="nsew")
result_text.config(yscrollcommand=scroll_vert.set)

root.mainloop()