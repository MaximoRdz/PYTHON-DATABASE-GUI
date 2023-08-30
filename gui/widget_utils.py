import time
import customtkinter
from tkinter import ttk, messagebox

import constants as ct
from utils import FontParams, RadioButton
from utils import periodic_to_str, payment_to_str
from utils import get_collector_values, save_new_collector, check_description_len


class DataTableWidget:
    """
    Control the table display of the data
    :param database_obj: It contains the parameters: username, container,
    client_database and every widget place in the database-gui
    """
    def __init__(self, database_obj):
        # Frame creation and positioning
        self.frame = customtkinter.CTkFrame(master=database_obj.container)
        # Place the widget frame in the container
        self.frame.grid(row=0, column=0, rowspan=4, columnspan=2,
                        padx=5, pady=5,
                        sticky="news")
        # Grid config (dim entries_lim, 6) -> rows, cols
        self.frame.columnconfigure(0, weight=1)
        self.frame.columnconfigure((1, 2, 3, 4, 5), weight=2)
        self.frame.columnconfigure(6, weight=3)
        self.frame.rowconfigure(tuple([i for i in range(1, ct.TABLE_WIDGET_ENTRIES)]), weight=2)

        # Client database info to be displayed
        client_database = database_obj.client_database
        table_data = client_database.get_gui_info(ct.TABLE_WIDGET_ENTRIES)

        # Write the table:
        self.font_params = FontParams()
        # header -----------
        header = ("Id", "Date", "Amount", "Collector", "P. Method", "Periodic", "Description")
        for i, name in enumerate(header):
            label = customtkinter.CTkLabel(master=self.frame, text=name, font=self.font_params.header_font)
            label.grid(row=0, column=i, padx=5, pady=5, sticky="n")

        # info -------------
        for i, data in enumerate(reversed(table_data)):
            # separator
            separator = ttk.Separator(self.frame, orient="horizontal")
            separator.grid(row=i+1, column=0, columnspan=7, sticky="enw")
            # id
            data_id = str(data[0])
            self.row_label(data_id, row=i+1, col=0)
            # date
            date = f"{data[3]}/{data[2]}/{data[1]}"
            self.row_label(date, row=i+1, col=1)
            # amount
            amount = str(round(data[4], 2))
            self.row_label(amount, row=i+1, col=2)
            # collector
            collector = data[5]
            self.row_label(collector, row=i+1, col=3)
            # payment method
            pmethod = data[6]
            self.row_label(pmethod, row=i+1, col=4)
            # periodic
            periodic = data[7]
            self.row_label(periodic, row=i+1, col=5)
            # description
            description = data[8][0:50-1]
            self.row_label(description, row=i+1, col=6)

    def row_label(self, label_text, row, col):
        """
        Place the row information in the table
        :param label_text: text to be written
        :param row: i position
        :param col: j position
        """
        label = customtkinter.CTkLabel(master=self.frame, text=label_text, font=self.font_params.text_font)
        label.grid(row=row, column=col, padx=5, pady=5, sticky="ns")

    def destroy_data_table(self):
        self.frame.destroy()


