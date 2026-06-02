import tkinter as tk
from tkinter import messagebox
import random
try:
    import winsound

    def play_sound():
        winsound.Beep(700, 100)
except:
    def play_sound():
        pass
root = tk.Tk()
root.title("Tic-Tac-Toe AI")
root.geometry("500x650")
root.configure(bg="#dff6ff")
board = [""] * 9
player = "X"
ai = "O"
player_score = 0
ai_score = 0
draw_score = 0
difficulty = tk.StringVar()
difficulty.set("Easy")
score_label = tk.Label(
    root,
    text="Player: 0 | AI: 0 | Draws: 0",
    font=("Arial", 14, "bold"),
    bg="#dff6ff"
)
score_label.pack(pady=10)
status_label = tk.Label(
    root,
    text="Your Turn (X)",
    font=("Arial", 16, "bold"),
    bg="#dff6ff",
    fg="blue"
)
status_label.pack()
frame_top = tk.Frame(root, bg="#dff6ff")
frame_top.pack(pady=10)

tk.Label(
    frame_top,
    text="Difficulty:",
    font=("Arial", 12),
    bg="#dff6ff"
).pack(side=tk.LEFT)

tk.OptionMenu(frame_top, difficulty, "Easy", "Hard").pack(side=tk.LEFT)
frame = tk.Frame(root, bg="#dff6ff")
frame.pack()
buttons = []
def update_score():
    score_label.config(
        text=f"Player: {player_score} | AI: {ai_score} | Draws: {draw_score}"
    )
def check_winner(symbol):
    wins = [
        [0,1,2],[3,4,5],[6,7,8],
        [0,3,6],[1,4,7],[2,5,8],
        [0,4,8],[2,4,6]
    ]
    for combo in wins:
        if all(board[i] == symbol for i in combo):
            return True
    return False
def board_full():
    return "" not in board
def end_game(message):
    global player_score, ai_score, draw_score
    if "You Win" in message:
        player_score += 1
    elif "AI Wins" in message:
        ai_score += 1
    else:
        draw_score += 1
    update_score()
    messagebox.showinfo("Game Over", message)
    reset_board()
def player_move(index):
    if board[index] != "":
        return
    board[index] = player
    buttons[index].config(
        text=player,
        bg="#90ee90",
        fg="black"
    )
    play_sound()
    if check_winner(player):
        end_game("You Win!")
        return
    if board_full():
        end_game("It's a Draw!")
        return
    status_label.config(text="AI Thinking...")
    root.after(500, ai_move)
def ai_move():
    if difficulty.get() == "Easy":
        easy_ai()
    else:
        hard_ai()
    if check_winner(ai):
        end_game("AI Wins!")
        return
    if board_full():
        end_game("It's a Draw!")
        return
    status_label.config(text="Your Turn (X)")
def easy_ai():
    empty = [i for i in range(9) if board[i] == ""]
    if empty:
        move = random.choice(empty)
        board[move] = ai
        buttons[move].config(
            text=ai,
            bg="#ffb6c1",
            fg="black"
        )
        play_sound()
def hard_ai():
    for i in range(9):
        if board[i] == "":
            board[i] = ai
            if check_winner(ai):
                buttons[i].config(
                    text=ai,
                    bg="#ffb6c1"
                )
                play_sound()
                return
            board[i] = ""
    for i in range(9):
        if board[i] == "":
            board[i] = player
            if check_winner(player):
                board[i] = ai
                buttons[i].config(
                    text=ai,
                    bg="#ffb6c1"
                )
                play_sound()
                return
            board[i] = ""
    if board[4] == "":
        board[4] = ai
        buttons[4].config(
            text=ai,
            bg="#ffb6c1"
        )
        play_sound()
        return
    empty = [i for i in range(9) if board[i] == ""]
    if empty:
        move = random.choice(empty)
        board[move] = ai
        buttons[move].config(
            text=ai,
            bg="#ffb6c1"
        )
        play_sound()
def reset_board():
    global board
    board = [""] * 9
    for button in buttons:
        button.config(
            text="",
            bg="white"
        )
    status_label.config(text="Your Turn (X)")
for row in range(3):
    for col in range(3):
        index = row * 3 + col
        button = tk.Button(
            frame,
            text="",
            font=("Arial", 24, "bold"),
            width=5,
            height=2,
            bg="white",
            command=lambda i=index: player_move(i)
        )
        button.grid(row=row, column=col, padx=5, pady=5)
        buttons.append(button)
reset_btn = tk.Button(
    root,
    text="Restart Game",
    font=("Arial", 14, "bold"),
    bg="orange",
    fg="black",
    command=reset_board
)
reset_btn.pack(pady=20)
root.mainloop()
