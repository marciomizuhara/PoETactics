import pygame
from enemies.monsters import *
import player_
from fonts import *
from settings import *

levels = {
        '2': 50,
        '3': 150,
        '4': 500,
        '5': 1000,
        '6': 1500,
        '7': 2500,
        '8': 4000,
        '9': 6000,
        '10': 9000,
        '11': 14000,
        '12': 20000,
        '13': 28000,
        '14': 38000,
        '15': 50000,
        '16': 65000,
        '17': 82000,
        '18': 100000,
        '19': 125000,
        '20': 175000,
        '21': '175000 (Max Level)'
}


def display_level_xp():
    level_text = get_regular_font(25).render(f"LEVEL: {player_.player.level}", True, WHITE)
    level_rect = level_text.get_rect(midright=(1260, 600))
    next_level = str(player_.player.level + 1)
    xp_text = get_regular_font(25).render(f"XP: {player_.player.xp}/{levels.get(next_level)}", True, WHITE)
    xp_rect = xp_text.get_rect(midright=(1260, 630))
    life_text = get_regular_font(25).render(f"Life Points: {round(player_.player.life)}/{player_.player.total_life}", True, WHITE)
    life_rect = life_text.get_rect(midright=(1260, 660))
    SCREEN.blit(life_text, life_rect)
    SCREEN.blit(level_text, level_rect)
    SCREEN.blit(xp_text, xp_rect)



















# class Levels:
#
#     def __init__(self, current_level, current_xp):
#         self.current_level = current_level
#         self.current_xp = current_xp





# def set_level():
#     next_level = str(player_level.current_level)
#     player_level.current_xp = player_level.current_xp + 10
#     if player_level.current_xp >= levels.get(next_level):
#         player_level.current_level = player_level.current_level + 1
#     else:
#         print(f"You've gained 10 xp!")
#         print(f"Experience: {player_level.current_xp}/{levels.get(next_level)}")


# print(current_level)
# set_level()
