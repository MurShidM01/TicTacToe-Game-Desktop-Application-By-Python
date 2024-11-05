from tkinter import *
from tkinter import messagebox
import random

# Initialize the main app window
app = Tk()
width, height = 540, 500
sys_width, sys_height = app.winfo_screenwidth(), app.winfo_screenheight()
c_x, c_y = int(sys_width/2 - width/2), int(sys_height/2 - height/2)
app.geometry(f'{width}x{height}+{c_x}+{c_y}')
app.title("TicTacToe Game")
app.resizable(False, False)
app.config(bg="#41cccc")
app.iconbitmap(r"D:\Programming\Python\TK-Inter\TicTacToe Game\Icon.ico")

# Game mode selection variable
game_mode = StringVar(value="Computer")

# Track current player, buttons, and game states
current_player = "X"
buttons = [[None for _ in range(3)] for _ in range(3)]
states = [[0 for _ in range(3)] for _ in range(3)]

# Function to switch between frames
def show_frame(frame):
    frame.tkraise()

# Update game status label
def update_status():
    status_label.config(text=f"Player {current_player}'s Turn" if game_mode.get() == "Friend" else f"{'Your Turn' if current_player == 'X' else 'Computer’s Turn'}", fg="black")

# Check for winner or draw
def check_winner():
    for row in range(3):
        if states[row][0] == states[row][1] == states[row][2] != 0:
            return states[row][0]
    for col in range(3):
        if states[0][col] == states[1][col] == states[2][col] != 0:
            return states[0][col]
    if states[0][0] == states[1][1] == states[2][2] != 0:
        return states[0][0]
    if states[0][2] == states[1][1] == states[2][0] != 0:
        return states[0][2]
    return None

# Handle button click
def clicked(r, c):
    global current_player
    if states[r][c] == 0:
        buttons[r][c].config(text=current_player, state="disabled")
        states[r][c] = current_player
        winner = check_winner()
        if winner:
            status_label.config(text=f"Player {winner} wins!" if game_mode.get() == "Friend" else f"{'You Win!' if winner == 'X' else 'Computer Wins!'}", fg="green")
            disable_all_buttons()
            messagebox.showinfo("Game Over", f"Player {winner} wins!" if game_mode.get() == "Friend" else f"{'You Win!' if winner == 'X' else 'Computer Wins!'}")
        elif all(states[i][j] != 0 for i in range(3) for j in range(3)):
            status_label.config(text="It's a draw!", fg="orange")
            messagebox.showinfo("Game Over", "It's a draw!")
        else:
            current_player = "O" if current_player == "X" else "X"
            if game_mode.get() == "Computer" and current_player == "O":
                app.after(500, computer_move)
            else:
                update_status()

# Computer's move in Computer Mode
def computer_move():
    available_moves = [(i, j) for i in range(3) for j in range(3) if states[i][j] == 0]
    if available_moves:
        r, c = random.choice(available_moves)
        clicked(r, c)

# Disable all buttons at end of game
def disable_all_buttons():
    for i in range(3):
        for j in range(3):
            buttons[i][j].config(state="disabled")

# Reset the game
def reset_game():
    global current_player
    current_player = "X"
    update_status()
    for i in range(3):
        for j in range(3):
            buttons[i][j].config(text="", state="normal", bg="#41cccc")
            states[i][j] = 0
    if game_mode.get() == "Computer" and current_player == "O":
        app.after(500, computer_move)

# Define Frames
frame1 = Frame(app, bg="#41cccc")
frame2 = Frame(app, bg="#41cccc")
frame3 = Frame(app, bg="#41cccc")
for frame in (frame1, frame2):
    frame.grid(row=0, column=0, sticky="nsew")

# Frame 1 - Game Mode Selection
Label(frame1, text="Welcome to Tic-Tac-Toe Game", bg="#41cccc", fg="black", font=("Cooper Black", 20)).pack(pady=60, padx=60)
Label(frame1, text="Select Mode of the Game", bg="#41cccc", font=("Cooper Black", 14)).pack(pady=20)

# Radio buttons for mode selection
Radiobutton(frame1, text="Computer Mode", variable=game_mode, value="Computer", font=("Cooper Black", 12), bg="#41cccc").pack(pady=5)
Radiobutton(frame1, text="Friend Mode", variable=game_mode, value="Friend", font=("Cooper Black", 12), bg="#41cccc").pack(pady=10)

# Start button
Button(frame1, text="Start Playing", font=("Cooper Black", 14), bg="red", fg="black", borderwidth=3, relief='solid', command=lambda: show_frame(frame2)).pack(pady=20)

# Frame 2 - Game Screen
Label(frame2, text="Tic-Tac-Toe Game", bg="#41cccc", fg="black", font=("Cooper Black", 20)).pack(pady=10)
status_label = Label(frame2, text="", bg="#41cccc", fg="red", font=("Cooper Black", 14))
status_label.pack(pady=10)
update_status()

# Game button grid
button_frame = Frame(frame2, bg="#41cccc")
button_frame.pack(pady=10)
for i in range(3):
    for j in range(3):
        buttons[i][j] = Button(
            button_frame, text="", height=2, width=6, font=("Cooper Black", 20),
            bg="white", fg="black", activebackground="#a8e6cf", borderwidth=3, relief='solid',
            command=lambda r=i, c=j: clicked(r, c)
        )
        buttons[i][j].grid(row=i, column=j, padx=3, pady=3)

# Reset and Back buttons in frame 2
button_frame = Frame(frame2, bg="#41cccc")
button_frame.pack(pady=15)

# Reset button
reset_button = Button(button_frame, text="Reset Game", font=("Cooper Black", 12), bg="red", fg="black", borderwidth=3, relief='solid', command=reset_game)
reset_button.pack(side=LEFT, padx=10)

# Back button
back_button = Button(button_frame, text="      Back      ", command=lambda: show_frame(frame1), bg="red", fg="black", font=("Cooper Black", 12), relief="solid", borderwidth=3)
back_button.pack(side=LEFT, padx=10)


# Footer Frame
footer_label = Label(frame3, text="© 2024 Developed By Ali Khan Jalbani", bg="#41cccc", fg="white", font=("Times New Roman", 11))
footer_label.pack()

# Pack the footer at the bottom
frame3.grid(row=1, column=0, sticky='ew')

# Show the initial frame
show_frame(frame1)
app.mainloop()
