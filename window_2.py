import random
from tkinter import *
from tkinter import messagebox
from random import randint
from playsound import playsound

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

        self.check_numbers = Button(root, text='Check Winnings', fg='#506352', bg='#47b553',
                                    command=self.check_lotto_numbers)
        self.check_numbers.place(relx=0.39, rely=0.8)

        self.claim = Button(root, text='Claim Prize', fg='#506352', bg='#47b553', command=self.claim)
        self.claim.place(relx=0.64, rely=0.8)

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

    # def replay(self, entry_list):
    #     entry_list.append([self.num1.get(), self.num2.get(), self.num3.get(), self.num4.get(), self.num5.get(),
    #                        self.num6.get()])
    #     print(entry_list)
    #     yes_no = messagebox.askyesno(message='Are you sure you would like to play again?')
    #     if yes_no:
    #         self.num1.delete(0, 'end')
    #         self.num2.delete(0, 'end')
    #         self.num3.delete(0, 'end')
    #         self.num4.delete(0, 'end')
    #         self.num5.delete(0, 'end')
    #         self.num6.delete(0, 'end')
    #
    #         self.num1.insert(0, 1)
    #         self.num2.insert(0, 1)
    #         self.num3.insert(0, 1)
    #         self.num4.insert(0, 1)
    #         self.num5.insert(0, 1)
    #         self.num6.insert(0, 1)
    #
    #     else:
    #         pass

    def generate_lotto(self):
        game_lists = [self.num1.get(), self.num2.get(), self.num3.get(), self.num4.get(), self.num5.get(),
                      self.num6.get()]
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
        try:
            total_winnings = 0
            for x in range(len(self.total_wins)):
                count = 0
                _set = self.total_wins[x]
                for y in range(len(set)):
                    if _set[y] == self.lotto_numbers[y]:
                        count += 1

                    winnings_breakdown = {0: 0, 1: 0, 2: 20, 3: 100.50, 4: 2384, 5: 8584, 6: 10000000}
                    total_winnings += winnings_breakdown[count]
                    win = {winnings_breakdown[count]}
                    self.text_to_file(win)

                    messagebox.showinfo(message='You have won R{}'.format(total_winnings))
        except ValueError:
            messagebox.showerror(message='Make sure you entered a number')

    def text_to_file(self, text):
        with open('prize_money.txt', 'a') as prize:
            prize.write(str(text))

            # if count == 1:
            #     messagebox.showinfo(message="You only got 1 correct number. Unfortunately you don't win anything.")
            # elif count == 2:
            #     messagebox.showinfo(message='You got 2 correct numbers. You have won R20!')
            # elif count == 3:
            #     messagebox.showinfo(message='You got 3 numbers correct. You have won R100,50!')
            # elif count == 4:
            #     messagebox.showinfo(message='You got 4 numbers correct. You have won R2384!')
            # elif count == 5:
            #     messagebox.showinfo(message='You got 5 numbers correct. You have won R8584!')
            # elif count == 6:
            #     messagebox.showinfo(message='CONGRATULATIONS! You won the lottery. You just earned R10 000 000!')
            # else:
            #     messagebox.showinfo(message='Unfortunately you have not won anything.')

    def claim(self):
        self.root.destroy()
        import claim_prize


UserID(master)
Lotto(master)
master.mainloop()
