COSTS = [60, 60, 180, 500, 1000, 2500, 5800, 7200]
REWARDS = [1, 3, 9, 30, 100, 250, 600, 1500, 3000]

def positive_probs():
    items = [1, 2, 3]
    weights = [0.81, 0.18, 0.01]
    return items, weights

def negative_probs():
    items = [-2, -1]
    weights = [0.25, 0.75]
    return items, weights

def neutral_probs():
    items = [0]
    weights = [1.0]
    return items, weights

def free_draw_probs():
    items = negative_probs()[0] + positive_probs()[0]
    weights = [num * 0.8 for num in negative_probs()[1]] + [num * 0.2 for num in positive_probs()[1]]
    return items, weights

def paid_draw_probs():
    items = neutral_probs()[0] + positive_probs()[0]
    weights = [num * 0.8 for num in neutral_probs()[1]] + [num * 0.2 for num in positive_probs()[1]]
    return items, weights

def first_draw_probs():
    return positive_probs()

def player_actions(n):
    return [1] + [(n >> i) & 1 for i in range(7)]