class DataEntryWidget:
    """
    Widget interface to entry the data.
    :param database_obj: It contains the parameters: username, container,
    client_database and every widget place in the database-gui
    """
    def __init__(self, database_obj):
        """self.root = root
        self.client_db = client_db
        self.database_frame = root.db_frame # frame de la tabla"""
        self.database_obj = database_obj
        # Frame creation and positioning.
        self.frame = customtkinter.CTkFrame(master=database_obj.container)
        # Place the data entry widget in the container frame.
        self.frame.grid(row=0, column=2, rowspan=2, padx=5, pady=5, sticky="new")
        # Grid settings: (7, 2) -> (rows, cols)
        self.frame.columnconfigure((0, 1), weight=1)
        self.frame.rowconfigure((0, 1, 2, 3, 4, 5, 6), weight=1)

        # Connect to the database to add the new expense.
        self.client_database = database_obj.client_database

        # Widget creation:
        font_params = FontParams()
        # Amount --------------
        amount_label = customtkinter.CTkLabel(master=self.frame,
                                              text="Amount", font=font_params.header_font)
        amount_label.grid(row=0, column=0, padx=5, pady=5)

        amount = customtkinter.StringVar()
        self.amount_entry = customtkinter.CTkEntry(master=self.frame,
                                                   font=font_params.text_font, textvariable=amount)
        self.amount_entry.grid(row=1, column=0, padx=5, pady=5)

        # Collector -----------
        collector_label = customtkinter.CTkLabel(master=self.frame,
                                                 text="Collector", font=font_params.header_font)
        collector_label.grid(row=0, column=1, padx=5, pady=5)

        self.collector_default_values = get_collector_values()
        self.collector_entry = customtkinter.CTkComboBox(master=self.frame,
                                                         font=font_params.text_font,
                                                         values=self.collector_default_values)
        self.collector_entry.grid(row=1, column=1, padx=5, pady=5)

        # Payment Method -------
        pm_label = customtkinter.CTkLabel(master=self.frame,
                                          text="Payment\nMethod", font=font_params.header_font)
        pm_label.grid(row=2, column=0, padx=5, pady=5)
        # Frame to place the radio buttons in:
        pm_frame = customtkinter.CTkFrame(master=self.frame)
        pm_frame.grid(row=3, column=0, padx=2, pady=2)
        # Add radio buttons to the frame:
        self.pm_radio_btns = RadioButton(pm_frame, "Cash", "Card")

        # Periodic Payment -------
        periodic_label = customtkinter.CTkLabel(master=self.frame,
                                                text="Periodic\nPayment", font=font_params.header_font)
        periodic_label.grid(row=2, column=1, padx=2, pady=2)
        # Frame to place the radio buttons in:
        periodic_frame = customtkinter.CTkFrame(master=self.frame)
        periodic_frame.grid(row=3, column=1, padx=5, pady=5)
        # Add radio buttons to the frame:
        self.periodic_radio_btns = RadioButton(periodic_frame, "True", "False")

        # Description -------------
        description_label = customtkinter.CTkLabel(master=self.frame,
                                                   text="Description", font=font_params.header_font)
        description_label.grid(row=4, column=0, padx=5, pady=5)

        self.description_entry = customtkinter.CTkTextbox(master=self.frame,
                                                          font=font_params.text_font, height=100)
        self.description_entry.grid(row=5, column=0, columnspan=2,
                                    padx=5, pady=5, sticky="wen")
        # Add button --------------
        add_btn = customtkinter.CTkButton(master=self.frame,
                                          text="Add", font=font_params.text_font, width=10,
                                          command=self.add_entry)
        add_btn.grid(row=6, column=1, pady=5, padx=5, sticky="e")

    def add_entry(self):
        """Collect the entry values and add them to the DB."""
        try:
            # Get the amount
            amount = round(float(self.amount_entry.get()), 2)
            # Get the collector
            collector = self.collector_entry.get().capitalize()
            save_new_collector(collector)
            # Get the payment method
            payment_method = payment_to_str(self.pm_radio_btns.radio_var.get())
            expense_type = periodic_to_str(self.periodic_radio_btns.radio_var.get())
            # Get the expense description
            description = self.description_entry.get("1.0", "end-1c")
            description = check_description_len(description)

            # Add new entry to the DB. --------------------------------
            self.client_database.add_expense(amount, collector, payment_method, expense_type, description)
            messagebox.showinfo(title="Expense Added", message="Expense added successfully")

            # reload database and data entry frame
            time.sleep(0.5)
            self.database_obj.destroy_data_table()
            self.database_obj.init_data_table()
            self.database_obj.destroy_data_entry()
            self.database_obj.init_data_entry()

        except ValueError:
            messagebox.showerror(title="Error", message="Check the values")

    def reset_entry_values(self):
        self.amount_entry.delete(0, customtkinter.END)
        self.amount_entry.delete(0, customtkinter.END)
        self.description_entry.delete("1.0", customtkinter.END)

    def destroy_entry_widget(self):
        self.frame.destroy()


class DeleteWidget:
    """
    Delete an entry of the database.
    :param database_obj: It contains the parameters: username, container,
    client_database and every widget place in the database-gui
    """
    def __init__(self, database_obj):
        self.database_obj = database_obj
        # Frame creation and positioning
        frame = customtkinter.CTkFrame(master=database_obj.container)
        # Place the widget frame in the container
        frame.grid(row=1, column=2, padx=5, pady=5, ipady=10, sticky="sew")
        # Grid config (1, 4) -> rows, cols
        frame.columnconfigure((0, 1, 2, 3), weight=1)
        frame.rowconfigure(0, weight=1)

        # Connect to the client database
        self.client_database = database_obj.client_database

        font_params = FontParams()
        # Delete label ------------------
        del_label = customtkinter.CTkLabel(frame, text="Delete ID: ", font=font_params.header_font)
        del_label.grid(row=0, column=0, ipadx=5)
        # Delete entry ------------------
        expense_id = customtkinter.IntVar()
        self.del_entry = customtkinter.CTkEntry(frame, font=font_params.text_font,
                                                width=50, textvariable=expense_id)
        self.del_entry.grid(row=0, column=1, columnspan=2, ipadx=60)
        # Ok button    ------------------
        del_ok_btn = customtkinter.CTkButton(frame, text="Ok", font=font_params.text_font,
                                             width=10, command=self.del_entry_func)
        del_ok_btn.grid(row=0, column=3)

    def del_entry_func(self):
        """Delete the id-entry from the client database."""
        expense_id = self.del_entry.get()
        answer = messagebox.askquestion(title="Delete Entry",
                                        message=f"Do you want to delete expense Id={expense_id} ?")
        if answer == "yes":
            self.client_database.delete_expense(expense_id)
            # reload database and data entry frame
            self.database_obj.destroy_data_table()
            self.database_obj.init_data_table()



