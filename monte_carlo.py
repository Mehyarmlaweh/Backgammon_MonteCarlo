from backgammon_state import BackgammonState, apply_move, generate_moves, roll_dice, is_game_over, evaluate_result, generate_standard_initial_state
import random

def monte_carlo_search(state, dice_roll, num_simulations=1000):
    moves = generate_moves(state, dice_roll)
    best_move = None
    best_score = float('-inf')
    for move in moves:
        total_score = 0
        for _ in range(num_simulations):
            simulated_state = state.copy()
            apply_move(simulated_state, move)
            result = simulate_game(simulated_state, state.player_turn)
            total_score += result
        average_score = total_score / num_simulations
        if average_score > best_score:
            best_score = average_score
            best_move = move
    return best_move

def simulate_game(state, player_turn):
    current_state = state.copy()
    while not is_game_over(current_state):
        dice_roll = roll_dice()
        moves = generate_moves(current_state, dice_roll)
        if moves:
            move = random.choice(moves) 
            apply_move(current_state, move)
        else:
            break  
    return evaluate_result(current_state, player_turn)