# -*- coding: utf-8 -*-
import re
from typing import List

from tkinter import *
from tkinter import messagebox, ttk

from algorithm.bin_sort import BinSort
from algorithm.bubble_sort import BubbleSort
from algorithm.heap_sort import HeapSort
from algorithm.quick_sort import QuickSort
from algorithm.radix_sort import RadixSort
from algorithm.shell_sort import ShellSort
from const.const import OPTIONS, TITLE
from window_menu import WindowMenu


arr = []

root = Tk()
root.title(TITLE)


def print_console(arr_data: List) -> None:
    """Print the contents of the array to the console."""
    for arr_value in arr_data:
        print(arr_value)


def show_in_text_field(field: Text, arr_data: List) -> None:
    """Display the contents of the array in the specified text field."""
    field.delete(1.0, END)
    field.insert(1.0, " ".join(map(str, arr_data)))


def show_result(sorted_arr) -> None:
    """Display the sorted array in the console and text field."""
    print_console(sorted_arr)
    show_in_text_field(result_text, sorted_arr)


def bubble_sort() -> None:
    """Sort the array using Bubble Sort and display the result."""
    sorted_arr = BubbleSort.bubble_sort_console(arr)
    show_result(sorted_arr)


def heap_sort() -> None:
    """Sort the array using Heap Sort and display the result."""
    sorted_arr = HeapSort().heap_sort_console(arr)
    show_result(sorted_arr)


def radix_sort() -> None:
    """Sort the array using Radix Sort and display the result."""
    sorted_arr = RadixSort().radix_sort_console(arr)
    show_result(sorted_arr)


def bin_sort() -> None:
    """Sort the array using Binary Insertion Sort and display the result."""
    sorted_arr = BinSort().insertion_sort_console(arr)
    show_result(sorted_arr)


def shell_sort() -> None:
    """Sort the array using Shell Sort and display the result."""
    sorted_arr = ShellSort.shell_sort_console(arr)
    show_result(sorted_arr)


def quick_sort() -> None:
    """Sort the array using Quick Sort and display the result."""
    sorted_arr = QuickSort().quick_sort_console(arr, 0, len(arr) - 1)
    show_result(sorted_arr)


sort_options = {
    "BinSort": bin_sort,
    "BubbleSort": bubble_sort,
    "HeapSort": heap_sort,
    "RadixSort": radix_sort,
    "ShellSort": shell_sort,
    "QuickSort": quick_sort,
}


def regex_for_sort() -> List[str]:
    """Return the regex for the selected sort type."""
    val = sort_combo.get()
    regex_data = []
    if val == OPTIONS[2]:
        regex_data.append("^[0-9]+$")
        regex_data.append("Just positive integers are allowed")
        return regex_data
    elif val in OPTIONS:
        regex_data.append("^[0-9]*[.]{0,1}[0-9]*$")
        regex_data.append("Just positive integers or floats are allowed")
        return regex_data
    else:
        messagebox.showerror(TITLE, "Unsupported sort type")
        return []


def clear_fields() -> None:
    """Clear all text fields and the array."""
    number_text.delete(1.0, END)
    result_text.delete(1.0, END)
    value_text.delete(1.0, END)
    arr.clear()


def clear_last_value() -> None:
    """Remove the last value from the array and update the text field."""
    if arr:
        arr.pop()
        show_in_text_field(value_text, arr)


def add_value() -> None:
    """Add a new value to the array if it matches the regex for the selected sort type."""
    val = number_text.get("1.0", END).strip()
    regex_data = regex_for_sort()
    if regex_data:
        if re.match(regex_data[0], val):
            arr.append(val)
            show_in_text_field(value_text, arr)
        else:
            messagebox.showerror(TITLE, regex_data[1])


def sort_data() -> None:
    """Sort the array based on the selected sort type."""

    val = sort_combo.get()
    if val in sort_options:
        print(f"Sorting using: {val}")
        sort_options[val]()
    else:
        messagebox.showerror(TITLE, "Sort type not supported")


action_buttons = [
    {"text": "Add", "command": add_value},
    {"text": "Clear last", "command": clear_last_value},
    {"text": "Clear all", "command": clear_fields},
    {"text": "Sort", "command": sort_data},
]

app_labels = [
    {"text": "Sort type: "},
    {"text": "New number: "},
    {"text": "Current numbers: "},
]


# ----------------Menu bar init ------------------

window_menu = WindowMenu(root)

menu_bar = Menu(root)
root.config(menu=menu_bar, width=300, height=300)

exit_menu = Menu(menu_bar, tearoff=0)
exit_menu.add_command(label="Exit", command=window_menu.exit_app)

help_menu = Menu(menu_bar, tearoff=0)
help_menu.add_command(label="Licence", command=WindowMenu.show_licence)

menu_bar.add_cascade(label="File", menu=exit_menu)
menu_bar.add_cascade(label="Help", menu=help_menu)

frame1 = Frame(root)
frame1.pack()

for label in app_labels:
    lbl = Label(frame1, text=label["text"])
    lbl.grid(row=app_labels.index(label), column=0, sticky="e", padx=10, pady=10)

sort_combo = ttk.Combobox(frame1, width=16, state="readonly", values=OPTIONS)
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

for action in action_buttons:
    button = Button(
        frame2, text=action["text"], width="10", height="1", command=action["command"]
    )
    button.grid(row=0, column=action_buttons.index(action), padx=10, pady=10)

frame3 = Frame()
frame3.pack()

result_text = Text(frame3, width=40, height=3)
result_text.grid(row=0, column=1, padx=10, pady=10)
scroll_vert = Scrollbar(frame3, command=result_text.yview)
scroll_vert.grid(row=0, column=2, sticky="nsew")
result_text.config(yscrollcommand=scroll_vert.set)

root.mainloop()
