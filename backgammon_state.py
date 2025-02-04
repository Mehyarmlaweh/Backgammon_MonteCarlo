import random

class BackgammonState:
    def __init__(self):
        # Initialize the board with 24 points + bar and off areas
        self.board = [0] * 26  # Points 1-24, bar at 25, off at 26
        self.bar = [0, 0]      # Bar for Player 1 and Player 2
        self.off = [0, 0]      # Pieces taken off for Player 1 and Player 2
        self.player_turn = 1   # 1 for Player 1, -1 for Player 2

    def copy(self):
        new_state = BackgammonState()
        new_state.board = self.board.copy()
        new_state.bar = self.bar.copy()
        new_state.off = self.off.copy()
        new_state.player_turn = self.player_turn
        return new_state

def generate_standard_initial_state():
    state = BackgammonState()
    # Player 1 (White)
    state.board[1] = 2
    state.board[6] = 5
    state.board[8] = 3
    state.board[12] = 5
    # Player 2 (Black)
    state.board[19] = -5
    state.board[21] = -3
    state.board[23] = -5
    state.board[24] = -2
    return state

def generate_moves(state, dice_roll):
    moves = []
    if state.bar[state.player_turn - 1] > 0:  # Check if any pieces are on the bar
        for die in dice_roll:
            target = state.player_turn * die
            if is_valid_move(state, target):
                moves.append([(25, target)])  
    else:
        # Generate moves for pieces on the board
        for point in range(1, 25):
            if state.board[point] * state.player_turn > 0:  # Player's piece exists here
                for die in dice_roll:
                    target = point + state.player_turn * die
                    if is_valid_move(state, target):
                        moves.append([(point, target)])
    return moves

def is_valid_move(state, target):
    if 1 <= target <= 24:
        return state.board[target] * state.player_turn >= -1  #  only if not blocked
    elif target == 26:  
        return True
    return False

def apply_move(state, move):
    for start, end in move:
        if start == 25: 
            state.bar[state.player_turn - 1] -= 1
        else:
            state.board[start] -= state.player_turn
        if 1 <= end <= 24:
            state.board[end] += state.player_turn
        elif end == 26:  # Bearing off
            state.off[state.player_turn - 1] += 1


def roll_dice():
    return sorted([random.randint(1, 6), random.randint(1, 6)])

def is_game_over(state):
    return state.off[0] == 15 or state.off[1] == 15

def evaluate_result(state, player_turn):
    if state.off[player_turn - 1] == 15:
        return 1  # Win
    elif state.off[-player_turn - 1] == 15:
        return -1  # Loss
    return 0  # Draw frequent cause of the first init of the board)
