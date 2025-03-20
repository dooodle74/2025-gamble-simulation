from game import play_until_level
import pandas as pd

def simulate_players_game(target, iterations):
    num_players = 2 ** (target - 1)
    simulation_results = []
    
    for player in range(num_players):
        player_results = []
        for _ in range(iterations):
            history, total_cost, total_reward = play_until_level(target, player)
            output = [player, total_cost, total_reward] + history
            player_results.append(output)
        simulation_results.append(player_results)

    return simulation_results

def main():
    targets = [1, 2, 7, 8]
    for target in targets:
        iterations = 1000
        simulation_results = simulate_players_game(target, iterations)

if __name__ == "__main__":
    main()