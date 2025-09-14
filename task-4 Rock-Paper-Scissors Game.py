import tkinter as tk
import random


def play(user_choice):
    computer_choice = random.choice(['Rock', 'Paper', 'Scissors'])
    result = ""

    if user_choice == computer_choice:
        result = "It's a tie!"
    elif (user_choice == 'Rock' and computer_choice == 'Scissors') or \
         (user_choice == 'Scissors' and computer_choice == 'Paper') or \
         (user_choice == 'Paper' and computer_choice == 'Rock'):
        result = "You win!"
    else:
        result = "Computer wins!"

    result_label.config(text=f"Your choice: {user_choice}\nComputer's choice: {computer_choice}\n{result}")


window = tk.Tk()
window.title("Rock-Paper-Scissors Game")
window.geometry("400x300")
window.config(bg="lightblue")


header = tk.Label(window, text="Choose Rock, Paper, or Scissors", font=("Arial", 16), bg="lightblue")
header.pack(pady=20)


button_frame = tk.Frame(window, bg="lightblue")
button_frame.pack()

rock_button = tk.Button(button_frame, text="Rock", width=10, command=lambda: play("Rock"))
rock_button.grid(row=0, column=0, padx=10)

paper_button = tk.Button(button_frame, text="Paper", width=10, command=lambda: play("Paper"))
paper_button.grid(row=0, column=1, padx=10)

scissors_button = tk.Button(button_frame, text="Scissors", width=10, command=lambda: play("Scissors"))
scissors_button.grid(row=0, column=2, padx=10)


result_label = tk.Label(window, text="", font=("Arial", 14), bg="lightblue")
result_label.pack(pady=30)


window.mainloop()
