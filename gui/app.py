import customtkinter

from utils import FontParams
from widget_utils import DataTableWidget, DataEntryWidget, DeleteWidget#, UpdateWidget, DeleteWidget
from database.database import Database


class UsernameGui:
    """
    Username user interface.
    Allow the user to enter the database id and launches the database gui.
    :param: container: root frame to place in the UsernameGui.
    """
    def __init__(self, container):
        self.container = container
        self.frame = customtkinter.CTkFrame(master=container)
        self.frame.pack(padx=20, pady=20, fill='both', expand=True)

        # grid structure 4, 3 (rows, columns).
        self.frame.columnconfigure((0, 1, 2), weight=1)
        self.frame.rowconfigure((0, 1, 2, 3), weight=1)

        font_params = FontParams()

        # User Label -------------------------
        user_label = customtkinter.CTkLabel(master=self.frame, text="Username", font=font_params.text_font)
        user_label.grid(row=0, column=0, pady=5, padx=5, columnspan=2, sticky='ws')
        # User Entry -------------------------
        user = customtkinter.StringVar()
        self.user_entry = customtkinter.CTkEntry(master=self.frame,
                                                 textvariable=user,
                                                 width=30, height=5,
                                                 font=font_params.text_font)
        self.user_entry.grid(row=2, column=0, pady=5, padx=5, columnspan=3, rowspan=1, sticky='nsew')
        # Ok Button -------------------------
        self.ok_btn = customtkinter.CTkButton(master=self.frame, text="Ok",
                                              width=10, font=font_params.text_font,
                                              command=self.database_gui)
        self.ok_btn.grid(row=3, column=2, pady=5, padx=5, sticky='nswe')

    def database_gui(self):
        # Get the current frame useful info and destroy it.
        username = self.user_entry.get()
        self.frame.destroy()
        self.container.title("Expenses Data Base: " + username)
        # Full screen dims.
        screen_width = self.container.winfo_screenwidth()
        screen_height = self.container.winfo_screenheight()
        self.container.geometry(f"{screen_width - 20}x{screen_height - 50}+0+0")
        # Create new frame to replace the old one.
        self.frame = customtkinter.CTkFrame(master=self.container)
        # grid structure 4, 3 (rows, columns).
        self.frame.columnconfigure((0, 1, 2), weight=1)
        self.frame.rowconfigure((0, 1, 2, 3), weight=1)
        self.frame.pack(padx=10, pady=10, fill='both', expand=True)

        # Launch the database gui.
        database_gui = DataBaseGui(username, self.frame)


class DataBaseGui:
    """
    DataBase complete user interface. It allows to set and
    remove every widget of the frame
    :param: username: client username
    :param: container: root of the app
    """
    def __init__(self, username, container):
        self.username = username
        self.container = container
        # Connect to the client database.
        self.client_database = Database(username)

        # Initialize every widget in the container
        self.data_table = None
        self.data_entry = None
        self.data_update = None
        self.data_delete = None

        self.init_data_table()
        self.init_data_entry()
        # self.init_data_update()
        self.init_data_delete()

    # ---------------- DataTableWidget FUNCTIONS --------------------
    def init_data_table(self):
        """Initialize the data table display widget. This procedure allows
        to destroy and relaunch this widget from outside this class"""
        self.data_table = DataTableWidget(self)

    def destroy_data_table(self):
        """Destroy the data table widget"""
        self.data_table.destroy_data_table()

    # ---------------- DataEntryWidget FUNCTIONS --------------------
    def init_data_entry(self):
        """Initialize the data entry widget. This procedure allows
        to destroy and relaunch this widget from outside this class"""
        self.data_entry = DataEntryWidget(self)

    def destroy_data_entry(self):
        """Destroy the data entry widget"""
        self.data_entry.destroy_entry_widget()

    # # ---------------- UpdateWidget FUNCTIONS --------------------
    # def init_data_update(self):
    #     """Initialize the data update widget. This procedure allows
    #     to destroy and relaunch this widget from outside this class"""
    #     self.data_update = UpdateWidget(self)
    #
    # def destroy_data_update(self):
    #     """Destroy the update-widget"""
    #     self.data_update.destroy()
    #
    # ---------------- DeleteWidget FUNCTIONS --------------------
    def init_data_delete(self):
        """Initialize the data delete widget. This procedure allows
        to destroy and relaunch this widget from outside this class"""
        self.data_delete = DeleteWidget(self)

    def destroy_data_delete(self):
        """Destroy the delete-widget"""
        self.data_delete.destroy()


class App(customtkinter.CTk):
    """Database gui launcher."""
    def __init__(self):
        super().__init__()
        customtkinter.set_appearance_mode("light")
        self.title("Expenses Data Base")
        self.geometry("300x220")
        # Initialize the user entry interface
        user = UsernameGui(self)


if __name__ == "__main__":
    app = App()
    app.mainloop()

