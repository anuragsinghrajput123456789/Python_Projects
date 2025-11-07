import tkinter as tk
from tkinter import messagebox
import random
import pandas as pd
import os

# Initialize window
root = tk.Tk()
root.title("Tic Tac Toe AI 🧠")
root.geometry("420x500")
root.config(bg="#222831")

current_player = "X"
buttons = []
mode = tk.StringVar(value="AI")  # Default: AI mode
score_data = []

# Excel file to store scores
excel_file = "tictactoe_scores.xlsx"

# Initialize score DataFrame
if os.path.exists(excel_file):
    df = pd.read_excel(excel_file)
else:
    df = pd.DataFrame(columns=["Player", "Opponent", "Result"])

# ----------- Game Logic -----------


def check_winner():
    """Check for a winner or draw."""
    win_combinations = [
        [0, 1, 2],
        [3, 4, 5],
        [6, 7, 8],
        [0, 3, 6],
        [1, 4, 7],
        [2, 5, 8],
        [0, 4, 8],
        [2, 4, 6],
    ]

    for combo in win_combinations:
        if (
            buttons[combo[0]]["text"]
            == buttons[combo[1]]["text"]
            == buttons[combo[2]]["text"]
            and buttons[combo[0]]["text"] != ""
        ):
            for i in combo:
                buttons[i].config(bg="#00ADB5")
            winner = buttons[combo[0]]["text"]
            messagebox.showinfo("Winner 🎉", f"Player {winner} wins!")
            record_score(winner)
            disable_buttons()
            return True

    if all(button["text"] != "" for button in buttons):
        messagebox.showinfo("Draw 🤝", "It's a Draw!")
        record_score("Draw")
        disable_buttons()
        return True

    return False


def ai_move():
    """AI makes its move intelligently."""
    available_moves = [i for i in range(9) if buttons[i]["text"] == ""]
    if not available_moves:
        return

    # Simple AI logic: Win > Block > Random
    for i in available_moves:
        buttons[i]["text"] = "O"
        if check_winner():
            return
        buttons[i]["text"] = ""

    for i in available_moves:
        buttons[i]["text"] = "X"
        if check_winner():
            buttons[i]["text"] = "O"
            return
        buttons[i]["text"] = ""

    # Random move if no immediate win/block
    move = random.choice(available_moves)
    buttons[move]["text"] = "O"
    buttons[move].config(fg="#EEEEEE")
    if check_winner():
        return


def button_click(index):
    global current_player
    if buttons[index]["text"] == "":
        buttons[index]["text"] = current_player
        buttons[index].config(fg="#EEEEEE")

        if check_winner():
            return

        # Player vs Player mode
        if mode.get() == "PVP":
            current_player = "O" if current_player == "X" else "X"
            label_turn.config(text=f"Player {current_player}'s Turn", fg="#00ADB5")

        # Player vs AI mode
        elif mode.get() == "AI":
            label_turn.config(text="Computer's Turn 🤖", fg="#FFB703")
            root.update()
            ai_move()
            label_turn.config(text="Your Turn (X)", fg="#00ADB5")

    else:
        messagebox.showwarning("Invalid Move", "This cell is already taken!")


def disable_buttons():
    for button in buttons:
        button.config(state="disabled")


def enable_buttons():
    for button in buttons:
        button.config(state="normal")


def record_score(result):
    """Save game result to Excel via pandas."""
    global df
    if mode.get() == "AI":
        player = "You"
        opponent = "Computer"
    else:
        player = "Player X"
        opponent = "Player O"

    if result == "X":
        outcome = f"{player} Won"
    elif result == "O":
        outcome = f"{opponent} Won"
    else:
        outcome = "Draw"

    new_row = {"Player": player, "Opponent": opponent, "Result": outcome}
    df = pd.concat([df, pd.DataFrame([new_row])], ignore_index=True)
    df.to_excel(excel_file, index=False)
    print(f"✅ Score updated in {excel_file}")


def reset_game():
    global current_player
    current_player = "X"
    for button in buttons:
        button.config(text="", state="normal", bg="#393E46", fg="#EEEEEE")
    label_turn.config(text="Player X's Turn", fg="#00ADB5")


# ----------- UI Section -----------

title_label = tk.Label(
    root, text="Tic Tac Toe 🕹️", font=("Poppins", 24, "bold"), bg="#222831", fg="#EEEEEE"
)
title_label.pack(pady=10)

# Game mode selection
mode_frame = tk.Frame(root, bg="#222831")
mode_frame.pack()

tk.Label(
    mode_frame, text="Select Mode:", bg="#222831", fg="#EEEEEE", font=("Poppins", 12)
).grid(row=0, column=0, padx=5)
tk.Radiobutton(
    mode_frame,
    text="Player vs AI",
    variable=mode,
    value="AI",
    bg="#222831",
    fg="#00ADB5",
    selectcolor="#393E46",
    font=("Poppins", 12),
).grid(row=0, column=1)
tk.Radiobutton(
    mode_frame,
    text="Player vs Player",
    variable=mode,
    value="PVP",
    bg="#222831",
    fg="#00ADB5",
    selectcolor="#393E46",
    font=("Poppins", 12),
).grid(row=0, column=2)

label_turn = tk.Label(
    root, text="Player X's Turn", font=("Poppins", 16), bg="#222831", fg="#00ADB5"
)
label_turn.pack(pady=5)

frame = tk.Frame(root, bg="#222831")
frame.pack()

for i in range(9):
    button = tk.Button(
        frame,
        text="",
        font=("Poppins", 20, "bold"),
        width=5,
        height=2,
        bg="#393E46",
        fg="#EEEEEE",
        activebackground="#00ADB5",
        command=lambda i=i: button_click(i),
    )
    button.grid(row=i // 3, column=i % 3, padx=5, pady=5)
    buttons.append(button)

reset_btn = tk.Button(
    root,
    text="Restart 🔁",
    font=("Poppins", 14, "bold"),
    bg="#00ADB5",
    fg="#EEEEEE",
    command=reset_game,
)
reset_btn.pack(pady=15)

# Run app
root.mainloop()
