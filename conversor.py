from cgitb import text
import tkinter as tk
import cryptocompare as cc
import time


class Conversor(tk.Tk):
    def __init__(self):

        super().__init__()
        self.title('Convert')
        self.geometry('300x120')
        self.resizable(False, False)
        self.result = 0
        self.ecuacion = ''

        self.main_frame = tk.Frame(self)
        self.main_frame.pack()

        fecha = time.strftime('%Y-%m-%d %H:%M:%S')
        self.time_label = tk.Label(self.main_frame, text=fecha)
        self.time_label.grid(row=0, column=1, columnspan=2)
        self.after(1000, self.update_time)

        self.coin_label = tk.Label(self.main_frame, text='Coin: ')
        self.coin_label.grid(row=1, column=0)
        self.coin_entry = tk.Entry(self.main_frame, width=10, justify='center')
        self.coin_entry.grid(row=1, column=1)

        self.currency_label = tk.Label(self.main_frame, text='Currency: ')
        self.currency_label.grid(row=2, column=0)
        self.currency_entry = tk.Entry(self.main_frame, width=10, justify='center')
        self.currency_entry.grid(row=2, column=1)

        self.amount_currency_label = tk.Label(self.main_frame, text='amount: ')
        self.amount_currency_label.grid(row=2, column=2)
        self.amount_currency_entry = tk.Entry(self.main_frame, width=10, justify='center')
        self.amount_currency_entry.grid(row=2, column=3)

        self.button = tk.Button(self.main_frame, text='Convert', command=self.convert, width=10)
        self.button.grid(row=3, column=1, columnspan=2)

        self.ecuacion_label = tk.Label(self.main_frame, text=self.ecuacion)
        self.ecuacion_label.grid(row=4, column=0, columnspan=4)

        self.mainloop()

    def update_time(self):
        self.time_label.config(text=time.strftime('%Y-%m-%d %H:%M:%S'))
        self.after(1000, self.update_time)

    def convert(self):
        self.contadorInicio = time.time()
        coin = self.coin_entry.get()
        currency = self.currency_entry.get()
        price = cc.get_price(coin, currency)
        price = price[coin.upper()][currency.upper()]

        amount_currency = self.amount_currency_entry.get()

        self.result = float(amount_currency) / float(price)
        self.result = round(self.result, 10)
        self.ecuacion = f'{amount_currency} {currency} = {self.result} {coin}'
        self.ecuacion_label.config(text=self.ecuacion)


# Main
#conver = Conversor()
#conver.mainloop()

