import tkinter as tk
from tkinter import Entry

window = tk.Tk()
window.title("Quize app")
window.geometry("400x300")

def correct():
    ans_lb.config(
        text="Correct",
        bg="green"
    )
    correct_btn.config(state="disabled")
    incorrect_btn1.config(state="disabled")
    incorrect_btn2.config(state="disabled")
    incorrect_btn3.config(state="disabled")
    reset_btn.pack(pady=5)

def incorrect():
    ans_lb.config(
        text="Incorrect, Try again!",
        bg="red"
    )

def reset():
    correct_btn.config(state="normal")
    incorrect_btn1.config(state="normal")
    incorrect_btn2.config(state="normal")
    incorrect_btn3.config(state="normal")
    ans_lb.config(
        text="",
        bg="SystemButtonFace"
    )
    reset_btn.pack_forget()


lb1 = tk.Label(
    window,
    text="What is 3 + 5?",
    font=(
        "times new roman",
        25,
        "bold"
    ),     
)
lb1.pack(padx=5)

incorrect_btn1 = tk.Button(
    window,
    text="10",
    command=incorrect
)
incorrect_btn1.pack(pady=5)

correct_btn = tk.Button(
    window,
    text="8",
    command=correct
)
correct_btn.pack(pady=5)

incorrect_btn2 = tk.Button(
    window,
    text="6",
    command=incorrect
)
incorrect_btn2.pack(pady=5)

incorrect_btn3 = tk.Button(
    window,
    text="7",
    command=incorrect
)
incorrect_btn3.pack(pady=5)

ans_lb = tk.Label(
    window,
    font=(
        "times new roman",
        20,
        "bold"
    ),
)
ans_lb.pack(padx=5)

reset_btn = tk.Button(
    window,
    text="Play again",
    command=reset
)

window.mainloop()