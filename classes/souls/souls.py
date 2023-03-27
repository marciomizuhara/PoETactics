import pygame
from assets.fonts.fonts import *
from classes import player_
from settings import *


def draw_souls_icon():
    souls_text = get_regular_font(25).render(f" {player_.player.souls}", True, WHITE)
    souls_rect = souls_text.get_rect(midleft=(1065, 653))
    SCREEN.blit(SOULS_ICON, (1020, 633))
    SCREEN.blit(souls_text, souls_rect)


def gain_souls(number):
    player_.player.souls += number