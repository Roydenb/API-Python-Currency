import requests
from tkinter import *
import tkinter as tk
from tkinter import ttk

url = 'https://api.exchangerate-api.com/v4/latest/USD'

# Creating a class to have the currency to be converted
class ConvertNow():
    def __init__(self,response):
            self.data = requests.get(response).json()
            self.currencies = self.data['rates']

    # Base currency
    def convert(self, from_currency, to_currency, amount):
        if from_currency != 'USD' :
            amount = amount / self.currencies[from_currency]

         # Rounding it off(4 decimal places)
        amount = round(amount * self.currencies[to_currency], 4)
        return amount

# Creating a class for tkinter
class GUI(tk.Tk):
      def __init__(self, converter):
            tk.Tk.__init__(self)
            self.title("Currency Converter")
            self.currency_converter = converter
            self.geometry("500x200")

            # The main label/the paragraph
            self.top_label = Label(self, text = 'Covert your Currency\n to another Currency in \n REAL TIME',  fg = 'green')
            self.top_label.config(font = ('FreeSerif',18,'bold'))
            self.top_label.place(x = 10 , y = 100)

            # The font you'll see before pressing on the drop down
            font = ("FreeSerif", 12, "bold")

            # dropdown Stringvar for the Currency change
            self.from_currency_var = StringVar(self)
            self.from_currency_var.set("USD") # default value
            self.to_currency_var = StringVar(self)
            self.to_currency_var.set("INR") # default value

            # Currency before change dropdown
            self.from_currency_dropdown = ttk.Combobox(self, textvariable=self.from_currency_var,values=list
            (self.currency_converter.currencies.keys()), font = font, state = 'readonly', width = 15, justify = tk.CENTER)
            self.from_currency_dropdown.place(x = 30,y= 10)

            # FROM entry
            self.amount_ent = Entry(self,bd = 3,relief = tk.RIDGE, justify = tk.CENTER, width = 17)
            self.amount_ent.place(x = 30, y = 50)

            # Currency changed dropdown
            self.to_currency_dropdown = ttk.Combobox(self, textvariable=self.to_currency_var,values=list
            (self.currency_converter.currencies.keys()), font = font, state = 'readonly', width = 13, justify = tk.CENTER)
            self.to_currency_dropdown.place(x = 250,y= 10)

            # Covert entry (TO)
            self.converted_amount_lbl = Label(self, text = '', fg = 'black', bg = 'white',
                                              relief = tk.RIDGE, justify = tk.CENTER, width = 17, borderwidth = 3)
            self.converted_amount_lbl.place(x = 250, y = 50)

          # Convert button from the one currency to the other
            self.convert_button = Button(self, text = "Convert", fg = "brown", command = self.my_function,width=20,height=2)
            self.convert_button.config(font=('FreeSerif', 15, 'bold'))
            self.convert_button.place(x=260,y=110)

      # Defining what should happen in the amount entery
      def my_function(self):
          amount = float(self.amount_ent.get())
          from_cur = self.from_currency_var.get()
          to_cur = self.to_currency_var.get()

          # Where the converted amount should display
          converted_amount = self.currency_converter.convert(from_cur,to_cur,amount)
          converted_amount = round(converted_amount, 2)
          self.converted_amount_lbl.config(text = str(converted_amount))

converter = ConvertNow(url)
GUI(converter)
mainloop()
