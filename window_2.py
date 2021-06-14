from tkinter import *
from tkinter import messagebox
from random import randint

root = Tk()
# Creating a title
root.title('Lotto Generator')
# Setting the window size
root.geometry("700x700")
# Setting a background color
root.config(bg="#4ad66d")


plays = Label(root, text='Select the amount of times you would like to play:')
plays.place(relx=0.2, rely=0.1)

amount_of_plays = Spinbox(root, from_=1, to=10)
amount_of_plays.place(relx=0.7, rely=0.1)

select = Label(root, text='Select your lucky Lotto numbers:')
select.place(relx=0.2, rely=0.2)

num1 = Spinbox(root, from_=0, to=49, width=5, font=10)
num1.place(relx=0.2, rely=0.3)

num2 = Spinbox(root, from_=0, to=49, width=5, font=10)
num2.place(relx=0.3, rely=0.3)

num3 = Spinbox(root, from_=0, to=49, width=5, font=10)
num3.place(relx=0.4, rely=0.3)

num4 = Spinbox(root, from_=0, to=49, width=5, font=10)
num4.place(relx=0.5, rely=0.3)

num5 = Spinbox(root, from_=0, to=49, width=5, font=10)
num5.place(relx=0.6, rely=0.3)

num6 = Spinbox(root, from_=0, to=49, width=5, font=10)
num6.place(relx=0.7, rely=0.3)

# def amount_of_plays():
#     if variable.get() == 'Select':
#         raise ValueError
#     elif variable.get() > 1:


play_again = Button(root, text='Play again')
play_again.place(relx=0.2, rely=0.4, width=20)


def generate_random():
    random_number = randint(0, 49)
    return random_number


def generate_lotto():
    lotto_numbers = []
    for current_lotto_number in range(7):
        random_number = generate_random()
        lotto_numbers.append(random_number)
        result = lotto_numbers.append(random_number)
        lotto1.config(state='normal')
        lotto1.insert(0, result[0])
        lotto1.config(state='readonly')

        lotto2.config(state='normal')
        lotto2.insert(0, result[1])
        lotto2.config(state='readonly')

        lotto3.config(state='normal')
        lotto3.insert(0, result[2])
        lotto3.config(state='readonly')

        lotto4.config(state='normal')
        lotto4.insert(0, result[3])
        lotto4.config(state='readonly')

        lotto5.config(state='normal')
        lotto5.insert(0, result[4])
        lotto5.config(state='readonly')

        lotto6.config(state='normal')
        lotto6.insert(0, result[5])
        lotto6.config(state='readonly')


reveal_lotto = Button(root, text='Reveal Lotto numbers', command=generate_lotto)
reveal_lotto.place(relx=0.5, rely=0.4)

lotto_label = Label(root, text='The winning Lotto numbers are:')
lotto_label.place(relx=0.2, rely=0.6)

lotto1 = Entry(root, bg='#d62e2e', state='readonly', width=5, font=10)
lotto1.place(relx=0.2, rely=0.7)

lotto2 = Entry(root, bg='#fc852a', state='readonly', width=5, font=10)
lotto2.place(relx=0.3, rely=0.7)

lotto3 = Entry(root, bg='#f6f841', state='readonly', width=5, font=10)
lotto3.place(relx=0.4, rely=0.7)

lotto4 = Entry(root, bg='#60c54d', state='readonly', width=5, font=10)
lotto4.place(relx=0.5, rely=0.7)

lotto5 = Entry(root, bg='#4cb4c5', state='readonly', width=5, font=10)
lotto5.place(relx=0.6, rely=0.7)

lotto6 = Entry(root, bg='#c659e7', state='readonly', width=5, font=10)
lotto6.place(relx=0.7, rely=0.7)

root.mainloop()
