import math
import random
from backgammon_state import BackgammonState, apply_move, generate_moves, roll_dice, is_game_over, evaluate_result, generate_standard_initial_state

class Node:
    def __init__(self, state, parent=None, move=None):
        self.state = state
        self.parent = parent
        self.move = move
        self.children = []
        self.visits = 0
        self.value = 0

    def is_fully_expanded(self):
        return len(self.children) == len(generate_moves(self.state, roll_dice()))

    def select_child(self):
        c = 1.4  # Exploration cst
        return max(self.children, key=lambda child: child.value / child.visits + c * (2 * math.log(self.visits) / child.visits) ** 0.5)

    def add_child(self, move):
        new_state = self.state.copy()
        apply_move(new_state, move)
        child_node = Node(new_state, parent=self, move=move)
        self.children.append(child_node)
        return child_node

    def update(self, result):
        self.visits += 1
        self.value += result

def mcts_search(initial_state, dice_roll, num_iterations=1000):
    root = Node(initial_state)
    for _ in range(num_iterations):
        node = root
        state = initial_state.copy()
        # Selection
        while node.is_fully_expanded() and not is_game_over(state):
            node = node.select_child()
            apply_move(state, node.move)
        # Expansion
        if not is_game_over(state):
            moves = generate_moves(state, roll_dice())
            if moves:
                move = random.choice(moves)
                node = node.add_child(move)
                apply_move(state, move)
        # Simulation
        result = simulate_game(state, initial_state.player_turn)
        # Backpropagation
        while node:
            node.update(result)
            node = node.parent

    best_child = max(root.children, key=lambda child: child.visits)
    return best_child.move

def simulate_game(state, player_turn):
    current_state = state.copy()
    while not is_game_over(current_state):
        dice_roll = roll_dice()
        moves = generate_moves(current_state, dice_roll)
        if moves:
            move = random.choice(moves) 
            apply_move(current_state, move)
        else:
            break  # No valid moves, skip turn
    return evaluate_result(current_state, player_turn)