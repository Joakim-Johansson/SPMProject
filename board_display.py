import os

# Define ANSI escape codes for red and green text
red_color = "\033[91m"   # Red color escape code
green_color = "\033[92m" # Green color escape code
reset_color = "\033[0m"  # Reset color escape code

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def display_board(player1, player2):
    # Create the formatted strings for Player 1 and Player 2
    formatted_player1 = f" Player 1  ({player1})"
    formatted_player2 = f" Player 2  ({player2})"

    # Create the game pieces here
    player1_pieces = f"{green_color}X{reset_color}" + " " * 5
    player2_pieces = f"{red_color}O{reset_color}" + " " * 5

    # Create the game board here
    board = f"""
{' ' * 10}{formatted_player1}{' ' * 58}{formatted_player2}

{'      ' + player1_pieces + ' ' * 65}{player2_pieces}
{'      ' + player1_pieces + ' ' * 65}{player2_pieces}
{'      ' + player1_pieces + ' ' * 65}{player2_pieces}
{'      ' + player1_pieces + ' ' * 65}{player2_pieces}
{'      ' + player1_pieces + ' ' * 65}{player2_pieces}
{'      ' + player1_pieces + ' ' * 65}{player2_pieces}
{'      ' + player1_pieces + ' ' * 65}{player2_pieces}
{'      ' + player1_pieces + ' ' * 65}{player2_pieces}
{'      ' + player1_pieces + ' ' * 65}{player2_pieces}


. ________________________________________ . _______________________________________ .
|                                          |                                         |                    
|                                          |                                         |
|            . ______________ . __________ . ___________________________ .           |                                       
|            |                             |                             |           |
|            |                             |                             |           |
|            |           . _______________ . ____________ .              |           |
|            |           |                                |              |           |
|            |           |                                |              |           |
|            |           |                                |              |           |
|            |           |                                |              |           |
. __________ . _________ .                                . ____________ . _________ .
|            |           |                                |              |           |
|            |           |                                |              |           |
|            |           |                                |              |           | 
|            |           |                                |              |           |
|            |           . _____________  .  ____________ .              |           |
|            |                            |                              |           |
|            |                            |                              |           |
|            . __________________________ . ____________________________ .           |                 
|                                         |                                          |
|                                         |                                          |
. _______________________________________ . ________________________________________ .

"""

    print(board)

