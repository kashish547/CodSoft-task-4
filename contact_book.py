import tkinter as tk
from tkinter import messagebox, simpledialog
import json

# Function to load contacts from a file
def load_contacts():
    try:
        with open("contacts.json", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return {}

# Function to save contacts to a file
def save_contacts():
    with open("contacts.json", "w") as file:
        json.dump(contacts, file)

# Function to add a new contact
def add_contact():
    name = simpledialog.askstring("Input", "Enter name:")
    if name in contacts:
        messagebox.showwarning("Warning", "Contact already exists.")
        return
    phone = simpledialog.askstring("Input", "Enter phone number:")
    email = simpledialog.askstring("Input", "Enter email:")
    address = simpledialog.askstring("Input", "Enter address:")
    contacts[name] = {"phone": phone, "email": email, "address": address}
    save_contacts()
    update_contact_list()

# Function to view all contacts
def view_contacts():
    contact_list.delete(0, tk.END)
    for name, info in contacts.items():
        contact_list.insert(tk.END, f"{name} - {info['phone']}")

# Function to search for a contact
def search_contact():
    search_term = simpledialog.askstring("Search", "Enter name or phone number:")
    contact_list.delete(0, tk.END)
    for name, info in contacts.items():
        if search_term.lower() in name.lower() or search_term in info["phone"]:
            contact_list.insert(tk.END, f"{name} - {info['phone']}")

# Function to update a contact
def update_contact():
    selected = contact_list.curselection()
    if not selected:
        messagebox.showwarning("Warning", "No contact selected.")
        return
    selected_contact = contact_list.get(selected[0]).split(" - ")[0]
    name = simpledialog.askstring("Input", "Enter name:", initialvalue=selected_contact)
    phone = simpledialog.askstring("Input", "Enter phone number:", initialvalue=contacts[selected_contact]["phone"])
    email = simpledialog.askstring("Input", "Enter email:", initialvalue=contacts[selected_contact]["email"])
    address = simpledialog.askstring("Input", "Enter address:", initialvalue=contacts[selected_contact]["address"])
    contacts.pop(selected_contact)
    contacts[name] = {"phone": phone, "email": email, "address": address}
    save_contacts()
    update_contact_list()

# Function to delete a contact
def delete_contact():
    selected = contact_list.curselection()
    if not selected:
        messagebox.showwarning("Warning", "No contact selected.")
        return
    selected_contact = contact_list.get(selected[0]).split(" - ")[0]
    contacts.pop(selected_contact)
    save_contacts()
    update_contact_list()

# Function to update the contact list display
def update_contact_list():
    contact_list.delete(0, tk.END)
    for name, info in contacts.items():
        contact_list.insert(tk.END, f"{name} - {info['phone']}")

# Load contacts from file
contacts = load_contacts()

# Create the main application window
root = tk.Tk()
root.title("Contact Book")
root.geometry("500x400")
root.configure(bg="#2e2e2e")

# Title label
title_label = tk.Label(root, text="Contact Book", font=("Arial", 20, "bold"), bg="#2e2e2e", fg="#ffffff")
title_label.pack(pady=20)

# Listbox to display contacts
contact_list = tk.Listbox(root, font=("Arial", 14), bg="#ffffff", fg="#000000", selectbackground="#add8e6")
contact_list.pack(pady=20, padx=20, fill=tk.BOTH, expand=True)

# Frame for buttons
button_frame = tk.Frame(root, bg="#2e2e2e")
button_frame.pack(pady=20)

# Add Contact button
add_button = tk.Button(button_frame, text="Add Contact", command=add_contact, font=("Arial", 12), bg="#4CAF50", fg="#ffffff")
add_button.grid(row=0, column=0, padx=10)

# View Contacts button
view_button = tk.Button(button_frame, text="View Contacts", command=view_contacts, font=("Arial", 12), bg="#2196F3", fg="#ffffff")
view_button.grid(row=0, column=1, padx=10)

# Search Contact button
search_button = tk.Button(button_frame, text="Search Contact", command=search_contact, font=("Arial", 12), bg="#FFC107", fg="#000000")
search_button.grid(row=0, column=2, padx=10)

# Update Contact button
update_button = tk.Button(button_frame, text="Update Contact", command=update_contact, font=("Arial", 12), bg="#FF9800", fg="#ffffff")
update_button.grid(row=0, column=3, padx=10)

# Delete Contact button
delete_button = tk.Button(button_frame, text="Delete Contact", command=delete_contact, font=("Arial", 12), bg="#f44336", fg="#ffffff")
delete_button.grid(row=0, column=4, padx=10)

# Update the contact list initially
update_contact_list()

# Run the main application loop
root.mainloop()
