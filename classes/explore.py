import pygame, random, sys, time
from button import *
from assets.fonts.fonts import *
from classes import battle
from classes import player_status_
from classes import character
from classes import encounter
from classes.souls import souls
from classes.monster import Monster
from classes.human import Human
from classes import player_
from classes import main_menu
from enemies.humans import *
from enemies.monsters import *
from enemies.enemy_type import *
from settings import *


def explore_menu():
    global enemy_setter
    SCREEN.blit(BG, (0, 0))
    SCREEN.blit(BATTLE_BOX, (60, 40))
    # PLAYER
    SCREEN.blit(player_.player.image, (130, 300))
    player_.display_level_xp()
    souls.draw_souls_icon()
    # ENEMY
    # CONVERTION
    player_ratio = player_.player.life / player_.player.total_life
    player_life_width = 200 * player_ratio

    life_color = player_status_.player_life_color()

    text1 = get_regular_font(20).render(f"{round(player_.player.life)}/{player_.player.total_life}" , True, life_color)
    text1_rect = text1.get_rect(midleft=(100, 540))

    text1_5 = get_bold_font(20).render(f"{player_.player.name}", True, WHITE)
    text1_5_rect = text1_5.get_rect(midleft=(100, 570))

    player_life_bar_rect = pygame.Rect(100, 500, 200, 20)  # left/ top / widht / height

    player_red_life_bar_rect = pygame.Rect(100, 500, player_life_width, 20)  # left/ top / widht / height

    pygame.draw.rect(pygame.display.get_surface(), DARK_GREY, player_life_bar_rect)
    pygame.draw.rect(pygame.display.get_surface(), BLUE, player_red_life_bar_rect)

    #
    # # SCREEN.blit(BLACK_LIFE_BAR, player_life_bar_rect)
    # SCREEN.blit(BLACK_LIFE_BAR, enemy_life_bar_rect)
    # # SCREEN.blit(RED_LIFE_BAR, player_red_life_bar_rect)
    # print(f'PLAYER WIDHT {player_life_width}')
    # SCREEN.blit(RED_LIFE_BAR, enemy_red_life_bar_rect)
    SCREEN.blit(text1, text1_rect)
    SCREEN.blit(text1_5, text1_5_rect)
    player_.check_player_life()


def explore():
    global LAST_TIME_MS, counter
    explore_menu()
    player_.display_level_xp()
    text0 = get_italic_font(25).render(f"The Kingdom of Ivalice is dangerous...", True, WHITE)
    text0_rect = text0.get_rect(center=(450, 110))
    text1 = get_italic_font(25).render(f"When you start exploring, you may face powerful enemies.", True, WHITE)
    text1_rect = text1.get_rect(center=(450, 170))
    text2 = get_italic_font(25).render(f"Make sure you got enough life points", True, WHITE)
    text2_rect = text2.get_rect(center=(450, 210))
    text3 = get_italic_font(25).render(f"and are properly equipped according to the level.", True, WHITE)
    text3_rect = text3.get_rect(center=(450, 250))
    SCREEN.blit(text0, text0_rect)
    SCREEN.blit(text1, text1_rect)
    SCREEN.blit(text2, text2_rect)
    SCREEN.blit(text3, text3_rect)
    while True:
        ENCOUNTER_MOUSE_POSITION = pygame.mouse.get_pos()
        BUTTONS = main_menu.main_menu_structure(ENCOUNTER_MOUSE_POSITION)
        EXPLORE = Button(image=pygame.image.load("assets/images/Next Rect.png"), pos=(SCREEN_WIDTH / 2 - 180, 450),
                        text_input="EXPLORE", font=get_bold_font(30), base_color="White", hovering_color=BLUE)
        # RUN = Button(image=pygame.image.load("assets/images/Next Rect.png"), pos=(300, 200),
        #              text_input="RUN", font=get_bold_font(30), base_color="White", hovering_color=BLUE)
        BUTTONS.extend([EXPLORE])

        diff_time_ms = int(round(time.time() * 4000)) - LAST_TIME_MS
        if diff_time_ms >= 4000:
            counter = counter + 1
            LAST_TIME_MS = int(round(time.time() * 4000))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                main_menu.main_menu_structure_events(ENCOUNTER_MOUSE_POSITION, BUTTONS)
                if EXPLORE.checkForInput(ENCOUNTER_MOUSE_POSITION):
                    counter = 0
                    encounter.encounter()
                # if RUN.checkForInput(ENCOUNTER_MOUSE_POSITION):
                #     counter = 0
                #     encounter.encounter()

        # if counter >= 2:
        for button in BUTTONS:
            button.changeColor(ENCOUNTER_MOUSE_POSITION)
            button.update(SCREEN)

        pygame.display.update()