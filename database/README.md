## DataBase Package
This module contains the python class Database which allows us to automatize (through the GUI) every managment operation needed. It uses the `sqlite3` python's SQL implementation. 
### Database Methods
```python
def create_database(self):
        """Create the relational database to save the expenses."""

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

def delete_expense(self, expense_id):
  """
  Delete an entry of the expense table via entry id.
  :param expense_id: expense to be deleted.
  :return: None
  """

def get_expense_info(self, expense_id):
  """
  Fetch the information of the expense_id entry.
  :param expense_id: expense id.
  :return: tuple (id, year, month, day, amount, collector,
                  payment_method, expense_type, description)
  """

def update_expense(self, new_expense_info):
  """
  Update the changeable (amount, collector, payment_method,
  expense_type, description) information of an entry.
  :param new_expense_info: tuple (id, year, month, day, amount, collector,
                                  payment_method, expense_type, description)
  """

def get_gui_info(self, display_lim):
"""
  Get the last display_lim rows of the expenses table that will be displayed
  on the gui
  :param display_lim: integer, number of rows to select
  :return: list of rows [(row1 info), (row2 info), ...]
"""
```
