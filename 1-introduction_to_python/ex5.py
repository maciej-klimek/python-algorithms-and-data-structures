
board = [
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0]
           ]

def print_board(board):
    c = 1
    print("\n----------------------------------")
    print("     a   b   c")
    for i in board:
        print("   -------------")
        print(f"{c}  |", end = '')
        c+=1
        for j in i:
            if j == 1:
                j = "x"
            elif j == 2:
                j = "o"
            else:
                j = " "

            print(f" {j} |", end ='')
        print()
    print("   -------------")


def check_win(board):
    # checking rows
    for row in board:
        if row[0] == row[1] == row[2] != 0:
            return row[0]

    # checking columns
    for column in range(3):
        if board[0][column] == board[1][column] == board[2][column] != 0:
            return board[0][column]

    # checking diagonals
    if board[0][0] == board[1][1] == board[2][2] != 0:
        return board[0][0]

    if board[0][2] == board[1][1] == board[2][0] != 0:
        return board[0][2]
    
    draw = True
    for row in board:
        for field in row:
            if field == 0:
                draw = False

    if draw == False:
        return 0 
    return 3
    

def move(tbl, player):
    valid = False
    while not valid:
        x, y = 3, 3
        if player == 1:
            player_display = 'x'
        else:
            player_display = 'o'

        print(f"Choose move for {player_display} \n-> ", end = '')
        move = str(input())
        if len(move) != 2:
            print("Invalid move")
        else:
        
            if move[0] == "a":
                y = 0
            elif move[0] == "b":
                y = 1
            elif move[0] == "c":
                y = 2
            

            if move[1] == "1":
                x = 0
            elif move[1] == "2":
                x = 1
            elif move[1] == "3":
                x = 2
            
            if x != 3 and y != 3 and tbl[x][y] == 0:
                valid = True
                tbl[x][y] = player
            else:
                print("Invalid move")


def main():
    
    result = 0
    player = [1,2]
    while result == 0:
        print_board(board)
        move(board, player[0])
        result = check_win(board)
        player[0], player[1] = player[1], player[0]


    print_board(board)
    if result == 1:
        print("Playet x won")
    elif result == 2:
        print("Player o won")
    else:
        print("Draw")


main()
