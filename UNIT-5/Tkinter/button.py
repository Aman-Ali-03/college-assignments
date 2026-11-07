import tkinter as tk 
display = tk.Tk()
display.geometry("400x500")

def hello():
    print("Hello i am your code.")

labeel = tk.Label(
    display,
    label = "Click to get Greed.",
    fg="black",
    bg="pink"
)
labeel.pack(pady=20)
button = tk.Button(
    display,

    text = "Click me",
    command=hello
)

button.pack(pady=40)
display.mainloop()

# import tkinter as tk

# root = tk.Tk()
# root.geometry("400x200")

# def say_hello():
#     print("Hello, Students!")

# button = tk.Button(
#     root,
#     text="Click Me",
#     command=say_hello
# )

# button.pack(pady=30)

# root.mainloop()