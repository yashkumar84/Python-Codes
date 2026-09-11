board = ["1" , "2" , "3" , "4" , "5" , "6" , "7" , "8" , "9"]

def showBoard():
    print()
    print(board[0] + " | " + board[1] + " | " +board[2] )
    print("--+---+--")
    print(board[3] + " | " + board[4] + " | " +board[5] )
    print("--+---+--")
    print(board[6] + " | " + board[7] + " | " +board[8] )


def checkWinner(player):
    if board[0] == player and board[1] == player and board[2] == player:
        return True
    if board[3] == player and board[4] == player and board[5] == player:
        return True
    if board[6] == player and board[7] == player and board[8] == player:
        return True
    if board[0] == player and board[3] == player and board[6] == player:
        return True
    if board[1] == player and board[4] == player and board[7] == player:
        return True
    if board[2] == player and board[5] == player and board[8] == player:
        return True
    if board[0] == player and board[4] == player and board[8] == player:
        return True
    if board[2] == player and board[4] == player and board[6] == player:
        return True
    return False

player = "X"
for turn in range(9):
    showBoard()
    position = int(input("Choose Player " + player + ", Position from (1 , 9)"))

    if board[position - 1] == "O" or board[position - 1] == "X":
        print("Position Already Taken")
        continue

    board[position - 1] = player

    if checkWinner(player):
        showBoard()
        print(player + " is Winner ")
        break

    if player == "X":
        player = "O"
    else:
        player="X"
else:
    showBoard()
    print("It is A Draw")

