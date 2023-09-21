red_color = "\033[91m"   # Red color escape code
green_color = "\033[92m" # Green color escape code
reset_color = "\033[0m"  # Reset color escape code

class NEMS:
    def __init__(self):
        self.players = {
            1: {
                'symbol': "X",
                'pieces_left': 3,
                'moves': []
            },
            2: {
                'symbol': "O",
                'pieces_left': 3,
                'moves': []
            }
        }

        # Two copies, one for current state of the board (positions), the other for keeping track of structure of board,
        # since positions will be edited
        self.positions = ["A1", "A2", "A3", "B1", "B2", "B3", "C1", "C2", "C3", "D1", "D2",
               "D3", "D4", "D5", "D6", "E1", "E2", "E3", "F1", "F2", "F3", "G1", "G2", "G3", "H1", "H2", "H3"]
        self.state = ["A1", "A2", "A3", "B1", "B2", "B3", "C1", "C2", "C3", "D1", "D2",
               "D3", "D4", "D5", "D6", "E1", "E2", "E3", "F1", "F2", "F3", "G1", "G2", "G3", "H1", "H2", "H3"]
        self.valid_moves = [["A1", "A2", "A3"], ["B1", "B2", "B3"], ["C1", "C2", "C3"],
                    ["D1", "D2", "D3"], ["D4", "D5", "D6"], ["E1", "E2", "E3"],
                    ["F1", "F2", "F3"], ["G1", "G2", "G3"], ["A1", "D1", "G1"],
                    ["B1", "C1", "E1"], ["C1", "D1", "E1"], ["C3", "D1", "E1"],
                    ["B3", "D2", "E3"], ["A3", "D3", "G3"], ["E2", "F2", "G2"]]

    def display_board(self, player1, player2):
        # Create the formatted strings for Player 1 and Player 2
        formatted_player1 = f" Player 1  ({player1})"
        formatted_player2 = f" Player 2  ({player2})"

        # Create the game pieces here
        player1_pieces = f"{green_color}X{reset_color}" + " " * 5
        player2_pieces = f"{red_color}O{reset_color}" + " " * 5

        # Create the game board here
        game_board = f"""
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

    {self.positions[0]}________________________________________ {self.positions[1]} _______________________________________ {self.positions[2]}
    |                                          |                                         |                    
    |                                          |                                         |
    |            {self.positions[3]} ________________________ {self.positions[4]} ___________________________ {self.positions[5]}           |                                       
    |            |                             |                             |           |
    |            |                             |                             |           |
    |            |           {self.positions[6]} _______________{self.positions[7]}____________{self.positions[8]}              |           |
    |            |           |                                |              |           |
    |            |           |                                |              |           |
    |            |           |                                |              |           |
    |            |           |                                |              |           |
    {self.positions[9]} __________ {self.positions[10]} _________ {self.positions[11]}                                {self.positions[12]} ____________ {self.positions[13]} _________ {self.positions[14]}
    |            |           |                                |              |           |
    |            |           |                                |              |           |
    |            |           |                                |              |           | 
    |            |           |                                |              |           |
    |            |           {self.positions[15]} ___________  {self.positions[16]}  ___________ {self.positions[17]}              |           |
    |            |                            |                              |           |
    |            |                            |                              |           |
    |            {self.positions[18]} _________________________ {self.positions[19]} __________________________ {self.positions[20]}           |                 
    |                                         |                                          |
    |                                         |                                          |
    {self.positions[21]} _______________________________________ {self.positions[22]} ________________________________________ {self.positions[23]}

    """

        return game_board

    def already_taken(self, position):
        for player_num in self.players:
            if position in self.players[player_num]['moves']:
                return True
        return False

    def remove_piece(self, position, player):
        pass
    

    # Check if 3 in a row
    def check_mills(self, position, player):
        for mills in self.valid_moves:
            if position in mills:
                x = 0
                for s in mills:
                    if s in self.players[player]['moves']:
                        x += 1
                if x == 3:
                    return True
        return False

    def can_reach(self, move_from, move_to):
        # Check if the move is valid (one step in either x or y direction)
        for x in self.valid_moves:
            if move_to in x:
                if move_from in x:
                    # Check if Adjacent
                    # For example, A1 to A3 should be invalid. But A1 to D1 is valid, so we'll need to use indexes.
                    if abs(x.index(move_from) - x.index(move_to)) == 1:
                        return True
        return False

    def place_piece(self, position, move_from, player):
        if self.already_taken(position):
            return False

        player_info = self.players[player]

        if move_from is None:
            player_info['pieces_left'] -= 1
            player_info['moves'].append(position)
        elif self.can_reach(move_from, position):
            player_info['moves'].remove(move_from)
            player_info['moves'].append(position)
        else:
            return False

        placement = self.positions.index(position)

        if move_from is not None:
            self.positions[self.state.index(move_from)] = move_from

        self.positions[placement] = player_info['symbol']

        print(self.display_board(green_color + "X" + reset_color, red_color + "O" + reset_color))
        return True

    def play(self):
        current_player = 1
        while True:
            player_info = self.players[current_player]
            if player_info['pieces_left'] == 0:
                player_position_from = input(f"Player {current_player}, enter your position from: ")
                player_position_to = input(f"Player {current_player}, enter your position to: ")
                self.place_piece(player_position_to, player_position_from, current_player)
            else:
                player_position_to = input(f"Player {current_player}, enter your position to: ")
                self.place_piece(player_position_to, None, current_player)

            if self.check_mills(player_position_to, current_player):
                removed_piece = input(f"Player {current_player}, enter opponent piece to remove: ")

            if len(self.players[3 - current_player]['moves']) + self.players[3 - current_player]['pieces_left'] == 2:
                print(f"Player {current_player} wins!")
                break

            current_player = 3 - current_player

if __name__ == "__main__":
    game = NEMS()
    game.play()
