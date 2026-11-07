import tkinter as tk 

root = tk.Tk()
root.geometry("400x300")
labeel = tk.Label(text="Enter your name: ", pady=20)
labeel.pack()
name_enter = tk.Entry(root)
name_enter.pack()

labeel = tk.Label(text="Enter your password: ",pady=20)
labeel.pack()
password_entry = tk.Entry(root,show="+")
password_entry.pack()

def show_name_pwd():
    name = name_enter.get()
    passwordd = password_entry.get()
    print(f"Hello {name}!")
    print(f"Your password : {passwordd}")

button = tk.Button(root,text="Greed" , command=show_name_pwd)
button.pack(pady=20)

root.mainloop()