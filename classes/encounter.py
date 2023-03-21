import pygame, random, sys, time
from button import *
from assets.fonts.fonts import *
from classes import battle
from classes import character
from classes import essences
from classes.monster import Monster
from classes.human import Human
from classes import player_
from classes import main_menu
from enemies.humans import *
from enemies.monsters import *
from enemies.enemy_type import *
from settings import *


def encounter():
    global enemy, LAST_TIME_MS, counter
    enemy_choice = random.choice(enemy_type)
    if enemy_choice == 'monster':
        enemy_type_choice = random.choice(list(monster_type))
        enemy_dict = monster_type[enemy_type_choice]
        enemy = Monster(enemy_dict['name'],
                        enemy_dict['life'],
                        enemy_dict['life'],
                        enemy_dict['attack'],
                        enemy_dict['defense'],
                        enemy_dict['level'],
                        enemy_dict['xp'],
                        enemy_dict['crit_chance'],
                        enemy_dict['delve_drop'],
                        enemy_dict['image'],
                        essence=False
                        )
    elif enemy_choice == 'human':
        enemy_type_choice = random.choice(list(human_type))
        enemy_dict = human_type[enemy_type_choice]
        enemy = Human(enemy_dict['name'],
                      enemy_dict['life'],
                      enemy_dict['life'],
                      enemy_dict['attack'],
                      enemy_dict['defense'],
                      enemy_dict['level'],
                      enemy_dict['xp'],
                      enemy_dict['crit_chance'],
                      enemy_dict['image'],
                      essence=False)
    # level setter
    if enemy.level > player_.player.level + 2:
        encounter()
    elif enemy.level < player_.player.level - 1:
        encounter()
    else:
        if player_.player.level == 5 and character.wiegraf1.status is True:
            enemy = character.wiegraf1
            battle.boss_battle(character.wiegraf1)
        elif player_.player.level == 10 and character.dycedarg1.status is True:
            enemy = character.dycedarg1
            battle.boss_battle(character.dycedarg1)
        elif player_.player.level == 15 and character.wiegraf2.status is True:
            enemy = character.wiegraf2
            battle.boss_battle(character.wiegraf2)
        elif player_.player.level == 20 and character.dycedarg2.status is True:
            enemy = character.dycedarg2
            battle.boss_battle(character.dycedarg2)
        else:
            pass
    enemy = essences.is_essence(enemy)
    battle.battle_elements_resetter()
    player_.display_level_xp()
    # level_text = get_regular_font(25).render(f"LEVEL: {player.player.level}", True, WHITE)
    # level_rect = level_text.get_rect(midright=(1260, 630))
    # next_level = str(player.player.level + 1)
    # xp_text = get_regular_font(25).render(f"XP: {player.player.xp}/{levels.get(next_level)}", True, WHITE)
    # xp_rect = xp_text.get_rect(midright=(1260, 660))
    # SCREEN.blit(level_text, level_rect)
    # SCREEN.blit(xp_text, xp_rect)
    text1 = get_bold_font(30).render(f"You've encountered a level {enemy.level} {enemy.name}!", True, WHITE)
    text1_rect = text1.get_rect(center=(440, 100))
    SCREEN.blit(text1, text1_rect)
    counter = 0
    while True:
        ENCOUNTER_MOUSE_POSITION = pygame.mouse.get_pos()
        # BUTTONS = main_menu.main_menu_structure(ENCOUNTER_MOUSE_POSITION)
        # ATTACK = Button(image=pygame.image.load("assets/images/Next Rect.png"), pos=(600, 200),
        #                 text_input="ATTACK", font=get_bold_font(30), base_color="White", hovering_color=BLUE)
        # RUN = Button(image=pygame.image.load("assets/images/Next Rect.png"), pos=(300, 200),
        #              text_input="RUN", font=get_bold_font(30), base_color="White", hovering_color=BLUE)
        # BUTTONS.extend([ATTACK, RUN])

        diff_time_ms = int(round(time.time() * 4000)) - LAST_TIME_MS
        if diff_time_ms >= 4000:
            counter = counter + 1
            LAST_TIME_MS = int(round(time.time() * 4000))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            # if event.type == pygame.MOUSEBUTTONDOWN:
            #     main_menu.main_menu_structure_events(ENCOUNTER_MOUSE_POSITION, BUTTONS)
            #     if ATTACK.checkForInput(ENCOUNTER_MOUSE_POSITION):
            #         counter = 0
            #         battle.battle_elements_resetter()
            #         battle.battle()
            #     if RUN.checkForInput(ENCOUNTER_MOUSE_POSITION):
            #         counter = 0
            #         encounter()

        # if counter >= 2:
        # for button in BUTTONS:
        #     button.changeColor(ENCOUNTER_MOUSE_POSITION)
        #     button.update(SCREEN)
        if counter > 2:
            battle.battle()

        pygame.display.update()