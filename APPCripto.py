from cgitb import text
from lib2to3.pytree import convert
import tkinter as tk
from webbrowser import open
import cryptocompare as cc
import time
from conversor import Conversor 


class App(tk.Tk):
    def __init__(self):
        self.contadorFin = time.time()
        self.contadorInicio = time.time()
        self.precio = 0
        self.coin = ''
        self.diferencia = 0

        super().__init__()
        self.title('Coin Compare')
        self.geometry('400x220')
        self.resizable(False, False)

        self.main_frame = tk.Frame(self)
        self.main_frame.pack()

        self.coin_label = tk.Label(self.main_frame, text='Coin: ')
        self.coin_label.grid(row=1, column=0)

        self.currency_label = tk.Label(self.main_frame, text='Currency: ')
        self.currency_label.grid(row=2, column=0)

        self.coin_entry = tk.Entry(self.main_frame, width=10, justify='center', bg='black', fg='white')
        self.coin_entry.grid(row=1, column=1)

        self.currency_entry = tk.Entry(self.main_frame, width=10, justify='center', bg='black', fg='white')
        self.currency_entry.grid(row=2, column=1)

        # separator
        self.separator = tk.Frame(self.main_frame, height=2, bd=1, relief=tk.SUNKEN)
        self.separator.grid(row=3, columnspan=2, sticky=tk.W+tk.E)

        self.button = tk.Button(self.main_frame, text='Get Price', command=self.get_price, width=10)
        self.button.grid(row=2, column=3, columnspan=2)
        
        # fecha y hora de cuando se ejecuta get_price
        self.time_price = tk.Label(self.main_frame, text="")
        self.time_price.grid(row=4, column=3, columnspan=2)

        self.price_label = tk.Label(self.main_frame, text='Price:')
        self.price_label.grid(row=4, column=0)

        self.price_entry = tk.Label(self.main_frame, text='0', fg='black')
        self.price_entry.grid(row=4, column=1)

        # mostar fecha y hora actual en la ventana actualiza cada segundo
        self.fecha_actual = tk.Label(self.main_frame, text='Fecha actual:')
        self.fecha_actual.grid(row=0, column=0)

        fecha = time.strftime('%Y-%m-%d %H:%M:%S')
        self.time_label = tk.Label(self.main_frame, text=fecha)
        self.time_label.grid(row=0, column=1, columnspan=2)
        self.after(1000, self.update_time)
        # incrementar contador cada segundo
        self.contador = tk.Label(self.main_frame, text="")
        self.contador.grid(row=5, column=0, columnspan=2)
        self.after(1000, self.update_contador)

        # separator
        self.separator = tk.Frame(self.main_frame, height=2, bd=1, relief=tk.SUNKEN)
        self.separator.grid(row=7, columnspan=2, sticky=tk.W+tk.E)

        # nombre del desarrollador
        self.author_label = tk.Label(self.main_frame, text='Developed by:')
        self.author_label.grid(row=8, column=0, columnspan=2)
        # ir a github
        self.github_button = tk.Button(self.main_frame, text='Github', command=lambda: open('https://github.com/AgustinDAmore'), width=10)
        self.github_button.grid(row=9, column=0, columnspan=2)

        self.coin_label = tk.Label(self.main_frame, text="coin information")
        self.coin_label.grid(row=5, column=3, columnspan=2)

        self.coin_button = tk.Button(self.main_frame,text="information", command=lambda: open(f'https://www.google.com/search?q={self.coin}'), width=10)
        self.coin_button.grid(row=6, column=3, columnspan=2)

        self.convert_button = tk.Button(self.main_frame,text="convert",command=Conversor, width=10)
        self.convert_button.grid(row=7, column=3, columnspan=2)

        self.diferencia_label = tk.Label(self.main_frame, text="diferencia: ")
        self.diferencia_label.grid(row=6, column=0, columnspan=2)

        self.valor_diferencia = tk.Label(self.main_frame, text=self.diferencia)
        self.valor_diferencia.grid(row=6, column=1, columnspan=2)
        self.mainloop()

    def update_time(self):
        self.time_label.config(text=time.strftime('%Y-%m-%d %H:%M:%S'))
        self.after(1000, self.update_time)
    
    def update_contador(self):
        self.contadorFin = time.time()
        self.contador.config(text="price ago: "+str(round(self.contadorFin-self.contadorInicio))+" seconds")
        self.after(1000, self.update_contador)

    def get_price(self):
        self.contadorInicio = time.time()
        coin = self.coin_entry.get()
        currency = self.currency_entry.get()
        price = cc.get_price(coin, currency)
        price = price[coin.upper()][currency.upper()]
        if self.precio > price:
            color = 'red'
        else:
            color = 'green'

        self.diferencia = round(price-self.precio,2)
        if self.diferencia == price:
            self.diferencia = 0

        if self.coin != coin:
            self.diferencia = 0

        self.valor_diferencia.config(text="$"+str(self.diferencia), fg=color)

        self.precio=price
        self.price_entry.config(text=price, fg=color)
        self.time_price.config(text=time.strftime('%Y-%m-%d %H:%M:%S'))
        self.coin = coin

# Main
app = App()
app.mainloop()

