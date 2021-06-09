# -*- coding: utf-8 -*-
import re
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import sort_alg

OPTIONS = ['BubbleSort', 'HeapSort', 'RadixSort',
           'BinSort', 'ShellSort', 'QuickSort']
TITLE = 'Sort Algorithms'
arr = []

root = Tk()
root.title(TITLE)


def print_console(arr, alg):
    n = len(arr)
    print('Array sorted using: ' + alg)
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
        messagebox.showerror(TITLE, 'Sort type not supported')


def show_result(sorted_arr, alg):
    print_console(sorted_arr, alg)
    show_in_text_field(result_text, sorted_arr)


def bubble_sort():
    print('BubleSort seleccionado')
    b_sort = sort_alg.BubbleSort()
    sorted_arr = b_sort.bubble_sort_console(arr)
    show_result(sorted_arr, 'BubleSort')


def heap_sort():
    print('HeapSort seleccionado')
    h_sort = sort_alg.HeapSort()
    sorted_arr = h_sort.heap_sort_console(arr)
    show_result(sorted_arr, 'HeapSort')


def radix_sort():
    print('RadixSort seleccionado')
    r_sort = sort_alg.RadixSort()
    sorted_arr = r_sort.radix_sort_console(arr)
    show_result(sorted_arr, 'RadixSort')


def bin_sort():
    print('BinSort seleccionado')
    bi_sort = sort_alg.BinSort()
    sorted_arr = bi_sort.insertion_sort_console(arr)
    show_result(sorted_arr, 'BinSort')


def shell_sort():
    print('ShellSort seleccionado')
    s_sort = sort_alg.ShellSort()
    sorted_arr = s_sort.shell_sort_console(arr)
    show_result(sorted_arr, 'ShellSort')


def quick_sort():
    print('QuickSort seleccionado')
    q_sort = sort_alg.QuickSort()
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
        regex_data.append(
            'Solo se permiten numeros/decimales con punto positivos')
        return regex_data
    else:
        messagebox.showerror(TITLE, 'Opcion de ordenamiento no soportada')


def clear_fields():
    number_text.delete(1.0, END)
    result_text.delete(1.0, END)
    value_text.delete(1.0, END)
    arr.clear()


def show_in_text_field(field, arr):
    field.delete(1.0, END)
    field.insert(1.0, ' '.join(map(str, arr)))


def clear_last_value():
    if arr:
        arr.pop()
        show_in_text_field(value_text, arr)


def add_value():
    val = number_text.get('1.0', END).strip()
    regex_data = regex_for_sort()
    if regex_data:
        if re.match(regex_data[0], val):
            arr.append(val)
            show_in_text_field(value_text, arr)
        else:
            messagebox.showerror(TITLE, regex_data[1])


def exit_app():
    value = messagebox.askokcancel("Exit", "Do you want to exit?")
    if value:
        root.destroy()


def show_licence():
    messagebox.showinfo("Licence", "GNU - Free software")


# ----------------comienzo barra Menu------------------

menu_bar = Menu(root)
root.config(menu=menu_bar, width=300, height=300)

exit_menu = Menu(menu_bar, tearoff=0)
exit_menu.add_command(label="Exit", command=exit_app)

help_menu = Menu(menu_bar, tearoff=0)
help_menu.add_command(label="Licence", command=show_licence)

menu_bar.add_cascade(label="File", menu=exit_menu)
menu_bar.add_cascade(label="Help", menu=help_menu)

frame1 = Frame(root)
frame1.pack()

sort_label = Label(frame1, text="Sort type: ")
sort_label.grid(row=0, column=0, sticky="e", padx=10, pady=10)

number_label = Label(frame1, text="New number: ")
number_label.grid(row=1, column=0, sticky="e", padx=10, pady=10)

value_label = Label(frame1, text="Current numbers: ")
value_label.grid(row=2, column=0, sticky="e", padx=10, pady=10)

sort_combo = ttk.Combobox(frame1, width=16, state='readonly', values=OPTIONS)
sort_combo.grid(row=0, column=1, padx=10, pady=10)
sort_combo.current(0)

number_text = Text(frame1, width=16, height=1)
number_text.grid(row=1, column=1, padx=10, pady=10)

value_text = Text(frame1, width=16, height=5)
value_text.grid(row=2, column=1, padx=10, pady=10)
scroll_vert = Scrollbar(frame1, command=value_text.yview)
scroll_vert.grid(row=2, column=2, sticky="nsew")
value_text.config(yscrollcommand=scroll_vert.set)

frame2 = Frame(root)
frame2.pack()

add_button = Button(frame2, text="Add", width="10",
                    height="1", command=add_value)
add_button.grid(row=0, column=0, padx=10, pady=10)
clear_last_button = Button(frame2, text="Clear last",
                           width="10", height="1", command=clear_last_value)
clear_last_button.grid(row=0, column=1, padx=10, pady=10)
clear_all_button = Button(frame2, text="Clear all",
                          width="10", height="1", command=clear_fields)
clear_all_button.grid(row=0, column=2, padx=10, pady=10)
sort_button = Button(frame2, text="Sort", width="10",
                     height="1", command=sort_data)
sort_button.grid(row=0, column=3, padx=10, pady=10)

frame3 = Frame()
frame3.pack()

result_text = Text(frame3, width=40, height=3)
result_text.grid(row=0, column=1, padx=10, pady=10)
scroll_vert = Scrollbar(frame3, command=result_text.yview)
scroll_vert.grid(row=0, column=2, sticky="nsew")
result_text.config(yscrollcommand=scroll_vert.set)

root.mainloop()
