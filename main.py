# Zoe Erispe, Class 1
import datetime
from tkinter import *
from tkinter import messagebox
import rsaidnumber
from dateutil import relativedelta
from datetime import *

from playsound import playsound

master = Tk()
# Creating a title
master.title('Lotto Generator')
# Setting the window size
master.geometry("700x400")
# Setting a background color
master.config(bg="#4ad66d")


class LogIn:
    def __init__(self, root):
        self.root = root

        self.name = Label(root, text='Please enter your name:', width=25)
        self.name.place(relx=0.2, rely=0.1)
        self.name_entry = Entry(root, width=20)
        self.name_entry.place(relx=0.51, rely=0.1)

        self.email = Label(root, text='Please enter your email:', width=25)
        self.email.place(relx=0.2, rely=0.2)
        self.email_entry = Entry(root, width=20)
        self.email_entry.place(relx=0.51, rely=0.2)

        self.id = Label(root, text='Please enter your ID number:', width=25)
        self.id.place(relx=0.2, rely=0.3)
        self.id_entry = Entry(root, width=20)
        self.id_entry.place(relx=0.51, rely=0.3)

        self.submit_button = Button(root, text='Submit', command=self.valid_id, width=10)
        self.submit_button.place(relx=0.25, rely=0.4)

        self.exit_button = Button(root, text='Exit', command='exit', width=10)
        self.exit_button.place(relx=0.55, rely=0.4)

    def valid_id(self):
        try:
            int(self.id_entry.get())
            ID = self.id_entry.get()
            user = self.name_entry.get()
            mail = self.email_entry.get()
            current_date = datetime.today()
            birthday = rsaidnumber.parse(ID).date_of_birth
            if user == "" or user == "":
                messagebox.showerror(message='Please enter your real name')
            if mail == "":
                messagebox.showerror(message='Please enter an email address')
            if "@" and "." not in mail:
                messagebox.showerror(message='Enter a valid email address')
            if len((self.id_entry.get())) != 13:
                raise ValueError
            elif relativedelta.relativedelta(current_date, birthday).years >= 18:
                messagebox.showinfo(message="You qualify to play! Let's get started.")
                self.root.destroy()
                import window_2
            else:
                messagebox.showerror(message='You are underage. Try again when you are 18.')
        except ValueError:
            messagebox.showerror(message='Enter a valid ID number.')


LogIn(master)
master.mainloop()