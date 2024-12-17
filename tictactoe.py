import tkinter
import random

#creating the tile
def set_tile(row, column):
    global current_player

    if game_over:
        return

    # Verifying if the spot is already taken
    if board[row][column]["text"] != "":
        return

    # Marking the board with the current player
    board[row][column]["text"] = current_player 

    # Finding who the current player is
    if current_player == playerO:
        current_player = playerX
    else:
        current_player = playerO

    # Displaying the current player for example - X's turn or O's turn
    label["text"] = current_player + "'s turn"

    # Checking the winner
    check_winner()

    #Creating the ai feature so that when the player doesn't have a move and the game is not over then the ai will choose.
    if not game_over and current_player == playerO:
        ai_move()

# Checking the board to see who wins (you or the ai)
def check_winner():
    global turns, game_over, user_score, ai_score
    turns += 1

    # Horizontally, check 3 rows
    for row in range(3):
        if (board[row][0]["text"] == board[row][1]["text"] == board[row][2]["text"] and board[row][0]["text"] != ""):
            # Shows the winner            
            label.config(text=board[row][0]["text"] + " is the winner!", foreground=red)
            for column in range(3):
                board[row][column].config(foreground=red, background=light_grey)
            # Set the game over to True so that the user can't keep playing once someone has won.            
            game_over = True
            # Update the scoreboard on the gui
            update_score(board[row][0]["text"])
            return

    # Vertically, check 3 rows
    for column in range(3):
        if (board[0][column]["text"] == board[1][column]["text"] == board[2][column]["text"] and board[0][column]["text"] != ""):
            # Shows the winner
            label.config(text=board[0][column]["text"] + " is the winner!", foreground=red)
            for row in range(3):
                board[row][column].config(foreground=red, background=light_grey)
            # Set the game over to True so that the user can't keep playing once someone has won.
            game_over = True
            # Update the scoreboard on the gui
            update_score(board[0][column]["text"])
            return

    # Checking diagonally - [0][0], [1][1], [2][2] - these are the positions of the grid for the diagonal line
    if (board[0][0]["text"] == board[1][1]["text"] == board[2][2]["text"] and board[0][0]["text"] != ""):
        label.config(text=board[0][0]["text"] + " is the winner!", foreground=red)
        for i in range(3):
            # Changes the colour of the background and the text colour to represent the user or ai has won.
            board[i][i].config(foreground=red, background=light_grey)
        game_over = True
        # Update the scoreboard on the gui
        update_score(board[0][0]["text"])
        return

    # Other diagonally side [0][2], [1][1], [2][0] - these are the positions of the other diagonal line
    if (board[0][2]["text"] == board[1][1]["text"] == board[2][0]["text"] and board[0][2]["text"] != ""):
        label.config(text=board[0][2]["text"] + " is the winner!", foreground=red)
        board[0][2].config(foreground=red, background=light_grey)
        board[1][1].config(foreground=red, background=light_grey)
        board[2][0].config(foreground=red, background=light_grey)
        game_over = True
        # Update the scoreboard on the gui
        update_score(board[0][2]["text"])
        return

    # Confirm if it's a tie
    if turns == 9:
        game_over = True
        label.config(text="Tie!", foreground=red)

# The scoreboard that's shown to the users of the current score between the user and the ai
def update_score(winner):
    global user_score, ai_score
    if winner == playerX:
        user_score += 1
    else:
        ai_score += 1
    score_label.config(text=f"Score - User: {user_score} | AI: {ai_score}")

def new_game():
    global turns, game_over, current_player

    # turns need to start at 0
    turns = 0
    # game over needs to be set at False at the start
    game_over = False
    # the current player is playerX (this is not important, this could also be playerO)
    current_player = playerX

    # Shows the player turn
    label.config(text=current_player + "'s turn", foreground="white")

    for row in range(3):
        for column in range(3):
            board[row][column].config(text="", foreground=light_blue, background=dark_grey)

# Creating the au movement
def ai_move():
    empty_tiles = [(row, column) for row in range(3) for column in range(3) if board[row][column]["text"] == ""]
    if empty_tiles:
        # Allows the ai to choose a random empty tile to place the letter in.
        row, column = random.choice(empty_tiles)
        set_tile(row, column)

# Game setup
playerX = "X"
playerO = "O"
current_player = playerX
board = [[0, 0, 0],
         [0, 0, 0],
         [0, 0, 0]]

# Fujitsu red and other colours
red = "#E60012"
light_blue = "#E2EAF4"
dark_grey = "#AFA8A8"
light_grey = "#E9E6E6"

# Setting global variables
turns = 0
game_over = False
user_score = 0
ai_score = 0

# Window setup
window = tkinter.Tk()
# Setting the title
window.title("The Greatest Tic Tac Toe")
# Making it so the user cant resize the window
window.resizable(False, False)

frame = tkinter.Frame(window)
# Shows the current player in Fujitsu font
label = tkinter.Label(frame, text=current_player + "'s turn", font=("Fujitsu Infinity Pro", 20), background=dark_grey, foreground="white")
# Shows the scoreboard
score_label = tkinter.Label(frame, text=f"Score - User: {user_score} | AI: {ai_score}", font=("Fujitsu Infinity Pro", 16), background=dark_grey, foreground="white")

label.grid(row=0, column=0, columnspan=3, sticky="we")
score_label.grid(row=1, column=0, columnspan=3, sticky="we")

for row in range(3):
    for column in range(3):
        board[row][column] = tkinter.Button(frame, text="", font=("Fujitsu Infinity Pro", 20, "bold"), background=dark_grey, foreground=light_blue, width=4, height=1,
                                            command=lambda row=row, column=column: set_tile(row, column))
        board[row][column].grid(row=row + 2, column=column)

button = tkinter.Button(frame, text="restart", font=("Fujitsu Infinity Pro", 20), background=dark_grey, foreground="white", command=new_game)

# This spreads the whole background/button across the whole screen "we" - stands for west to east
button.grid(row=5, column=0, columnspan=3, sticky="we")
frame.pack()

# Update ethe window so that all the elements are rendered
window.update()

# Get the width and height of the window 
window_width = window.winfo_width()
window_height = window.winfo_height()

# Get the width and height of the screen
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

# Calculate the x and y coordinates to center the window on the screen
window_x = int((screen_width / 2) - (window_width / 2))
window_y = int((screen_height / 2) - (window_height / 2))

# Set the geometry of the window to center it on the screen
window.geometry(f"{window_width}x{window_height}+{window_x}+{window_y}")

window.mainloop()