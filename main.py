# Zoe Erispe, Class 1
import datetime
from tkinter import *
from tkinter import messagebox
import rsaidnumber
from dateutil import relativedelta
from datetime import *
import validate_email

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

        self.img = PhotoImage(file='lotto-balls-removebg-preview.png')
        self.image_label = Label(self.root, image=self.img)
        self.img = self.img.subsample(10)
        self.image_label.place(relx=0.5, rely=0.1)

        self.header = Label(self.root, text='Lotto Generator', fg='#506352', bg='#4ad66d', font=25)
        self.header.place(relx=0.23, rely=0.1)

        self.name = Label(self.root, text='Please enter your name:', width=25, fg='#506352', bg='#4ad66d')
        self.name.place(relx=0.2, rely=0.2)
        self.name_entry = Entry(self.root, width=20)
        self.name_entry.place(relx=0.51, rely=0.2)

        self.email = Label(self.root, text='Please enter your email:', width=25, fg='#506352', bg='#4ad66d')
        self.email.place(relx=0.2, rely=0.3)
        self.email_entry = Entry(self.root, width=20)
        self.email_entry.place(relx=0.51, rely=0.3)

        self.id = Label(self.root, text='Please enter your ID number:', width=25, fg='#506352', bg='#4ad66d')
        self.id.place(relx=0.2, rely=0.4)
        self.id_entry = Entry(self.root, width=20)
        self.id_entry.place(relx=0.51, rely=0.4)

        self.submit_button = Button(self.root, text='Submit', command=self.valid_id, width=10, fg='#506352', bg='#47b553')
        self.submit_button.place(relx=0.25, rely=0.5)

        self.exit_button = Button(self.root, text='Exit', command='exit', width=10, fg='#506352', bg='#47b553')
        self.exit_button.place(relx=0.55, rely=0.5)

        self.root.mainloop()

    def valid_id(self):
        try:
            int(self.id_entry.get())
            ID = self.id_entry.get()
            user = self.name_entry.get()
            mail = self.email_entry.get()
            current_date = datetime.today()
            birthday = rsaidnumber.parse(ID).date_of_birth
            if user == "":
                messagebox.showerror(message='Please enter your name')
            elif mail == "":
                messagebox.showerror(message='Please enter your email address')
            elif not validate_email.validate_email(mail, verify=True):
                messagebox.showerror(message='Please enter a valid email address.')
            elif len((self.id_entry.get())) != 13:
                raise ValueError
            elif relativedelta.relativedelta(current_date, birthday).years >= 18:
                info_entered = {'name': user, 'email': mail, 'id': ID}
                self.text_to_file(info_entered)
                player_id = user + ID[9:-1]
                self.text_to_file2(player_id)
                messagebox.showinfo(message="You qualify to play! Let's get started.")
                self.root.destroy()
                import window_2
            else:
                messagebox.showerror(message='You are underage. Try again when you are 18.')
        except ValueError:
            messagebox.showerror(message='Enter a valid ID number.')

    def text_to_file(self, text):
        with open('user_info.txt', 'a') as user_info:
            user_info.write(str(text))

    def text_to_file2(self, text):
        with open('user_id.txt', 'a') as user_id:
            user_id.write("User ID: {}\n".format(str(text)))


LogIn(master)
