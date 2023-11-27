## Python DataBase GUI
This project uses PYTHON's Tkinter library to create a user interface 
that enables the user to keep track of its expenses saving the information
in a well structure database. The app includes the "delete" and "update"
features so entries can be easily modify.

## Tutorial
The app track 4 attributes per expense: `Amount | Collector | Payment Method | Payment Type | Description`.
### Add
Here it is a simple example of how to add an entry to the database. Take into account that every attribute is sensitive
to the type of variable is introduced (`Amount` [float], `Collector | Description` [str]) if there is a mismatch the app 
will raise an error window so the values can be corrected.

<img width="500" alt="add" src="https://github.com/MaximoRdz/PYTHON-DATABASE-GUI/blob/main/images/add_example.gif" loading="lazy">


### Update
Entry update via `id`. Unique `id` and `date` remain untouched.

<img width="500" alt="add" src="https://github.com/MaximoRdz/PYTHON-DATABASE-GUI/blob/main/images/update_example.gif" loading="lazy">

### Delete
Entry delete via `id`.

<img width="500" alt="add" src="https://github.com/MaximoRdz/PYTHON-DATABASE-GUI/blob/main/images/delete.gif" loading="lazy">

### Packages 
* `database`: Module required to create and manage the database. ([here](https://github.com/MaximoRdz/PYTHON-DATABASE-GUI/tree/main/database))
* `gui`: Necessary modules to define the user interface. ([here](https://github.com/MaximoRdz/PYTHON-DATABASE-GUI/tree/main/gui))

## Technologies used
![Tkinter](https://img.shields.io/badge/Tkinter-4B8BBE?style=for-the-badge&logo=tkinter&logoColor=white)
![CustomTkinter](https://img.shields.io/badge/CustomTkinter-4B8BBE?style=for-the-badge&logo=tkinter&logoColor=white)

![SQLite3](https://img.shields.io/badge/SQLite3-003B57?style=for-the-badge&logo=sqlite&logoColor=white)

## TODO
- ✅ Create database for new clients if username is not register.
- ✅ Compartmentalize everything in classes to allow cross functionality among frames.
- ✅ Self executing file for windows.
- ✅ Automatically fill the old expense info when updating it (PopWindow).
- ✅ Increase the collector list if it is one not previously used.
- ✅ README app instructions.
- ⬜ Pretiffy text entries.
- ⬜ Check if the selected expense index is real. If not raise error window.
- ⬜ Previous and Next buttons bellow the expenses' display table.
- ⬜ Create test cases `pytest`. 
