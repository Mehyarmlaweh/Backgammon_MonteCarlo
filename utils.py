import time
import random
from backgammon_state import BackgammonState, generate_standard_initial_state, apply_move, generate_moves, roll_dice, is_game_over, evaluate_result
from monte_carlo import monte_carlo_search
from mcts import mcts_search

def heuristic_simulation(state, player_turn, fixed_move=None, max_turns=100):
    current_state = state.copy()
    if fixed_move:
        apply_move(current_state, fixed_move)
    
    turn_count = 0
    while not is_game_over(current_state) and turn_count < max_turns:
        dice_roll = roll_dice()
        moves = generate_moves(current_state, dice_roll)
        if moves:
            # 1 - moves that bear off pieces
            best_move = None
            for move in moves:
                if any(end == 26 for _, end in move):
                    best_move = move
                    break
            if best_move is None:
                # 2-  moves that block opponent s home board
                for move in moves:
                    if any(19 <= end <= 24 for _, end in move) and current_state.player_turn == 1:
                        best_move = move
                        break
                    elif any(1 <= end <= 6 for _, end in move) and current_state.player_turn == -1:
                        best_move = move
                        break
            if best_move is None:
                best_move = random.choice(moves)
            apply_move(current_state, best_move)
        else:
            break  
        turn_count += 1
    
    return evaluate_result(current_state, player_turn)

def compare_methods(num_games=100, num_simulations_mc=1000, num_iterations_mcts=1000):
    mc_wins = 0
    mcts_wins = 0
    for game in range(num_games):
        print(f"Game {game + 1}/{num_games}")
        initial_state = generate_standard_initial_state()
        dice_roll = roll_dice()
        # Monte Carlo
        start_time = time.time()
        mc_move = monte_carlo_search(initial_state, dice_roll, num_simulations=num_simulations_mc)
        mc_time = time.time() - start_time
        # MCTS
        start_time = time.time()
        mcts_move = mcts_search(initial_state, dice_roll, num_iterations=num_iterations_mcts)
        mcts_time = time.time() - start_time
        # Simulate games to determine winner using enhanced heuristic
        mc_result = heuristic_simulation(initial_state.copy(), initial_state.player_turn, fixed_move=mc_move)
        mcts_result = heuristic_simulation(initial_state.copy(), initial_state.player_turn, fixed_move=mcts_move)
        if mc_result > mcts_result:
            mc_wins += 1
        elif mc_result < mcts_result:
            mcts_wins += 1
        print(f"MC Move: {mc_move}, Time: {mc_time:.2f}s")
        print(f"MCTS Move: {mcts_move}, Time: {mcts_time:.2f}s")
        print(f"MC Result: {mc_result}, MCTS Result: {mcts_result}")
    print("\nComparison Results:")
    print(f"MC Wins: {mc_wins}, MCTS Wins: {mcts_wins}")
    print(f"Total Games: {num_games}")
