import tkinter as tk
from tkinter import Entry

window = tk.Tk()
window.title("Find the Square")
window.geometry("400x300")

def calculate_square():
    user_text = entry.get()

    if user_text.strip() == "":
        result.config(text="Please Enter a number",bg="orange")
        entry.delete(0,tk.END)
        return
    try:
        number = float(user_text)
    except ValueError:
        result.config(text="This is not a number",bg="red")
        entry.delete(0,tk.END)
        return
    
    square = number**2
    result.config(text=square,bg="green")
    entry.delete(0,tk.END)


entry = Entry(
    window,
    width=5
)
entry.pack(pady=5)

result = tk.Label(
    window,
    text="",
    font=(
        "times new roman",
        30,
        "bold italic"
    )
)
result.pack(pady=5)

btn = tk.Button(
    window,
    text="Calculate",
    command=calculate_square
)
btn.pack()

window.mainloop()