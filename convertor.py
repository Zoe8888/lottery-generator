from tkinter import *
from tkinter import messagebox



master = Tk()
master.title('Currency Converter')
master.geometry('400x400')
master.resizable('False', 'False')
master.config(bg='#4ad66d')


class Convert:
    def __init__(self, root):
        self.root = root
        self.currency = Label(root, text='Enter the currency code you wish to convert: ', bg='#4ad66d')
        self.currency.place(relx=0.16, rely=0.1)

        self.currency_entry = Entry(root, width=25, bg='#e4e4e0')
        self.currency_entry.place(relx=0.25, rely=0.2)

        self.amount = Label(root, text='Enter an amount you would like converted: ', bg='#4ad66d')
        self.amount.place(relx=0.16, rely=0.3)

        self.amount_entry = Entry(root, width=25, bg='#e4e4e0')
        self.amount_entry.place(relx=0.25, rely=0.4)

        self.button = Button(root, text='Convert to currency selected', command=self.convert, bg='#4ad66d')
        self.button.place(relx=0.29, rely=0.5)

        self.answer = Label(root, width=25)
        self.answer.place(relx=0.25, rely=0.6)

        self.clear = Button(root, text='Clear', command=self.delete, bg='#4ad66d', width=8)
        self.clear.place(relx=0.25, rely=0.7)

        self.exit = Button(root, text='Exit', command=exit, bg='#4ad66d', width=8)
        self.exit.place(relx=0.54, rely=0.7)

    def convert(self):
        api = "https://v6.exchangerate-api.com/v6/4a704b6911da3fab9b1df53d/latest/ZAR"
        data = requests.get(api).json()
        result = int(self.amount_entry.get()) * data['conversion_rates'](self.currency_entry.get())
        print(result)
        self.answer.config(text=result)

    def delete(self):
        self.amount_entry.delete(0, END)
        self.amount_entry.focus()
        self.currency_entry.delete(0, END)


Convert(master)
master.mainloop()
