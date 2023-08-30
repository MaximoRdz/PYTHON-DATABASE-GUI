import os
import customtkinter

from tkinter import messagebox

import gui.constants as ct


def periodic_to_str(periodic_num):
    """
    Convert 1/0 into False/True str
    :param periodic_num: integer 0 or 1.
    """
    return str(not periodic_num)


def payment_to_str(payment_num):
    """Convert 0/1 into Cash/Card string."""
    if payment_num:
        return "Card"
    else:
        return "Cash"

# def zero_to_one(num):
#     """Given num 0 or 1 returns 1 or 0 respectively."""
#     return int(not num)


def get_collector_values():
    """Get the collector saved values from a txt file."""
    try:
        collector_values = list()
        with open("collector.txt", "r") as file:
            for line in file:
                collector_values.append(line)
        return collector_values
    except FileNotFoundError:
        with open("collector.txt", "w") as file:
            file.write("")
        return [""]


def save_new_collector(new_collector):
    """If the new collector is not in the saved list add it"""
    if new_collector not in get_collector_values():
        with open("collector.txt", "a") as file:
            file.write("\n" + new_collector)


def check_description_len(description):
    """Check the text length and return a clipped version if needed."""
    if len(description) > ct.DESCRIPTION_DISPLAY_LEN:
        description = description[0:ct.DESCRIPTION_DISPLAY_LEN - 1]
        messagebox.showinfo(title="Text Length", message="The text has been shorten to fit "
                                                         "in the table but it will be save "
                                                         "complete in the database.")
    return description


class FontParams:
    """Font properties family and size."""
    def __init__(self):
        self.text_font = customtkinter.CTkFont(family="helvetica", size=ct.FONTSIZE_TEXT)
        self.header_font = customtkinter.CTkFont(family="helvetica", size=ct.FONTSIZE_HEADER, weight="bold")


class RadioButton:
    """
    Radio button widget.
    :container: frame to place the radio buttons in.
    :args: list with the text name of each button.
    """
    def __init__(self, container, *args):
        font_params = FontParams()
        self.btns = list()    # list that contains every button object.
        args_len = len(args)
        self.radio_var = customtkinter.IntVar()
        # set the grid with 1 column and 1 row for every radio button.
        container.columnconfigure(0, weight=1)
        container.rowconfigure(tuple([i for i in range(1, args_len+1)]), weight=1)

        for i, arg in enumerate(args):
            self.btns.append(customtkinter.CTkRadioButton(master=container,
                                                          text=arg, font=font_params.text_font,
                                                          value=i, variable=self.radio_var))
            self.btns[i].grid(row=i, column=0, padx=5, pady=5)





