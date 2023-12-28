import tkinter as tk
from tkinter import messagebox

class Charity:
    def __init__(self, name):
        self.name = name
        self.total = 0

class DonationSystem:
    def __init__(self):
        self.charities = []

    def add_charity(self, charity):
        self.charities.append(charity)

    def donate(self, charity_index, bill):
        donation = bill * 0.01
        self.charities[charity_index].total += donation
        return donation

def add_charity():
    name = charity_entry.get()
    system.add_charity(Charity(name))
    charity_list.insert(tk.END, name)
    if len(system.charities) == 3:
        root.destroy()

def donate():
    charity_index = int(charity_var.get().split(' : ')[0]) - 1
    bill = float(bill_entry.get())
    donation = system.donate(charity_index, bill)
    messagebox.showinfo("Donation", f"Donated ${donation:.2f} to {system.charities[charity_index].name}")

def show_totals():
    totals = [(charity.name, charity.total) for charity in system.charities]
    totals.sort(key=lambda x: x[1], reverse=True)
    grand_total = sum(charity.total for charity in system.charities)
    messagebox.showinfo("Totals", "\n".join(f"{name}: ${total:.2f}" for name, total in totals) + f"\nGRAND TOTAL DONATED TO CHARITY: ${grand_total:.2f}")

system = DonationSystem()

root = tk.Tk()
root.geometry("300x300")



charity_label = tk.Label(root, text="Charity name:")
charity_label.pack()
charity_entry = tk.Entry(root)
charity_entry.pack()

add_button = tk.Button(root, text="Add charity", command=add_charity)
add_button.pack()

charity_list = tk.Listbox(root)
charity_list.pack()

root.mainloop()

root = tk.Tk()
root.geometry("300x300")


charity_var = tk.StringVar(root)
charity_var.set('1 : ' + system.charities[0].name)  # default value
charity_option = tk.OptionMenu(root, charity_var, '1 : ' + system.charities[0].name, '2 : ' + system.charities[1].name, '3 : ' + system.charities[2].name)
charity_option.pack()

bill_label = tk.Label(root, text="Shopping bill:")
bill_label.pack()
bill_entry = tk.Entry(root)
bill_entry.pack()

donate_button = tk.Button(root, text="Donate", command=donate)
donate_button.pack()

totals_button = tk.Button(root, text="Show totals", command=show_totals)
totals_button.pack()

root.mainloop()
