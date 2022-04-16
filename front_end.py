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
from back_end import BooksDatabase


class Window:
    def __init__(self, db):
        self.selected_tuple = None
        self.db = db
        # create main window
        self.window = Tk()

        self.window.wm_title("BookStore")
        # create label for Title entry
        label1 = Label(self.window, text="Title")
        label1.grid(row=0, column=0)

        # create label for Author entry
        label2 = Label(self.window, text="Author")
        label2.grid(row=0, column=2)

        # create label for Year entry
        label3 = Label(self.window, text="Year")
        label3.grid(row=1, column=0)

        # create label for ISBN entry
        label4 = Label(self.window, text="ISBN")
        label4.grid(row=1, column=2)

        # create cell to enter value for Title
        self.title_text = StringVar()
        self.entry1 = Entry(self.window, textvariable=self.title_text)
        self.entry1.grid(row=0, column=1)

        # create cell to enter value for Author
        self.author_text = StringVar()
        self.entry2 = Entry(self.window, textvariable=self.author_text)
        self.entry2.grid(row=0, column=3)

        # create cell to enter value for Year
        self.year_text = StringVar()
        self.entry3 = Entry(self.window, textvariable=self.year_text)
        self.entry3.grid(row=1, column=1)

        # create cell to enter value for ISBN
        self.isbn_text = StringVar()
        self.entry4 = Entry(self.window, textvariable=self.isbn_text)
        self.entry4.grid(row=1, column=3)

        # create the listbox where to show all the results
        self.list1 = Listbox(self.window, height=6, width=35)
        self.list1.grid(row=2, column=0, rowspan=6, columnspan=2)

        # create a scrollbar for the list
        scroll_bar1 = Scrollbar(self.window)
        scroll_bar1.grid(row=2, column=2, rowspan=6)

        # attach a scrollbar to the list
        self.list1.configure(yscrollcommand=scroll_bar1.set)
        scroll_bar1.configure(command=self.list1.yview)

        self.list1.bind("<<ListboxSelect>>", self.get_selected_row)

        # add all the buttons
        # button for viewing all records
        button1 = Button(self.window, text="View all", width=12, command=self.view_command)
        button1.grid(row=2, column=3)

        # button for Searching an entry
        button2 = Button(self.window, text="Search entry", width=12, command=self.search_command)
        button2.grid(row=3, column=3)

        # button for Adding an entry
        button3 = Button(self.window, text="Add entry", width=12, command=self.add_command)
        button3.grid(row=4, column=3)

        # button for Updating an entry
        button4 = Button(self.window, text="Update selected", width=12, command=self.update_command)
        button4.grid(row=5, column=3)

        # button for deleting an entry
        button5 = Button(self.window, text="Delete selected", width=12, command=self.delete_command)
        button5.grid(row=6, column=3)

        # button for closing the app
        button6 = Button(self.window, text="Close", width=12, command=self.close_command)
        button6.grid(row=7, column=3)

        # make the main window remain open
        self.window.mainloop()

    def get_selected_row(self, event):
        try:
            index = self.list1.curselection()[0]
            self.selected_tuple = self.list1.get(index)
            self.entry1.delete(0, END)
            self.entry1.insert(END, self.selected_tuple[1])
            self.entry2.delete(0, END)
            self.entry2.insert(END, self.selected_tuple[2])
            self.entry3.delete(0, END)
            self.entry3.insert(END, self.selected_tuple[3])
            self.entry4.delete(0, END)
            self.entry4.insert(END, self.selected_tuple[4])
        except IndexError:
            pass

    def view_command(self):
        self.list1.delete(0, END)
        for row in self.db.view():
            self.list1.insert(END, row)

    def search_command(self):
        self.list1.delete(0, END)
        for row in self.db.search(self.title_text.get(), self.author_text.get(),
                                  self.year_text.get(), self.isbn_text.get()):
            self.list1.insert(END, row)

    def add_command(self):
        self.db.insert(self.title_text.get(), self.author_text.get(), self.year_text.get(), self.isbn_text.get())
        self.list1.delete(0, END)
        self.list1.insert(END, (self.title_text.get(), self.author_text.get(),
                                self.year_text.get(), self.isbn_text.get()))

    def update_command(self):
        self.db.update(self.selected_tuple[0], self.title_text.get(), self.author_text.get(),
                       self.year_text.get(), self.isbn_text.get())
        self.list1.delete(0, END)
        self.list1.insert(END, (self.title_text.get(), self.author_text.get(),
                                self.year_text.get(), self.isbn_text.get()))

    def delete_command(self):
        self.db.delete(self.selected_tuple[0])

    def close_command(self):
        self.db.close()
        self.window.destroy()


if __name__ == "__main__":
    database = BooksDatabase("books.db")
    Window(database)
