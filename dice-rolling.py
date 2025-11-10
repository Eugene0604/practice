import random

# 定义一个函数，用于模拟掷骰子
def roll_dice(sides=6):
    return random.randint(1, sides)

# 定义一个函数，用于模拟掷骰子多次
def roll_dice_multiple(sides=6, times=1):
    return [roll_dice(sides) for _ in range(times)]

# 定义一个函数，用于模拟掷骰子多次
def roll_dice_multiple(sides=6, times=1):
    return [roll_dice(sides) for _ in range(times)] 
