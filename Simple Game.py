def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

def check_winner(board):
    # Check rows
    for row in board:
        if row[0] == row[1] == row[2] != ' ':
            return row[0]
    
    # Check columns
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] != ' ':
            return board[0][col]
    
    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] != ' ':
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] != ' ':
        return board[0][2]
    
    return None

def is_board_full(board):
    for row in board:
        for cell in row:
            if cell == ' ':
                return False
    return True

def tic_tac_toe():
    print("Welcome to Tic-Tac-Toe!")
    print("Player 1 is 'X', Player 2 is 'O'. Let's begin!")
    
    current_player = 'X'
    board = [[' ' for _ in range(3)] for _ in range(3)]
    winner = None
    
    while not winner and not is_board_full(board):
        print_board(board)
        print(f"Player {current_player}, it's your turn.")
        
        valid_move = False
        while not valid_move:
            try:
                row = int(input("Enter row number (1-3): ")) - 1
                col = int(input("Enter column number (1-3): ")) - 1
                
                if 0 <= row < 3 and 0 <= col < 3 and board[row][col] == ' ':
                    board[row][col] = current_player
                    valid_move = True
                else:
                    print("Invalid move. Please try again.")
            except ValueError:
                print("Invalid input. Please enter a number.")

        winner = check_winner(board)
        if winner:
            print_board(board)
            print(f"Player {winner} wins!")
        elif is_board_full(board):
            print_board(board)
            print("It's a draw!")

        # Switch turns
        if current_player == 'X':
            current_player = 'O'
        else:
            current_player = 'X'

if __name__ == "__main__":
    tic_tac_toe()
