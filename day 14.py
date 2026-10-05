from tkinter import messagebox
from tkinter import ttk
import tkinter as tk
# root=tk.Tk()
# root.title("My First GUI")
# root.geometry("400x300")
# label = tk.Label(root, text="Hello Tkinter!", font=("Arial", 16))
# label.pack()
# name_entry = tk.Entry(root, width=30)
# name_entry.pack()
# label = tk.Label(root, text="Type your comments", font=("Arial", 16))
# label.pack()
# text_box = tk.Text(root, height=5, width=40)
# text_box.pack()
# subscribe = tk.BooleanVar()
# check = tk.Checkbutton(root, text="Subscribe", variable=subscribe)
# check.pack()
# gender = tk.StringVar(value="none")
# tk.Radiobutton(root, text="Male", value="Male", variable=gender).pack()
# tk.Radiobutton(root, text="Female", value="Female", variable=gender).pack()
# options = ["High", "Medium", "Low"]
# priority = tk.StringVar()
# combo = ttk.Combobox(root, values=options,
#                      textvariable=priority, state="readonly")
# combo.pack()
# messagebox.showinfo("Success", "Data Saved!")
# messagebox.showwarning("Warning", "Invalid Input!")
# messagebox.showerror("Error", "Something went wrong!")
# def show():
#     print("Button clicked!")
# btn = tk.Button(root, text="Click Me", command=show)
# btn.pack()
# root.resizable(False, False)
# root.mainloop()


# import tkinter as tk
# from tkinter import messagebox
# root = tk.Tk()
# root.title("Login Panel")
# root.geometry("300x200")
# tk.Label(root, text="Username").pack()
# user = tk.Entry(root)
# user.pack()
# tk.Label(root, text="Password").pack()
# pwd = tk.Entry(root, show="*")
# pwd.pack()
# def login():
#     if user.get() == "admin" and pwd.get() == "1234":
#         messagebox.showinfo("Success", "Login Successful")
#     else:
#         messagebox.showerror("Error", "Invalid Login")
# tk.Button(root, text="Login", command=login).pack(pady=10)
# root.mainloop()

import tkinter as tk
from tkinter import messagebox
import openpyxl
import os
file_path = "users.xlsx"
# Create file if not exists
if not os.path.exists(file_path):
    workbook = openpyxl.Workbook()
    sheet = workbook.active
    sheet.append(["Name", "Email"])
    workbook.save(file_path)
root = tk.Tk()
root.title("User Form")
root.geometry("400x250")
tk.Label(root, text="Name").pack()
name_var = tk.Entry(root)
name_var.pack()
tk.Label(root, text="Email").pack()
email_var = tk.Entry(root)
email_var.pack()
def save_data():
    name = name_var.get()
    email = email_var.get()
    if name == "" or email == "":
        messagebox.showwarning("Error", "All fields required!")
        return
    workbook = openpyxl.load_workbook(file_path)
    sheet = workbook.active
    sheet.append([name, email])
    workbook.save(file_path)
    messagebox.showinfo("Success", "Data Saved!")
    name_var.delete(0, tk.END)
    email_var.delete(0, tk.END)
tk.Button(root, text="Submit", command=save_data).pack(pady=10)
root.mainloop()

