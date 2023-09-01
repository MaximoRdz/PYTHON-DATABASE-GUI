import os
import sqlite3

from database.utils import get_date


class Database:
    def __init__(self, username):
        """Init the user expenses database."""
        self.user_db = username+".db"

    def create_database(self):
        """Create the relational database to save the expenses."""
        # create connection
        conn = sqlite3.connect(self.user_db)
        cursor = conn.cursor()
        # create the table
        sql_create = """CREATE TABLE IF NOT EXISTS expenses (
                            id INTEGER PRIMARY KEY AUTOINCREMENT, 
                            year INTEGER,
                            month INTEGER,
                            day INTEGER,
                            amount REAL,
                            collector TEXT,
                            payment_method TEXT,
                            expense_type TEXT,
                            description TEXT               
                            );"""
        cursor.execute(sql_create)
        conn.close()

    def create_connection(self):
        """
        Create the connection to an existing database or if not exists
        create first the database and then the connection.
        :return: sqlite3 connection to self.user_db
        """
        if not os.path.isfile(self.user_db):
            self.create_database()

        return sqlite3.connect(self.user_db)

    def add_expense(self, amount, collector, payment_method, expense_type, description):
        """
        Query to add an entry to the expenses table
        :param amount: money spent float
        :param collector: person/institution that receives the money
        :param payment_method: card/cash
        :param expense_type: one-time/periodic
        :param description: expense description
        :return: None
        """
        year, month, day = get_date()
        conn = self.create_connection()
        cursor = conn.cursor()
        sql_entry = """INSERT INTO expenses (year, month, day, amount, collector, 
                                             payment_method, expense_type, description)
                        VALUES (?, ?, ?, ?, ?, ?, ?, ?)"""
        values = year, month, day, amount, collector, payment_method, expense_type, description
        cursor.execute(sql_entry, values)
        conn.commit()
        conn.close()

    def delete_expense(self, expense_id):
        """
        Delete an entry of the expense table via entry id.
        :param expense_id: expense to be deleted.
        :return: None
        """
        conn = self.create_connection()
        cursor = conn.cursor()
        sql_delete = f"""DELETE FROM expenses WHERE id={expense_id}"""
        cursor.execute(sql_delete)
        conn.commit()
        conn.close()

    def get_expense_info(self, expense_id):
        """
        Fetch the information of the expense_id entry.
        :param expense_id: expense id.
        :return: tuple (id, year, month, day, amount, collector,
                        payment_method, expense_type, description)
        """
        conn = self.create_connection()
        cursor = conn.cursor()
        sql_get = f"""SELECT * FROM expenses WHERE id={expense_id}"""
        cursor.execute(sql_get)
        expense_info = cursor.fetchall()
        conn.close()
        return expense_info[0]

    def update_expense(self, new_expense_info):
        """
        Update the changeable (amount, collector, payment_method,
        expense_type, description) information of an entry.
        :param new_expense_info: tuple (id, year, month, day, amount, collector,
                                        payment_method, expense_type, description)
        :return:
        """
        expense_id, year, month, day, *change_info = new_expense_info
        conn = self.create_connection()
        cursor = conn.cursor()
        sql_update = """UPDATE expenses 
                        SET amount={}, collector="{}",
                        payment_method="{}", 
                        expense_type="{}", 
                        description="{}"
                        WHERE id={}""".format(*change_info, expense_id)
        cursor.execute(sql_update)
        conn.commit()
        conn.close()

    def get_gui_info(self, display_lim):
        """
        Get the last display_lim rows of the expenses table that will be displayed
        on the gui
        :param display_lim: integer, number of rows to select
        :return: list of rows [(row1 info), (row2 info), ...]
        """
        conn = self.create_connection()
        cursor = conn.cursor()
        sql_get = f"""SELECT * FROM expenses 
                      ORDER BY id DESC
                      LIMIT {display_lim}"""
        cursor.execute(sql_get)
        gui_info = cursor.fetchall()
        conn.close()
        return gui_info
