from tkinter import *
from tkinter import messagebox
from random import randint

import main

master = Tk()
# Creating a title
master.title('Lotto Generator')
# Setting the window size
master.geometry("700x700")
# Setting a background color
master.config(bg="#4ad66d")


class UserID:
    def __init__(self, root):
        self.root = root
        self.user_id = Label(root, text='User ID')
        self.user_id.place(relx=0.8, rely=0.1)
        self.user_id_entry = Entry(root, state='readonly')

    def user_id(self):
        user = main.LogIn.root.name_entry.get()
        ID = main.LogIn.self.id_entry.get()
        user_name = user + ID[9:-1]
        self.user_id_entry.config(state='normal')
        self.user_id_entry.insert(0, user_name)
        self.user_id_entry(state='readonly')


class Lotto:
    def __init__(self, root):
        self.select = Label(root, text='Select your lucky Lotto numbers:')
        self.select.place(relx=0.2, rely=0.2)

        self.num1 = Spinbox(root, from_=0, to=49, width=5, font=10)
        self.num1.place(relx=0.2, rely=0.3)

        self.num2 = Spinbox(root, from_=0, to=49, width=5, font=10)
        self.num2.place(relx=0.3, rely=0.3)

        self.num3 = Spinbox(root, from_=0, to=49, width=5, font=10)
        self.num3.place(relx=0.4, rely=0.3)

        self.num4 = Spinbox(root, from_=0, to=49, width=5, font=10)
        self.num4.place(relx=0.5, rely=0.3)

        self.num5 = Spinbox(root, from_=0, to=49, width=5, font=10)
        self.num5.place(relx=0.6, rely=0.3)

        self.num6 = Spinbox(root, from_=0, to=49, width=5, font=10)
        self.num6.place(relx=0.7, rely=0.3)

        self.play_again = Button(root, text='Play again')
        self.play_again.place(relx=0.2, rely=0.4)

        self.reveal_lotto = Button(root, text='Reveal Lotto numbers', command=self.generate_lotto)
        self.reveal_lotto.place(relx=0.5, rely=0.4)

        self.lotto_label = Label(root, text='The winning Lotto numbers are:')
        self.lotto_label.place(relx=0.2, rely=0.6)

        self.lotto1 = Entry(root, bg='#d62e2e', state='readonly', width=5, font=10)
        self.lotto1.place(relx=0.2, rely=0.7)

        self.lotto2 = Entry(root, bg='#fc852a', state='readonly', width=5, font=10)
        self.lotto2.place(relx=0.3, rely=0.7)

        self.lotto3 = Entry(root, bg='#f6f841', state='readonly', width=5, font=10)
        self.lotto3.place(relx=0.4, rely=0.7)

        self.lotto4 = Entry(root, bg='#60c54d', state='readonly', width=5, font=10)
        self.lotto4.place(relx=0.5, rely=0.7)

        self.lotto5 = Entry(root, bg='#4cb4c5', state='readonly', width=5, font=10)
        self.lotto5.place(relx=0.6, rely=0.7)

        self.lotto6 = Entry(root, bg='#c659e7', state='readonly', width=5, font=10)
        self.lotto6.place(relx=0.7, rely=0.7)

        self.lotto_numbers = []
        for x in range(6):
            self.lotto_numbers.append(randint(1, 49))
            if randint(1, 49) in self.lotto_numbers:
                self.lotto_numbers.remove(randint(1, 49))
            print(self.lotto_numbers)

    def replay(self, entry_list):
        entry_list.append([self.num1.get(), self.num2.get(), self.num3.get(), self.num4.get(), self.num5.get(),
                           self.num6.get()])
        print(entry_list)
        yes_no = messagebox.askyesno(message='Are you sure you would like to play again?')
        if yes_no:
            self.num1.delete(0, 'end')
            self.num2.delete(0, 'end')
            self.num3.delete(0, 'end')
            self.num4.delete(0, 'end')
            self.num5.delete(0, 'end')
            self.num6.delete(0, 'end')

            self.num1.insert(0, 1)
            self.num2.insert(0, 1)
            self.num3.insert(0, 1)
            self.num4.insert(0, 1)
            self.num5.insert(0, 1)
            self.num6.insert(0, 1)

        else:
            pass

    def generate_lotto(self):
        self.lotto1.config(state='normal')
        self.lotto1.insert(0, self.lotto_numbers[0])
        self.lotto1.config(state='readonly')

        self.lotto2.config(state='normal')
        self.lotto2.insert(0, self.lotto_numbers[1])
        self.lotto2.config(state='readonly')

        self.lotto3.config(state='normal')
        self.lotto3.insert(0, self.lotto_numbers[2])
        self.lotto3.config(state='readonly')

        self.lotto4.config(state='normal')
        self.lotto4.insert(0, self.lotto_numbers[3])
        self.lotto4.config(state='readonly')

        self.lotto5.config(state='normal')
        self.lotto5.insert(0, self.lotto_numbers[4])
        self.lotto5.config(state='readonly')

        self.lotto6.config(state='normal')
        self.lotto6.insert(0, self.lotto_numbers[5])
        self.lotto6.config(state='readonly')


UserID(master)
Lotto(master)
master.mainloop()
