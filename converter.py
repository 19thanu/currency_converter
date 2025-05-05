import tkinter as tk
from tkinter import ttk, messagebox
import requests

# Function to get exchange rates
def get_exchange_rate(from_currency, to_currency):
    url = f"https://api.exchangerate.host/convert?from={from_currency}&to={to_currency}"
    response = requests.get(url)
    if response.status_code != 200:
        raise Exception("Failed to fetch exchange rates")
    data = response.json()
    return data["info"]["rate"]

# Convert button action
def convert_currency():
    try:
        amount = float(amount_entry.get())
        from_currency = from_currency_combo.get()
        to_currency = to_currency_combo.get()

        if from_currency == "" or to_currency == "":
            messagebox.showerror("Input Error", "Please select both currencies.")
            return

        rate = get_exchange_rate(from_currency, to_currency)
        converted_amount = amount * rate
        result_label.config(text=f"{amount:.2f} {from_currency} = {converted_amount:.2f} {to_currency}")
    except ValueError:
        messagebox.showerror("Input Error", "Please enter a valid amount.")
    except Exception as e:
        messagebox.showerror("Error", str(e))

# Currency list (ISO codes)
currencies = ["USD", "EUR", "GBP", "INR", "AUD", "CAD", "JPY", "CNY", "CHF", "NZD"]

# GUI Setup
root = tk.Tk()
root.title("Currency Converter")
root.geometry("400x300")
root.resizable(False, False)

# Title label
title_label = tk.Label(root, text="Currency Converter", font=("Helvetica", 16))
title_label.pack(pady=10)

# Amount Entry
amount_entry = tk.Entry(root, width=20, font=("Helvetica", 14))
amount_entry.pack(pady=10)
amount_entry.insert(0, "1.0")

# Currency selection
from_currency_combo = ttk.Combobox(root, values=currencies, font=("Helvetica", 12))
from_currency_combo.set("USD")
from_currency_combo.pack(pady=5)

to_currency_combo = ttk.Combobox(root, values=currencies, font=("Helvetica", 12))
to_currency_combo.set("INR")
to_currency_combo.pack(pady=5)

# Convert Button
convert_button = tk.Button(root, text="Convert", command=convert_currency, font=("Helvetica", 12), bg="lightblue")
convert_button.pack(pady=10)

# Result Label
result_label = tk.Label(root, text="", font=("Helvetica", 14))
result_label.pack(pady=10)

# Run the GUI
root.mainloop()
