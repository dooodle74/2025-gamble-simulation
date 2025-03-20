import random
from utils import free_draw_probs, paid_draw_probs, first_draw_probs
from utils import COSTS, REWARDS, MAX_LEVEL, player_actions

def play_turn(draw = 0):
    if draw == 0:
        items, weights = free_draw_probs()
    elif draw == 1:
        items, weights = paid_draw_probs()
    elif draw == 2:
        items, weights = first_draw_probs()
    else:
        raise ValueError("Invalid draw type. 0 = free, 1 = paid, 2 = first/failsafe")

    result = random.choices(items, weights)[0]
    return result

def play_until_level(target = 8, player = 0, max_iterations = 1000):
    actions = player_actions(player)
    failsafe_trigger = 2

    level = 0
    history = []
    failsafe = 0

    total_cost = 0
    total_reward = 0

    iterations = 0
    while level < target and iterations < max_iterations:
        iterations += 1        
        if level == 0:
            total_cost += COSTS[0]
            draw_result = play_turn(2)
        else:
            action = actions[level]
            if action == 0:
                draw_result = play_turn(0)
            
            elif action == 1:
                total_cost += COSTS[level]
                if failsafe >= failsafe_trigger:
                    draw_result = play_turn(2)
                else:
                    draw_result = play_turn(1)
                
                if draw_result == 0:
                    failsafe += 1
                else:
                    failsafe = 0

        level += draw_result

        if level <= 0:
            total_reward += REWARDS[0]
            level = 0
        level = min(MAX_LEVEL, level)

        history.append(level)
    
    total_reward += REWARDS[level]
    return history, total_cost, total_reward