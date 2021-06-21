import random
from tkinter import *
from tkinter import messagebox
from random import randint
from playsound import playsound

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
        self.user_id = Label(root, text='User ID:', fg='#506352', bg='#4ad66d')
        self.user_id.place(relx=0.5, rely=0.1)
        self.user_id_entry = Entry(root, state='readonly')
        self.user_id_entry.place(relx=0.65, rely=0.1)
        with open('user_id.txt', 'r') as file:
            for line in file:
                if "User" in line:
                    user = line[9:-1]
            self.user_id_entry.config(state='normal')
            self.user_id_entry.insert(0, user)
            self.user_id_entry.config(state='readonly')


class Lotto:
    def __init__(self, root):
        self.root = root
        self.count = 0

        self.select = Label(root, text='Select your lucky Lotto numbers:', fg='#506352', bg='#4ad66d', font=20)
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

        self.reveal_lotto = Button(root, text='Reveal Lotto numbers', command=self.generate_lotto,
                                   fg='#506352', bg='#47b553')
        self.reveal_lotto.place(relx=0.4, rely=0.4)

        self.lotto_label = Label(root, text='The winning Lotto numbers are:', fg='#506352', bg='#4ad66d', font=20)
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

        self.play_again = Button(root, text='Play Again', fg='#506352', bg='#47b553', command=self.replay)
        self.play_again.place(relx=0.2, rely=0.8)

        self.check_numbers = Button(root, text='Are you a winner?', fg='#506352', bg='#47b553',
                                    command=self.check_lotto_numbers)
        self.check_numbers.place(relx=0.39, rely=0.8)

        self.claim_prize = Button(root, text='Claim Prize', fg='#506352', bg='#47b553', command=self.claim)
        self.claim_prize.place(relx=0.64, rely=0.8)

        self.total_lists = []

        self.lotto_numbers = []
        while len(self.lotto_numbers) < 6:
            number = random.randint(1, 49)
            if number not in self.lotto_numbers:
                self.lotto_numbers.append(number)
            print(self.lotto_numbers)

        self.total_wins = []

    def replay(self):
        yes_no = messagebox.askyesno(message='Would you like to play again?')
        if yes_no:
            self.lotto_numbers = []
            while len(self.lotto_numbers) < 6:
                number = random.randint(1, 49)
                if number not in self.lotto_numbers:
                    self.lotto_numbers.append(number)
                print(self.lotto_numbers)
            self.num1.delete(0, 'end')
            self.num2.delete(0, 'end')
            self.num3.delete(0, 'end')
            self.num4.delete(0, 'end')
            self.num5.delete(0, 'end')
            self.num6.delete(0, 'end')

            self.lotto1.config(state='normal')
            self.lotto1.delete(0, 'end')
            self.lotto1.config(state='readonly')

            self.lotto2.config(state='normal')
            self.lotto2.delete(0, 'end')
            self.lotto2.config(state='readonly')

            self.lotto3.config(state='normal')
            self.lotto3.delete(0, 'end')
            self.lotto3.config(state='readonly')

            self.lotto4.config(state='normal')
            self.lotto4.delete(0, 'end')
            self.lotto4.config(state='readonly')

            self.lotto5.config(state='normal')
            self.lotto5.delete(0, 'end')
            self.lotto5.config(state='readonly')

            self.lotto6.config(state='normal')
            self.lotto6.delete(0, 'end')
            self.lotto6.config(state='readonly')

            self.reveal_lotto.config(state='normal')

    def generate_lotto(self):
        game_lists = [self.num1.get(), self.num2.get(), self.num3.get(), self.num4.get(), self.num5.get(),
                      self.num6.get()]
        self.total_lists.clear()
        self.total_lists.append(game_lists)
        print(self.total_lists)

        self.lotto1.config(state='normal')
        self.lotto1.delete(0, 'end')
        self.lotto1.insert(0, self.lotto_numbers[0])
        self.lotto1.config(state='readonly')

        self.lotto2.config(state='normal')
        self.lotto2.delete(0, 'end')
        self.lotto2.insert(0, self.lotto_numbers[1])
        self.lotto2.config(state='readonly')

        self.lotto3.config(state='normal')
        self.lotto3.delete(0, 'end')
        self.lotto3.insert(0, self.lotto_numbers[2])
        self.lotto3.config(state='readonly')

        self.lotto4.config(state='normal')
        self.lotto4.delete(0, 'end')
        self.lotto4.insert(0, self.lotto_numbers[3])
        self.lotto4.config(state='readonly')

        self.lotto5.config(state='normal')
        self.lotto5.delete(0, 'end')
        self.lotto5.insert(0, self.lotto_numbers[4])
        self.lotto5.config(state='readonly')

        self.lotto6.config(state='normal')
        self.lotto6.delete(0, 'end')
        self.lotto6.insert(0, self.lotto_numbers[5])
        self.lotto6.config(state='readonly')

        self.reveal_lotto.config(state='disabled')

        playsound('drum-roll.mp3')

    def check_lotto_numbers(self):
        if str(self.num1.get()) == str(self.lotto1.get()):
            self.count = self.count + 1
        if str(self.num2.get()) == str(self.lotto2.get()):
            self.count = self.count + 1
        if str(self.num3.get()) == str(self.lotto3.get()):
            self.count = self.count + 1
        if str(self.num4.get()) == str(self.lotto4.get()):
            self.count = self.count + 1
        if str(self.num5.get()) == str(self.lotto5.get()):
            self.count = self.count + 1
        if str(self.num6.get()) == str(self.lotto6.get()):
            self.count = self.count + 1
        try:
            file = open('prize_money.txt', 'a')
            if self.count == 1:
                messagebox.showinfo(message="You got 1 correct number. Unfortunately you have not won anything.")
                file.write('Total 0 \n')
            elif self.count == 2:
                messagebox.showinfo(message='You got 2 correct numbers. You have won R20!')
                file.write('Total 20 \n')
            elif self.count == 3:
                messagebox.showinfo(message='You got 3 numbers correct. You have won R100,50!')
                file.write('Total 100,50 \n')
            elif self.count == 4:
                messagebox.showinfo(message='You got 4 numbers correct. You have won R2384!')
                file.write('Total 2384 \n')
            elif self.count == 5:
                messagebox.showinfo(message='You got 5 numbers correct. You have won R8584!')
                file.write('Total 8584 \n')
            elif self.count == 6:
                messagebox.showinfo(message='CONGRATULATIONS! You won the Lottery. You just earned R10 000 000!')
                file.write('Total 10000000 \n')
            else:
                messagebox.showinfo(message='You got no numbers correct. You have not won anything.')
                file.write('Total 0 \n')
            file.close()

        except ValueError:
            messagebox.showerror(message='Make sure you entered a number')

    def claim(self):
        self.root.destroy()
        import claim_prize


UserID(master)
Lotto(master)
master.mainloop()
