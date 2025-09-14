import tkinter as tk
from tkinter import messagebox

class ContactBook:
    def __init__(self):
        self.contacts = {}

    def add_contact(self, name, phone, email, address):
        self.contacts[name] = {'Phone': phone, 'Email': email, 'Address': address}

    def delete_contact(self, name):
        if name in self.contacts:
            del self.contacts[name]
            return True
        return False

    def get_contact(self, name):
        return self.contacts.get(name, None)

def add_contact():
    name = entry_name.get().strip()
    phone = entry_phone.get().strip()
    email = entry_email.get().strip()
    address = entry_address.get().strip()
    if name and phone:
        contact_book.add_contact(name, phone, email, address)
        messagebox.showinfo("Success", f"Added {name} to contact book")
        clear_entries()
    else:
        messagebox.showerror("Error", "Name and Phone are required")

def view_contact():
    name = entry_name.get().strip()
    contact = contact_book.get_contact(name)
    if contact:
        entry_phone.delete(0, tk.END)
        entry_email.delete(0, tk.END)
        entry_address.delete(0, tk.END)
        entry_phone.insert(0, contact['Phone'])
        entry_email.insert(0, contact['Email'])
        entry_address.insert(0, contact['Address'])
    else:
        messagebox.showerror("Not Found", f"No contact named {name}")

def delete_contact():
    name = entry_name.get().strip()
    if contact_book.delete_contact(name):
        messagebox.showinfo("Deleted", f"{name} has been removed")
        clear_entries()
    else:
        messagebox.showerror("Error", "Contact not found")

def clear_entries():
    entry_name.delete(0, tk.END)
    entry_phone.delete(0, tk.END)
    entry_email.delete(0, tk.END)
    entry_address.delete(0, tk.END)

contact_book = ContactBook()


root = tk.Tk()
root.title("Contact Book")
root.geometry("500x350")  


tk.Label(root, text="Name").grid(row=0, column=0, padx=10, pady=10, sticky='e')
entry_name = tk.Entry(root, width=30)
entry_name.grid(row=0, column=1, padx=10, pady=10)

tk.Label(root, text="Phone").grid(row=1, column=0, padx=10, pady=10, sticky='e')
entry_phone = tk.Entry(root, width=30)
entry_phone.grid(row=1, column=1, padx=10, pady=10)

tk.Label(root, text="Email").grid(row=2, column=0, padx=10, pady=10, sticky='e')
entry_email = tk.Entry(root, width=30)
entry_email.grid(row=2, column=1, padx=10, pady=10)

tk.Label(root, text="Address").grid(row=3, column=0, padx=10, pady=10, sticky='e')
entry_address = tk.Entry(root, width=30)
entry_address.grid(row=3, column=1, padx=10, pady=10)


tk.Button(root, text="Add Contact", width=15, command=add_contact).grid(row=4, column=0, padx=10, pady=15)
tk.Button(root, text="View Contact", width=15, command=view_contact).grid(row=4, column=1, padx=10, pady=15)
tk.Button(root, text="Delete Contact", width=15, command=delete_contact).grid(row=5, column=0, padx=10, pady=10)
tk.Button(root, text="Clear Fields", width=15, command=clear_entries).grid(row=5, column=1, padx=10, pady=10)

root.mainloop()