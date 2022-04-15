"""
A program that stores this book information:

Title, Author
Year, ISBN

User can:

View all records
Search an entry
Add entry
Update entry
Delete and entry
Close the app
"""

from tkinter import *
import back_end


def get_selected_row(event):
    global selected_tuple
    try:
        index = list1.curselection()[0]
        selected_tuple = list1.get(index)
        entry1.delete(0, END)
        entry1.insert(END, selected_tuple[1])
        entry2.delete(0, END)
        entry2.insert(END, selected_tuple[2])
        entry3.delete(0, END)
        entry3.insert(END, selected_tuple[3])
        entry4.delete(0, END)
        entry4.insert(END, selected_tuple[4])
    except IndexError:
        pass


def view_command():
    list1.delete(0, END)
    for row in back_end.view():
        list1.insert(END, row)


def search_command():
    list1.delete(0, END)
    for row in back_end.search(title_text.get(), author_text.get(), year_text.get(), isbn_text.get()):
        list1.insert(END, row)


def add_command():
    back_end.insert(title_text.get(), author_text.get(), year_text.get(), isbn_text.get())
    list1.delete(0, END)
    list1.insert(END, (title_text.get(), author_text.get(), year_text.get(), isbn_text.get()))


def update_command():
    back_end.update(selected_tuple[0], title_text.get(), author_text.get(), year_text.get(), isbn_text.get())
    list1.delete(0, END)
    list1.insert(END, (title_text.get(), author_text.get(), year_text.get(), isbn_text.get()))


def delete_command():
    back_end.delete(selected_tuple[0])


# create main window
window = Tk()

window.wm_title("BookStore")
# create label for Title entry
label1 = Label(window, text="Title")
label1.grid(row=0, column=0)

# create label for Author entry
label2 = Label(window, text="Author")
label2.grid(row=0, column=2)

# create label for Year entry
label3 = Label(window, text="Year")
label3.grid(row=1, column=0)

# create label for ISBN entry
label4 = Label(window, text="ISBN")
label4.grid(row=1, column=2)

# create cell to enter value for Title
title_text = StringVar()
entry1 = Entry(window, textvariable=title_text)
entry1.grid(row=0, column=1)

# create cell to enter value for Author
author_text = StringVar()
entry2 = Entry(window, textvariable=author_text)
entry2.grid(row=0, column=3)

# create cell to enter value for Year
year_text = StringVar()
entry3 = Entry(window, textvariable=year_text)
entry3.grid(row=1, column=1)

# create cell to enter value for ISBN
isbn_text = StringVar()
entry4 = Entry(window, textvariable=isbn_text)
entry4.grid(row=1, column=3)

# create the listbox where to show all the results
list1 = Listbox(window, height=6, width=35)
list1.grid(row=2, column=0, rowspan=6, columnspan=2)

# create a scrollbar for the list
scroll_bar1 = Scrollbar(window)
scroll_bar1.grid(row=2, column=2, rowspan=6)

# attach a scrollbar to the list
list1.configure(yscrollcommand=scroll_bar1.set)
scroll_bar1.configure(command=list1.yview)

list1.bind("<<ListboxSelect>>", get_selected_row)

# add all the buttons
# button for viewing all records
button1 = Button(window, text="View all", width=12, command=view_command)
button1.grid(row=2, column=3)

# button for Searching an entry
button2 = Button(window, text="Search entry", width=12, command=search_command)
button2.grid(row=3, column=3)

# button for Adding an entry
button3 = Button(window, text="Add entry", width=12, command=add_command)
button3.grid(row=4, column=3)

# button for Updating an entry
button4 = Button(window, text="Update selected", width=12, command=update_command)
button4.grid(row=5, column=3)

# button for deleting an entry
button5 = Button(window, text="Delete selected", width=12, command=delete_command)
button5.grid(row=6, column=3)

# button for closing the app
button6 = Button(window, text="Close", width=12, command=window.destroy)
button6.grid(row=7, column=3)

# make the main window remain open
window.mainloop()
