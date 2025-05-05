import tkinter as tk
from tkinter import ttk, messagebox
import requests

# Function to get exchange rate using your API key
def get_exchange_rate(from_currency, to_currency, api_key):
    url = f"https://api.exchangerate-api.com/v4/latest/{from_currency}?apikey={api_key}"
    response = requests.get(url)
    
    if response.status_code != 200:
        raise Exception("Failed to fetch exchange rates.")
    
    data = response.json()
    
    if "rates" not in data or to_currency not in data["rates"]:
        raise Exception(f"Exchange rate for {to_currency} not found.")
    
    rate = data["rates"][to_currency]
    return rate

# Function triggered by Convert button
def convert_currency():
    try:
        # Get user input
        amount = float(amount_entry.get())
        from_curr = from_currency_combo.get()
        to_curr = to_currency_combo.get()

        # Check if currencies are selected
        if not from_curr or not to_curr:
            messagebox.showerror("Input Error", "Please select both currencies.")
            return
        
        # API key for exchange rate API
        api_key = "cur_live_AInqdDEWXCz7Ia9yqSh1RiDwwf4iMOn6Hzi8pjL6"
        
        # Get the exchange rate and convert
        rate = get_exchange_rate(from_curr, to_curr, api_key)
        result = amount * rate
        
        # Show the result
        result_label.config(text=f"{amount:.2f} {from_curr} = {result:.2f} {to_curr}")
    
    except ValueError:
        messagebox.showerror("Input Error", "Please enter a valid numeric amount.")
    except Exception as e:
        messagebox.showerror("Error", str(e))

# List of currency ISO codes
currencies = ["USD", "EUR", "GBP", "INR", "AUD", "CAD", "JPY", "CNY", "CHF", "NZD"]

# GUI Setup
root = tk.Tk()
root.title("Currency Converter")
root.geometry("400x300")
root.resizable(False, False)

# Title Label
tk.Label(root, text="Currency Converter", font=("Helvetica", 16)).pack(pady=10)

# Amount Entry
amount_entry = tk.Entry(root, font=("Helvetica", 14), justify="center")
amount_entry.insert(0, "1.0")
amount_entry.pack(pady=10)

# From Currency ComboBox
from_currency_combo = ttk.Combobox(root, values=currencies, font=("Helvetica", 12), state="readonly")
from_currency_combo.set("USD")  # Default to USD
from_currency_combo.pack(pady=5)

# To Currency ComboBox
to_currency_combo = ttk.Combobox(root, values=currencies, font=("Helvetica", 12), state="readonly")
to_currency_combo.set("INR")  # Default to INR
to_currency_combo.pack(pady=5)

# Convert Button
convert_button = tk.Button(root, text="Convert", command=convert_currency, font=("Helvetica", 12), bg="lightblue")
convert_button.pack(pady=10)

# Result Label
result_label = tk.Label(root, text="", font=("Helvetica", 14))
result_label.pack(pady=10)

# Run the application
root.mainloop()
