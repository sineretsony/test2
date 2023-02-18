import tkinter as tk

def greet():
    greeting_label.config(text="Kolya hello")

root = tk.Tk()
root.geometry("1200x800")

greeting_label = tk.Label(root, text="")
greeting_label.pack()

greet_button = tk.Button(root, text="Greet", command=greet)
greet_button.pack()

root.mainloop()