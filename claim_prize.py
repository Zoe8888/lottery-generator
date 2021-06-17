from tkinter import *
import requests

master = Tk()
master.title('Claim Your Prize')
master.geometry('700x550')
master.resizable('False', 'False')
master.config(bg='#4ad66d')


class Prize:
    def __init__(self, root):
        self.root = root
        self.header = Label(root, text="Congratulations! You're a winner!", fg='#506352', bg='#4ad66d', font=30)
        self.header.place(relx=0.1, rely=0.05)

        # self.user_id = Label(root, text='User ID:', fg='#506352', bg='#4ad66d')
        # self.user_id.place(relx=0.5, rely=0.2)
        #
        # self.user_id_entry = Entry(root, state='readonly')
        # self.user_id_entry.place(relx=0.7, rely=0.2)

        self.prize_amount = Label(root, text='You have won (R):', fg='#506352', bg='#4ad66d')
        self.prize_amount.place(relx=0.1, rely=0.1)

        self.prize_amount_entry = Entry(root, state='readonly')
        self.prize_amount_entry.place(relx=0.5, rely=0.1)

        self.banking_info = Label(root, text='Please enter your bank information:', fg='#506352', bg='#4ad66d', font=20)
        self.banking_info.place(relx=0.1, rely=0.2)

        self.account_holder = Label(root, text='Account holder:', fg='#506352', bg='#4ad66d')
        self.account_holder.place(relx=0.1, rely=0.25)

        self.account_holder_entry = Entry(root, bg='#e4e4e0')
        self.account_holder_entry.place(relx=0.5, rely=0.25)

        self.account_number = Label(root, text='Account number:', fg='#506352', bg='#4ad66d')
        self.account_number.place(relx=0.1, rely=0.3)

        self.account_number_entry = Entry(root, bg='#e4e4e0')
        self.account_number_entry.place(relx=0.5, rely=0.3)

        self.select_bank = Label(root, text='Select your bank:', fg='#506352', bg='#4ad66d')
        self.select_bank.place(relx=0.1, rely=0.35)

        self.options = ['Select...', 'ABSA', 'FNB', 'Nedbank', 'Standard Bank']
        self.variable = StringVar(root)
        self.variable.set(self.options[0])
        self.bank_menu = OptionMenu(root, self.variable, *self.options)
        self.bank_menu.place(relx=0.5, rely=0.35)

        self.convert_label = Label(root, text='Would you like to convert your money to another currency?', fg='#506352',
                                   bg='#4ad66d', font=20)
        self.convert_label.place(relx=0.1, rely=0.45)

        self.currency = Label(root, text='Enter the desired currency code: ', fg='#506352', bg='#4ad66d')
        self.currency.place(relx=0.1, rely=0.5)

        self.currency_entry = Entry(root, bg='#e4e4e0')
        self.currency_entry.place(relx=0.5, rely=0.5)

        self.amount = Label(root, text='Enter an amount you want converted: ', fg='#506352', bg='#4ad66d')
        self.amount.place(relx=0.1, rely=0.55)

        self.amount_entry = Entry(root, bg='#e4e4e0')
        self.amount_entry.place(relx=0.5, rely=0.55)

        self.convert_money = Button(root, text='Convert Prize Money', command=self.convert, fg='#506352', bg='#47b553')
        self.convert_money.place(relx=0.1, rely=0.65)

        self.answer = Label(root, bg='#e4e4e0', width=20)
        self.answer.place(relx=0.5, rely=0.65)

        self.submit = Button(root, text='Submit', fg='#506352', bg='#47b553', width=20)
        self.submit.place(relx=0.1, rely=0.75)

        self.play_again = Button(root, text='Play again', fg='#506352', bg='#47b553', width=20)
        self.play_again.place(relx=0.47, rely=0.75)

    def convert(self):
        api = "https://v6.exchangerate-api.com/v6/4a704b6911da3fab9b1df53d/latest/ZAR"
        data = requests.get(api).json()
        result = round(int(self.amount_entry.get()) * data['conversion_rates'][self.currency_entry.get()], 2)
        result_text = "{} {}".format(result, self.currency_entry.get())
        self.answer.config(text=result_text)

    def play_again(self):
        self.root.destroy()
        import window_2


Prize(master)
master.mainloop()