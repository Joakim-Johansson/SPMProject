
import os


def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


def display_title():
    clear_screen()
    neon_green = "\033[1;32m"  # ANSI escape code for neon green text
    reset_color = "\033[0m"    # ANSI escape code to reset text color

    print(f"{neon_green}███╗   ██╗███████╗███╗   ███╗███████╗")
    print(f"████╗  ██║██╔════╝████╗ ████║██╔════╝")
    print(f"██╔██╗ ██║█████╗  ██╔████╔██║███████╗")
    print(f"██║╚██╗██║██╔══╝  ██║╚██╔╝██║╚════██║")
    print(f"██║ ╚████║███████╗██║ ╚═╝ ██║███████║")
    print(f"╚═╝  ╚═══╝╚══════╝╚═╝     ╚═╝╚══════╝{reset_color}")
    input("Press Enter to continue...")




def display_menu():
    clear_screen()
    print("╔════════════════════════════╗")
    print("║        MAIN MENU           ║")
    print("╠════════════════════════════╣")

    print("╠════════════════════════════╣")
    print("║  1. PLAY                   ║")
    print("╠════════════════════════════╣")

    print("╠════════════════════════════╣")
    print("║  2. INSTRUCTIONS           ║")
    print("╠════════════════════════════╣")

    print("╠════════════════════════════╣")
    print("║  3. QUIT                   ║")
    print("╚════════════════════════════╝")


def play_game():
    clear_screen()
    print("Let's play NEMS!")
    # Add your game logic here
    input("Press Enter to return to the main menu...")

def display_instructions():
    clear_screen()
    instructions = """
NEMS Instructions:
NEMS is a two-player board game played in the terminal. Please ensure you have Python installed on your system.

Game Overview:
- NEMS is played on a 24-intersection square board.
- Each player has two sets of 9 pieces, one in red and one in green, allowing for variety and strategy.
- Turns alternate between players, starting with Player 1.
- The game is divided into three phases: Fill the board, move pieces, and advanced strategy (optional).

Game Phases:
- In Phase 1, both players fill the board with their pieces.
- In Phase 2, players take turns moving one piece to an adjacent intersection.
- In Phase 3 (optional), when only three pieces are left for each player, they can move to any available intersection, adding an extra layer of strategy.

Winning and Losing:
- Players aim to form 'mills' by placing three of their pieces in a row on the same line (excluding diagonals).
- Forming a mill allows a player to remove one opponent's piece.
- The game continues until one player is left with only two pieces, resulting in a loss for that player.
- The game can also end after a total of 300 moves with no clear winner.

GET READY TO PLAY! Enjoy NEMS!
"""
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





