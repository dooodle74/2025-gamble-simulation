from game import play_until_level
import pandas as pd
import numpy as np

players_stats = []
for i in range(0, 8):
    players_stats.append([None] * (2 ** i))

def simulate_target(target, iterations = 1000):
    global players_stats

    num_players = 2 ** (target - 1)
    target_results = []
    
    for player in range(num_players):
        player_results = []
        player_total_costs = []
        player_total_rewards = []
        
        for _ in range(iterations):
            history, total_cost, total_reward = play_until_level(target, player)
            player_total_costs.append(total_cost)
            player_total_rewards.append(total_reward)

            output = [player, total_cost, total_reward] + history
            player_results.append(output)
        
        players_stats[target - 1][player] = (player_total_costs, player_total_rewards)
        target_results.append(player_results)
        print(f"{target}:{player} completed.", flush=True)
    
    print(f"Target {target} completed.")
    return target_results

def main():
    targets = [i for i in range(1, 9)]
    iterations = 1000
    simulation_filename = "simulation_results.xlsx"

    with pd.ExcelWriter(simulation_filename, engine="xlsxwriter") as writer:
        for target in targets:
            target_results = simulate_target(target, iterations)
            
            # Flatten target_results for DataFrame (converting nested lists)
            flattened_results = [entry for player_results in target_results for entry in player_results]
            
            df = pd.DataFrame(flattened_results)
            df.to_excel(writer, sheet_name=f"Target {target}", index=False, header=False)

    print(f"Excel file '{simulation_filename}' saved with multiple sheets!")

    stats_filename = "player_stats.xlsx"
    with pd.ExcelWriter(stats_filename, engine="xlsxwriter") as writer:
        for level, player_group in enumerate(players_stats):
            level_data = []

            player_index = 0
            for player_tuple in player_group:
                if player_tuple is not None:
                    costs, rewards = player_tuple
                    
                    # Compute required statistics
                    cost_mean = np.mean(costs)
                    cost_std = np.std(costs)
                    reward_mean = np.mean(rewards)
                    
                    # Avoid division by zero
                    mean_cost_reward = cost_mean / reward_mean if reward_mean != 0 else np.nan
                    
                    level_data.append([player_index, cost_mean, cost_std, reward_mean, mean_cost_reward])
                player_index += 1

            # Convert to DataFrame and save to Excel
            df = pd.DataFrame(level_data, columns=["Player", "Cost Mean", "Cost STD Dev", "Reward Mean", "Mean Cost/Reward"])
            df.to_excel(writer, sheet_name=f"Level {level+1}", index=False)

    print(f"Excel file '{stats_filename}' saved with statistics for each level.")


if __name__ == "__main__":
    main()