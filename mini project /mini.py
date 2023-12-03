

def display_board():
    print(f"{board[0]} | {board[1]} | {board[2]}")
    print("--+---+--")
    print(f"{board[3]} | {board[4]} | {board[5]}")
    print("--+---+--")
    print(f"{board[6]} | {board[7]} | {board[8]}")

def player_input(player):
    position = int(input(f"Player {player}, enter a position (1-9): ")) - 1
    if board[position] == " ":
        board[position] = "X" if player == 1 else "O"
    else:
        print("Invalid move. Try again.")
        player_input(player)

def check_win():
    for i in range(0, 3):
        if (board[i] == board[i + 3] == board[i + 6] != " ") or \
           (board[i * 3] == board[i * 3 + 1] == board[i * 3 + 2] != " "):
            return True
    if (board[0] == board[4] == board[8] != " ") or (board[2] == board[4] == board[6] != " "):
        return True
    return False

def play():
    display_board()
    for turn in range(9):
        player = 1 if turn % 2 == 0 else 2
        player_input(player)
        display_board()
        if check_win():
            print(f"Player {player} wins!")
            break
    else:
        print("It's a draw!")

play()