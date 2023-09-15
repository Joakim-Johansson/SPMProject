import os

# Define ANSI escape codes for red and green text
red_color = "\033[91m"   # Red color escape code
green_color = "\033[92m" # Green color escape code
reset_color = "\033[0m"  # Reset color escape code

from instructions import get_instructions  # Import the function from instructions.py
from title_display import display_title  # Import the function from title_display.py
from menu_display import display_menu  # Import the function from menu_display.py
from board_display import display_board # Import the board from board_display.py


def clear_screen():  
    os.system('cls' if os.name == 'nt' else 'clear')

def play_game():
    clear_screen()
    print("Let's play NEMS!")

    # Call the display_board function with player names to display the game board
    display_board(green_color + "X" + reset_color, red_color + "O" + reset_color)  # Pass the player names without extra formatting
    # Add your game logic here
    input("Press Enter to return to the main menu...")

def display_instructions():
    clear_screen()
    instructions = get_instructions()  # Use the imported function to get the instructions
    print(instructions)
    input("Press Enter to return to the main menu...")
    
def main():
    while True:
        display_title()
        display_menu()
        choice = input("Enter your choice (1/2/3): ")
        
        if choice == '1':
            play_game()
        elif choice == '2':
            display_instructions()
        elif choice == '3':
            print("Thanks for playing NEMS! Goodbye!")
            break
        else:
            input("Invalid choice. Press Enter to try again...")

if __name__ == "__main__":
    main()
