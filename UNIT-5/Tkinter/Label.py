import tkinter as tk 

display = tk.Tk()
display.geometry("300x400")
display.configure(bg="grey")
labeel = tk.Label(
    display,
    text = "This is the label.",
    font = ("Arial",18,"bold"),
    fg = "red",
    bg = "yellow",
    padx = 12,
    pady = 15
)

labeel.pack(pady=25)
display.mainloop()