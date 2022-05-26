# Assignment 3 - Implement Hill Climbing Algorithm For 8-Puzzle
# Name - Hasnain Merchant Div - B Roll No - 30
# Goal Configuration Of Board
from copy import deepcopy
goal = [
    [1, 2, 3],
    [8, 0, 4],
    [7, 6, 5]]
# Heuristic Value Of Tiles In Place
def calculate_heuristic(cal_config):
    h = 0
    for i in range(0, 3):
        for j in range(0, 3):
            if cal_config[i][j] == goal[i][j]:
                h += 1
    return h
def isSafe(x, y):
    return x >= 0 and x < 3 and y >= 0 and y < 3
def print_board(print_config):
    for i in range(0, 3):
        for j in range(0, 3):
            print(" " + str(print_config[i][j]) + " ", end= "")
        print()
# Function To Find All Possible Board Configurations From Given Configurations
def find_all_configs(all_config):
    config_boards = []
    config1 = deepcopy(all_config)
    config2 = deepcopy(all_config)
    config3 = deepcopy(all_config)
    config4 = deepcopy(all_config)
    for i in range(0, 3):
        for j in range(0, 3):
            if all_config[i][j] != 0:
                # Check If We Can Move To The Top
                if isSafe(i - 1, j):
                    if all_config[i - 1][j] == 0:
                        # Move Tile
                        config1[i - 1][j] = config1[i][j]
                        config1[i][j] = 0
                        config_boards.append(config1)
                # Check If We Can Move To The Bottom
                if isSafe(i + 1, j):
                    if all_config[i + 1][j] == 0:
                        # Move Tile
                        config2[i + 1][j] = config2[i][j]
                        config2[i][j] = 0
                        config_boards.append(config2)
                # Check If We Can Move To The Right
                if isSafe(i, j + 1):
                    if all_config[i][j + 1] == 0:
                        config3[i][j + 1] = config3[i][j]
                        config3[i][j] = 0
                        config_boards.append(config3)
                # Check If We Can Move To The Left
                if isSafe(i, j - 1):
                    if all_config[i][j - 1] == 0:
                        config4[i][j - 1] = config4[i][j]
                        config4[i][j] = 0
                        config_boards.append(config4)
    return config_boards
# Hill Climbing Algorithm Function
def hill_climbing(config, goal_heuristic):
    objective_values = []
    new_config = config
    boards_configs = []
    while True:
        count = 0
        boards_configs.clear()
        #Calculate Heuristic Value Of New Board Configurations
        heuristic_value = calculate_heuristic(new_config)
        if heuristic_value == goal_heuristic:
            print("Solution Reached !!")
            break
        print("Selected Board Configuration - ")
        print_board(new_config)
        print("Selected Board Heuristic Value - " + str(heuristic_value))
        boards_configs = find_all_configs(new_config)
        print("\n\n\n")
# Calculating Heuristic Values For All Child Configurations
        for i in boards_configs:
            count += 1
            print("\tConfiguration " + str(count))
            print_board(i)
            h = calculate_heuristic(i)
            print("\tHeuristic Value - " + str(h))
            objective_values.append(h)
            print("\n")
# Selecting Maximum Heuristic Value From Child Nodes
        max_value = max(objective_values)
        max_value_index = objective_values.index(max_value)
        objective_values.remove(max_value)
    # If There Are Duplicate Entries For Maximum Heuristic Value, We Have Reached A Plateau
        if max_value in objective_values:
            print("We Have Reached A Plateau....Stopping Algorithm")
            break
    # Else, Selected Board Configuration Is The One With Maximum Heuristic Value
        else:
            new_config = boards_configs[max_value_index]
            print("\n\n\t\t\t\t\tMax Heuristic Value - " + str(max_value) + " ......Selecting Board Configuration - " + str(max_value_index+1))
            objective_values.clear()
# Driver Code
# Configuration 1 Of Board Which Will Lead To Plateau
board_config1 = [
    [2, 8, 3],
    [1, 6, 4],
    [7, 0, 5]]
# Configuration 2 Of Board Which Will Lead To Solution
board_config2 = [
    [0, 2, 3],
    [1, 8, 4],
    [7, 6, 5]]
goal_heuristic = calculate_heuristic(goal)
# Calling Hill Climbing For Configuration 1
hill_climbing(board_config1, goal_heuristic)
# Calling Hill Climbing For Configuration 2
hill_climbing(board_config2, goal_heuristic)
