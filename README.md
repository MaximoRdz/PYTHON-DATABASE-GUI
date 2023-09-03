## Python DataBase GUI
This project uses PYTHON's Tkinter library to create a user interface 
that enables the user to keep track of its expenses saving the information
in a well structure database. The app includes the "delete" and "update"
features so entries can be easily modify.

## Tutorial
### Add
<img width="500" alt="add" src="https://github.com/MaximoRdz/PYTHON-DATABASE-GUI/blob/main/images/add_expense.gif">

### Delete and Update
### Packages 
* `database`: Module required to create and manage the database.
* `gui`: Necessary modules to define the user interface.
  * `app`: Main body of the application.
  * `widget_utils`: Floating widgets (data entry, data display, data update and data delete).
### Technologies used
![Tkinter](https://img.shields.io/badge/Tkinter-4B8BBE?style=for-the-badge&logo=tkinter&logoColor=white)
![CustomTkinter](https://img.shields.io/badge/CustomTkinter-4B8BBE?style=for-the-badge&logo=tkinter&logoColor=white)

![SQLite3](https://img.shields.io/badge/SQLite3-003B57?style=for-the-badge&logo=sqlite&logoColor=white)

#### TODO
- ✅ Create database for new clients if username is not register.
- ✅ Compartmentalize everything in classes to allow cross functionality among frames.
- ✅ Self executing file for windows.
- ✅ Automatically fill the old expense info when updating it (PopWindow).
- ✅ Increase the collector list if it is one not previously used.
- ✅ README app instructions.
- ⬜ Pretiffy text entries.
- ⬜ Check if the selected expense index is real. If not raise error window.
- ⬜ Previous and Next buttons bellow the expenses' display table.
