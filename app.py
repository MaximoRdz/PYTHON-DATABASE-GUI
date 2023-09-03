import customtkinter

from gui.user_launcher import UsernameGui


class App(customtkinter.CTk):
    """Database gui launcher."""
    def __init__(self):
        super().__init__()
        customtkinter.set_appearance_mode("light")
        self.title("Expenses Data Base")
        self.geometry("300x220")
        self.resizable("False", "False")
        # Initialize the user entry interface
        user = UsernameGui(self)


if __name__ == "__main__":
    app = App()
    app.mainloop()
