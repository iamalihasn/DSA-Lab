import tkinter as tk
from tkinter import Entry

window = tk.Tk()
window.title("My Entry App")
window.geometry("400x300")

def great():
    ent = entry.get()

    if ent == "":
        result.config(
            text="Please Enter name",
            bg="red",
            fg="white",    
        )
    else:
        result.config(
            text=f"Hello {ent}",
            fg="white",
            bg="green"
        )
    entry.delete(0,tk.END)

entry = Entry(
    window,
    width= 10,
    fg="red",
    font=(
        "times new roman",
        15,
        "italic"
    ),
    justify="center"
)
entry.pack(pady=5,ipadx=5,ipady=5)
entry.insert(0,"Enter name")
entry.focus()


result = tk.Label(
    window,
    text="",
    font=(
        "times new roman",
        20,
        "bold"
    )
)
result.pack(pady=5)

read_btn = tk.Button(
    window,
    text="Read",
    cursor="hand2",
    command=great
)
read_btn.pack(pady=5)

window.mainloop()