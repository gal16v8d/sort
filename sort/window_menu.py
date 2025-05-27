"""Window menu actions for the application."""

from tkinter import messagebox, Tk


class WindowMenu:
    """Class to handle the window menu actions."""

    def __init__(self, root: Tk) -> None:
        """Initialize the WindowMenu class."""
        self.root = root

    def exit_app(self) -> None:
        """Show a modal to determine if exit the application or not."""
        value = messagebox.askokcancel("Exit", "Do you want to exit?")
        if value:
            self.root.destroy()

    @staticmethod
    def show_licence() -> None:
        """Show licence information."""
        messagebox.showinfo("Licence", "GNU - Free software")
