from cgitb import text
from email.mime import image
from lib2to3.pytree import convert
import tkinter as tk
from PIL import Image,ImageTk
from webbrowser import open
import cryptocompare as cc
import time
from convert import Convert 


class CoinCompare(tk.Tk):
    def __init__(self):
        self.contadorFin = time.time()
        self.contadorInicio = time.time()
        self.price = 0
        self.coin = 'btc'
        self.difference = 0

        super().__init__()
        self.title('Coin Compare')
        self.geometry('400x260')
        self.resizable(False, False)

        self.main_frame = tk.Frame(self)
        self.main_frame.pack()

        self.coin_label = tk.Label(self.main_frame, text='Coin: ')
        self.coin_label.grid(row=1, column=0)

        self.currency_label = tk.Label(self.main_frame, text='Currency: ')
        self.currency_label.grid(row=2, column=0)
#####################################################################################################
        inputtext = Image.open('inputtext.png')
        inputtext = inputtext.resize((30, 30), Image.ANTIALIAS) # Redimension (Alto, Ancho)
        inputtext = ImageTk.PhotoImage(inputtext)

        self.coin_entry = tk.Entry(self.main_frame,image=inputtext, width=10, justify='center')
        self.coin_entry.grid(row=1, column=1)

        self.currency_entry = tk.Entry(self.main_frame,image=inputtext, width=10, justify='center')
        self.currency_entry.grid(row=2, column=1)
#####################################################################################################

        self.separator = tk.Frame(self.main_frame, height=2, bd=1, relief=tk.SUNKEN)
        self.separator.grid(row=3, columnspan=2, sticky=tk.W+tk.E)

        imgGetprice = Image.open('getprice.png')
        imgGetprice = imgGetprice.resize((30, 30), Image.ANTIALIAS) # Redimension (Alto, Ancho)
        imgGetprice = ImageTk.PhotoImage(imgGetprice)
        self.button = tk.Button(self.main_frame,image=imgGetprice, command=self.get_price, width=50, height=30, bg='White')
        self.button.grid(row=2, column=3, columnspan=2)
        
        self.time_price = tk.Label(self.main_frame, text="")
        self.time_price.grid(row=4, column=3, columnspan=2)

        self.price_label = tk.Label(self.main_frame, text='Price:')
        self.price_label.grid(row=4, column=0)

        self.price_entry = tk.Label(self.main_frame, text='0', fg='black')
        self.price_entry.grid(row=4, column=1)

        self.current_date = tk.Label(self.main_frame, text='Current date:')
        self.current_date.grid(row=0, column=0)
####################################################################
        fecha = time.strftime('%Y-%m-%d %H:%M:%S')
        self.time_label = tk.Label(self.main_frame, text=fecha)
        self.time_label.grid(row=0, column=1, columnspan=2)
        self.after(1000, self.update_time)
####################################################################
        self.contador = tk.Label(self.main_frame, text="")
        self.contador.grid(row=5, column=0, columnspan=2)
        self.after(1000, self.update_contador)
####################################################################
        self.separator = tk.Frame(self.main_frame, height=2, bd=1, relief=tk.SUNKEN)
        self.separator.grid(row=7, columnspan=2, sticky=tk.W+tk.E)
####################################################################
        self.author_label = tk.Label(self.main_frame, text='Developed by:')
        self.author_label.grid(row=8, column=0, columnspan=2)

        imgGit = Image.open('git.png')
        imgGit = imgGit.resize((30, 30), Image.ANTIALIAS) # Redimension (Alto, Ancho)
        imgGit = ImageTk.PhotoImage(imgGit)
        self.github_button = tk.Button(self.main_frame, image=imgGit, command=lambda: open('https://github.com/AgustinDAmore'), width=30)
        self.github_button.grid(row=9, column=0, columnspan=2)
####################################################################
        self.coin_label = tk.Label(self.main_frame, text="coin information")
        self.coin_label.grid(row=5, column=3, columnspan=2)

        imgInformation = Image.open('information.png')
        imgInformation = imgInformation.resize((30, 30), Image.ANTIALIAS) # Redimension (Alto, Ancho)
        imgInformation = ImageTk.PhotoImage(imgInformation)
        self.coin_button = tk.Button(self.main_frame,image=imgInformation, command=lambda: open(f'https://www.google.com/search?q={self.coin}'), width=30, height=30, bg='White')
        self.coin_button.grid(row=6, column=3, columnspan=2)
####################################################################
        self.coin_label = tk.Label(self.main_frame, text="convert")
        self.coin_label.grid(row=7, column=3, columnspan=2)

        imgConvert = Image.open('convert.png')
        imgConvert = imgConvert.resize((30, 30), Image.ANTIALIAS) # Redimension (Alto, Ancho)
        imgConvert = ImageTk.PhotoImage(imgConvert)
        self.convert_button = tk.Button(self.main_frame,image=imgConvert,command=Convert, width=30, height=30,bg="white")
        self.convert_button.grid(row=8, column=3, columnspan=2)
####################################################################
        self.difference_label = tk.Label(self.main_frame, text="difference: ")
        self.difference_label.grid(row=6, column=0, columnspan=2)

        self.different_value = tk.Label(self.main_frame, text=self.difference)
        self.different_value.grid(row=6, column=1, columnspan=2)
        self.mainloop()
####################################################################
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
        if self.price > price:
            color = 'red'
        else:
            color = 'green'

        self.difference = round(price-self.price,2)
        if self.difference == price:
            self.difference = 0

        if self.coin != coin:
            self.difference = 0

        self.different_value.config(text="$"+str(self.difference), fg=color)

        self.price=price
        self.price_entry.config(text=price, fg=color)
        self.time_price.config(text=time.strftime('%Y-%m-%d %H:%M:%S'))
        self.coin = coin

# Main
if __name__ == '__main__':
        CoinCompare()