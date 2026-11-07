import tkinter as tk

display = tk.Tk()
display.geometry("400x400")
display.configure(bg="grey")
# display.titles("Table Display")
label = tk.Label(display,text="Enter number to display the table: ")
label.pack(pady=20)
number = tk.Entry(display)
number.pack()

def display_table():
    number1 = number.get()
    num = int(number1)
    for i in range(1,11):
        print(f"{num} x {i} = {num*i}")

button = tk.Button(display,text="Print Table",command=display_table)
button.pack(pady=20)
display.mainloop()