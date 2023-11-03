from tkinter import *
from tkinter import ttk


window = Tk()
window.geometry("500x300")
window.title("Currency converter")

window.configure(background="light blue")
head_label = Label(window, text="Currency convertor", fg="black", bg="light blue", justify=CENTER, font=("Times 30 bold"))
head_label.grid(row=0, column=0)

amount = Label(window, text="Amount", fg="black", bg="light blue")
amount.grid(row=1, column=0)

amount_entry = Entry(window, width=25)
amount_entry.grid(row=1, column=1)

from_currency = Label(window, text="FROM", fg="black", bg="light blue")
from_currency.grid(row=2, column=0, padx=10, pady=10)

to_currency = Label(window, text="TO", fg="black", bg="light blue")
to_currency.grid(row=3, column=0, padx=10, pady=10)

from_currency_combo = ttk.Combobox(window, width=14, values=["TSHS", "USD", "EUR", "CAD", "KRW"])
from_currency_combo.grid(row=2, column=1, padx=10, pady=10)

to_currency_combo = ttk.Combobox(window, width=14, values=["TSHS", "USD", "EUR", "CAD", "KRW"])
to_currency_combo.grid(row=3, column=1, padx=10, pady=10)

button1 = Button(window, text="Convert", bg="red", fg="black")
button1.grid(row=4, column=1, padx=10, pady=10)

convert = Label(window, text="Converted amount", bg="light blue", fg="black")
convert.grid(row=5, column=0)

convert_entry = Entry(width=25)
convert_entry.grid(row=5, column=1)

window.mainloop()
