## Expenses control GUI
The graphic user interface is designed to first launch a user-entry frame `user_launcher.py` and then open/create the user exepenses table. Once the main app frame `..\app.py` is loaded,
every widget is represented by a python class and they work simultaneously so that is possible to reload one widget from another in order to keep the display widget up to date showing the latest database info.

The app architecture is based on the `Tkinter` package and its newer implementation `CustomTkinter`.

### Main contents
* `user_launcher.py`:

  * UsernameGui:  Get the user information and launch the database.
    
  * DatabaseGui:  Initialize the main frame of the database app.
    
* `widget_classes.py`:
  
  * DataTableWidget:  Data display widget.
    
  * DataEntryWidget:  Entry data `Amount | Collector | Payment Method | Payment Type | Description`.
    
  * DeleteWidget:  Delete entry by id.
    
  * UpdateWidget:  Raise the update widget and update old values except the entry `date` and the `expense_id`.
    
