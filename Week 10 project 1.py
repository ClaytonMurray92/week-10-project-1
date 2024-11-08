import tkinter as tk
from tkinter import messagebox
def calculate_tax():
    try:
        gross_income = float(gross_income_entry.get())
        num_dependents = int(dependents_entry.get())
        deduction_per_dependent = 3000
        taxable_income = gross_income - (num_dependents * deduction_per_dependent)
        tax_rate = 0.2
        total_tax = taxable_income * tax_rate if taxable_income > 0 else 0
        total_tax_var.set(f"{total_tax:.2f}")
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter valid numeric values.")
root = tk.Tk()
root.title("Tax Calculator")
tk.Label(root, text="Gross income").grid(row=0, column=0, padx=5, pady=5, sticky="e")
gross_income_entry = tk.Entry(root)
gross_income_entry.grid(row=0, column=1, padx=5, pady=5)
tk.Label(root, text="Dependents").grid(row=1, column=0, padx=5, pady=5, sticky="e")
dependents_entry = tk.Entry(root)
dependents_entry.grid(row=1, column=1, padx=5, pady=5)
compute_button = tk.Button(root, text="Compute", command=calculate_tax)
compute_button.grid(row=2, column=0, columnspan=2, pady=5)
tk.Label(root, text="Total tax").grid(row=3, column=0, padx=5, pady=5, sticky="e")
total_tax_var = tk.StringVar(value="0.0")
tk.Label(root, textvariable=total_tax_var).grid(row=3, column=1, padx=5, pady=5, sticky="w")
root.mainloop()
