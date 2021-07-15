from random import randint

from colors import *


# random color function
def random_color():
    color_choice = randint(0, 5)
    if color_choice == 0:
        return RED
    if color_choice == 1:
        return YELLOW
    if color_choice == 2:
        return GREEN
    if color_choice == 3:
        return INDIGO
    if color_choice == 4:
        return BLUE
    if color_choice == 5:
        return MAGENTA

# checks if an object is in range function
def in_range(position_1, position_2, radius):
    if position_1[0][0] > position_2[0][0] - radius and position_1[0][0] < position_2[0][0] + radius:
        if position_1[1][0] > position_2[1][0] - radius and position_1[1][0] < position_2[1][0] + radius:
            if position_1[2][0] > position_2[2][0] - radius and position_1[2][0] < position_2[2][0] + radius:
                return True
            else:
                return False
        else:
            return False
    else:
        return False