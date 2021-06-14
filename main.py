# Zoe Erispe, Class 1
from tkinter import *
from tkinter import messagebox
import datetime
from datetime import date

from playsound import playsound

root = Tk()
# Creating a title
root.title('Lotto Generator')
# Setting the window size
root.geometry("700x400")
# Setting a background color
root.config(bg="#4ad66d")

name = Label(root, text='Please enter your name:', width=25)
name.place(relx=0.2, rely=0.1)

name_entry = Entry(root, width=20)
name_entry.place(relx=0.51, rely=0.1)

email = Label(root, text='Please enter your email:', width=25)
email.place(relx=0.2, rely=0.2)

email_entry = Entry(root, width=20)
email_entry.place(relx=0.51, rely=0.2)

id = Label(root, text='Please enter your ID number:', width=25)
id.place(relx=0.2, rely=0.3)

id_entry = Entry(root, width=20)
id_entry.place(relx=0.51, rely=0.3)


def valid_id():
    try:
        int(id_entry.get())
        ID = id_entry.get()
        user = name_entry.get()
        mail = email_entry.get()
        current_date = date
        if user == "" or user == int:
            messagebox.showerror(message='Please enter your real name')
        if mail == "":
            messagebox.showerror(message='Please enter an email address')
        if len((id_entry.get())) != 13 or len(id_entry.get()) < 13:
            raise ValueError
        if 22 <= int(ID[0:2]) <= 99:
            messagebox.showinfo(message='You qualify to play!')
            root.destroy()
            import window_2
        elif 3 >= int(ID[0:2]):
            # if int(ID[0:4]) >= current_date:
                messagebox.showinfo(message='You qualify to play!')
                root.destroy()
                import window_2
        else:
            messagebox.showerror(message='You are underage. Try again when you are 18.')
    except ValueError:
        messagebox.showerror(message='Enter a valid ID number.')

# def user_id():
#     try:
#         user = name_entry.get()
#         ID = id_entry.get()
#         if user == "" or ID == "":
#             raise ValueError
#         else user[0] + str(ID[9:13]) = user_id()



submit_button = Button(root, text='Submit', command=valid_id, width=10)
submit_button.place(relx=0.25, rely=0.4)

exit_button = Button(root, text='Exit', command='exit', width=10)
exit_button.place(relx=0.55, rely=0.4)

print(date.today())

root.mainloop()