import math
import random
import time
import threading
import pygame, sys
import numpy as np
from button import *
from objects.card import *
from objects.character import *
from objects.consumable_item import *
from objects.delve import *
from objects.enemy import *
from objects.fossil import *
from objects.human import *
from objects.item import *
from objects.monster import *
from objects.player import *
from objects.player_slot import *
from objects.unique import *
from cs50 import SQL
from itertools import groupby
from operator import itemgetter
from playsound import playsound
from items.cards import *
from enemies.characters import *
from enemies.enemy_type import *
from enemies.monsters import *
from enemies.humans import *
from levels_xp import *
from items.amulets import *
from items.armors import *
from items.boots import *
from items.consumables import *
from items.gear_type import *
from items.gloves import *
from items.helmets import *
from items.legs import *
from items.rings import *
from items.second_hands import *
from items.gear_type import *
from items.uniques import *
from items.weapons import *
from assets.music.music import *
from settings import *
from roulette_wheel import *

pygame.init()
clock = pygame.time.Clock()
clock.tick(FPS)

# PYGAME CONSTANTS
SCREEN = pygame.display.set_mode(WINDOW_SIZE)

GEAR_DROP_RATE = 35
CONSUMABLE_DROP_RATE = 100
TICKET_DROP_RATE = 20
CARD_DROP_RATE = 100
DELVE_DROP_RATE = 100
UNIQUE_DROP_RATE = 7
DROP_HEIGHT = 210

# Setting database
db = SQL("sqlite:///database.db")

# Temp variables
temp_gear_drop = []

temp_unique_drop = []
temp_consumable_drop = []
temp_ticket_drop = []

temp_gear_change = []
temp_gear_change_inventory = []
temp_level_up = False

# Main containers
uniques_list = []
inventory = []


# Setup variables
drop_quantity = 1
counter = 0
card_counter = 0
last_time_ms = int(round(time.time() * 4000))
click_blocking = True


def counter_helper(counter):
    counter_text = get_bold_font(40).render(f'{counter}', True, WHITE)
    counter_text_rect = counter_text.get_rect(center=(SCREEN_WIDTH / 2, 30))
    SCREEN.blit(counter_text, counter_text_rect)


def get_bold_font(size):
    return pygame.font.Font('assets/fonts/AvenirNextLTPro-DemiCond.otf', size)


def get_regular_font(size):
    return pygame.font.Font('assets/fonts/AvenirNextLTPro-LightCond.otf', size)


def get_quote_font(size):
    return pygame.font.Font('assets/fonts/AvenirNextLTPro-LightCondItalic.otf', size)


"""
UNDER DEVELOPMENT
"""
# def word_wrap(surf, text, font, color):
#     font.origin = True
#     words = text.split(' ')
#     width, height = 600, 400
#     line_spacing = font.get_sized_height() + 2
#     x, y = 0, line_spacing
#     space = font.get_rect(' ')
#     for word in words:
#         bounds = font.get_rect(word)
#         if x + bounds.width + bounds.x >= width:
#             x, y = 0, y + line_spacing
#         if x + bounds.width + bounds.x >= width:
#             raise ValueError("word too wide for the surface")
#         if y + bounds.height - bounds.y >= height:
#             raise ValueError("text to long for the surface")
#         font.render_to(surf, (x, y), None, color)
#         x += bounds.width + space.width
#     return x, y
"""
UNDER DEVELOPMENT
"""


def main_menu_structure(mouse):
    if player.level != 20 and dycedarg2.status is True:
        START_BATTLE = Button(image=pygame.image.load("assets/images/ONE_LINE_OPTION.png"), pos=(1100, 100),
                              text_input="EXPLORE", font=get_bold_font(30), base_color="White",
                              hovering_color=BLUE)
        INVENTORY = Button(image=pygame.image.load("assets/images/ONE_LINE_OPTION.png"), pos=(1100, 155),
                           text_input="INVENTORY", font=get_bold_font(30), base_color="White", hovering_color=BLUE)
        CONSUMABLE_ITEMS = Button(image=pygame.image.load("assets/images/ONE_LINE_OPTION.png"),
                                  pos=(SCREEN_WIDTH - 180, 210),
                                  text_input="CONSUMABLE ITEMS", font=get_bold_font(30), base_color="White",
                                  hovering_color=BLUE)
        PLAYER_STATUS = Button(image=pygame.image.load("assets/images/ONE_LINE_OPTION.png"), pos=(1100, 265),
                               text_input="PLAYER STATUS", font=get_bold_font(30), base_color="White",
                               hovering_color=BLUE)
        EXTRAS = Button(image=pygame.image.load("assets/images/ONE_LINE_OPTION.png"), pos=(1100, 320),
                        text_input="EXTRAS", font=get_bold_font(30), base_color="White",
                        hovering_color=BLUE)
        HELP = Button(image=pygame.image.load("assets/images/ONE_LINE_OPTION.png"), pos=(1100, 375),
                      text_input="HELP", font=get_bold_font(30), base_color="White", hovering_color=BLUE)
        QUIT_BUTTON = Button(image=pygame.image.load("assets/images/ONE_LINE_OPTION.png"), pos=(1100, 430),
                             text_input="QUIT", font=get_bold_font(30), base_color="White", hovering_color=BLUE)
        BUTTONS = [START_BATTLE, INVENTORY, CONSUMABLE_ITEMS, PLAYER_STATUS, EXTRAS, HELP, QUIT_BUTTON]
        return BUTTONS
    else:
        START_BATTLE = Button(image=pygame.image.load("assets/images/ONE_LINE_OPTION.png"), pos=(1100, 100),
                              text_input="EXPLORE", font=get_bold_font(30), base_color="White",
                              hovering_color=BLUE)
        INVENTORY = Button(image=pygame.image.load("assets/images/ONE_LINE_OPTION.png"), pos=(1100, 155),
                           text_input="INVENTORY", font=get_bold_font(30), base_color="White", hovering_color=BLUE)
        CONSUMABLE_ITEMS = Button(image=pygame.image.load("assets/images/ONE_LINE_OPTION.png"), pos=(1100, 210),
                                  text_input="CONSUMABLE ITEMS", font=get_bold_font(30), base_color="White",
                                  hovering_color=BLUE)
        PLAYER_STATUS = Button(image=pygame.image.load("assets/images/ONE_LINE_OPTION.png"), pos=(1100, 265),
                               text_input="PLAYER STATUS", font=get_bold_font(30), base_color="White",
                               hovering_color=BLUE)
        DELVE = Button(image=pygame.image.load("assets/images/ONE_LINE_OPTION.png"), pos=(1100, 320),
                       text_input="DELVE", font=get_bold_font(30), base_color="White",
                       hovering_color=BLUE)
        ENDGAME_BOSSES = Button(image=pygame.image.load("assets/images/ONE_LINE_OPTION.png"), pos=(1100, 375),
                                text_input="ENDGAME BOSSES", font=get_bold_font(30), base_color="White",
                                hovering_color=BLUE)
        EXTRAS = Button(image=pygame.image.load("assets/images/ONE_LINE_OPTION.png"), pos=(1100, 430),
                        text_input="EXTRAS", font=get_bold_font(30), base_color="White",
                        hovering_color=BLUE)
        HELP = Button(image=pygame.image.load("assets/images/ONE_LINE_OPTION.png"), pos=(1100, 485),
                      text_input="HELP", font=get_bold_font(30), base_color="White", hovering_color=BLUE)
        QUIT_BUTTON = Button(image=pygame.image.load("assets/images/ONE_LINE_OPTION.png"), pos=(1100, 540),
                             text_input="QUIT", font=get_bold_font(30), base_color="White", hovering_color=BLUE)
        BUTTONS_LIST = [START_BATTLE, INVENTORY, CONSUMABLE_ITEMS, PLAYER_STATUS, DELVE, ENDGAME_BOSSES, EXTRAS, HELP,
                        QUIT_BUTTON]
        return BUTTONS_LIST


def main_menu_structure_events(mouse, buttons):
    if player.level == 20:
        if buttons[0].checkForInput(mouse):
            encounter()
        if buttons[1].checkForInput(mouse):
            show_inventory_page_1(1)
        if buttons[2].checkForInput(mouse):
            show_consumable_items()
        if buttons[3].checkForInput(mouse):
            player_status()
        if buttons[4].checkForInput(mouse):
            pygame.mixer.music.fadeout(2)
            pygame.mixer.music.stop()
            delve_music()
            delve_menu()
            delve_menu()
        if buttons[5].checkForInput(mouse):
            pass
        if buttons[6].checkForInput(mouse):
            extras()  # help
        if buttons[7].checkForInput(mouse):
            pygame.quit()
            sys.exit()
    else:
        if buttons[0].checkForInput(mouse):
            encounter()
        if buttons[1].checkForInput(mouse):
            show_inventory_page_1(1)
        if buttons[2].checkForInput(mouse):
            show_consumable_items()
        if buttons[3].checkForInput(mouse):
            player_status()
        if buttons[4].checkForInput(mouse):
            extras()
        if buttons[5].checkForInput(mouse):
            pygame.quit()
            sys.exit()


def show_item(item_index, item):
    SCREEN.blit(BG, (0, 0))
    SCREEN.blit(BATTLE_BOX, (60, 40))
    sorted_inventory = sorted(inventory, key=lambda x: (x.level, x.type), reverse=True)

    color = ORANGE if item.rarity == 'unique' else WHITE
    text1 = get_bold_font(40).render(f"{item.name}", True, color)
    level_text = get_regular_font(30).render(f"Level {item.level}", True, WHITE)
    type_text = get_bold_font(30).render(f"Type: {item.type}", True, WHITE)
    life_text = get_bold_font(30).render(f"Life: {item.life}", True, WHITE)
    attack_text = get_bold_font(30).render(f"Attack: {item.attack}", True, WHITE)
    defense_text = get_bold_font(30).render(f"Defense: {item.defense}", True, WHITE)
    crit_chance_text = get_bold_font(30).render(f"Critical Chance: {item.crit_chance} %", True, WHITE)
    crit_damage_text = get_bold_font(30).render(f"Critical Damage: {item.crit_damage} %", True, WHITE)
    magic_find_text = get_bold_font(30).render(f"Magic Find: {round(item.magic_find * 100, 2)} %", True, WHITE)
    WIDTH = 806 / 2
    text1_rect = text1.get_rect(center=(WIDTH, 100))
    level_text_rect = level_text.get_rect(center=(WIDTH, 140))
    type_text_rect = type_text.get_rect(midleft=(100, 200))
    life_text_rect = life_text.get_rect(midleft=(100, 240))
    attack_text_rect = attack_text.get_rect(midleft=(100, 280))
    defense_text_rect = defense_text.get_rect(midleft=(100, 320))
    crit_chance_text_rect = crit_chance_text.get_rect(midleft=(100, 360))
    crit_damage_text_rect = crit_damage_text.get_rect(midleft=(100, 400))
    magic_find_text_rect = magic_find_text.get_rect(midleft=(100, 440))
    SCREEN.blit(text1, text1_rect)
    SCREEN.blit(type_text, type_text_rect)
    SCREEN.blit(level_text, level_text_rect)
    SCREEN.blit(life_text, life_text_rect)
    SCREEN.blit(attack_text, attack_text_rect)
    SCREEN.blit(defense_text, defense_text_rect)
    SCREEN.blit(crit_chance_text, crit_chance_text_rect)
    SCREEN.blit(crit_damage_text, crit_damage_text_rect)
    SCREEN.blit(magic_find_text, magic_find_text_rect)

    while True:

        ITEM_DISP_MOUSE_POSITION = pygame.mouse.get_pos()
        BUTTONS = main_menu_structure(ITEM_DISP_MOUSE_POSITION)
        DELETE_ITEM = Button(image=pygame.image.load("assets/images/Smallest Rect.png"), pos=(380, 600),
                             text_input="DELETE", font=get_bold_font(30), base_color="White", hovering_color=BLUE)
        EQUIP_ITEM = Button(image=pygame.image.load("assets/images/Smallest Rect.png"), pos=(540, 600),
                            text_input="EQUIP", font=get_bold_font(30), base_color="White", hovering_color=BLUE)
        BACK = Button(image=pygame.image.load("assets/images/Smallest Rect.png"), pos=(160, 600),
                      text_input="BACK", font=get_bold_font(30), base_color="White", hovering_color=BLUE)
        NEXT = Button(image=pygame.image.load("assets/images/Smallest Rect.png"), pos=(770, 600),
                      text_input="NEXT", font=get_bold_font(30), base_color="White", hovering_color=BLUE)
        BUTTONS.extend([DELETE_ITEM, EQUIP_ITEM, BACK, NEXT])

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                main_menu_structure_events(ITEM_DISP_MOUSE_POSITION, BUTTONS)
                if NEXT.checkForInput(ITEM_DISP_MOUSE_POSITION):
                    item_index = item_index + 1
                    show_item(item_index, sorted_inventory[item_index])
                if BACK.checkForInput(ITEM_DISP_MOUSE_POSITION):
                    item_index = item_index - 1
                    if item_index < 0:
                        item_index = 0
                    show_item(item_index, sorted_inventory[item_index])
                if DELETE_ITEM.checkForInput(ITEM_DISP_MOUSE_POSITION):
                    delete_item_confirmation(item_index, item)

                if EQUIP_ITEM.checkForInput(ITEM_DISP_MOUSE_POSITION):
                    print('aqui 1')
                    item_type_confirmation(item_index, item)

        for button in BUTTONS:
            button.changeColor(ITEM_DISP_MOUSE_POSITION)
            button.update(SCREEN)

        pygame.display.update()


def delete_item_confirmation(item_index, item):
    global counter
    SCREEN.blit(BG, (0, 0))
    SCREEN.blit(BATTLE_BOX, (60, 40))
    display_level_xp()

    text1 = get_bold_font(40).render(f"{item.name}", True, WHITE)
    level_text = get_regular_font(30).render(f"Level {item.level}", True, WHITE)
    type_text = get_bold_font(30).render(f"Type: {item.type}", True, WHITE)
    life_text = get_bold_font(30).render(f"Life: {item.life}", True, WHITE)
    attack_text = get_bold_font(30).render(f"Attack: {item.attack}", True, WHITE)
    defense_text = get_bold_font(30).render(f"Defense: {item.defense}", True, WHITE)
    crit_chance_text = get_bold_font(30).render(f"Critical Chance: {item.crit_chance} %", True, WHITE)
    crit_damage_text = get_bold_font(30).render(f"Critical Damage: {item.crit_damage} %", True, WHITE)
    magic_find_text = get_bold_font(30).render(f"Magic Find: {round(item.magic_find * 100, 2)} %", True, WHITE)
    text1_rect = text1.get_rect(center=(SCREEN_WIDTH / 2 - 180, 80))
    level_text_rect = level_text.get_rect(center=(SCREEN_WIDTH / 2 - 180, 120))
    type_text_rect = type_text.get_rect(center=(SCREEN_WIDTH / 2 - 180, 170))
    life_text_rect = life_text.get_rect(center=(SCREEN_WIDTH / 2 - 180, 210))
    attack_text_rect = attack_text.get_rect(center=(SCREEN_WIDTH / 2 - 180, 250))
    defense_text_rect = defense_text.get_rect(center=(SCREEN_WIDTH / 2 - 180, 290))
    crit_chance_text_rect = crit_chance_text.get_rect(center=(SCREEN_WIDTH / 2 - 180, 330))
    crit_damage_text_rect = crit_damage_text.get_rect(center=(SCREEN_WIDTH / 2 - 180, 370))
    magic_find_text_rect = magic_find_text.get_rect(center=(SCREEN_WIDTH / 2 - 180, 410))
    SCREEN.blit(text1, text1_rect)
    SCREEN.blit(type_text, type_text_rect)
    SCREEN.blit(level_text, level_text_rect)
    SCREEN.blit(life_text, life_text_rect)
    SCREEN.blit(attack_text, attack_text_rect)
    SCREEN.blit(defense_text, defense_text_rect)
    SCREEN.blit(crit_chance_text, crit_chance_text_rect)
    SCREEN.blit(crit_damage_text, crit_damage_text_rect)
    SCREEN.blit(magic_find_text, magic_find_text_rect)

    confirm_text1 = get_bold_font(35).render(
        f"Confirm you want to delete {item.__dict__['name']} level {item.__dict__['level']}?", True, WHITE)
    confirm_text1_rect = confirm_text1.get_rect(center=(SCREEN_WIDTH / 2 - 180, 480))

    SCREEN.blit(confirm_text1, confirm_text1_rect)

    while True:

        DELETE_ITEM_CONFIRMATION_MOUSE_POSITION = pygame.mouse.get_pos()
        BUTTONS = main_menu_structure(DELETE_ITEM_CONFIRMATION_MOUSE_POSITION)
        NO_BUTTON = Button(image=pygame.image.load("assets/images/Smallest Rect.png"), pos=(380, 600),
                           text_input="NO", font=get_bold_font(30), base_color="White", hovering_color=BLUE)
        YES_BUTTON = Button(image=pygame.image.load("assets/images/Smallest Rect.png"), pos=(540, 600),
                            text_input="YES", font=get_bold_font(30), base_color="White", hovering_color=BLUE)
        BUTTONS.extend([NO_BUTTON, YES_BUTTON])

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                main_menu_structure_events(DELETE_ITEM_CONFIRMATION_MOUSE_POSITION, BUTTONS)
                if YES_BUTTON.checkForInput(DELETE_ITEM_CONFIRMATION_MOUSE_POSITION):
                    counter = 0
                    delete_item(item_index, item)
                if NO_BUTTON.checkForInput(DELETE_ITEM_CONFIRMATION_MOUSE_POSITION):
                    show_item(item_index, item)

        for button in BUTTONS:
            button.changeColor(DELETE_ITEM_CONFIRMATION_MOUSE_POSITION)
            button.update(SCREEN)

        pygame.display.update()


def delete_item(item_index, item):
    global counter, last_time_ms
    SCREEN.blit(BG, (0, 0))
    SCREEN.blit(BATTLE_BOX, (60, 40))
    display_level_xp()
    delete_setter = False
    row = db.execute("SELECT * FROM inventory WHERE username = :username AND name = :name AND level = :level",
                     username=player.name,
                     name=item.__dict__['name'],
                     level=item.__dict__['level'])
    id = (row[0]['id'])
    db.execute("DELETE FROM inventory WHERE id = :id",
               id=id)
    inventory.clear()
    save_state()

    load_state()

    temp_level_up = False
    while True:
        confirm_text1 = get_bold_font(40).render(
            f"{item.__dict__['name']} level {item.__dict__['level']} deleted!", True, RED)
        confirm_text1_rect = confirm_text1.get_rect(center=(SCREEN_WIDTH / 2 - 180, 280))

        DELETE_ITEM_MOUSE_POSITION = pygame.mouse.get_pos()
        BUTTONS = main_menu_structure(DELETE_ITEM_MOUSE_POSITION)
        CONTINUE = Button(image=pygame.image.load("assets/images/Smallest Rect.png"), pos=(SCREEN_WIDTH / 2 - 180, 550),
                          text_input="CONTINUE", font=get_bold_font(30), base_color="White", hovering_color=BLUE)
        BUTTONS.append(CONTINUE)

        diff_time_ms = int(round(time.time() * 4000)) - last_time_ms
        if diff_time_ms >= 4000:
            counter = counter + 1
            last_time_ms = int(round(time.time() * 4000))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                main_menu_structure_events(DELETE_ITEM_MOUSE_POSITION, BUTTONS)
                if CONTINUE.checkForInput(DELETE_ITEM_MOUSE_POSITION):
                    counter = 0
                    show_inventory_page_1(1)

        if counter >= 0:
            if delete_setter is False:
                SCREEN.blit(confirm_text1, confirm_text1_rect)
                delete_setter = True
                counter = 0
        if counter > 1:
            for button in BUTTONS:
                button.changeColor(DELETE_ITEM_MOUSE_POSITION)
                button.update(SCREEN)

        pygame.display.update()


def show_inventory_page_1(consumable_type):
    item_index = 1
    SCREEN.blit(BG, (0, 0))
    SCREEN.blit(BATTLE_BOX, (60, 40))

    HEIGHT = 100
    sorted_inventory = sorted(inventory, key=lambda x: (x.level, x.type), reverse=True)
    iteration_rect = []
    column_a = 0
    for i in range(0, len(sorted_inventory)):
        color = ORANGE if sorted_inventory[i].__dict__['rarity'] == 'unique' else WHITE
        text1 = get_bold_font(22).render(
            f"{item_index} — {sorted_inventory[i].__dict__['name']} (level {sorted_inventory[i].__dict__['level']})",
            True, color)
        text1_rect = text1.get_rect(midleft=(100, HEIGHT))
        HEIGHT = HEIGHT + 23
        SCREEN.blit(text1, text1_rect)
        item_index += 1
        iteration_rect.append(text1_rect)
        column_a += 1
        if column_a == 20:
            break
    HEIGHT2 = 100
    column_b = 0
    for i in range(20, len(sorted_inventory)):
        color = ORANGE if sorted_inventory[i].__dict__['rarity'] == 'unique' else WHITE
        text1 = get_bold_font(22).render(
            f"{item_index} — {sorted_inventory[i].__dict__['name']} (level {sorted_inventory[i].__dict__['level']})",
            True, color)
        text1_rect = text1.get_rect(midleft=(550, HEIGHT2))
        HEIGHT2 = HEIGHT2 + 23
        SCREEN.blit(text1, text1_rect)
        item_index += 1
        iteration_rect.append(text1_rect)
        column_b += 1
        if column_b == 20:
            break

    while True:

        INVENTORY_MOUSE_POSITION = pygame.mouse.get_pos()
        BUTTONS = main_menu_structure(INVENTORY_MOUSE_POSITION)

        NEXT = Button(image=pygame.image.load("assets/images/Smallest Rect.png"), pos=(770, 600),
                      text_input="NEXT", font=get_bold_font(30), base_color="White", hovering_color=BLUE)
        BUTTONS.append(NEXT)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                main_menu_structure_events(INVENTORY_MOUSE_POSITION, BUTTONS)
                if NEXT.checkForInput(INVENTORY_MOUSE_POSITION):
                    if consumable_type == 1:
                        show_inventory_page_2(1)
                    else:
                        print('page 2')
                        show_inventory_page_2(consumable_type)
                for i in range(len(iteration_rect)):
                    if iteration_rect[i].collidepoint(INVENTORY_MOUSE_POSITION):
                        if consumable_type == 1:
                            show_item(i, sorted_inventory[i])
                        else:
                            use_fossil(consumable_type, i, sorted_inventory[i])

        for button in BUTTONS:
            button.changeColor(INVENTORY_MOUSE_POSITION)
            button.update(SCREEN)

        pygame.display.update()


def show_inventory_page_2(consumable_type):
    item_index = 41
    SCREEN.blit(BG, (0, 0))
    SCREEN.blit(BATTLE_BOX, (60, 40))
    display_level_xp()
    HEIGHT = 100
    sorted_inventory = sorted(inventory, key=lambda x: (x.level, x.type), reverse=True)
    iteration_rect = []
    column_a = 0
    for i in range(40, len(sorted_inventory)):
        color = ORANGE if sorted_inventory[i].__dict__['rarity'] == 'unique' else WHITE
        text1 = get_bold_font(22).render(
            f"{item_index} — {sorted_inventory[i].__dict__['name']} (level {sorted_inventory[i].__dict__['level']})",
            True, color)
        text1_rect = text1.get_rect(midleft=(100, HEIGHT))
        HEIGHT = HEIGHT + 23
        SCREEN.blit(text1, text1_rect)
        item_index += 1
        iteration_rect.append(text1_rect)
        column_a += 1
        if column_a == 20:
            break
    HEIGHT2 = 100
    column_b = 0
    for i in range(60, len(sorted_inventory)):
        color = ORANGE if sorted_inventory[i].__dict__['rarity'] == 'unique' else WHITE
        text1 = get_bold_font(22).render(
            f"{item_index} — {sorted_inventory[i].__dict__['name']} (level {sorted_inventory[i].__dict__['level']})",
            True, color)
        text1_rect = text1.get_rect(midleft=(550, HEIGHT2))
        HEIGHT2 = HEIGHT2 + 23
        SCREEN.blit(text1, text1_rect)
        item_index += 1
        iteration_rect.append(text1_rect)
        column_b += 1
        if column_b == 20:
            break

    while True:

        INVENTORY_MOUSE_POSITION = pygame.mouse.get_pos()
        BUTTONS = main_menu_structure(INVENTORY_MOUSE_POSITION)

        BACK = Button(image=pygame.image.load("assets/images/Smallest Rect.png"), pos=(160, 600),
                      text_input="BACK", font=get_bold_font(30), base_color="White", hovering_color=BLUE)
        NEXT = Button(image=pygame.image.load("assets/images/Smallest Rect.png"), pos=(770, 600),
                      text_input="NEXT", font=get_bold_font(30), base_color="White", hovering_color=BLUE)

        BUTTONS.extend([BACK, NEXT])

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                main_menu_structure_events(INVENTORY_MOUSE_POSITION, BUTTONS)
                if NEXT.checkForInput(INVENTORY_MOUSE_POSITION):
                    if consumable_type == 1:
                        show_inventory_page_3(1)
                    else:
                        print('page 3')
                        show_inventory_page_3(consumable_type)
                if BACK.checkForInput(INVENTORY_MOUSE_POSITION):
                    if consumable_type == 1:
                        show_inventory_page_1(1)
                    else:
                        show_inventory_page_1(consumable_type)
                for i in range(len(iteration_rect)):
                    if iteration_rect[i].collidepoint(INVENTORY_MOUSE_POSITION):
                        i = i + 40
                        if consumable_type == 1:
                            show_item(i, sorted_inventory[i])
                        else:
                            use_fossil(consumable_type, i, sorted_inventory[i])

        for button in BUTTONS:
            button.changeColor(INVENTORY_MOUSE_POSITION)
            button.update(SCREEN)

        pygame.display.update()


def show_inventory_page_3(consumable_type):
    item_index = 81
    SCREEN.blit(BG, (0, 0))
    SCREEN.blit(BATTLE_BOX, (60, 40))
    display_level_xp()
    HEIGHT = 100
    sorted_inventory = sorted(inventory, key=lambda x: (x.level, x.type), reverse=True)
    iteration_rect = []
    column_a = 0
    for i in range(80, len(sorted_inventory)):
        color = ORANGE if sorted_inventory[i].__dict__['rarity'] == 'unique' else WHITE
        text1 = get_bold_font(22).render(
            f"{item_index} — {sorted_inventory[i].__dict__['name']} (level {sorted_inventory[i].__dict__['level']})",
            True, color)
        text1_rect = text1.get_rect(midleft=(100, HEIGHT))
        HEIGHT = HEIGHT + 23
        SCREEN.blit(text1, text1_rect)
        item_index += 1
        iteration_rect.append(text1_rect)
        column_a += 1
        if column_a == 20:
            break
    HEIGHT2 = 100
    column_b = 0
    for i in range(100, len(sorted_inventory)):
        color = ORANGE if sorted_inventory[i].__dict__['rarity'] == 'unique' else WHITE
        text1 = get_bold_font(22).render(
            f"{item_index} — {sorted_inventory[i].__dict__['name']} (level {sorted_inventory[i].__dict__['level']})",
            True, color)
        text1_rect = text1.get_rect(midleft=(550, HEIGHT2))
        HEIGHT2 = HEIGHT2 + 23
        SCREEN.blit(text1, text1_rect)
        item_index += 1
        iteration_rect.append(text1_rect)
        column_b += 1
        if column_b == 20:
            break

    while True:

        INVENTORY_MOUSE_POSITION = pygame.mouse.get_pos()
        BUTTONS = main_menu_structure(INVENTORY_MOUSE_POSITION)

        BACK = Button(image=pygame.image.load("assets/images/Smallest Rect.png"), pos=(160, 600),
                      text_input="BACK", font=get_bold_font(30), base_color="White", hovering_color=BLUE)
        NEXT = Button(image=pygame.image.load("assets/images/Smallest Rect.png"), pos=(770, 600),
                      text_input="NEXT", font=get_bold_font(30), base_color="White", hovering_color=BLUE)
        BUTTONS.extend([BACK, NEXT])

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                main_menu_structure_events(INVENTORY_MOUSE_POSITION, BUTTONS)
                if NEXT.checkForInput(INVENTORY_MOUSE_POSITION):
                    if consumable_type == 1:
                        show_inventory_page_4(1)
                    else:
                        show_inventory_page_4(consumable_type)
                if BACK.checkForInput(INVENTORY_MOUSE_POSITION):
                    if consumable_type == 1:
                        show_inventory_page_2(1)
                    else:
                        show_inventory_page_2(consumable_type)
                for i in range(len(iteration_rect)):
                    if iteration_rect[i].collidepoint(INVENTORY_MOUSE_POSITION):
                        i = i + 80
                        if consumable_type == 1:
                            show_item(i, sorted_inventory[i])
                        else:
                            use_fossil(consumable_type, i, sorted_inventory[i])

        for button in BUTTONS:
            button.changeColor(INVENTORY_MOUSE_POSITION)
            button.update(SCREEN)

        pygame.display.update()


def show_inventory_page_4(consumable_type):
    item_index = 121
    SCREEN.blit(BG, (0, 0))
    SCREEN.blit(BATTLE_BOX, (60, 40))
    display_level_xp()
    HEIGHT = 100
    sorted_inventory = sorted(inventory, key=lambda x: (x.level, x.type), reverse=True)
    iteration_rect = []
    column_a = 0
    for i in range(120, len(sorted_inventory)):
        color = ORANGE if sorted_inventory[i].__dict__['rarity'] == 'unique' else WHITE
        text1 = get_bold_font(22).render(
            f"{item_index} — {sorted_inventory[i].__dict__['name']} (level {sorted_inventory[i].__dict__['level']})",
            True, color)
        text1_rect = text1.get_rect(midleft=(100, HEIGHT))
        HEIGHT = HEIGHT + 23
        SCREEN.blit(text1, text1_rect)
        item_index += 1
        iteration_rect.append(text1_rect)
        column_a += 1
        if column_a == 20:
            break
    HEIGHT2 = 100
    column_b = 0
    for i in range(140, len(sorted_inventory)):
        color = ORANGE if sorted_inventory[i].__dict__['rarity'] == 'unique' else WHITE
        text1 = get_bold_font(22).render(
            f"{item_index} — {sorted_inventory[i].__dict__['name']} (level {sorted_inventory[i].__dict__['level']})",
            True, color)
        text1_rect = text1.get_rect(midleft=(550, HEIGHT2))
        HEIGHT2 = HEIGHT2 + 23
        SCREEN.blit(text1, text1_rect)
        item_index += 1
        iteration_rect.append(text1_rect)
        column_b += 1
        if column_b == 20:
            break

    while True:

        INVENTORY_MOUSE_POSITION = pygame.mouse.get_pos()
        BUTTONS = main_menu_structure(INVENTORY_MOUSE_POSITION)

        BACK = Button(image=pygame.image.load("assets/images/Smallest Rect.png"), pos=(160, 600),
                      text_input="BACK", font=get_bold_font(30), base_color="White", hovering_color=BLUE)

        BUTTONS.extend([BACK])

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                main_menu_structure_events(INVENTORY_MOUSE_POSITION, BUTTONS)
                if BACK.checkForInput(INVENTORY_MOUSE_POSITION):
                    if consumable_type == 1:
                        show_inventory_page_3(1)
                    else:
                        show_inventory_page_3(consumable_type)
                for i in range(len(iteration_rect)):
                    if iteration_rect[i].collidepoint(INVENTORY_MOUSE_POSITION):
                        i = i + 120
                        if consumable_type == 1:
                            show_item(i, sorted_inventory[i])
                        else:
                            use_fossil(consumable_type, i, sorted_inventory[i])

        for button in BUTTONS:
            button.changeColor(INVENTORY_MOUSE_POSITION)
            button.update(SCREEN)

        pygame.display.update()


def show_consumable_items():
    global INPUT_TEXT
    SCREEN.blit(BG, (0, 0))
    SCREEN.blit(CONSUMABLES_GRID, (60, 40))
    SCREEN.blit(player.image, (130, 300))
    display_level_xp()
    # Items images
    if potion.quantity != 0:
        SCREEN.blit(POTION, (310, 120))
    else:
        SCREEN.blit(G_POTION, (310, 120))
    potion_quantity_text = get_bold_font(20).render(f'{potion.quantity}', True, WHITE)
    potion_quantity_text_rect = potion_quantity_text.get_rect(midleft=(290, 115))
    SCREEN.blit(potion_quantity_text, potion_quantity_text_rect)

    if hi_potion.quantity != 0:
        SCREEN.blit(HI_POTION, (420, 120))
    else:
        SCREEN.blit(G_HI_POTION, (420, 120))
    hi_potion_quantity_text = get_bold_font(20).render(f'{hi_potion.quantity}', True, WHITE)
    hi_potion_quantity_text_rect = hi_potion_quantity_text.get_rect(midleft=(400, 115))
    SCREEN.blit(hi_potion_quantity_text, hi_potion_quantity_text_rect)

    if x_potion.quantity != 0:
        SCREEN.blit(X_POTION, (525, 120))
    else:
        SCREEN.blit(G_X_POTION, (525, 120))
    x_potion_quantity_text = get_bold_font(20).render(f'{x_potion.quantity}', True, WHITE)
    x_potion_quantity_text_rect = x_potion_quantity_text.get_rect(midleft=(505, 115))
    SCREEN.blit(x_potion_quantity_text, x_potion_quantity_text_rect)

    if elixir.quantity != 0:
        SCREEN.blit(ELIXIR, (635, 120))
    else:
        SCREEN.blit(G_ELIXIR, (635, 120))
    elixir_quantity_text = get_bold_font(20).render(f'{elixir.quantity}', True, WHITE)
    elixir_quantity_text_rect = elixir_quantity_text.get_rect(midleft=(615, 115))
    SCREEN.blit(elixir_quantity_text, elixir_quantity_text_rect)

    if chaos_orb.quantity != 0:
        SCREEN.blit(CHAOS_ORB, (745, 120))
    else:
        SCREEN.blit(G_CHAOS_ORB, (745, 120))
    chaos_orb_quantity_text = get_bold_font(20).render(f'{chaos_orb.quantity}', True, WHITE)
    chaos_orb_quantity_text_rect = chaos_orb_quantity_text.get_rect(midleft=(725, 115))
    SCREEN.blit(chaos_orb_quantity_text, chaos_orb_quantity_text_rect)

    if divine_orb.quantity != 0:
        SCREEN.blit(DIVINE_ORB, (305, 225))
    else:
        SCREEN.blit(G_DIVINE_ORB, (305, 225))
    divine_orb_quantity_text = get_bold_font(20).render(f'{divine_orb.quantity}', True, WHITE)
    divine_orb_quantity_text_rect = divine_orb_quantity_text.get_rect(midleft=(290, 220))
    SCREEN.blit(divine_orb_quantity_text, divine_orb_quantity_text_rect)

    if exalted_orb.quantity != 0:
        SCREEN.blit(EXALTED_ORB, (410, 225))
    else:
        SCREEN.blit(G_EXALTED_ORB, (410, 225))
    exalted_orb_quantity_text = get_bold_font(20).render(f'{exalted_orb.quantity}', True, WHITE)
    exalted_orb_quantity_text_rect = exalted_orb_quantity_text.get_rect(midleft=(400, 220))
    SCREEN.blit(exalted_orb_quantity_text, exalted_orb_quantity_text_rect)

    if mirror_of_kalandra.quantity != 0:
        SCREEN.blit(MIRROR_OF_KALANDRA, (520, 220))
    else:
        SCREEN.blit(G_MIRROR_OF_KALANDRA, (520, 220))
    mirror_of_kalandra_quantity_text = get_bold_font(20).render(f'{mirror_of_kalandra.quantity}', True, WHITE)
    mirror_of_kalandra_quantity_text_rect = mirror_of_kalandra_quantity_text.get_rect(midleft=(505, 220))
    SCREEN.blit(mirror_of_kalandra_quantity_text, mirror_of_kalandra_quantity_text_rect)

    if roulette_wheel_ticket.quantity != 0:
        SCREEN.blit(ROULETTE_WHEEL2_TICKET, (630, 320))
    else:
        SCREEN.blit(G_ROULETTE_WHEEL2_TICKET, (630, 320))
    roulette_wheel_ticket_text = get_bold_font(20).render(f'{roulette_wheel_ticket.quantity}', True, WHITE)
    roulette_wheel_ticket_text_rect = roulette_wheel_ticket_text.get_rect(midleft=(615, 325))
    SCREEN.blit(roulette_wheel_ticket_text, roulette_wheel_ticket_text_rect)

    if dense_fossil.quantity != 0:
        SCREEN.blit(DENSE_FOSSIL, (630, 220))
    else:
        SCREEN.blit(G_DENSE_FOSSIL, (630, 220))
    dense_fossil_quantity_text = get_bold_font(20).render(f'{dense_fossil.quantity}', True, WHITE)
    dense_fossil_quantity_text_rect = dense_fossil_quantity_text.get_rect(midleft=(615, 220))
    SCREEN.blit(dense_fossil_quantity_text, dense_fossil_quantity_text_rect)

    if serrated_fossil.quantity != 0:
        SCREEN.blit(SERRATED_FOSSIL, (740, 220))
    else:
        SCREEN.blit(G_SERRATED_FOSSIL, (740, 220))
    serrated_fossil_quantity_text = get_bold_font(20).render(f'{serrated_fossil.quantity}', True, WHITE)
    serrated_fossil_quantity_text_rect = serrated_fossil_quantity_text.get_rect(midleft=(725, 220))
    SCREEN.blit(serrated_fossil_quantity_text, serrated_fossil_quantity_text_rect)

    if pristine_fossil.quantity != 0:
        SCREEN.blit(PRISTINE_FOSSIL, (295, 320))
    else:
        SCREEN.blit(G_PRISTINE_FOSSIL, (295, 320))
    pristine_fossil_quantity_text = get_bold_font(20).render(f'{pristine_fossil.quantity}', True, WHITE)
    pristine_fossil_quantity_text_rect = pristine_fossil_quantity_text.get_rect(midleft=(290, 325))
    SCREEN.blit(pristine_fossil_quantity_text, pristine_fossil_quantity_text_rect)

    if deft_fossil.quantity != 0:
        SCREEN.blit(DEFT_FOSSIL, (405, 320))
    else:
        SCREEN.blit(G_DEFT_FOSSIL, (405, 320))
    deft_fossil_quantity_text = get_bold_font(20).render(f'{deft_fossil.quantity}', True, WHITE)
    deft_fossil_quantity_text_rect = deft_fossil_quantity_text.get_rect(midleft=(400, 325))
    SCREEN.blit(deft_fossil_quantity_text, deft_fossil_quantity_text_rect)

    if fractured_fossil.quantity != 0:
        SCREEN.blit(FRACTURED_FOSSIL, (515, 320))
    else:
        SCREEN.blit(G_FRACTURED_FOSSIL, (515, 320))
    fractured_fossil_quantity_text = get_bold_font(20).render(f'{fractured_fossil.quantity}', True, WHITE)
    fractured_fossil_quantity_text_rect = fractured_fossil_quantity_text.get_rect(midleft=(505, 325))
    SCREEN.blit(fractured_fossil_quantity_text, fractured_fossil_quantity_text_rect)

    potion_rect = POTION.get_rect(center=(330, 150))
    hi_potion_rect = HI_POTION.get_rect(center=(440, 150))
    x_potion_rect = X_POTION.get_rect(center=(545, 150))
    elixir_rect = ELIXIR.get_rect(center=(670, 150))
    chaos_orb_rect = CHAOS_ORB.get_rect(center=(780, 150))
    divine_orb_rect = DIVINE_ORB.get_rect(center=(330, 260))
    exalted_orb_rect = EXALTED_ORB.get_rect(center=(440, 260))
    mirror_of_kalandra_rect = MIRROR_OF_KALANDRA.get_rect(center=(540, 260))
    roulette_wheel_ticket_rect = ROULETTE_WHEEL2_TICKET.get_rect(center=(650, 350))
    dense_fossil_rect = DENSE_FOSSIL.get_rect(center=(650, 260))
    serrated_fossil_rect = SERRATED_FOSSIL.get_rect(center=(765, 260))
    pristine_fossil_rect = PRISTINE_FOSSIL.get_rect(center=(320, 350))
    deft_fossil_rect = DEFT_FOSSIL.get_rect(center=(420, 350))
    fractured_fossil_rect = FRACTURED_FOSSIL.get_rect(center=(520, 350))

    INPUT_TEXT = ''

    while True:

        SHOW_CONSUMABLES_MOUSE_POSITION = pygame.mouse.get_pos()
        BUTTONS = main_menu_structure(SHOW_CONSUMABLES_MOUSE_POSITION)

        BOX = Box(image=pygame.image.load("assets/images/CONSUMABLE_ONE_LINE_BOX.png"), pos=(550, 600),
                  text_input=INPUT_TEXT, font=get_bold_font(20), base_color="White", hovering_color=BLUE)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                main_menu_structure_events(SHOW_CONSUMABLES_MOUSE_POSITION, BUTTONS)
                if potion_rect.collidepoint(SHOW_CONSUMABLES_MOUSE_POSITION):
                    if potion.quantity > 0:
                        confirm_use_consumable_item(potion)
                if hi_potion_rect.collidepoint(SHOW_CONSUMABLES_MOUSE_POSITION):
                    if hi_potion.quantity > 0:
                        confirm_use_consumable_item(hi_potion)
                if x_potion_rect.collidepoint(SHOW_CONSUMABLES_MOUSE_POSITION):
                    if x_potion.quantity > 0:
                        confirm_use_consumable_item(x_potion)
                if elixir_rect.collidepoint(SHOW_CONSUMABLES_MOUSE_POSITION):
                    if elixir.quantity > 0:
                        confirm_use_consumable_item(elixir)
                if chaos_orb_rect.collidepoint(SHOW_CONSUMABLES_MOUSE_POSITION):
                    if chaos_orb.quantity > 0:
                        confirm_use_consumable_item(chaos_orb)
                if divine_orb_rect.collidepoint(SHOW_CONSUMABLES_MOUSE_POSITION):
                    if divine_orb.quantity > 0:
                        confirm_use_consumable_item(divine_orb)
                if exalted_orb_rect.collidepoint(SHOW_CONSUMABLES_MOUSE_POSITION):
                    if exalted_orb.quantity > 0:
                        confirm_use_consumable_item(exalted_orb)
                if mirror_of_kalandra_rect.collidepoint(SHOW_CONSUMABLES_MOUSE_POSITION):
                    if mirror_of_kalandra.quantity > 0:
                        confirm_use_consumable_item(mirror_of_kalandra)
                if roulette_wheel_ticket_rect.collidepoint(SHOW_CONSUMABLES_MOUSE_POSITION):
                    if roulette_wheel_ticket.quantity > 0:
                        roulette()
                if dense_fossil_rect.collidepoint(SHOW_CONSUMABLES_MOUSE_POSITION):
                    if dense_fossil.quantity > 0:
                        show_inventory_page_1(dense_fossil)
                if serrated_fossil_rect.collidepoint(SHOW_CONSUMABLES_MOUSE_POSITION):
                    if serrated_fossil.quantity > 0:
                        show_inventory_page_1(serrated_fossil)
                if pristine_fossil_rect.collidepoint(SHOW_CONSUMABLES_MOUSE_POSITION):
                    if pristine_fossil.quantity > 0:
                        show_inventory_page_1(pristine_fossil)
                if deft_fossil_rect.collidepoint(SHOW_CONSUMABLES_MOUSE_POSITION):
                    if deft_fossil.quantity > 0:
                        show_inventory_page_1(deft_fossil)
                if fractured_fossil_rect.collidepoint(SHOW_CONSUMABLES_MOUSE_POSITION):
                    if fractured_fossil.quantity > 0:
                        show_inventory_page_1(fractured_fossil)
            if potion_rect.collidepoint(SHOW_CONSUMABLES_MOUSE_POSITION):
                BOX.update(screen=SCREEN)
                INPUT_TEXT = f"{potion.name}: Restores {potion.value} life points"

            if hi_potion_rect.collidepoint(SHOW_CONSUMABLES_MOUSE_POSITION):
                BOX.update(screen=SCREEN)
                INPUT_TEXT = f"{hi_potion.name}: Restores {hi_potion.value} life points"

            if x_potion_rect.collidepoint(SHOW_CONSUMABLES_MOUSE_POSITION):
                BOX.update(screen=SCREEN)
                INPUT_TEXT = f"{x_potion.name}: Restores {x_potion.value} life points"

            if elixir_rect.collidepoint(SHOW_CONSUMABLES_MOUSE_POSITION):
                BOX.update(screen=SCREEN)
                INPUT_TEXT = f"{elixir.name}: Restores full life points"

            if chaos_orb_rect.collidepoint(SHOW_CONSUMABLES_MOUSE_POSITION):
                BOX.update(screen=SCREEN)
                INPUT_TEXT = f"{chaos_orb.name}: Permanently adds +{chaos_orb.value} to player's attack"

            if divine_orb_rect.collidepoint(SHOW_CONSUMABLES_MOUSE_POSITION):
                BOX.update(screen=SCREEN)
                INPUT_TEXT = f"{divine_orb.name}: Permanently adds +{divine_orb.value} to player's defense"

            if exalted_orb_rect.collidepoint(SHOW_CONSUMABLES_MOUSE_POSITION):
                BOX.update(screen=SCREEN)
                INPUT_TEXT = f"{exalted_orb.name}: Permanently adds +{exalted_orb.value} to player's total life"

            if mirror_of_kalandra_rect.collidepoint(SHOW_CONSUMABLES_MOUSE_POSITION):
                BOX.update(screen=SCREEN)
                INPUT_TEXT = f"{mirror_of_kalandra.name}: +{mirror_of_kalandra.value.split()[0]} to total life, " \
                             f"+{mirror_of_kalandra.value.split()[1]} to attack, +{mirror_of_kalandra.value.split()[2]} to defense"
            if roulette_wheel_ticket_rect.collidepoint(SHOW_CONSUMABLES_MOUSE_POSITION):
                BOX.update(screen=SCREEN)
                INPUT_TEXT = f"{roulette_wheel_ticket.name}: You can try your luck at the Roulette Wheel"
            if dense_fossil_rect.collidepoint(SHOW_CONSUMABLES_MOUSE_POSITION):
                BOX.update(screen=SCREEN)
                INPUT_TEXT = f"{dense_fossil.name}: Unpredicably reforges the defense value of an item"

            if serrated_fossil_rect.collidepoint(SHOW_CONSUMABLES_MOUSE_POSITION):
                BOX.update(screen=SCREEN)
                INPUT_TEXT = f"{serrated_fossil.name}: Unpredicably reforges the attack value of an item"

            if pristine_fossil_rect.collidepoint(SHOW_CONSUMABLES_MOUSE_POSITION):
                BOX.update(screen=SCREEN)
                INPUT_TEXT = f"{pristine_fossil.name}: Unpredicably reforges the life value of an item"

            if deft_fossil_rect.collidepoint(SHOW_CONSUMABLES_MOUSE_POSITION):
                BOX.update(screen=SCREEN)
                INPUT_TEXT = f"{deft_fossil.name}: Unpredicably reforges the critical damage value of an item"

            if fractured_fossil_rect.collidepoint(SHOW_CONSUMABLES_MOUSE_POSITION):
                BOX.update(screen=SCREEN)
                INPUT_TEXT = f"{fractured_fossil.name}: Unpredicably reforges all values of an item"

            for button in BUTTONS:
                button.changeColor(SHOW_CONSUMABLES_MOUSE_POSITION)
                button.update(SCREEN)
        pygame.display.update()


def shaman():
    player.life += player.shaman
    if player.life > player.total_life:
        player.life = player.total_life
    else:
        pass


def player_level_up():
    global temp_level_up
    next_level = str(player.level + 1)

    if player.xp >= 175000:
        player.xp = 175000
    else:
        player.xp += enemy.xp

        if player.xp >= levels.get(next_level):
            # player.level = player.level + 1
            # total_life_level_up = player.total_life * 0.1
            # shaman_level_up = 1.5
            # attack_level_up = player.attack * 0.02
            # defense_level_up = player.defense * 0.02
            # crit_chance_level_up = 0.5
            # crit_damage_level_up = 0.1
            print('chegou aqui morto')
            temp_level_up = True
            draw_player_level_up()
        else:
            battle_finish()


def draw_player_level_up():
    global temp_level_up, counter, last_time_ms
    level_up_sound_setter = False
    if temp_level_up is True:
        battle_elements_resetter()
        player.level += 1
        total_life_level_up = player.total_life * 0.1
        shaman_level_up = 1.5
        attack_level_up = player.attack * 0.02
        defense_level_up = player.defense * 0.02
        crit_chance_level_up = 0.5
        crit_damage_level_up = 0.5
        player.total_life = round(player.total_life + total_life_level_up)
        player.life = player.total_life
        player.shaman += shaman_level_up
        player.attack = round(player.attack + attack_level_up)
        player.defense = round(player.defense + defense_level_up)
        player.crit_chance += crit_chance_level_up
        player.crit_damage += crit_damage_level_up
        SCREEN.fill(0)
        SCREEN.blit(BG, (0, 0))
        SCREEN.blit(BATTLE_BOX, (60, 40))
        display_level_xp()
        # PLAYER
        SCREEN.blit(player.image, (130, 300))
        level_up_text = get_bold_font(40).render(
            f"Congratulations, you've leveled up to level {player.level}!", True, WHITE)
        level_up_text_rect = level_up_text.get_rect(center=(SCREEN_WIDTH / 2 - 180, 100))
        text1 = get_bold_font(30).render(f"You've gained:", True, WHITE)
        text1_rect = text1.get_rect(midleft=(SCREEN_WIDTH / 2 - 250, 200))
        text2 = get_bold_font(30).render(f"{round(total_life_level_up, 1)} to total life points:", True,
                                         CYAN)
        text2_rect = text1.get_rect(midleft=(SCREEN_WIDTH / 2 - 250, 260))
        text3 = get_bold_font(30).render(f"{round(shaman_level_up, 1)} to shaman", True, CYAN)
        text3_rect = text1.get_rect(midleft=(SCREEN_WIDTH / 2 - 250, 300))
        text4 = get_bold_font(30).render(f"{round(attack_level_up)} to attack", True, CYAN)
        text4_rect = text1.get_rect(midleft=(SCREEN_WIDTH / 2 - 250, 340))
        text5 = get_bold_font(30).render(f"{round(defense_level_up)} to defense", True, CYAN)
        text5_rect = text1.get_rect(midleft=(SCREEN_WIDTH / 2 - 250, 380))
        text6 = get_bold_font(30).render(f"{round(crit_chance_level_up, 1)}% to critical chance", True,
                                         CYAN)
        text6_rect = text1.get_rect(midleft=(SCREEN_WIDTH / 2 - 250, 420))
        text7 = get_bold_font(30).render(f"{round(crit_damage_level_up, 1)}% to critical damage", True,
                                         CYAN)
        text7_rect = text1.get_rect(midleft=(SCREEN_WIDTH / 2 - 250, 460))

        SCREEN.blit(level_up_text, level_up_text_rect)
        SCREEN.blit(text1, text1_rect)
        SCREEN.blit(text2, text2_rect)
        SCREEN.blit(text3, text3_rect)
        SCREEN.blit(text4, text4_rect)
        SCREEN.blit(text5, text5_rect)
        SCREEN.blit(text6, text6_rect)
        SCREEN.blit(text7, text7_rect)
        temp_level_up = False
        while True:

            DRAW_PLAYER_LEVEL_UP_MOUSE_POSITION = pygame.mouse.get_pos()

            CONTINUE = Button(image=pygame.image.load("assets/images/Smallest Rect.png"), pos=(SCREEN_WIDTH / 2 - 180, 550),
                              text_input="CONTINUE", font=get_bold_font(30), base_color="White", hovering_color=BLUE)

            diff_time_ms = int(round(time.time() * 4000)) - last_time_ms
            if diff_time_ms >= 4000:
                counter = counter + 1
                last_time_ms = int(round(time.time() * 4000))

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if CONTINUE.checkForInput(DRAW_PLAYER_LEVEL_UP_MOUSE_POSITION):
                        counter = 0
                        battle_finish()

            if counter >= 0:
                if level_up_sound_setter is False:
                    playsound(PLAYER_LEVEL_UP, False)
                    level_up_sound_setter = True
                    counter = 0
            if counter > 2:
                for button in [CONTINUE]:
                    button.changeColor(DRAW_PLAYER_LEVEL_UP_MOUSE_POSITION)
                    button.update(SCREEN)

            pygame.display.update()
    else:
        pass


def game_over():
    global counter, last_time_ms
    SCREEN.fill(BLACK)
    life_checking_setter = False
    welcome_setter = False

    while True:
        SCREEN.fill(BLACK)
        pygame.display.set_caption("PoETactics")
        GAME_OVER_MOUSE_POSITION = pygame.mouse.get_pos()

        text1 = get_bold_font(100).render(f"GAME OVER!", True, RED)
        menu_rect1 = text1.get_rect(center=(SCREEN_WIDTH / 2, 300))

        SCREEN.blit(text1, menu_rect1)

        CONTINUE = Button(image=pygame.image.load("assets/images/Next Rect.png"),
                          pos=(SCREEN_WIDTH / 2, SCREEN_HEIGHT - 200),
                          text_input="CONTINUE", font=get_bold_font(40), base_color="White", hovering_color=PINK)

        diff_time_ms = int(round(time.time() * 4000)) - last_time_ms
        if diff_time_ms >= 4000:
            counter = counter + 1
            last_time_ms = int(round(time.time() * 4000))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if CONTINUE.checkForInput(GAME_OVER_MOUSE_POSITION):
                    inventory.clear()
                    login_menu()

        if counter >= 1:
            SCREEN.blit(text1, menu_rect1)
        if counter >= 2:
            for button in [CONTINUE]:
                button.changeColor(GAME_OVER_MOUSE_POSITION)
                button.update(SCREEN)

        pygame.display.update()


def check_player_life():
    global counter, last_time_ms
    death_setter = False
    if player.life <= 0:
        player.life = 0
        counter = 0
        player_ratio = player.life / player.total_life
        player_life_width = 200 * player_ratio

        text0 = get_bold_font(60).render(f"You have perished...", True, RED)
        text0_rect = text0.get_rect(center=(SCREEN_WIDTH / 2 - 180, 200))
        text1 = get_regular_font(20).render(f"{player.life}/{player.total_life}", True, WHITE)
        text1_rect = text1.get_rect(midleft=(100, 540))

        player_life_bar_rect = pygame.Rect(100, 500, 200, 20)  # left/ top / widht / height
        player_red_life_bar_rect = pygame.Rect(100, 500, player_life_width, 20)  # left/ top / widht / height
        pygame.draw.rect(pygame.display.get_surface(), DARK_GREY, player_life_bar_rect)
        pygame.draw.rect(pygame.display.get_surface(), BLUE, player_red_life_bar_rect)

        SCREEN.blit(text1, text1_rect)
        while True:
            diff_time_ms = int(round(time.time() * 4000)) - last_time_ms
            if diff_time_ms >= 4000:
                counter = counter + 1
                last_time_ms = int(round(time.time() * 4000))
            if counter >= 1:
                pygame.mixer.music.fadeout(2)
                pygame.mixer.music.stop()
                background_music()
            if death_setter is not True:
                SCREEN.blit(text0, text0_rect)
                death_setter = True
            if counter >= 5:
                counter = 0
                game_over()
            pygame.display.update()


def inventory_limit():
    limit = 150
    if len(inventory) >= limit:
        to_remove = sorted(inventory, key=lambda x: (x.level, x.type), reverse=True).pop(-1)
        row = db.execute("SELECT * FROM inventory WHERE username = :username AND name = :name AND level = :level",
                         username=player.name, name=to_remove.name, level=to_remove.level)
        id = (row[0]['id'])
        db.execute("DELETE FROM inventory WHERE id = :id",
                   id=id)


def gear_drop_rate():
    drop_rate_value = random.randint(0, 100)
    if drop_rate_value <= GEAR_DROP_RATE + (GEAR_DROP_RATE * player.magic_find):
        if len(inventory) >= 150:
            pass
        else:
            enemy_gear_drop()
    else:
        pass


def enemy_gear_drop():
    drop = random.choice(gear_type)
    item_type = []
    """
    UNDER DEVELOPMENT
    """
    # MAKE SURE ITEM DROPPED DOES NOT EXCEED 2 COPIES OF A SAME ITEM IN THE INVENTORY:
    # temp_duplicates = []
    # for item in inventory:
    #     if item_type[0]['name'] == item.__dict__['name']:
    #         temp_duplicates.append(item.__dict__['name'])
    # try:
    #     if item_type[0]['name'] in temp_duplicates and temp_duplicates.count(item_type[0]['name']) >= 2:
    #         temp_duplicates.clear()
    #         enemy_gear_drop()
    # except:
    #     pass
    # temp_duplicates.clear()
    """
    UNDER DEVELOPMENT
    """
    if drop == 'weapon':
        item_drop = item_level_random_setter(weapon_type)
        item_type.append(item_drop)
    elif drop == 'amulet':
        item_drop = item_level_random_setter(amulet_type)
        item_type.append(item_drop)
    elif drop == 'armor':
        item_drop = item_level_random_setter(armor_type)
        item_type.append(item_drop)
    elif drop == 'boots':
        item_drop = item_level_random_setter(boots_type)
        item_type.append(item_drop)
    elif drop == 'gloves':
        item_drop = item_level_random_setter(gloves_type)
        item_type.append(item_drop)
    elif drop == 'helmet':
        item_drop = item_level_random_setter(helmet_type)
        item_type.append(item_drop)
    elif drop == 'legs':
        item_drop = item_level_random_setter(legs_type)
        item_type.append(item_drop)
    elif drop == 'ring':
        item_drop = item_level_random_setter(ring_type)
        item_type.append(item_drop)
    elif drop == 'second_hand':
        item_drop = item_level_random_setter(second_hand_type)
        item_type.append(item_drop)
    else:
        pass

    new_item = Item(item_type[0]['type'],
                    item_type[0]['name'],
                    item_type[0]['level'],
                    item_type[0]['life'],
                    item_type[0]['attack'],
                    item_type[0]['defense'],
                    item_type[0]['crit_chance'],
                    item_type[0]['crit_damage'],
                    item_type[0]['magic_find'],
                    item_type[0]['rarity'],
                    )

    inventory.append(new_item)
    temp_gear_drop.append(new_item)
    inventory_update(player.name, new_item)
    inventory_limit()


def consumable_drop_rate():
    consumable_drop_rate_value = random.randint(0, 100)
    print(f'com magic find {CONSUMABLE_DROP_RATE + (player.magic_find * 100)}')
    if consumable_drop_rate_value <= CONSUMABLE_DROP_RATE + (CONSUMABLE_DROP_RATE * player.magic_find):
        enemy_consumable_drop()
    else:
        pass


def enemy_consumable_drop():
    global drop_quantity

    drop = random.randint(0, 100)
    quantity = random.randint(0, 100)
    ticket_drop = random.randint(0, 100)

    if quantity >= 95:
        drop_quantity += 2
    elif 75 <= quantity < 95:
        drop_quantity += 1
    else:
        pass

    if 0 <= drop < 70:
        if 10 < player.level < 15:
            hi_potion.quantity += drop_quantity
            temp_consumable_drop.append(hi_potion)
        elif 15 <= player.level < 18:
            x_potion.quantity += drop_quantity
            temp_consumable_drop.append(x_potion)
        elif 18 <= player.level < 20:
            drop2 = random.randint(0, 100)
            if drop2 < 50:
                x_potion.quantity += drop_quantity
                temp_consumable_drop.append(x_potion)
            else:
                elixir.quantity += drop_quantity
                temp_consumable_drop.append(elixir)
        elif player.level == 20:
            elixir.quantity += drop_quantity
            temp_consumable_drop.append(elixir)
        else:
            potion.quantity += drop_quantity
            temp_consumable_drop.append(potion)
            # mirror_of_kalandra.quantity = mirror_of_kalandra.quantity + 1
            # temp_consumable_drop.append(mirror_of_kalandra)
    elif 70 <= drop < 78:
        hi_potion.quantity += drop_quantity
        temp_consumable_drop.append(hi_potion)
    elif 78 <= drop < 85:
        x_potion.quantity += drop_quantity
        temp_consumable_drop.append(x_potion)
    elif 85 <= drop < 91:
        elixir.quantity += drop_quantity
        temp_consumable_drop.append(elixir)
    elif 91 <= drop < 94:
        chaos_orb.quantity += drop_quantity
        temp_consumable_drop.append(chaos_orb)
    elif 94 <= drop < 97:
        divine_orb.quantity += drop_quantity
        temp_consumable_drop.append(divine_orb)
    elif 97 <= drop <= 99:
        exalted_orb.quantity += drop_quantity
        temp_consumable_drop.append(exalted_orb)
    else:
        random2 = random.randint(0, 100)
        if random2 <= 80:
            exalted_orb.quantity += drop_quantity
            temp_consumable_drop.append(exalted_orb)
        else:
            mirror_of_kalandra.quantity += 1
            temp_consumable_drop.append(mirror_of_kalandra)
    if ticket_drop < TICKET_DROP_RATE:
        roulette_wheel_ticket.quantity += 1
        temp_ticket_drop.append(roulette_wheel_ticket)


def unique_drop_rate():
    drop_rate_value = random.randint(0, 100)
    if len(list(set(uniques_list))) >= 9:
        pass
    else:
        if drop_rate_value <= UNIQUE_DROP_RATE + (UNIQUE_DROP_RATE * player.magic_find):
            drop = random.choice(uniques)
            inventory_uniques = [value for elem in inventory for value in elem.__dict__.values()]
            if drop['name'] in inventory_uniques:
                if drop['name'] in uniques_list:
                    pass
                else:
                    uniques_list.append(drop['name'])
                unique_drop_rate()
            elif drop['name'] == player_slot.amulet['name'] or drop['name'] == player_slot.armor['name'] or drop[
                'name'] == \
                    player_slot.boots['name'] or drop['name'] == player_slot.gloves['name'] or drop['name'] == \
                    player_slot.helmet['name'] or drop['name'] == player_slot.legs['name'] or drop['name'] == \
                    player_slot.ring1['name'] or drop['name'] == player_slot.ring2['name'] or drop['name'] == \
                    player_slot.second_hand['name'] or drop['name'] == player_slot.weapon['name']:
                if drop['name'] in uniques_list:
                    pass
                else:
                    uniques_list.append(drop['name'])
                unique_drop_rate()
            else:
                new_item = Unique(drop['type'],
                                  drop['name'],
                                  drop['level'],
                                  drop['life'],
                                  drop['attack'],
                                  drop['defense'],
                                  drop['crit_chance'],
                                  drop['crit_damage'],
                                  drop['magic_find'],
                                  drop['rarity'],
                                  )
                if drop['name'] in uniques_list:
                    pass
                else:
                    uniques_list.append(drop['name'])
                inventory.append(new_item)
                db.execute("INSERT INTO uniques_list (username, name) VALUES (:username, :name)",
                           username=player.name, name=drop['name'])
                inventory_update(player.name, new_item)
                temp_unique_drop.append(new_item)


def item_level_random_setter(gear_type):
    filtered_dict = (
        [x for x in gear_type if x['level'] > player.level - 2 and x['level'] < player.level + 2 and x['level'] > 1])
    filtered_drop = random.choice(filtered_dict)
    if filtered_drop['level'] > 25:
        filtered_drop['level'] = 25
    elif filtered_drop['level'] <= 1:
        filtered_drop['level'] = 2
    elif filtered_drop['level'] is None:
        filtered_drop['level'] = player.level
    return filtered_drop


def item_type_confirmation(item_index, item):
    global counter
    if item.type == 'ring':
        ring_slot_confirmation(item_index, item)
    else:
        equip_item(item_index, item, 0)


def ring_slot_confirmation(item_index, item):
    SCREEN.blit(BG, (0, 0))
    SCREEN.blit(BATTLE_BOX, (60, 40))

    # Ring slot 1
    ring1 = get_bold_font(30).render(f"{player_slot.ring1['name']}", True, WHITE)
    level_ring1 = get_regular_font(20).render(f"level {player_slot.ring1['level']}", True, WHITE)
    type_ring1 = get_bold_font(20).render(f"Type: {player_slot.ring1['type']}", True, WHITE)
    life_ring1 = get_bold_font(20).render(f"Life: {player_slot.ring1['life']}", True, WHITE)
    attack_ring1 = get_bold_font(20).render(f"Attack: {player_slot.ring1['attack']}", True, WHITE)
    defense_ring1 = get_bold_font(20).render(f"Defense: {player_slot.ring1['defense']}", True, WHITE)
    crit_chance_ring1 = get_bold_font(20).render(f"Critical Chance: {round((player_slot.ring1['crit_chance']), 2)} %",
                                                 True, WHITE)
    crit_damage_ring1 = get_bold_font(20).render(f"Critical Damage: {round((player_slot.ring1['crit_damage']), 2)} %",
                                                 True, WHITE)
    magic_find_ring1 = get_bold_font(20).render(f"Magic Find: {round((player_slot.ring1['magic_find'] * 100), 2)} %",
                                                True, WHITE)
    ring1_rect = ring1.get_rect(midleft=(100, 100))
    level_ring1_rect = level_ring1.get_rect(midleft=(100, 130))
    type_ring1_rect = type_ring1.get_rect(midleft=(100, 180))
    life_ring1_rect = life_ring1.get_rect(midleft=(100, 210))
    attack_ring1_rect = attack_ring1.get_rect(midleft=(100, 240))
    defense_ring1_rect = defense_ring1.get_rect(midleft=(100, 270))
    crit_chance_ring1_rect = crit_chance_ring1.get_rect(midleft=(100, 300))
    crit_damage_ring1_rect = crit_damage_ring1.get_rect(midleft=(100, 330))
    magic_find_ring1_rect = magic_find_ring1.get_rect(midleft=(100, 360))
    SCREEN.blit(ring1, ring1_rect)
    SCREEN.blit(type_ring1, type_ring1_rect)
    SCREEN.blit(level_ring1, level_ring1_rect)
    SCREEN.blit(life_ring1, life_ring1_rect)
    SCREEN.blit(attack_ring1, attack_ring1_rect)
    SCREEN.blit(defense_ring1, defense_ring1_rect)
    SCREEN.blit(crit_chance_ring1, crit_chance_ring1_rect)
    SCREEN.blit(crit_damage_ring1, crit_damage_ring1_rect)
    SCREEN.blit(magic_find_ring1, magic_find_ring1_rect)

    # Ring slot 2
    ring2 = get_bold_font(30).render(f"{player_slot.ring2['name']}", True, WHITE)
    level_ring2 = get_regular_font(20).render(f"level {player_slot.ring2['level']}", True, WHITE)
    type_ring2 = get_bold_font(20).render(f"Type: {player_slot.ring2['type']}", True, WHITE)
    life_ring2 = get_bold_font(20).render(f"Life: {player_slot.ring2['life']}", True, WHITE)
    attack_ring2 = get_bold_font(20).render(f"Attack: {player_slot.ring2['attack']}", True, WHITE)
    defense_ring2 = get_bold_font(20).render(f"Defense: {player_slot.ring2['defense']}", True, WHITE)
    crit_chance_ring2 = get_bold_font(20).render(f"Critical Chance: {round((player_slot.ring2['crit_chance']), 2)} %",
                                                 True, WHITE)
    crit_damage_ring2 = get_bold_font(20).render(f"Critical Damage: {round((player_slot.ring2['crit_damage']), 2)} %",
                                                 True, WHITE)
    magic_find_ring2 = get_bold_font(20).render(f"Magic Find: {round((player_slot.ring1['magic_find'] * 100), 2)} %",
                                                True, WHITE)
    ring2_rect = ring2.get_rect(midleft=(600, 100))
    level_ring2_rect = level_ring2.get_rect(midleft=(600, 130))
    type_ring2_rect = type_ring2.get_rect(midleft=(600, 180))
    life_ring2_rect = life_ring2.get_rect(midleft=(600, 210))
    attack_ring2_rect = attack_ring2.get_rect(midleft=(600, 240))
    defense_ring2_rect = defense_ring2.get_rect(midleft=(600, 270))
    crit_chance_ring2_rect = crit_chance_ring2.get_rect(midleft=(600, 300))
    crit_damage_ring2_rect = crit_damage_ring2.get_rect(midleft=(600, 330))
    magic_find_ring2_rect = magic_find_ring2.get_rect(midleft=(600, 360))
    SCREEN.blit(ring2, ring2_rect)
    SCREEN.blit(type_ring2, type_ring2_rect)
    SCREEN.blit(level_ring2, level_ring2_rect)
    SCREEN.blit(life_ring2, life_ring2_rect)
    SCREEN.blit(attack_ring2, attack_ring2_rect)
    SCREEN.blit(defense_ring2, defense_ring2_rect)
    SCREEN.blit(crit_chance_ring2, crit_chance_ring2_rect)
    SCREEN.blit(crit_damage_ring2, crit_damage_ring2_rect)
    SCREEN.blit(magic_find_ring2, magic_find_ring2_rect)

    none_text1 = get_bold_font(30).render(f"{item.name}", True, WHITE)
    none_text1_rect = none_text1.get_rect(midleft=(700, 100))

    confirm_text = get_bold_font(40).render(f"To which ring slot you want to equip it?", True, WHITE)
    confirm_text_rect = confirm_text.get_rect(center=(SCREEN_WIDTH / 2 - 180, 550))

    SCREEN.blit(confirm_text, confirm_text_rect)

    while True:

        ITEM_DISP_MOUSE_POSITION = pygame.mouse.get_pos()
        BUTTONS = main_menu_structure(ITEM_DISP_MOUSE_POSITION)
        RING_SLOT_1 = Button(image=pygame.image.load("assets/images/Smallest Rect.png"), pos=(160, 450),
                             text_input="RING SLOT 1", font=get_bold_font(30), base_color="White", hovering_color=BLUE)
        RING_SLOT_2 = Button(image=pygame.image.load("assets/images/Smallest Rect.png"), pos=(700, 450),
                             text_input="RING SLOT 2", font=get_bold_font(30), base_color="White", hovering_color=BLUE)
        BUTTONS.extend([RING_SLOT_1, RING_SLOT_2])

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                main_menu_structure_events(ITEM_DISP_MOUSE_POSITION, BUTTONS)
                if RING_SLOT_1.checkForInput(ITEM_DISP_MOUSE_POSITION):
                    equip_item(item_index, item, 1)
                if RING_SLOT_2.checkForInput(ITEM_DISP_MOUSE_POSITION):
                    equip_item(item_index, item, 2)

        for button in BUTTONS:
            button.changeColor(ITEM_DISP_MOUSE_POSITION)
            button.update(SCREEN)

        pygame.display.update()


def equip_item(item_index, item, ring_slot):
    global counter, slot_item

    SCREEN.blit(BG, (0, 0))
    SCREEN.blit(BATTLE_BOX, (60, 40))
    text1 = get_bold_font(30).render(f"{item.name}", True, WHITE)
    level_text = get_regular_font(20).render(f"Level {item.level}", True, WHITE)
    type_text = get_bold_font(20).render(f"Type: {item.type}", True, WHITE)
    life_text = get_bold_font(20).render(f"Life: {item.life}", True, WHITE)
    attack_text = get_bold_font(20).render(f"Attack: {item.attack}", True, WHITE)
    defense_text = get_bold_font(20).render(f"Defense: {item.defense}", True, WHITE)
    crit_chance_text = get_bold_font(20).render(f"Critical Chance: {item.crit_chance} %", True, WHITE)
    crit_damage_text = get_bold_font(20).render(f"Critical Damage: {item.crit_damage} %", True, WHITE)
    magic_find_text = get_bold_font(20).render(f"Magic Find: {round(item.magic_find * 100, 2)} %", True, WHITE)
    text1_rect = text1.get_rect(midleft=(600, 100))
    level_text_rect = level_text.get_rect(midleft=(600, 130))
    type_text_rect = type_text.get_rect(midleft=(600, 180))
    life_text_rect = life_text.get_rect(midleft=(600, 210))
    attack_text_rect = attack_text.get_rect(midleft=(600, 240))
    defense_text_rect = defense_text.get_rect(midleft=(600, 270))
    crit_chance_text_rect = crit_chance_text.get_rect(midleft=(600, 300))
    crit_damage_text_rect = crit_damage_text.get_rect(midleft=(600, 330))
    magic_find_text_rect = magic_find_text.get_rect(midleft=(600, 360))
    SCREEN.blit(text1, text1_rect)
    SCREEN.blit(type_text, type_text_rect)
    SCREEN.blit(level_text, level_text_rect)
    SCREEN.blit(life_text, life_text_rect)
    SCREEN.blit(attack_text, attack_text_rect)
    SCREEN.blit(defense_text, defense_text_rect)
    SCREEN.blit(crit_chance_text, crit_chance_text_rect)
    SCREEN.blit(crit_damage_text, crit_damage_text_rect)
    SCREEN.blit(magic_find_text, magic_find_text_rect)

    if ring_slot == 1:
        slot_item = getattr(player_slot, item.type + '1')
    elif ring_slot == 2:
        slot_item = getattr(player_slot, item.type + '2')
    elif ring_slot == 0:
        slot_item = getattr(player_slot, item.type)

    print(f'aqui B {slot_item}')
    slot_text1 = get_bold_font(30).render(f"{slot_item['name']}", True, BLUE)
    slot_level_text = get_regular_font(20).render(f"Level {slot_item['level']}", True, BLUE)
    slot_type_text = get_bold_font(20).render(f"Type: {slot_item['type']}", True, BLUE)
    slot_life_text = get_bold_font(20).render(f"Life: {slot_item['life']}", True, BLUE)
    slot_attack_text = get_bold_font(20).render(f"Attack: {slot_item['attack']}", True, BLUE)
    slot_defense_text = get_bold_font(20).render(f"Defense: {slot_item['defense']}", True, BLUE)
    slot_crit_chance_text = get_bold_font(20).render(f"Critical Chance: {slot_item['crit_chance']} %", True, BLUE)
    slot_crit_damage_text = get_bold_font(20).render(f"Critical Damage: {slot_item['crit_damage']} %", True, BLUE)
    slot_magic_find_text = get_bold_font(20).render(f"Magic Find: {round(slot_item['magic_find'] * 100, 2)} %", True,
                                                    BLUE)
    slot_text1_rect = slot_text1.get_rect(midleft=(100, 100))
    slot_level_text_rect = slot_level_text.get_rect(midleft=(100, 130))
    slot_type_text_rect = slot_type_text.get_rect(midleft=(100, 180))
    slot_life_text_rect = slot_life_text.get_rect(midleft=(100, 210))
    slot_attack_text_rect = slot_attack_text.get_rect(midleft=(100, 240))
    slot_defense_text_rect = slot_defense_text.get_rect(midleft=(100, 270))
    slot_crit_chance_text_rect = slot_crit_chance_text.get_rect(midleft=(100, 300))
    slot_crit_damage_text_rect = slot_crit_damage_text.get_rect(midleft=(100, 330))
    slot_magic_find_text_rect = slot_magic_find_text.get_rect(midleft=(100, 360))
    SCREEN.blit(slot_text1, slot_text1_rect)
    SCREEN.blit(slot_type_text, slot_type_text_rect)
    SCREEN.blit(slot_level_text, slot_level_text_rect)
    SCREEN.blit(slot_life_text, slot_life_text_rect)
    SCREEN.blit(slot_attack_text, slot_attack_text_rect)
    SCREEN.blit(slot_defense_text, slot_defense_text_rect)
    SCREEN.blit(slot_crit_chance_text, slot_crit_chance_text_rect)
    SCREEN.blit(slot_crit_damage_text, slot_crit_damage_text_rect)
    SCREEN.blit(slot_magic_find_text, slot_magic_find_text_rect)

    none_text1 = get_bold_font(30).render(f"{item.name}", True, WHITE)
    none_text1_rect = none_text1.get_rect(midleft=(700, 100))

    confirm_text = get_bold_font(30).render(f"Confirm you want to equip?", True, WHITE)
    confirm_text_rect = confirm_text.get_rect(center=(SCREEN_WIDTH / 2 - 180, 430))

    item_to_equip_text = get_bold_font(50).render(f"{item.name} level {item.level}", True, WHITE)
    item_to_equip_text_rect = item_to_equip_text.get_rect(center=(SCREEN_WIDTH / 2 - 180, 500))

    SCREEN.blit(confirm_text, confirm_text_rect)
    SCREEN.blit(item_to_equip_text, item_to_equip_text_rect)
    # Equipping item
    # if ring_slot == 0:
    #     slot_item = getattr(player_slot, item.type + '1')
    # elif ring_slot == 2:
    #     slot_item = getattr(player_slot, item.type + '2')
    # elif ring_slot == 0:
    #     slot_item = getattr(player_slot, item.type)

    # item_type = item.type
    # slot_item = getattr(player_slot, item_type)
    if slot_item is None:
        SCREEN.blit(none_text1, none_text1_rect)
    else:
        pass

    while True:

        EQUIP_ITEM_MOUSE_POSITION = pygame.mouse.get_pos()
        BUTTONS = main_menu_structure(EQUIP_ITEM_MOUSE_POSITION)
        NO_BUTTON = Button(image=pygame.image.load("assets/images/Smallest Rect.png"), pos=(380, 600),
                           text_input="NO", font=get_bold_font(30), base_color="White", hovering_color=BLUE)
        YES_BUTTON = Button(image=pygame.image.load("assets/images/Smallest Rect.png"), pos=(540, 600),
                            text_input="YES", font=get_bold_font(30), base_color="White", hovering_color=BLUE)
        BUTTONS.extend([NO_BUTTON, YES_BUTTON])

        # BACK = Button(image=pygame.image.load("images/Smallest Rect.png"), pos=(160, 600),
        #               text_input="BACK", font=get_bold_font(30), base_color="White", hovering_color=BLUE)
        # NEXT = Button(image=pygame.image.load("images/Smallest Rect.png"), pos=(770, 600),
        #               text_input="NEXT", font=get_bold_font(30), base_color="White", hovering_color=BLUE)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                main_menu_structure_events(EQUIP_ITEM_MOUSE_POSITION, BUTTONS)
                if YES_BUTTON.checkForInput(EQUIP_ITEM_MOUSE_POSITION):
                    counter = 0
                    item_equipped_confirmation(item_index, item, ring_slot)
                if NO_BUTTON.checkForInput(EQUIP_ITEM_MOUSE_POSITION):
                    show_item(item_index, item)

        for button in BUTTONS:
            button.changeColor(EQUIP_ITEM_MOUSE_POSITION)
            button.update(SCREEN)

        pygame.display.update()


def item_equipped_confirmation(item_index, item, ring_slot):
    global last_time_ms, counter, slot_item

    if ring_slot == 1:
        slot_item = getattr(player_slot, item.type + '1')
    elif ring_slot == 2:
        slot_item = getattr(player_slot, item.type + '2')
    elif ring_slot == 0:
        slot_item = getattr(player_slot, item.type)
    item_type = item.type
    print(f'item type {item_type}')
    print(ring_slot)
    if slot_item is None:
        pass
        # setattr(player_slot, item_type, item)
        # inventory.remove(item)
        # inventory_removal(player.name, item)
        # item = getattr(player_slot, item_type)
        # counter = 0
        # item_equipped_confirmation(item_index, item)

    elif ring_slot == 1:
        to_inventory = getattr(player_slot, item_type + '1')
        new_item = Item(to_inventory['type'],
                        to_inventory['name'],
                        to_inventory['level'],
                        to_inventory['life'],
                        to_inventory['attack'],
                        to_inventory['defense'],
                        to_inventory['crit_chance'],
                        to_inventory['crit_damage'],
                        to_inventory['magic_find'],
                        to_inventory['rarity']
                        )
        inventory.append(new_item)
        unequip_update_status(new_item)
        inventory.remove(item)
        inventory_removal(player.name, item)
        player_slot.ring1 = item.__dict__
        equip_update_status(item)
        print(f"{item.__dict__['name']} level {item.__dict__['level']} equipped!")
        save_state()
    elif ring_slot == 2:
        to_inventory = getattr(player_slot, item_type + '2')
        new_item = Item(to_inventory['type'],
                        to_inventory['name'],
                        to_inventory['level'],
                        to_inventory['life'],
                        to_inventory['attack'],
                        to_inventory['defense'],
                        to_inventory['crit_chance'],
                        to_inventory['crit_damage'],
                        to_inventory['magic_find'],
                        to_inventory['rarity']
                        )
        inventory.append(new_item)
        unequip_update_status(new_item)
        inventory.remove(item)
        inventory_removal(player.name, item)
        player_slot.ring2 = item.__dict__
        equip_update_status(item)
        print(f"{item.__dict__['name']} level {item.__dict__['level']} equipped!")
        save_state()
    else:
        to_inventory = getattr(player_slot, item_type)
        new_item = Item(to_inventory['type'],
                        to_inventory['name'],
                        to_inventory['level'],
                        to_inventory['life'],
                        to_inventory['attack'],
                        to_inventory['defense'],
                        to_inventory['crit_chance'],
                        to_inventory['crit_damage'],
                        to_inventory['magic_find'],
                        to_inventory['rarity']
                        )
        # inventory list
        inventory.append(new_item)
        # database
        inventory_update(player.name, new_item)
        # slot
        unequip_update_status(new_item)
        setattr(player_slot, item_type, item.__dict__)
        print('-' * DASH)
        print(f"{item.__dict__['name']} level {item.__dict__['level']} equipped!")

        # status
        equip_update_status(item)
        # removal from inventory list
        inventory.remove(item)

        # removal from database
        inventory_removal(player.name, item)
        save_state()

    while True:
        item_to_equip_text = get_bold_font(40).render(f"{item.name} level {item.level} equipped!", True, YELLOW)
        item_to_equip_text_rect = item_to_equip_text.get_rect(center=(SCREEN_WIDTH / 2 - 180, 250))

        diff_time_ms = int(round(time.time() * 4000)) - last_time_ms
        if diff_time_ms >= 4000:
            counter = counter + 1
            last_time_ms = int(round(time.time() * 4000))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        if counter == 1:
            SCREEN.blit(BG, (0, 0))
            SCREEN.blit(BATTLE_BOX, (60, 40))
            # text1 = get_bold_font(30).render(f"{item.name}", True, WHITE)
            # level_text = get_regular_font(20).render(f"Level {item.level}", True, WHITE)
            # type_text = get_bold_font(20).render(f"Type: {item.type}", True, WHITE)
            # life_text = get_bold_font(20).render(f"Life: {item.life}", True, WHITE)
            # attack_text = get_bold_font(20).render(f"Attack: {item.attack}", True, WHITE)
            # defense_text = get_bold_font(20).render(f"Defense: {item.defense}", True, WHITE)
            # crit_chance_text = get_bold_font(20).render(f"Critical Chance: {item.crit_chance} %", True, WHITE)
            # crit_damage_text = get_bold_font(20).render(f"Critical Damage: {item.crit_damage} %", True, WHITE)
            # magic_find_text = get_bold_font(30).render(f"Magic Find: {round(item.magic_find * 100, 2)} %", True, WHITE)
            # text1_rect = text1.get_rect(center=(SCREEN_WIDTH / 2 - 200, 100))
            # level_text_rect = level_text.get_rect(center=(SCREEN_WIDTH / 2- 200, 140))
            # type_text_rect = type_text.get_rect(center=(SCREEN_WIDTH / 2- 200, 190))
            # life_text_rect = life_text.get_rect(center=(SCREEN_WIDTH / 2- 200, 230))
            # attack_text_rect = attack_text.get_rect(center=(SCREEN_WIDTH / 2 - 200, 270))
            # defense_text_rect = defense_text.get_rect(center=(SCREEN_WIDTH / 2- 200, 310))
            # crit_chance_text_rect = crit_chance_text.get_rect(center=(SCREEN_WIDTH / 2- 200, 350))
            # crit_damage_text_rect = crit_damage_text.get_rect(center=(SCREEN_WIDTH / 2- 200, 390))
            # magic_find_text_rect = magic_find_text.get_rect(center=(SCREEN_WIDTH / 2- 200, 430))
            # SCREEN.blit(text1, text1_rect)
            # SCREEN.blit(type_text, type_text_rect)
            # SCREEN.blit(level_text, level_text_rect)
            # SCREEN.blit(life_text, life_text_rect)
            # SCREEN.blit(attack_text, attack_text_rect)
            # SCREEN.blit(defense_text, defense_text_rect)
            # SCREEN.blit(crit_chance_text, crit_chance_text_rect)
            # SCREEN.blit(crit_damage_text, crit_damage_text_rect)
            # SCREEN.blit(magic_find_text, magic_find_text_rect)

            SCREEN.blit(item_to_equip_text, item_to_equip_text_rect)
        if counter == 3:
            show_inventory_page_1(1)

        pygame.display.update()


def confirm_use_consumable_item(item):
    global counter
    SCREEN.blit(BG, (0, 0))
    SCREEN.blit(BATTLE_BOX, (60, 40))
    SCREEN.blit(player.image, (130, 300))
    confirm_text = get_bold_font(40).render(f'Confirm you want to use {item.name}?', True, WHITE)
    confirm_text_rect = confirm_text.get_rect(center=(SCREEN_WIDTH / 2 - 180, 270))
    SCREEN.blit(confirm_text, confirm_text_rect)

    while True:
        CONFIRM_USE_CONSUMABLE_ITEM_MOUSE_POSITION = pygame.mouse.get_pos()
        BUTTONS = main_menu_structure(CONFIRM_USE_CONSUMABLE_ITEM_MOUSE_POSITION)
        YES_BUTTON = Button(image=pygame.image.load("assets/images/Smallest Rect.png"), pos=(540, 400),
                            text_input="YES", font=get_bold_font(30), base_color="White", hovering_color=BLUE)
        NO_BUTTON = Button(image=pygame.image.load("assets/images/Smallest Rect.png"), pos=(380, 400),
                           text_input="NO", font=get_bold_font(30), base_color="White", hovering_color=BLUE)
        BUTTONS.extend([YES_BUTTON, NO_BUTTON])

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                main_menu_structure_events(CONFIRM_USE_CONSUMABLE_ITEM_MOUSE_POSITION, BUTTONS)
                if YES_BUTTON.checkForInput(CONFIRM_USE_CONSUMABLE_ITEM_MOUSE_POSITION):
                    counter = 0
                    use_consumable_item(item)
                if NO_BUTTON.checkForInput(CONFIRM_USE_CONSUMABLE_ITEM_MOUSE_POSITION):
                    show_consumable_items()
            for button in BUTTONS:
                button.changeColor(CONFIRM_USE_CONSUMABLE_ITEM_MOUSE_POSITION)
                button.update(SCREEN)
        pygame.display.update()


def use_consumable_item(item):
    global counter, last_time_ms
    SCREEN.blit(BG, (0, 0))
    SCREEN.blit(BATTLE_BOX, (60, 40))
    SCREEN.blit(player.image, (130, 300))
    potion_setter = False
    hi_potion_setter = False
    x_potion_setter = False
    elixir_setter = False
    chaos_orb_setter = False
    divine_orb_setter = False
    exalted_orb_setter = False
    mirror_of_kalandra_setter = False

    if item.name == 'Potion' and item.quantity > 0:
        player.life = player.life + potion.value
        potion.quantity = potion.quantity - 1
        if player.life > player.total_life:
            player.life = player.total_life
    if item.name == 'Hi-Potion' and item.quantity > 0:
        player.life = player.life + hi_potion.value
        hi_potion.quantity = hi_potion.quantity - 1
        if player.life > player.total_life:
            player.life = player.total_life
    if item.name == 'X-Potion' and item.quantity > 0:
        player.life = player.life + x_potion.value
        x_potion.quantity = x_potion.quantity - 1
        if player.life > player.total_life:
            player.life = player.total_life
    if item.name == 'Elixir' and item.quantity > 0:
        player.life = player.total_life
        elixir.quantity = elixir.quantity - 1
    if item.name == 'Chaos Orb' and item.quantity > 0:
        player.attack = player.attack + chaos_orb.value
        chaos_orb.quantity = chaos_orb.quantity - 1
    if item.name == 'Divine Orb' and item.quantity > 0:
        player.defense = player.defense + divine_orb.value
        divine_orb.quantity = divine_orb.quantity - 1
    if item.name == 'Exalted Orb' and item.quantity > 0:
        player.total_life = player.total_life + exalted_orb.value
        exalted_orb.quantity = exalted_orb.quantity - 1
    if item.name == 'Mirror of Kalandra' and item.quantity > 0:
        player.total_life = player.total_life + int(mirror_of_kalandra.value.split(', ')[0])
        player.attack = player.attack + int(mirror_of_kalandra.value.split(', ')[1])
        player.defense = player.defense + int(mirror_of_kalandra.value.split(', ')[2])
        mirror_of_kalandra.quantity = mirror_of_kalandra.quantity - 1
    if item.name == 'Dense Fossil' and item.quantity > 0:
        pass
    if item.name == 'Serrated Fossil' and item.quantity > 0:
        pass
    if item.name == 'Pristine Fossil' and item.quantity > 0:
        pass
    if item.name == 'Deft Fossil' and item.quantity > 0:
        pass
    if item.name == 'Fractured Fossil' and item.quantity > 0:
        pass

    save_state()
    counter = 0
    while True:
        USE_CONSUMABLE_ITEM_CONFIRMATION_MOUSE_POSITION = pygame.mouse.get_pos()

        potion_text = get_bold_font(40).render(f'You restored {potion.value} life points!', True, YELLOW)
        potion_text_rect = potion_text.get_rect(center=(SCREEN_WIDTH / 2 - 180, 260))
        hi_potion_text = get_bold_font(40).render(f'You restored {hi_potion.value} life points!', True, YELLOW)
        hi_potion_text_rect = hi_potion_text.get_rect(center=(SCREEN_WIDTH / 2 - 180, 260))
        x_potion_text = get_bold_font(40).render(f'You restored {x_potion.value} life points!', True, YELLOW)
        x_potion_text_rect = x_potion_text.get_rect(center=(SCREEN_WIDTH / 2 - 180, 260))
        elixir_text = get_bold_font(40).render(f'You restored all your life points!', True, YELLOW)
        elixir_text_rect = elixir_text.get_rect(center=(SCREEN_WIDTH / 2 - 180, 260))
        chaos_orb_text = get_bold_font(40).render(f'Your permanently added +{chaos_orb.value} to your attack!', True,
                                                  YELLOW)
        chaos_orb_text_rect = chaos_orb_text.get_rect(center=(SCREEN_WIDTH / 2 - 180, 260))
        divine_orb_text = get_bold_font(40).render(f'Your permanently added +{divine_orb.value} to your defense!', True,
                                                   YELLOW)
        divine_orb_text_rect = divine_orb_text.get_rect(center=(SCREEN_WIDTH / 2 - 180, 260))
        exalted_orb_text = get_bold_font(40).render(f'Your permanently added +{exalted_orb.value} to your life points!',
                                                    True, YELLOW)
        exalted_orb_text_rect = exalted_orb_text.get_rect(center=(SCREEN_WIDTH / 2 - 180, 260))
        mirror_text1 = get_bold_font(40).render(f"Your permanently added +{(mirror_of_kalandra.value.split(', ')[0])} "
                                                f"to your life points,", True, YELLOW)
        mirror_text1_rect = mirror_text1.get_rect(center=(SCREEN_WIDTH / 2 - 180, 220))
        mirror_text2 = get_bold_font(40).render(f"+{(mirror_of_kalandra.value.split(', ')[1])} to your attack and "
                                                f"+{(mirror_of_kalandra.value.split(', ')[2])} to your defense!", True,
                                                YELLOW)
        mirror_text2_rect = mirror_text2.get_rect(center=(SCREEN_WIDTH / 2 - 180, 275))

        BUTTONS = main_menu_structure(USE_CONSUMABLE_ITEM_CONFIRMATION_MOUSE_POSITION)
        CONTINUE = Button(image=pygame.image.load("assets/images/Smallest Rect.png"), pos=(SCREEN_WIDTH / 2 - 180, 400),
                          text_input="CONTINUE", font=get_bold_font(30), base_color="White", hovering_color=BLUE)
        BUTTONS.append(CONTINUE)

        diff_time_ms = int(round(time.time() * 4000)) - last_time_ms

        if diff_time_ms >= 4000:
            counter = counter + 1
            last_time_ms = int(round(time.time() * 4000))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                main_menu_structure_events(USE_CONSUMABLE_ITEM_CONFIRMATION_MOUSE_POSITION, BUTTONS)
                if CONTINUE.checkForInput(USE_CONSUMABLE_ITEM_CONFIRMATION_MOUSE_POSITION):
                    counter = 0
                    show_consumable_items()

        if counter >= 0 and item.name == 'Potion':
            if not potion_setter:
                SCREEN.blit(potion_text, potion_text_rect)
                potion_setter = True
        if counter >= 0 and item.name == 'Hi-Potion':
            if not hi_potion_setter:
                SCREEN.blit(hi_potion_text, hi_potion_text_rect)
                hi_potion_setter = True
        if counter >= 0 and item.name == 'X-Potion':
            if not x_potion_setter:
                SCREEN.blit(x_potion_text, x_potion_text_rect)
                x_potion_setter = True
        if counter >= 0 and item.name == 'Elixir':
            if not elixir_setter:
                SCREEN.blit(elixir_text, elixir_text_rect)
                elixir_setter = True
        if counter >= 0 and item.name == 'Chaos Orb':
            if not chaos_orb_setter:
                SCREEN.blit(chaos_orb_text, chaos_orb_text_rect)
                chaos_orb_setter = True
        if counter >= 0 and item.name == 'Divine Orb':
            if not divine_orb_setter:
                SCREEN.blit(divine_orb_text, divine_orb_text_rect)
                divine_orb_setter = True
        if counter >= 0 and item.name == 'Exalted Orb':
            if not exalted_orb_setter:
                SCREEN.blit(exalted_orb_text, exalted_orb_text_rect)
                exalted_orb_setter = True
        if counter >= 0 and item.name == 'Mirror of Kalandra':
            if not mirror_of_kalandra_setter:
                SCREEN.blit(mirror_text1, mirror_text1_rect)
                SCREEN.blit(mirror_text2, mirror_text2_rect)
                mirror_of_kalandra_setter = True

        if counter >= 1:
            for button in BUTTONS:
                button.changeColor(USE_CONSUMABLE_ITEM_CONFIRMATION_MOUSE_POSITION)
                button.update(SCREEN)

        pygame.display.update()


def use_fossil(fossil, item_index, item):
    # item_index = 1
    SCREEN.blit(BG, (0, 0))
    SCREEN.blit(BATTLE_BOX, (60, 40))
    display_level_xp()
    confirm_text1 = get_bold_font(35).render(f'Confirm you want to reforge it with {fossil.name}?', True, WHITE)
    confirm_text1_rect = confirm_text1.get_rect(center=(SCREEN_WIDTH / 2 - 180, 480))
    text2 = get_bold_font(25).render(f'(1% chance for the item to get destroyed)', True, WHITE)
    text2_rect = text2.get_rect(center=(SCREEN_WIDTH / 2 - 180, 520))

    text1 = get_bold_font(40).render(f"{item.name}", True, WHITE)
    level_text = get_regular_font(30).render(f"Level {item.level}", True, WHITE)
    type_text = get_bold_font(30).render(f"Type: {item.type}", True, WHITE)
    life_text = get_bold_font(30).render(f"Life: {item.life}", True, WHITE)
    attack_text = get_bold_font(30).render(f"Attack: {item.attack}", True, WHITE)
    defense_text = get_bold_font(30).render(f"Defense: {item.defense}", True, WHITE)
    crit_chance_text = get_bold_font(30).render(f"Critical Chance: {item.crit_chance} %", True, WHITE)
    crit_damage_text = get_bold_font(30).render(f"Critical Damage: {item.crit_damage} %", True, WHITE)
    magic_find_text = get_bold_font(30).render(f"Magic Find: {round(item.magic_find * 100, 2)} %", True, WHITE)
    WIDTH = 806 / 2
    text1_rect = text1.get_rect(center=(WIDTH, 90))
    level_text_rect = level_text.get_rect(center=(WIDTH, 130))
    type_text_rect = type_text.get_rect(midleft=(100, 160))
    life_text_rect = life_text.get_rect(midleft=(100, 200))
    attack_text_rect = attack_text.get_rect(midleft=(100, 240))
    defense_text_rect = defense_text.get_rect(midleft=(100, 280))
    crit_chance_text_rect = crit_chance_text.get_rect(midleft=(100, 320))
    crit_damage_text_rect = crit_damage_text.get_rect(midleft=(100, 360))
    magic_find_text_rect = magic_find_text.get_rect(midleft=(100, 400))
    SCREEN.blit(text1, text1_rect)
    SCREEN.blit(type_text, type_text_rect)
    SCREEN.blit(level_text, level_text_rect)
    SCREEN.blit(life_text, life_text_rect)
    SCREEN.blit(attack_text, attack_text_rect)
    SCREEN.blit(defense_text, defense_text_rect)
    SCREEN.blit(crit_chance_text, crit_chance_text_rect)
    SCREEN.blit(crit_damage_text, crit_damage_text_rect)
    SCREEN.blit(magic_find_text, magic_find_text_rect)

    SCREEN.blit(confirm_text1, confirm_text1_rect)
    SCREEN.blit(text2, text2_rect)

    while True:
        USE_FOSSIL_MOUSE_POSITION = pygame.mouse.get_pos()
        BUTTONS = main_menu_structure(USE_FOSSIL_MOUSE_POSITION)
        NO_BUTTON = Button(image=pygame.image.load("assets/images/Smallest Rect.png"), pos=(380, 600),
                           text_input="NO", font=get_bold_font(30), base_color="White", hovering_color=BLUE)
        YES_BUTTON = Button(image=pygame.image.load("assets/images/Smallest Rect.png"), pos=(540, 600),
                            text_input="YES", font=get_bold_font(30), base_color="White", hovering_color=BLUE)
        BUTTONS.extend([NO_BUTTON, YES_BUTTON])

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                main_menu_structure_events(USE_FOSSIL_MOUSE_POSITION, BUTTONS)
                if YES_BUTTON.checkForInput(USE_FOSSIL_MOUSE_POSITION):
                    fossil_reforge(fossil, item_index, item)
                if NO_BUTTON.checkForInput(USE_FOSSIL_MOUSE_POSITION):
                    show_consumable_items()

        for button in BUTTONS:
            button.changeColor(USE_FOSSIL_MOUSE_POSITION)
            button.update(SCREEN)
        pygame.display.update()


def fossil_reforge(fossil, item_index, item_to_reforge):
    choice = random.randint(0, 100)
    fossil.quantity = fossil.quantity - 1
    old_item_name = item_to_reforge.__dict__['name']
    old_item_level = item_to_reforge.__dict__['level']
    print(choice)
    if choice <= 99:
        if fossil.name == 'Dense Fossil':
            number = random.randint(dense_fossil.value // 2, dense_fossil.value)
            item_to_reforge.__dict__['defense'] = item_to_reforge.__dict__['defense'] + number
            item_to_reforge.__dict__['level'] = item_to_reforge.__dict__['level'] + 1
            if '*' in item_to_reforge.__dict__['name']:
                pass
            else:
                item_to_reforge.__dict__['name'] = '*' + item_to_reforge.__dict__['name']
            fossil_reforge_success(fossil, item_index, old_item_name, old_item_level, item_to_reforge)
        elif fossil.name == 'Serrated Fossil':
            number = random.randint(serrated_fossil.value // 2, serrated_fossil.value)
            item_to_reforge.__dict__['attack'] = item_to_reforge.__dict__['attack'] + number
            item_to_reforge.__dict__['level'] = item_to_reforge.__dict__['level'] + 1
            if '*' in item_to_reforge.__dict__['name']:
                pass
            else:
                item_to_reforge.__dict__['name'] = '*' + item_to_reforge.__dict__['name']
            fossil_reforge_success(fossil, item_index, old_item_name, old_item_level, item_to_reforge)
        elif fossil.name == 'Pristine Fossil':
            number = random.randint(pristine_fossil.value // 2, pristine_fossil.value)
            item_to_reforge.__dict__['life'] = item_to_reforge.__dict__['life'] + number
            item_to_reforge.__dict__['level'] = item_to_reforge.__dict__['level'] + 1
            if '*' in item_to_reforge.__dict__['name']:
                pass
            else:
                item_to_reforge.__dict__['name'] = '*' + item_to_reforge.__dict__['name']
            fossil_reforge_success(fossil, item_index, old_item_name, old_item_level, item_to_reforge)
        elif fossil.name == 'Deft Fossil':
            number = random.randint(deft_fossil.value // 2, deft_fossil.value)
            item_to_reforge.__dict__['crit_damage'] = item_to_reforge.__dict__['crit_damage'] + number
            item_to_reforge.__dict__['level'] = item_to_reforge.__dict__['level'] + 1
            if '*' in item_to_reforge.__dict__['name']:
                pass
            else:
                item_to_reforge.__dict__['name'] = '*' + item_to_reforge.__dict__['name']
            fossil_reforge_success(fossil, item_index, old_item_name, old_item_level, item_to_reforge)
        elif fossil.name == 'Fractured Fossil':
            number = random.randint(fractured_fossil.value // 2, fractured_fossil.value)
            item_to_reforge.__dict__['life'] = item_to_reforge.__dict__['life'] + number
            item_to_reforge.__dict__['attack'] = item_to_reforge.__dict__['attack'] + number
            item_to_reforge.__dict__['defense'] = item_to_reforge.__dict__['defense'] + number
            item_to_reforge.__dict__['crit_chance'] = item_to_reforge.__dict__['crit_chance'] + number
            item_to_reforge.__dict__['crit_damage'] = item_to_reforge.__dict__['crit_damage'] + number
            item_to_reforge.__dict__['level'] = item_to_reforge.__dict__['level'] + 1
            if '*' in item_to_reforge.__dict__['name']:
                pass
            else:
                item_to_reforge.__dict__['name'] = '*' + item_to_reforge.__dict__['name']
            fossil_reforge_success(fossil, item_index, old_item_name, old_item_level, item_to_reforge)
        else:
            pass

    else:
        fossil_reforge_failure(item_index, item_to_reforge)


def fossil_reforge_success(fossil, item_index, old_item_name, old_item_level, new_item):
    SCREEN.blit(BG, (0, 0))
    SCREEN.blit(BATTLE_BOX, (60, 40))
    display_level_xp()
    reforged_item_update(item_index, old_item_name, old_item_level, new_item)
    confirm_text1 = get_bold_font(35).render(
        f"{new_item.__dict__['name']} level {new_item.__dict__['level']} was reforged", True, YELLOW)
    confirm_text1_rect = confirm_text1.get_rect(center=(SCREEN_WIDTH / 2 - 180, 520))
    # text2 = get_bold_font(25).render(f'(10% chance for the item to get destroyed)', True, WHITE)
    # text2_rect = text2.get_rect(center=(SCREEN_WIDTH / 2 - 180, 520))
    SCREEN.blit(confirm_text1, confirm_text1_rect)

    text1 = get_bold_font(40).render(f"{new_item.name}", True, WHITE)
    level_text = get_regular_font(30).render(f"Level {new_item.level}", True, WHITE)
    type_text = get_bold_font(30).render(f"Type: {new_item.type}", True, WHITE)
    life_text = get_bold_font(30).render(f"Life: {new_item.life}", True, WHITE)
    attack_text = get_bold_font(30).render(f"Attack: {new_item.attack}", True, WHITE)
    defense_text = get_bold_font(30).render(f"Defense: {new_item.defense}", True, WHITE)
    crit_chance_text = get_bold_font(30).render(f"Critical Chance: {new_item.crit_chance} %", True, WHITE)
    crit_damage_text = get_bold_font(30).render(f"Critical Damage: {new_item.crit_damage} %", True, WHITE)
    magic_find_text = get_bold_font(30).render(f"Magic Find: {round(new_item.magic_find * 100, 2)} %", True, WHITE)
    text1_rect = text1.get_rect(center=(SCREEN_WIDTH / 2 - 200, 100))
    level_text_rect = level_text.get_rect(center=(SCREEN_WIDTH / 2 - 200, 140))
    type_text_rect = type_text.get_rect(center=(SCREEN_WIDTH / 2 - 200, 190))
    life_text_rect = life_text.get_rect(center=(SCREEN_WIDTH / 2 - 200, 230))
    attack_text_rect = attack_text.get_rect(center=(SCREEN_WIDTH / 2 - 200, 270))
    defense_text_rect = defense_text.get_rect(center=(SCREEN_WIDTH / 2 - 200, 310))
    crit_chance_text_rect = crit_chance_text.get_rect(center=(SCREEN_WIDTH / 2 - 200, 350))
    crit_damage_text_rect = crit_damage_text.get_rect(center=(SCREEN_WIDTH / 2 - 200, 390))
    magic_find_text_rect = magic_find_text.get_rect(center=(SCREEN_WIDTH / 2 - 200, 430))
    SCREEN.blit(text1, text1_rect)
    SCREEN.blit(type_text, type_text_rect)
    SCREEN.blit(level_text, level_text_rect)
    SCREEN.blit(life_text, life_text_rect)
    SCREEN.blit(attack_text, attack_text_rect)
    SCREEN.blit(defense_text, defense_text_rect)
    SCREEN.blit(crit_chance_text, crit_chance_text_rect)
    SCREEN.blit(crit_damage_text, crit_damage_text_rect)
    SCREEN.blit(magic_find_text, magic_find_text_rect)

    while True:
        USE_FOSSIL_MOUSE_POSITION = pygame.mouse.get_pos()
        BUTTONS = main_menu_structure(USE_FOSSIL_MOUSE_POSITION)
        CONTINUE = Button(image=pygame.image.load("assets/images/Smallest Rect.png"), pos=(SCREEN_WIDTH / 2 - 180, 590),
                          text_input="CONTINUE", font=get_bold_font(30), base_color="White", hovering_color=BLUE)
        BUTTONS.append(CONTINUE)

        # NO_BUTTON = Button(image=pygame.image.load("images/Smallest Rect.png"), pos=(380, 600),
        #                      text_input="NO", font=get_bold_font(30), base_color="White", hovering_color=BLUE)
        # YES_BUTTON = Button(image=pygame.image.load("images/Smallest Rect.png"), pos=(540, 600),
        #                     text_input="YES", font=get_bold_font(30), base_color="White", hovering_color=BLUE)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                main_menu_structure_events(USE_FOSSIL_MOUSE_POSITION, BUTTONS)
                if CONTINUE.checkForInput(USE_FOSSIL_MOUSE_POSITION):
                    show_consumable_items()

        for button in BUTTONS:
            button.changeColor(USE_FOSSIL_MOUSE_POSITION)
            button.update(SCREEN)
        pygame.display.update()


def reforged_item_update(item_index, old_item_name, old_item_level, new_item):
    row = db.execute("SELECT * FROM inventory WHERE username = :username AND name = :name AND level = :level",
                     username=player.name, name=old_item_name, level=old_item_level)
    id = (row[0]['id'])

    db.execute("DELETE FROM inventory WHERE id = :id",
               id=id)
    db.execute(
        "INSERT INTO inventory (username, name, type, level, life, attack, defense, crit_chance, crit_damage, magic_find, rarity)"
        "VALUES (:username, :name, :type, :level, :life, :attack, :defense, :crit_chance, :crit_damage, :magic_find, :rarity)",
        username=player.name,
        name=new_item.__dict__['name'],
        type=new_item.__dict__['type'],
        level=new_item.__dict__['level'],
        life=new_item.__dict__['life'],
        attack=new_item.__dict__['attack'],
        defense=new_item.__dict__['defense'],
        crit_chance=new_item.__dict__['crit_chance'],
        crit_damage=new_item.__dict__['crit_damage'],
        magic_find=new_item.__dict__['magic_find'],
        rarity=new_item.__dict__['rarity'])


def fossil_reforge_failure(item_index, item_to_reforge):
    SCREEN.blit(BG, (0, 0))
    SCREEN.blit(BATTLE_BOX, (60, 40))
    display_level_xp()
    row = db.execute("SELECT * FROM inventory WHERE username = :username AND name = :name AND level = :level",
                     username=player.name,
                     name=item_to_reforge.__dict__['name'],
                     level=item_to_reforge.__dict__['level'])
    id = (row[0]['id'])
    db.execute("DELETE FROM inventory WHERE id = :id",
               id=id)

    text1 = get_bold_font(40).render(
        f"{item_to_reforge.__dict__['name']} {item_to_reforge.__dict__['level']} was destroyed!", True, RED)
    text1_rect = text1.get_rect(center=(SCREEN_WIDTH / 2 - 180, 250))
    SCREEN.blit(text1, text1_rect)
    # inventory.remove(item_index)
    inventory.clear()
    save_state()
    # inventory_update(player.name, item_to_reforge)
    load_state()
    while True:
        FOSSIL_REFORGE_FAILURE_MOUSE_POSITION = pygame.mouse.get_pos()
        BUTTONS = main_menu_structure(FOSSIL_REFORGE_FAILURE_MOUSE_POSITION)
        CONTINUE = Button(image=pygame.image.load("assets/images/Smallest Rect.png"), pos=(SCREEN_WIDTH / 2 - 180, 550),
                          text_input="CONTINUE", font=get_bold_font(30), base_color="White", hovering_color=BLUE)
        BUTTONS.append(CONTINUE)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                main_menu_structure_events(FOSSIL_REFORGE_FAILURE_MOUSE_POSITION, BUTTONS)
                if CONTINUE.checkForInput(FOSSIL_REFORGE_FAILURE_MOUSE_POSITION):
                    show_consumable_items()

        for button in BUTTONS:
            button.changeColor(FOSSIL_REFORGE_FAILURE_MOUSE_POSITION)
            button.update(SCREEN)
        pygame.display.update()


def equip_update_status(item):
    player.total_life = player.total_life + int(item.life)
    player.attack = player.attack + int(item.attack)
    player.defense = player.defense + int(item.defense)
    player.crit_chance = player.crit_chance + int(item.crit_chance)
    player.crit_damage = player.crit_damage + int(item.crit_damage)
    player.magic_find = player.magic_find + item.magic_find


def unequip_update_status(item):
    player.total_life = player.total_life - int(item.life)
    player.attack = player.attack - int(item.attack)
    player.defense = player.defense - int(item.defense)
    player.crit_chance = player.crit_chance - int(item.crit_chance)
    player.crit_damage = player.crit_damage - int(item.crit_damage)
    player.magic_find = player.magic_find - item.magic_find


def crit_chance(character_crit_chance, character_attack, character_critdamage):
    crit_chance_random = random.randint(1, 100)
    if crit_chance_random <= character_crit_chance:
        random2 = random.randint(10, character_attack // 2)
        crit_damage = int((character_attack + random2) + (character_critdamage / character_attack * 100))
        return crit_damage
    else:
        return character_attack


def battle():
    global counter
    if enemy.life > 0:
        # life_bars()
        battle_elements_resetter()

        # IF ENEMY ATTACK IS ZERO
        if enemy.attack <= player.defense:
            battle_condition_1()

        # # IF ENEMY ATTACK IS NOT ZERO
        else:
            a = crit_chance(player.crit_chance, player.attack, player.crit_damage)
            b = crit_chance(enemy.crit_chance, enemy.attack, 1.4)
            # PLAYER CRITICAL AND ENEMY NORMAL ATTACK
            if a > player.attack and b == enemy.attack:
                enemy_damage = a - enemy.defense
                counter = 0
                battle_condition_2a(enemy_damage)

            # PLAYER AND ENEMY CRITICAL
            elif a > player.attack and b > enemy.attack:
                enemy_damage = a - enemy.defense
                player_damage = b - player.defense
                counter = 0
                battle_condition_2b(enemy_damage, player_damage)

            # PLAYER NORMAL ATTACK AND ENEMY CRITICAL
            elif a == player.attack and b > enemy.attack:
                enemy_damage = player.attack - enemy.defense
                player_damage = b - player.defense
                counter = 0
                battle_condition_2c(enemy_damage, player_damage)

            else:
                enemy_damage = player.attack - enemy.defense
                player_damage = enemy.attack - player.defense
                counter = 0
                battle_condition_2d(enemy_damage, player_damage)

    else:
        enemy.life = 0
        battle_elements_resetter()
        if enemy in [wiegraf1, wiegraf2, dycedarg1, dycedarg2]:
            show_dialogue(enemy)
        if enemy.life == 0:
            SCREEN.fill(0)
            SCREEN.blit(BG, (0, 0))
            SCREEN.blit(BATTLE_BOX, (60, 40))
            # PLAYER
            SCREEN.blit(player.image, (130, 300))
            player_level_up()
            battle_finish()
            # battle_elements_resetter()


# IF ENEMY ATTACK IS ZERO AND PLAYER ATTACK IS CRITICAL
def battle_condition_1_a(player_damage, a):
    global counter, last_time_ms
    display_level_xp()
    enemy_damage = a - enemy.defense
    enemy.life = enemy.life - enemy_damage
    player.life = player.life - player_damage
    counter = 0
    c_a = False
    e_a_s = False
    while True:
        text0 = get_regular_font(20).render(f'CRITICAL!', True, WHITE)
        text0_rect = text0.get_rect(center=(750, 220))
        text1 = get_bold_font(70).render(f'{enemy_damage}', True, ORANGE)
        text1_rect = text1.get_rect(center=(750, 260))
        text2 = get_regular_font(20).render(f'MISS!', True, WHITE)
        text2_rect = text2.get_rect(center=(170, 260))

        diff_time_ms = int(round(time.time() * 4000)) - last_time_ms

        if diff_time_ms >= 4000:
            counter = counter + 1
            last_time_ms = int(round(time.time() * 4000))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        if counter == 1:
            SCREEN.blit(text0, text0_rect)
            SCREEN.blit(text1, text1_rect)
            if not c_a:
                critical_attack_sound()
                c_a = True
        if counter == 2:
            SCREEN.blit(text2, text2_rect)
            if not e_a_s:
                enemy_attack_sound()
                e_a_s = True
        if counter == 3:
            counter = 0
            battle()
        pygame.display.update()


# IF ENEMY ATTACK IS ZERO AND PLAYER ATTACK IS NORMAL
def battle_condition_1_b(player_damage):
    display_level_xp()
    global last_time_ms, counter
    p_a_s = False
    e_a_s = False
    enemy_damage = player.attack - enemy.defense
    enemy.life = enemy.life - enemy_damage
    player.life = player.life - player_damage

    while True:
        text1 = get_bold_font(50).render(f'{enemy_damage}', True, RED)
        text1_rect = text1.get_rect(center=(750, 260))
        text2 = get_bold_font(20).render(f'MISS!', True, WHITE)
        text2_rect = text2.get_rect(center=(180, 260))

        diff_time_ms = int(round(time.time() * 4000)) - last_time_ms

        if diff_time_ms >= 4000:
            counter = counter + 1
            last_time_ms = int(round(time.time() * 4000))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        if counter == 1:
            if not p_a_s:
                SCREEN.blit(text1, text1_rect)
                critical_attack_sound()
                p_a_s = True
        if counter == 2:
            if not e_a_s:
                SCREEN.blit(text2, text2_rect)
                enemy_attack_sound()
                e_a_s = True
        if counter == 3:
            counter = 0
            battle()
        pygame.display.update()


# IF ENEMY ATTACK IS ZERO
def battle_condition_1():
    global counter
    player_damage = 0
    a = crit_chance(player.crit_chance, player.attack, player.crit_damage)
    if a > player.attack:
        counter = 0
        battle_condition_1_a(player_damage, a)
    else:
        counter = 0
        battle_condition_1_b(player_damage)


# PLAYER CRITICAL AND ENEMY NORMAL ATTACK
def battle_condition_2a(e_damage):
    global counter, last_time_ms
    display_level_xp()
    player_damage = enemy.attack - player.defense
    enemy.life = enemy.life - e_damage
    player.life = player.life - player_damage
    c_a = False
    e_a_s = False

    while True:
        text0 = get_regular_font(20).render(f'CRITICAL!', True, WHITE)
        text0_rect = text0.get_rect(center=(750, 220))
        text1 = get_bold_font(70).render(f'{e_damage}', True, ORANGE)
        text1_rect = text1.get_rect(center=(750, 260))
        text2 = get_bold_font(50).render(f'{player_damage}', True, RED)
        text2_rect = text2.get_rect(center=(180, 260))

        diff_time_ms = int(round(time.time() * 4000)) - last_time_ms

        if diff_time_ms >= 4000:
            counter = counter + 1
            last_time_ms = int(round(time.time() * 4000))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        if counter == 1:
            if not c_a:
                SCREEN.blit(text0, text0_rect)
                SCREEN.blit(text1, text1_rect)
                critical_attack_sound()
                c_a = True
        if counter == 2:
            if not e_a_s:
                SCREEN.blit(text2, text2_rect)
                enemy_attack_sound()
                e_a_s = True
        if counter == 3:
            counter = 0
            battle()
        pygame.display.update()


# PLAYER AND ENEMY CRITICAL
def battle_condition_2b(e_damage, p_damage):
    global counter, last_time_ms
    display_level_xp()
    enemy.life = enemy.life - e_damage
    player.life = player.life - p_damage
    c_a = False
    c_a_2 = False

    while True:
        text0 = get_regular_font(20).render(f'CRITICAL!', True, WHITE)
        text0_rect = text0.get_rect(center=(750, 220))
        text1 = get_bold_font(70).render(f'{e_damage}', True, ORANGE)
        text1_rect = text1.get_rect(center=(750, 260))
        text1_5 = get_regular_font(20).render(f'CRITICAL!', True, WHITE)
        text1_5_rect = text1_5.get_rect(center=(180, 220))
        text2 = get_bold_font(70).render(f'{p_damage}', True, ORANGE)
        text2_rect = text2.get_rect(center=(180, 260))

        diff_time_ms = int(round(time.time() * 4000)) - last_time_ms

        if diff_time_ms >= 4000:
            counter = counter + 1
            last_time_ms = int(round(time.time() * 4000))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        if counter == 1:
            if not c_a:
                SCREEN.blit(text0, text0_rect)
                SCREEN.blit(text1, text1_rect)
                critical_attack_sound()
                c_a = True
        if counter == 2:
            if not c_a_2:
                SCREEN.blit(text1_5, text1_5_rect)
                SCREEN.blit(text2, text2_rect)
                critical_attack_sound()
                c_a_2 = True
        if counter == 3:
            counter = 0
            battle()
        pygame.display.update()


# PLAYER NORMAL ATTACK AND ENEMY CRITICAL
def battle_condition_2c(e_damage, p_damage):
    global counter, last_time_ms
    display_level_xp()
    enemy.life = enemy.life - e_damage
    player.life = player.life - p_damage
    p_a_s = False
    c_a = False
    while True:
        # text0 = get_regular_font(20).render(f'CRITICAL!', True, WHITE)
        # text0_rect = text0.get_rect(center=(750, 220))
        text1 = get_bold_font(50).render(f'{e_damage}', True, RED)
        text1_rect = text1.get_rect(center=(750, 260))
        text1_5 = get_regular_font(20).render(f'CRITICAL!', True, WHITE)
        text1_5_rect = text1_5.get_rect(center=(180, 220))
        text2 = get_bold_font(70).render(f'{p_damage}', True, ORANGE)
        text2_rect = text2.get_rect(center=(180, 260))

        diff_time_ms = int(round(time.time() * 4000)) - last_time_ms

        if diff_time_ms >= 4000:
            counter = counter + 1
            last_time_ms = int(round(time.time() * 4000))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        if counter == 1:
            if not p_a_s:
                SCREEN.blit(text1, text1_rect)
                player_attack_sound()
                p_a_s = True
        if counter == 2:
            if not c_a:
                SCREEN.blit(text1_5, text1_5_rect)
                SCREEN.blit(text2, text2_rect)
                critical_attack_sound()
                c_a = True
        if counter == 3:
            counter = 0
            battle()
        pygame.display.update()


# PLAYER AND ENEMY NORMAL ATTACK
def battle_condition_2d(e_damage, p_damage):
    global counter, last_time_ms
    display_level_xp()
    enemy.life = enemy.life - e_damage
    player.life = player.life - p_damage
    p_a_s = False
    e_a_s = False
    while True:
        text1 = get_bold_font(50).render(f'{e_damage}', True, RED)
        text1_rect = text1.get_rect(center=(750, 260))
        text2 = get_bold_font(50).render(f'{p_damage}', True, RED)
        text2_rect = text2.get_rect(center=(180, 260))

        diff_time_ms = int(round(time.time() * 4000)) - last_time_ms

        if diff_time_ms >= 4000:
            counter = counter + 1
            last_time_ms = int(round(time.time() * 4000))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        if counter == 1:
            if not p_a_s:
                SCREEN.blit(text1, text1_rect)
                player_attack_sound()
                p_a_s = True
        if counter == 2:
            if not e_a_s:
                SCREEN.blit(text2, text2_rect)
                critical_attack_sound()
                e_a_s = True
        if counter == 3:
            counter = 0
            battle()
        pygame.display.update()


def battle_finish():
    global counter, last_time_ms, DROP_HEIGHT, drop_quantity
    check_player_life()
    shaman()
    gear_drop_rate()
    unique_drop_rate()
    consumable_drop_rate()
    # player_level_up()
    draw_player_level_up()
    save_state()

    if enemy.name == 'Wiegraf':
        wiegraf1.status = False
    elif enemy.name == 'Dycedarg':
        dycedarg1.status = False
    elif enemy.name == 'Wiegraf, Corpse Brigade Head':
        wiegraf2.status = False
    elif enemy.name == 'Dycedarg, the Betrayer God':
        dycedarg2.status = False
    else:
        pass
    battle_elements_resetter()
    display_level_xp()
    counter = 0
    text1 = get_bold_font(30).render(
        f"You've defeated level {enemy.level} {enemy.name} and gained {enemy.xp} xp points!", True, "White")
    text1_rect = text1.get_rect(center=(440, 100))
    SCREEN.blit(text1, text1_rect)
    text2 = get_regular_font(25).render(f"Your shaman healed you {player.shaman} life points!", True, "White")
    text2_rect = text2.get_rect(center=(440, 170))
    SCREEN.blit(text2, text2_rect)
    drop_setter = False
    unique_setter = False
    consumable_setter = False
    ticket_setter = False
    while True:
        # battle_elements_resetter()
        BATTLE_FINISH_MOUSE_POSITION = pygame.mouse.get_pos()
        BUTTONS = main_menu_structure(BATTLE_FINISH_MOUSE_POSITION)
        CONTINUE = Button(image=pygame.image.load("assets/images/Smallest Rect.png"), pos=(SCREEN_WIDTH / 2 - 180, 550),
                          text_input="CONTINUE", font=get_bold_font(30), base_color="White", hovering_color=BLUE)
        BUTTONS.append(CONTINUE)

        diff_time_ms = int(round(time.time() * 4000)) - last_time_ms
        if diff_time_ms >= 4000:
            counter = counter + 1
            last_time_ms = int(round(time.time() * 4000))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                main_menu_structure_events(BATTLE_FINISH_MOUSE_POSITION, BUTTONS)
                if CONTINUE.checkForInput(BATTLE_FINISH_MOUSE_POSITION):
                    DROP_HEIGHT = 210
                    counter = 0
                    encounter()

        if counter == 1:
            if len(temp_gear_drop) != 0:
                if drop_setter is False:
                    if len(inventory) >= 150:
                        gear_drop_text = get_bold_font(35).render(f"[INVENTORY FULL! Get rid of unwanted gear first!]",
                                                                  True, YELLOW)
                    else:
                        gear_drop_text = get_bold_font(35).render(f"{temp_gear_drop[-1].__dict__['name']} level "
                                                                  f"{temp_gear_drop[-1].__dict__['level']} dropped!",
                                                                  True,
                                                                  YELLOW)
                    gear_drop_text_rect = gear_drop_text.get_rect(center=(440, DROP_HEIGHT))
                    SCREEN.blit(gear_drop_text, gear_drop_text_rect)
                    gear_drop_sound()
                    # playsound(DROP_1, True)
                    temp_gear_drop.clear()
                    DROP_HEIGHT = DROP_HEIGHT + 40
                    drop_setter = True
                    counter = 0

        if counter == 1:
            if len(temp_unique_drop) != 0:
                if unique_setter is False:
                    unique_drop_text = get_bold_font(35).render(f"{temp_unique_drop[-1].__dict__['name']} level "
                                                                f"{temp_unique_drop[-1].__dict__['level']} dropped!",
                                                                True,
                                                                ORANGE)
                    unique_drop_text_rect = unique_drop_text.get_rect(center=(440, DROP_HEIGHT))
                    SCREEN.blit(unique_drop_text, unique_drop_text_rect)
                    gear_drop_sound()
                    # playsound(DROP_1, False)
                    temp_unique_drop.clear()
                    DROP_HEIGHT = DROP_HEIGHT + 40
                    unique_setter = True
                    counter = 0

        if counter == 1:
            if len(temp_consumable_drop) != 0:
                if consumable_setter is False:
                    consumable_drop_text = get_bold_font(35).render(
                        f"{drop_quantity}x {temp_consumable_drop[-1].__dict__['name']} dropped!",
                        True, CYAN)
                    consumable_drop_text_rect = consumable_drop_text.get_rect(center=(440, DROP_HEIGHT))
                    SCREEN.blit(consumable_drop_text, consumable_drop_text_rect)
                    consumable_drop_sound()
                    temp_consumable_drop.clear()
                    drop_quantity = 1
                    consumable_setter = True
                    counter = 0
        if counter == 1:
            if len(temp_ticket_drop) != 0:
                if ticket_setter is False:
                    DROP_HEIGHT = DROP_HEIGHT + 40
                    ticket_drop_text = get_bold_font(35).render(
                        f"{temp_ticket_drop[-1].__dict__['name']} dropped!",
                        True, PINK)
                    ticket_drop_text_rect = ticket_drop_text.get_rect(center=(440, DROP_HEIGHT))
                    SCREEN.blit(ticket_drop_text, ticket_drop_text_rect)
                    consumable_drop_sound()
                    # playsound(temp_ticket_drop[0].__dict__['sound'], False)
                    temp_ticket_drop.clear()
                    ticket_setter = True
                    counter = 0

        if counter >= 1:
            DROP_HEIGHT = 210

        for button in BUTTONS:
            button.changeColor(BATTLE_FINISH_MOUSE_POSITION)
            button.update(SCREEN)

        pygame.display.update()


# def show_dialogue(character, quote):
#     global counter, last_time_ms
#
#     dialogue_setter = False
#     SCREEN.blit(BG, (0, 0))
#     SCREEN.blit(BATTLE_BOX, (60, 40))
#     myNewSurface = pygame.Surface((806, 641))
#
#
#     # PLAYER
#     SCREEN.blit(player.image, (130, 300))
#     # ENEMY
#     SCREEN.blit(pygame.image.load(hoard[i].image), (700, 300))
#
#     # battle_elements_resetter()
#     # SCREEN.blit(BG, (0, 0))
#     # SCREEN.blit(BATTLE_BOX, (60, 40))
#     # SCREEN.blit(PLAYER_STATUS_BOX, (80, 60))
#     # SCREEN.blit(PLAYER_STATUS, (SCREEN_WIDTH / 2 - 70, 180))
#
#     display_level_xp()
#     while True:
#         QUOTING_MOUSE_POSITION = pygame.mouse.get_pos()
#         BUTTONS = main_menu_structure(QUOTING_MOUSE_POSITION)
#
#         CONTINUE = Button(image=pygame.image.load("images/Smallest Rect.png"), pos=(SCREEN_WIDTH / 2 - 180, 590),
#                           text_input="CONTINUE", font=get_bold_font(30), base_color="White", hovering_color=BLUE)
#
#         diff_time_ms = int(round(time.time() * 4000)) - last_time_ms
#         if diff_time_ms >= 4000:
#             counter = counter + 1
#             last_time_ms = int(round(time.time() * 4000))
#
#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 pygame.quit()
#                 sys.exit()
#             if event.type == pygame.MOUSEBUTTONDOWN:
#                 main_menu_structure_events(QUOTING_MOUSE_POSITION, BUTTONS)
#
#         if counter > 1:
#             if dialogue_setter is not True:
#                 word_wrap(myNewSurface, text=quote, font=get_dialog_font(20), color=WHITE)
#                 dialogue_setter = True
#         if counter > 3:
#             for button in [BUTTONS[0], BUTTONS[1], BUTTONS[2], BUTTONS[3], BUTTONS[4], BUTTONS[5], CONTINUE]:
#                 button.changeColor(QUOTING_MOUSE_POSITION)
#                 button.update(SCREEN)
#
#         pygame.display.update()
def show_dialogue(character):
    print(f'{character.name}')
    global counter, last_time_ms
    height = 100
    character_setter = False
    quote1_setter = False
    quote2_setter = False
    quote3_setter = False
    quote4_setter = False

    SCREEN.blit(BG, (0, 0))
    SCREEN.blit(BATTLE_BOX, (60, 40))

    # PLAYER
    SCREEN.blit(player.image, (130, 300))
    # ENEMY
    image_rect = pygame.image.load(enemy.image).get_rect(midbottom=(750, 500))
    SCREEN.blit(pygame.image.load(enemy.image), image_rect)

    display_level_xp()
    while True:
        QUOTING_MOUSE_POSITION = pygame.mouse.get_pos()
        CONTINUE = Button(image=pygame.image.load("assets/images/Smallest Rect.png"), pos=(SCREEN_WIDTH / 2 - 180, 590),
                          text_input="CONTINUE", font=get_bold_font(30), base_color="White", hovering_color=BLUE)

        diff_time_ms = int(round(time.time() * 4000)) - last_time_ms
        if diff_time_ms >= 4000:
            counter = counter + 1
            last_time_ms = int(round(time.time() * 4000))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if CONTINUE.checkForInput(QUOTING_MOUSE_POSITION):
                    if character.life != 0:
                        print('entrou char vivo')
                        battle()
                    else:
                        print('entrou char morto')
                        character.status = False
                        username = player.name
                        if character.name == 'Wiegraf':
                            db.execute("UPDATE boss_instance SET wiegraf1 = :wiegraf1 WHERE username = :username",
                                       wiegraf1=0,
                                       username=username)
                        elif character.name == 'Dycedarg':
                            db.execute("UPDATE boss_instance SET dycedarg1 = :dycedarg1 WHERE username = :username",
                                       dycedarg1=0,
                                       username=username)
                        elif character.name == 'Wiegraf, Corpse Brigade Head':
                            db.execute("UPDATE boss_instance SET wiegraf2 = :wiegraf2 WHERE username = :username",
                                       wiegraf2=0,
                                       username=username)
                        elif character.name == 'Dycedarg, the Betrayer God':
                            db.execute("UPDATE boss_instance SET dycedarg2 = :dycedarg2 WHERE username = :username",
                                       dycedarg2=0,
                                       username=username)
                        else:
                            pass
                        pygame.mixer.music.fadeout(3)
                        pygame.mixer.music.stop()
                        background_music()
                        battle_elements_resetter()
                        battle_finish()

        if counter > 0 and character.life == 0:
            if quote4_setter is not True:
                quote4 = get_quote_font(40).render(f'{character.quote4}', True, WHITE)
                quote4_rect = quote4.get_rect(center=(SCREEN_WIDTH / 2 - 180, height))
                SCREEN.blit(quote4, quote4_rect)
                height = height + 50
                quote4_setter = True

        if counter > 1 and character.life == 0:
            for button in [CONTINUE]:
                button.changeColor(QUOTING_MOUSE_POSITION)
                button.update(SCREEN)

        if counter > 0 and character.life != 0:
            if character_setter is not True:
                character1 = get_bold_font(30).render(f'{character.name}:', True, WHITE)
                character1_rect = character1.get_rect(center=(SCREEN_WIDTH / 2 - 180, height))
                SCREEN.blit(character1, character1_rect)
                height = height + 50
                character_setter = True
        if counter > 1 and character.life != 0:
            if quote1_setter is not True:
                quote1 = get_quote_font(25).render(f'{character.quote1}', True, WHITE)
                quote1_rect = quote1.get_rect(center=(SCREEN_WIDTH / 2 - 180, height))
                SCREEN.blit(quote1, quote1_rect)
                height = height + 50
                quote1_setter = True
        if counter > 2 and character.life != 0:
            if quote2_setter is not True:
                quote2 = get_quote_font(25).render(f'{character.quote2}', True, WHITE)
                quote2_rect = quote2.get_rect(center=(SCREEN_WIDTH / 2 - 180, height))
                SCREEN.blit(quote2, quote2_rect)
                height = height + 50
                quote2_setter = True
        if counter > 3 and character.life != 0:
            if quote3_setter is not True:
                quote3 = get_quote_font(25).render(f'{character.quote3}', True, WHITE)
                quote3_rect = quote3.get_rect(center=(SCREEN_WIDTH / 2 - 180, height))
                SCREEN.blit(quote3, quote3_rect)
                quote3_setter = True
        if counter > 4 and character.life != 0:
            for button in [CONTINUE]:
                button.changeColor(QUOTING_MOUSE_POSITION)
                button.update(SCREEN)

        pygame.display.update()


def boss_battle(boss_instance):
    global counter
    boss_music()
    show_dialogue(boss_instance)
    # show_dialogue(wiegraf1)
    # show_dialogue(wiegraf1)
    # show_dialogue(wiegraf1)
    # print('aqui 3')
    # input(f'{boss_instance.name}: {boss_instance.quote1}')
    # while boss_instance.life > 0:
    #     if boss_instance.attack <= player.defense:
    #         player_damage = 0
    #         a = crit_chance(player.crit_chance, player.attack, player.crit_damage)
    #         if a > player.attack:
    #             enemy_damage = a - boss_instance.defense
    #             boss_instance.life = boss_instance.life - enemy_damage
    #             player.life = player.life - player_damage
    #             print(f"- CRITICAL HIT! You've attacked {boss_instance.name} and dealt {enemy_damage} damage!")
    #             critical_attack_sound()
    #             time.sleep(0.5)
    #             print(f"- {boss_instance.name} attacked you and dealt {player_damage} damage!")
    #             enemy_attack_sound()
    #             time.sleep(0.5)
    #         else:
    #             enemy_damage = player.attack - boss_instance.defense
    #             boss_instance.life = boss_instance.life - enemy_damage
    #             player.life = player.life - player_damage
    #             print(f"- You've attacked {boss_instance.name} and dealt {enemy_damage} damage!")
    #             player_attack_sound()
    #             print(f"- {boss_instance.name} attacked you and dealt {player_damage} damage!")
    #             enemy_attack_sound()
    #             time.sleep(0.5)
    #     else:
    #         a = crit_chance(player.crit_chance, player.attack, player.crit_damage)
    #         b = crit_chance(boss_instance.crit_chance, boss_instance.attack, 1.4)
    #         if a > player.attack and b == boss_instance.attack:
    #             enemy_damage = a - boss_instance.defense
    #             player_damage = boss_instance.attack - player.defense
    #             boss_instance.life = boss_instance.life - enemy_damage
    #             player.life = player.life - player_damage
    #             print(f"- CRITICAL HIT! You've attacked {boss_instance.name} and dealt {enemy_damage} damage!")
    #             critical_attack_sound()
    #             print(f"- {boss_instance.name} attacked you and dealt {player_damage} damage!")
    #             enemy_attack_sound()
    #             time.sleep(0.5)
    #         elif a > player.attack and b > boss_instance.attack:
    #             enemy_damage = a - boss_instance.defense
    #             player_damage = b - player.defense
    #             boss_instance.life = boss_instance.life - enemy_damage
    #             player.life = player.life - player_damage
    #             print(f"- CRITICAL HIT! You've attacked {boss_instance.name} and dealt {enemy_damage} damage!")
    #             critical_attack_sound()
    #             print(f"- CRITICAL HIT! {boss_instance.name} attacked you and dealt {player_damage} damage!")
    #             critical_attack_sound()
    #         elif a == player.attack and b > boss_instance.attack:
    #             enemy_damage = player.attack - boss_instance.defense
    #             player_damage = b - player.defense
    #             boss_instance.life = boss_instance.life - enemy_damage
    #             player.life = player.life - player_damage
    #             print(f"- You've attacked {boss_instance.name} and dealt {enemy_damage} damage!")
    #             player_attack_sound()
    #             print(f"- CRITICAL HIT! {boss_instance.name} attacked you and dealt {player_damage} damage!")
    #             critical_attack_sound()
    #             time.sleep(0.5)
    #         else:
    #             enemy_damage = player.attack - boss_instance.defense
    #             player_damage = boss_instance.attack - player.defense
    #             boss_instance.life = boss_instance.life - enemy_damage
    #             player.life = player.life - player_damage
    #             print(f"- You've attacked {boss_instance.name} and dealt {enemy_damage} damage!")
    #             player_attack_sound()
    #             print(f"- {boss_instance.name} attacked you and dealt {player_damage} damage!")
    #             enemy_attack_sound()
    #             time.sleep(0.5)
    # if boss_instance.life < 0:
    #     boss_instance.life = 0
    # print('-' * DASH)
    # check_player_life()
    # input(f'{boss_instance.name}: {boss_instance.quote2}\n')
    # if boss_instance.name == dycedarg2.name:
    #     print(
    #         f"Congratulations! You've defeated {dycedarg2.name} and reached the endgame of Final Fantasy Tactics—The Idle Game.\n"
    #         f"Please check the Help menu for more information")
    #     print('-' * DASH)
    # else:
    #     print(f'You have defeated {boss_instance.name} and gained {boss_instance.xp} xp points!')
    # boss_instance.status = False
    # username = player.name
    # if boss_instance.name == 'Wiegraf':
    #     db.execute("UPDATE boss_instance SET wiegraf1 = :wiegraf1 WHERE username = :username", wiegraf1=0,
    #                username=username)
    # elif boss_instance.name == 'Dycedarg':
    #     db.execute("UPDATE boss_instance SET dycedarg1 = :dycedarg1 WHERE username = :username", dycedarg1=0,
    #                username=username)
    # elif boss_instance.name == 'Wiegraf, Corpse Brigade Head':
    #     db.execute("UPDATE boss_instance SET wiegraf2 = :wiegraf2 WHERE username = :username", wiegraf2=0,
    #                username=username)
    # elif boss_instance.name == 'Dycedarg, the Betrayer God':
    #     db.execute("UPDATE boss_instance SET dycedarg2 = :dycedarg2 WHERE username = :username", dycedarg2=0,
    #                username=username)
    # else:
    #     pass
    # pygame.mixer.music.fadeout(3)
    # pygame.mixer.music.stop()
    # background_music()
    # input('Press any key to continue...')
    # print('-' * DASH)
    # shaman()
    # player_level_up()
    # gear_drop_rate()
    # unique_drop_rate()
    # consumable_drop_rate()
    # save_state()
    # encounter()


def bg_box_resetter():
    SCREEN.blit(BG, (0, 0))
    SCREEN.blit(BATTLE_BOX, (60, 40))


def battle_elements_resetter():
    # if hoard[i].life > 0:
    # print('still life')
    # BG AND BOX
    SCREEN.blit(BG, (0, 0))
    SCREEN.blit(BATTLE_BOX, (60, 40))
    # PLAYER
    SCREEN.blit(player.image, (130, 300))
    # ENEMY
    if enemy.life > 0:
        image_rect = pygame.image.load(enemy.image).get_rect(midbottom=(750, 500))
        SCREEN.blit(pygame.image.load(enemy.image), image_rect)
    if player.life < 0:
        player.life = 0

    # CONVERTION
    player_ratio = player.life / player.total_life
    player_life_width = 200 * player_ratio

    enemy_ratio = enemy.life / enemy.total_life
    enemy_life_width = 200 * enemy_ratio

    text1 = get_regular_font(20).render(f"{round(player.life)}/{player.total_life}", True, WHITE)
    text1_rect = text1.get_rect(midleft=(100, 540))
    text1_5 = get_bold_font(20).render(f"{player.name}", True, WHITE)
    text1_5_rect = text1_5.get_rect(midleft=(100, 570))
    text2 = get_regular_font(20).render(f"{round(enemy.life)}/{enemy.total_life}", True, WHITE)
    text2_rect = text2.get_rect(midright=(830, 540))
    text3 = get_bold_font(20).render(f"{enemy.name}", True, WHITE)
    text3_rect = text3.get_rect(midright=(830, 570))
    player_life_bar_rect = pygame.Rect(100, 500, 200, 20)  # left/ top / widht / height
    enemy_life_bar_rect = pygame.Rect(630, 500, 200, 20)  # left/ top / widht / height
    player_red_life_bar_rect = pygame.Rect(100, 500, player_life_width, 20)  # left/ top / widht / height
    enemy_red_life_bar_rect = pygame.Rect(630, 500, enemy_life_width, 20)
    pygame.draw.rect(pygame.display.get_surface(), DARK_GREY, player_life_bar_rect)
    pygame.draw.rect(pygame.display.get_surface(), BLUE, player_red_life_bar_rect)
    pygame.draw.rect(pygame.display.get_surface(), DARK_GREY, enemy_life_bar_rect)
    pygame.draw.rect(pygame.display.get_surface(), BLUE, enemy_red_life_bar_rect)
    #
    # # SCREEN.blit(BLACK_LIFE_BAR, player_life_bar_rect)
    # SCREEN.blit(BLACK_LIFE_BAR, enemy_life_bar_rect)
    # # SCREEN.blit(RED_LIFE_BAR, player_red_life_bar_rect)
    # print(f'PLAYER WIDHT {player_life_width}')
    # SCREEN.blit(RED_LIFE_BAR, enemy_red_life_bar_rect)
    SCREEN.blit(text1, text1_rect)
    SCREEN.blit(text1_5, text1_5_rect)
    SCREEN.blit(text2, text2_rect)
    SCREEN.blit(text3, text3_rect)
    check_player_life()


def display_level_xp():
    level_text = get_regular_font(25).render(f"LEVEL: {player.level}", True, WHITE)
    level_rect = level_text.get_rect(midright=(1260, 600))
    next_level = str(player.level + 1)
    xp_text = get_regular_font(25).render(f"XP: {player.xp}/{levels.get(next_level)}", True, WHITE)
    xp_rect = xp_text.get_rect(midright=(1260, 630))
    life_text = get_regular_font(25).render(f"Life Points: {round(player.life)}/{player.total_life}", True, WHITE)
    life_rect = life_text.get_rect(midright=(1260, 660))
    SCREEN.blit(life_text, life_rect)
    SCREEN.blit(level_text, level_rect)
    SCREEN.blit(xp_text, xp_rect)


def display_delve_depth():
    level_text = get_regular_font(25).render(f"DEPTH: {Delve.depth}", True, WHITE)
    level_rect = level_text.get_rect(midright=(1260, 630))
    life_text = get_regular_font(25).render(f"Life Points: {player.life}/{player.total_life}", True, WHITE)
    life_rect = life_text.get_rect(midright=(1260, 660))
    SCREEN.blit(level_text, level_rect)
    SCREEN.blit(life_text, life_rect)


def encounter():
    global enemy, last_time_ms, counter
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
                        enemy_dict['image']

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
                      enemy_dict['image'])
    # level setter
    if enemy.level > player.level + 2:
        encounter()
    elif enemy.level < player.level - 1:
        encounter()
    else:
        if player.level == 5 and wiegraf1.status is True:
            enemy = wiegraf1
            boss_battle(wiegraf1)
        elif player.level == 10 and dycedarg1.status is True:
            enemy = dycedarg1
            boss_battle(dycedarg1)
        elif player.level == 15 and wiegraf2.status is True:
            enemy = wiegraf2
            boss_battle(wiegraf2)
        elif player.level == 20 and dycedarg2.status is True:
            enemy = dycedarg2
            boss_battle(dycedarg2)
        else:
            pass
    battle_elements_resetter()
    display_level_xp()
    # level_text = get_regular_font(25).render(f"LEVEL: {player.level}", True, WHITE)
    # level_rect = level_text.get_rect(midright=(1260, 630))
    # next_level = str(player.level + 1)
    # xp_text = get_regular_font(25).render(f"XP: {player.xp}/{levels.get(next_level)}", True, WHITE)
    # xp_rect = xp_text.get_rect(midright=(1260, 660))
    # SCREEN.blit(level_text, level_rect)
    # SCREEN.blit(xp_text, xp_rect)
    text1 = get_bold_font(35).render(f"You've encountered a level {enemy.level} {enemy.name}!", True, WHITE)
    text1_rect = text1.get_rect(center=(440, 100))
    SCREEN.blit(text1, text1_rect)
    while True:
        ENCOUNTER_MOUSE_POSITION = pygame.mouse.get_pos()
        BUTTONS = main_menu_structure(ENCOUNTER_MOUSE_POSITION)
        ATTACK = Button(image=pygame.image.load("assets/images/Next Rect.png"), pos=(600, 200),
                        text_input="ATTACK", font=get_bold_font(30), base_color="White", hovering_color=BLUE)
        RUN = Button(image=pygame.image.load("assets/images/Next Rect.png"), pos=(300, 200),
                     text_input="RUN", font=get_bold_font(30), base_color="White", hovering_color=BLUE)
        BUTTONS.extend([ATTACK, RUN])

        diff_time_ms = int(round(time.time() * 4000)) - last_time_ms
        if diff_time_ms >= 4000:
            counter = counter + 1
            last_time_ms = int(round(time.time() * 4000))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                main_menu_structure_events(ENCOUNTER_MOUSE_POSITION, BUTTONS)
                if ATTACK.checkForInput(ENCOUNTER_MOUSE_POSITION):
                    counter = 0
                    battle_elements_resetter()
                    battle()
                if RUN.checkForInput(ENCOUNTER_MOUSE_POSITION):
                    counter = 0
                    encounter()

        # if counter >= 2:
        for button in BUTTONS:
            button.changeColor(ENCOUNTER_MOUSE_POSITION)
            button.update(SCREEN)

        pygame.display.update()


def show_player_slot_helper(text1, level_text, type_text, life_text, attack_text, defense_text,
                            crit_chance_text, crit_damage_text, magic_find_text):
    text1_rect = text1.get_rect(midleft=(100, 160))
    level_text_rect = level_text.get_rect(midleft=(100, 200))
    type_text_rect = type_text.get_rect(midleft=(100, 260))
    life_text_rect = life_text.get_rect(midleft=(100, 300))
    attack_text_rect = attack_text.get_rect(midleft=(100, 340))
    defense_text_rect = defense_text.get_rect(midleft=(100, 380))
    crit_chance_text_rect = crit_chance_text.get_rect(midleft=(100, 420))
    crit_damage_text_rect = crit_damage_text.get_rect(midleft=(100, 460))
    magic_find_text_rect = magic_find_text.get_rect(midleft=(100, 500))
    SCREEN.blit(text1, text1_rect)
    SCREEN.blit(type_text, type_text_rect)
    SCREEN.blit(level_text, level_text_rect)
    SCREEN.blit(life_text, life_text_rect)
    SCREEN.blit(attack_text, attack_text_rect)
    SCREEN.blit(defense_text, defense_text_rect)
    SCREEN.blit(crit_chance_text, crit_chance_text_rect)
    SCREEN.blit(crit_damage_text, crit_damage_text_rect)
    SCREEN.blit(magic_find_text, magic_find_text_rect)


def show_player_slot(gear_type):
    if gear_type == 'amulet':
        text1 = get_bold_font(35).render(f"{player_slot.amulet['name']}", True, WHITE)
        level_text = get_regular_font(25).render(f"Level {player_slot.amulet['level']}", True, WHITE)
        type_text = get_bold_font(25).render(f"Type: {player_slot.amulet['type']}", True, WHITE)
        life_text = get_bold_font(25).render(f"Life: {player_slot.amulet['life']}", True, WHITE)
        attack_text = get_bold_font(25).render(f"Attack: {player_slot.amulet['attack']}", True, WHITE)
        defense_text = get_bold_font(25).render(f"Defense: {player_slot.amulet['defense']}", True, WHITE)
        crit_chance_text = get_bold_font(25).render(f"Critical Chance: {player_slot.amulet['crit_chance']} %", True,
                                                    WHITE)
        crit_damage_text = get_bold_font(25).render(f"Critical Damage: {player_slot.amulet['crit_damage']} %", True,
                                                    WHITE)
        magic_find_text = get_bold_font(25).render(f"Magic Find: {round(player_slot.amulet['magic_find'] * 100, 2)} %",
                                                   True, WHITE)
        show_player_slot_helper(text1, level_text, type_text, life_text, attack_text, defense_text,
                                crit_chance_text, crit_damage_text, magic_find_text)
    elif gear_type == 'armor':
        text1 = get_bold_font(35).render(f"{player_slot.armor['name']}", True, WHITE)
        level_text = get_regular_font(25).render(f"Level {player_slot.armor['level']}", True, WHITE)
        type_text = get_bold_font(25).render(f"Type: {player_slot.armor['type']}", True, WHITE)
        life_text = get_bold_font(25).render(f"Life: {player_slot.armor['life']}", True, WHITE)
        attack_text = get_bold_font(25).render(f"Attack: {player_slot.armor['attack']}", True, WHITE)
        defense_text = get_bold_font(25).render(f"Defense: {player_slot.armor['defense']}", True, WHITE)
        crit_chance_text = get_bold_font(25).render(f"Critical Chance: {player_slot.armor['crit_chance']} %", True,
                                                    WHITE)
        crit_damage_text = get_bold_font(25).render(f"Critical Damage: {player_slot.armor['crit_damage']} %", True,
                                                    WHITE)
        magic_find_text = get_bold_font(25).render(f"Magic Find: {round(player_slot.armor['magic_find'] * 100, 2)} %",
                                                   True, WHITE)
        show_player_slot_helper(text1, level_text, type_text, life_text, attack_text, defense_text,
                                crit_chance_text, crit_damage_text, magic_find_text)
    elif gear_type == 'second_hand':
        text1 = get_bold_font(35).render(f"{player_slot.second_hand['name']}", True, WHITE)
        level_text = get_regular_font(25).render(f"Level {player_slot.second_hand['level']}", True, WHITE)
        type_text = get_bold_font(25).render(f"Type: {player_slot.second_hand['type']}", True, WHITE)
        life_text = get_bold_font(25).render(f"Life: {player_slot.second_hand['life']}", True, WHITE)
        attack_text = get_bold_font(25).render(f"Attack: {player_slot.second_hand['attack']}", True, WHITE)
        defense_text = get_bold_font(25).render(f"Defense: {player_slot.second_hand['defense']}", True, WHITE)
        crit_chance_text = get_bold_font(25).render(f"Critical Chance: {player_slot.second_hand['crit_chance']} %",
                                                    True, WHITE)
        crit_damage_text = get_bold_font(25).render(f"Critical Damage: {player_slot.second_hand['crit_damage']} %",
                                                    True, WHITE)
        magic_find_text = get_bold_font(25).render(
            f"Magic Find: {round(player_slot.second_hand['magic_find'] * 100, 2)} %",
            True, WHITE)
        show_player_slot_helper(text1, level_text, type_text, life_text, attack_text, defense_text,
                                crit_chance_text, crit_damage_text, magic_find_text)
    elif gear_type == 'legs':
        text1 = get_bold_font(35).render(f"{player_slot.legs['name']}", True, WHITE)
        level_text = get_regular_font(25).render(f"Level {player_slot.legs['level']}", True, WHITE)
        type_text = get_bold_font(25).render(f"Type: {player_slot.legs['type']}", True, WHITE)
        life_text = get_bold_font(25).render(f"Life: {player_slot.legs['life']}", True, WHITE)
        attack_text = get_bold_font(25).render(f"Attack: {player_slot.legs['attack']}", True, WHITE)
        defense_text = get_bold_font(25).render(f"Defense: {player_slot.legs['defense']}", True, WHITE)
        crit_chance_text = get_bold_font(25).render(f"Critical Chance: {player_slot.legs['crit_chance']} %", True,
                                                    WHITE)
        crit_damage_text = get_bold_font(25).render(f"Critical Damage: {player_slot.legs['crit_damage']} %", True,
                                                    WHITE)
        magic_find_text = get_bold_font(25).render(f"Magic Find: {round(player_slot.legs['magic_find'] * 100, 2)} %",
                                                   True, WHITE)
        show_player_slot_helper(text1, level_text, type_text, life_text, attack_text, defense_text,
                                crit_chance_text, crit_damage_text, magic_find_text)
    elif gear_type == 'gloves':
        text1 = get_bold_font(35).render(f"{player_slot.gloves['name']}", True, WHITE)
        level_text = get_regular_font(25).render(f"Level {player_slot.gloves['level']}", True, WHITE)
        type_text = get_bold_font(25).render(f"Type: {player_slot.gloves['type']}", True, WHITE)
        life_text = get_bold_font(25).render(f"Life: {player_slot.gloves['life']}", True, WHITE)
        attack_text = get_bold_font(25).render(f"Attack: {player_slot.gloves['attack']}", True, WHITE)
        defense_text = get_bold_font(25).render(f"Defense: {player_slot.gloves['defense']}", True, WHITE)
        crit_chance_text = get_bold_font(25).render(f"Critical Chance: {player_slot.gloves['crit_chance']} %", True,
                                                    WHITE)
        crit_damage_text = get_bold_font(25).render(f"Critical Damage: {player_slot.gloves['crit_damage']} %", True,
                                                    WHITE)
        magic_find_text = get_bold_font(25).render(f"Magic Find: {round(player_slot.gloves['magic_find'] * 100, 2)} %",
                                                   True, WHITE)
        show_player_slot_helper(text1, level_text, type_text, life_text, attack_text, defense_text,
                                crit_chance_text, crit_damage_text, magic_find_text)
    elif gear_type == 'boots':
        text1 = get_bold_font(35).render(f"{player_slot.boots['name']}", True, WHITE)
        level_text = get_regular_font(25).render(f"Level {player_slot.boots['level']}", True, WHITE)
        type_text = get_bold_font(25).render(f"Type: {player_slot.boots['type']}", True, WHITE)
        life_text = get_bold_font(25).render(f"Life: {player_slot.boots['life']}", True, WHITE)
        attack_text = get_bold_font(25).render(f"Attack: {player_slot.boots['attack']}", True, WHITE)
        defense_text = get_bold_font(25).render(f"Defense: {player_slot.boots['defense']}", True, WHITE)
        crit_chance_text = get_bold_font(25).render(f"Critical Chance: {player_slot.boots['crit_chance']} %", True,
                                                    WHITE)
        crit_damage_text = get_bold_font(25).render(f"Critical Damage: {player_slot.boots['crit_damage']} %", True,
                                                    WHITE)
        magic_find_text = get_bold_font(25).render(f"Magic Find: {round(player_slot.boots['magic_find'] * 100, 2)} %",
                                                   True, WHITE)
        show_player_slot_helper(text1, level_text, type_text, life_text, attack_text, defense_text,
                                crit_chance_text, crit_damage_text, magic_find_text)
    elif gear_type == 'ring1':
        text1 = get_bold_font(35).render(f"{player_slot.ring1['name']}", True, WHITE)
        level_text = get_regular_font(25).render(f"Level {player_slot.ring1['level']}", True, WHITE)
        type_text = get_bold_font(25).render(f"Type: {player_slot.ring1['type']}", True, WHITE)
        life_text = get_bold_font(25).render(f"Life: {player_slot.ring1['life']}", True, WHITE)
        attack_text = get_bold_font(25).render(f"Attack: {player_slot.ring1['attack']}", True, WHITE)
        defense_text = get_bold_font(25).render(f"Defense: {player_slot.ring1['defense']}", True, WHITE)
        crit_chance_text = get_bold_font(25).render(f"Critical Chance: {player_slot.ring1['crit_chance']} %", True,
                                                    WHITE)
        crit_damage_text = get_bold_font(25).render(f"Critical Damage: {player_slot.ring1['crit_damage']} %", True,
                                                    WHITE)
        magic_find_text = get_bold_font(25).render(f"Magic Find: {round(player_slot.ring1['magic_find'] * 100, 2)} %",
                                                   True, WHITE)
        show_player_slot_helper(text1, level_text, type_text, life_text, attack_text, defense_text,
                                crit_chance_text, crit_damage_text, magic_find_text)

    elif gear_type == 'ring2':
        text1 = get_bold_font(35).render(f"{player_slot.ring2['name']}", True, WHITE)
        level_text = get_regular_font(25).render(f"Level {player_slot.ring2['level']}", True, WHITE)
        type_text = get_bold_font(25).render(f"Type: {player_slot.ring2['type']}", True, WHITE)
        life_text = get_bold_font(25).render(f"Life: {player_slot.ring2['life']}", True, WHITE)
        attack_text = get_bold_font(25).render(f"Attack: {player_slot.ring2['attack']}", True, WHITE)
        defense_text = get_bold_font(25).render(f"Defense: {player_slot.ring2['defense']}", True, WHITE)
        crit_chance_text = get_bold_font(25).render(f"Critical Chance: {player_slot.ring2['crit_chance']} %", True,
                                                    WHITE)
        crit_damage_text = get_bold_font(25).render(f"Critical Damage: {player_slot.ring2['crit_damage']} %", True,
                                                    WHITE)
        magic_find_text = get_bold_font(25).render(f"Magic Find: {round(player_slot.ring2['magic_find'] * 100, 2)} %",
                                                   True, WHITE)
        show_player_slot_helper(text1, level_text, type_text, life_text, attack_text, defense_text,
                                crit_chance_text, crit_damage_text, magic_find_text)
    elif gear_type == 'weapon':
        text1 = get_bold_font(35).render(f"{player_slot.weapon['name']}", True, WHITE)
        level_text = get_regular_font(25).render(f"Level {player_slot.weapon['level']}", True, WHITE)
        type_text = get_bold_font(25).render(f"Type: {player_slot.weapon['type']}", True, WHITE)
        life_text = get_bold_font(25).render(f"Life: {player_slot.weapon['life']}", True, WHITE)
        attack_text = get_bold_font(25).render(f"Attack: {player_slot.weapon['attack']}", True, WHITE)
        defense_text = get_bold_font(25).render(f"Defense: {player_slot.weapon['defense']}", True, WHITE)
        crit_chance_text = get_bold_font(25).render(f"Critical Chance: {player_slot.weapon['crit_chance']} %", True,
                                                    WHITE)
        crit_damage_text = get_bold_font(25).render(f"Critical Damage: {player_slot.weapon['crit_damage']} %", True,
                                                    WHITE)
        magic_find_text = get_bold_font(25).render(f"Magic Find: {round(player_slot.weapon['magic_find'] * 100, 2)} %",
                                                   True, WHITE)
        show_player_slot_helper(text1, level_text, type_text, life_text, attack_text, defense_text,
                                crit_chance_text, crit_damage_text, magic_find_text)

    elif gear_type == 'helmet':
        text1 = get_bold_font(35).render(f"{player_slot.helmet['name']}", True, WHITE)
        level_text = get_regular_font(25).render(f"Level {player_slot.helmet['level']}", True, WHITE)
        type_text = get_bold_font(25).render(f"Type: {player_slot.helmet['type']}", True, WHITE)
        life_text = get_bold_font(25).render(f"Life: {player_slot.helmet['life']}", True, WHITE)
        attack_text = get_bold_font(25).render(f"Attack: {player_slot.helmet['attack']}", True, WHITE)
        defense_text = get_bold_font(25).render(f"Defense: {player_slot.helmet['defense']}", True, WHITE)
        crit_chance_text = get_bold_font(25).render(f"Critical Chance: {player_slot.helmet['crit_chance']} %", True,
                                                    WHITE)
        crit_damage_text = get_bold_font(25).render(f"Critical Damage: {player_slot.helmet['crit_damage']} %", True,
                                                    WHITE)
        magic_find_text = get_bold_font(25).render(f"Magic Find: {round(player_slot.helmet['magic_find'] * 100, 2)} %",
                                                   True, WHITE)
        show_player_slot_helper(text1, level_text, type_text, life_text, attack_text, defense_text,
                                crit_chance_text, crit_damage_text, magic_find_text)


def player_status():
    global temp_gear_change, temp_gear_change_inventory

    temp_gear_change_inventory.clear()
    SCREEN.blit(BG, (0, 0))
    SCREEN.blit(BATTLE_BOX_LARGE, (60, 40))
    SCREEN.blit(PLAYER_STATUS_BOX, (80, 60))
    SCREEN.blit(PLAYER_STATUS, (SCREEN_WIDTH / 2 - 70, 180))

    # PLAYER STATUS
    next_level = str(player.level + 1)
    player_text1 = get_bold_font(35).render(f"PLAYER STATUS", True, WHITE)
    player_name_text = get_bold_font(25).render(f"Name: {player.name}", True, WHITE)
    player_level_text = get_bold_font(25).render(f"Level: {player.level}", True, WHITE)
    player_experience_text = get_bold_font(25).render(f"Experience: {player.xp}/{str(levels.get(next_level))[:6]}",
                                                      True, WHITE)
    player_life_text = get_bold_font(25).render(f"Life Points: {player.life}/{player.total_life}", True, WHITE)
    player_attack_text = get_bold_font(25).render(f"Attack: {player.attack}", True, WHITE)
    player_defense_text = get_bold_font(25).render(f"Defense: {player.defense}", True, WHITE)
    player_crit_chance_text = get_bold_font(25).render(f"Critical Chance: {round(player.crit_chance, 2)} %", True,
                                                       WHITE)
    player_crit_damage_text = get_bold_font(25).render(f"Critical Damage: {round(player.crit_damage, 2)} %", True,
                                                       WHITE)
    player_magic_find_text = get_bold_font(25).render(f"Magic Find: {round(player.magic_find * 100, 2)} %", True, WHITE)

    player_text1_rect = player_text1.get_rect(midleft=(900, 100))
    player_name_text_rect = player_name_text.get_rect(midleft=(900, 160))
    player_level_text_rect = player_level_text.get_rect(midleft=(900, 200))
    player_experience_text_rect = player_experience_text.get_rect(midleft=(900, 240))
    player_life_text_rect = player_life_text.get_rect(midleft=(900, 280))
    player_attack_text_rect = player_attack_text.get_rect(midleft=(900, 320))
    player_defense_text_rect = player_defense_text.get_rect(midleft=(900, 360))
    player_crit_chance_text_rect = player_crit_chance_text.get_rect(midleft=(900, 400))
    player_crit_damage_text_rect = player_crit_damage_text.get_rect(midleft=(900, 440))
    player_magic_find_text_rect = player_magic_find_text.get_rect(midleft=(900, 480))

    SCREEN.blit(player_text1, player_text1_rect)
    SCREEN.blit(player_name_text, player_name_text_rect)
    SCREEN.blit(player_level_text, player_level_text_rect)
    SCREEN.blit(player_experience_text, player_experience_text_rect)
    SCREEN.blit(player_life_text, player_life_text_rect)
    SCREEN.blit(player_attack_text, player_attack_text_rect)
    SCREEN.blit(player_defense_text, player_defense_text_rect)
    SCREEN.blit(player_crit_chance_text, player_crit_chance_text_rect)
    SCREEN.blit(player_crit_damage_text, player_crit_damage_text_rect)
    SCREEN.blit(player_magic_find_text, player_magic_find_text_rect)

    gear_slot = get_bold_font(35).render(f"GEAR SLOT", True, WHITE)
    gear_slot_rect = gear_slot.get_rect(midleft=(100, 100))
    SCREEN.blit(gear_slot, gear_slot_rect)

    # display_level_xp()
    #
    # weapon_setter = False
    # amulet_setter = False
    # armor_setter = False
    # gloves_setter = False
    # boots_setter = False
    # amulet_setter = False
    # helmet_setter = False
    # legs_setter = False
    # ring1_setter = False
    # ring2_setter = False
    # second_hand_setter = False

    # Status

    # Icones
    SCREEN.blit(WEAPON, (SCREEN_WIDTH / 2 - 170, 80))
    SCREEN.blit(HELMET, (SCREEN_WIDTH / 2 - 40, 80))
    SCREEN.blit(ARMOR, (SCREEN_WIDTH / 2 - 170, 230))
    SCREEN.blit(SHIELD, (SCREEN_WIDTH / 2 + 90, 80))
    SCREEN.blit(LEGS, (SCREEN_WIDTH / 2 + 90, 230))
    SCREEN.blit(GLOVES, (SCREEN_WIDTH / 2 - 170, 370))
    SCREEN.blit(BOOTS, (SCREEN_WIDTH / 2 + 90, 370))
    SCREEN.blit(RING, (SCREEN_WIDTH / 2 - 170, 520))
    SCREEN.blit(RING, (SCREEN_WIDTH / 2 + 90, 520))
    SCREEN.blit(AMULET, (SCREEN_WIDTH / 2 - 20, 520))

    weapon_rect = WEAPON.get_rect(center=(SCREEN_WIDTH / 2 - 140, 110))
    helmet_rect = HELMET.get_rect(center=(SCREEN_WIDTH / 2 - 10, 110))
    armor_rect = ARMOR.get_rect(center=(SCREEN_WIDTH / 2 - 140, 260))
    second_hand_rect = SHIELD.get_rect(center=(SCREEN_WIDTH / 2 + 120, 110))
    legs_rect = LEGS.get_rect(center=(SCREEN_WIDTH / 2 + 120, 260))
    gloves_rect = GLOVES.get_rect(center=(SCREEN_WIDTH / 2 - 140, 390))
    boots_rect = BOOTS.get_rect(center=(SCREEN_WIDTH / 2 + 120, 390))
    ring1_rect = RING.get_rect(center=(SCREEN_WIDTH / 2 - 140, 550))
    ring2_rect = RING.get_rect(center=(SCREEN_WIDTH / 2 + 120, 550))
    amulet_rect = AMULET.get_rect(center=(SCREEN_WIDTH / 2, 550))

    while True:
        PLAYER_STATUS_MOUSE_POSITION = pygame.mouse.get_pos()
        # BUTTONS = main_menu_structure(PLAYER_STATUS_MOUSE_POSITION)

        BACK = Button(image=pygame.image.load("assets/images/Smallest Rect.png"), pos=(1000, 600),
                      text_input="BACK", font=get_bold_font(30), base_color="White", hovering_color=BLUE)
        CHANGE = Button(image=pygame.image.load("assets/images/Smallest Rect.png"), pos=(230, 600),
                        text_input="CHANGE", font=get_bold_font(30), base_color="White", hovering_color=BLUE)

        # NO_BUTTON = Button(image=pygame.image.load("images/Smallest Rect.png"), pos=(380, 600),
        #                      text_input="NO", font=get_bold_font(30), base_color="White", hovering_color=BLUE)
        # YES_BUTTON = Button(image=pygame.image.load("images/Smallest Rect.png"), pos=(540, 600),
        #                     text_input="YES", font=get_bold_font(30), base_color="White", hovering_color=BLUE)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if BACK.checkForInput(PLAYER_STATUS_MOUSE_POSITION):
                    counter = 0
                    encounter()
                if CHANGE.checkForInput(PLAYER_STATUS_MOUSE_POSITION):
                    temp_gear_change_inventory.clear()
                    counter = 0
                    change_gear()
            if weapon_rect.collidepoint(PLAYER_STATUS_MOUSE_POSITION):
                SCREEN.blit(PLAYER_STATUS_BOX, (80, 60))
                SCREEN.blit(gear_slot, gear_slot_rect)
                temp_gear_change.clear()
                temp_gear_change.append(player_slot.weapon)
                show_player_slot('weapon')

            if amulet_rect.collidepoint(PLAYER_STATUS_MOUSE_POSITION):
                SCREEN.blit(PLAYER_STATUS_BOX, (80, 60))
                SCREEN.blit(gear_slot, gear_slot_rect)
                temp_gear_change.clear()
                temp_gear_change.append(player_slot.amulet)
                show_player_slot('amulet')

            if armor_rect.collidepoint(PLAYER_STATUS_MOUSE_POSITION):
                SCREEN.blit(PLAYER_STATUS_BOX, (80, 60))
                SCREEN.blit(gear_slot, gear_slot_rect)
                temp_gear_change.clear()
                temp_gear_change.append(player_slot.armor)
                show_player_slot('armor')

            if boots_rect.collidepoint(PLAYER_STATUS_MOUSE_POSITION):
                SCREEN.blit(PLAYER_STATUS_BOX, (80, 60))
                SCREEN.blit(gear_slot, gear_slot_rect)
                temp_gear_change.clear()
                temp_gear_change.append(player_slot.boots)
                show_player_slot('boots')

            if gloves_rect.collidepoint(PLAYER_STATUS_MOUSE_POSITION):
                SCREEN.blit(PLAYER_STATUS_BOX, (80, 60))
                SCREEN.blit(gear_slot, gear_slot_rect)
                temp_gear_change.clear()
                temp_gear_change.append(player_slot.gloves)
                show_player_slot('gloves')

            if helmet_rect.collidepoint(PLAYER_STATUS_MOUSE_POSITION):
                SCREEN.blit(PLAYER_STATUS_BOX, (80, 60))
                SCREEN.blit(gear_slot, gear_slot_rect)
                temp_gear_change.clear()
                temp_gear_change.append(player_slot.helmet)
                show_player_slot('helmet')

            if legs_rect.collidepoint(PLAYER_STATUS_MOUSE_POSITION):
                SCREEN.blit(PLAYER_STATUS_BOX, (80, 60))
                SCREEN.blit(gear_slot, gear_slot_rect)
                temp_gear_change.clear()
                temp_gear_change.append(player_slot.legs)
                show_player_slot('legs')

            if ring1_rect.collidepoint(PLAYER_STATUS_MOUSE_POSITION):
                SCREEN.blit(PLAYER_STATUS_BOX, (80, 60))
                SCREEN.blit(gear_slot, gear_slot_rect)
                temp_gear_change.clear()
                temp_gear_change.append(player_slot.ring1)
                show_player_slot('ring1')

            if ring2_rect.collidepoint(PLAYER_STATUS_MOUSE_POSITION):
                SCREEN.blit(PLAYER_STATUS_BOX, (80, 60))
                SCREEN.blit(gear_slot, gear_slot_rect)
                temp_gear_change.clear()
                temp_gear_change.append(player_slot.ring2)
                show_player_slot('ring2')

            if second_hand_rect.collidepoint(PLAYER_STATUS_MOUSE_POSITION):
                SCREEN.blit(PLAYER_STATUS_BOX, (80, 60))
                SCREEN.blit(gear_slot, gear_slot_rect)
                temp_gear_change.clear()
                temp_gear_change.append(player_slot.second_hand)
                show_player_slot('second_hand')

            for button in [BACK, CHANGE]:
                button.changeColor(PLAYER_STATUS_MOUSE_POSITION)
                button.update(SCREEN)
            pygame.display.update()

    # next_level = str(player.level + 1)
    # if int(next_level) > 20:
    #     next_level = str(20)
    # print('-' * DASH)
    # print(f"Name: {player.name}\t\t\t\t| Weapon: {player_slot.weapon['name']:<35} level {player_slot.weapon['level']}\n"
    #       f"Level: {player.level}\t\t\t\t\t| Helmet: {player_slot.helmet['name']:<35} level {player_slot.helmet['level']}\n"
    #       f"Experience: {player.xp}/{levels.get(next_level)}\t\t\t| Second-hand: {player_slot.second_hand['name']:<35} level {player_slot.second_hand['level']}\n"
    #       f"HP: {player.life}/{player.total_life}\t\t\t\t\t| Armor: {player_slot.armor['name']:<35} level {player_slot.armor['level']}\n"
    #       f"Attack: {player.attack}\t\t\t\t\t| Gloves: {player_slot.gloves['name']:<35} level {player_slot.gloves['level']}\n"
    #       f"Defense: {player.defense}\t\t\t\t| Legs: {player_slot.legs['name']:<35} level {player_slot.legs['level']}\n"
    #       f"Critical Chance: {player.crit_chance}%\t\t| Ring 1: {player_slot.ring1['name']:<35} level {player_slot.ring1['level']}\n"
    #       f"Critical Damage: {round(player.crit_damage, 1)}%\t\t| Ring 2: {player_slot.ring2['name']:<35} level {player_slot.ring2['level']}\n"
    #       f"Magic Find: {round((player.magic_find * 100), 1)}%\t\t\t| Amulet: {player_slot.amulet['name']:<35} level {player_slot.amulet['level']}\n"
    #       f"Delve Depth: {Delve.depth}\t\t\t\t| Boots: {player_slot.boots['name']:<35} level {player_slot.boots['level']}"
    #       )
    # print('-' * DASH)
    # input('Press any key to continue...')
    # load_data_menu()


def change_gear():
    global temp_gear_change, temp_gear_change_inventory

    item_index = 1
    SCREEN.blit(BG, (0, 0))
    SCREEN.blit(BATTLE_BOX, (60, 40))
    temp_iterable = []

    HEIGHT = 100
    sorted_inventory = sorted(inventory, key=lambda x: (x.level, x.type), reverse=True)
    iteration_rect = []
    column_a = 0
    for i in range(0, len(sorted_inventory)):
        if sorted_inventory[i].__dict__['type'] == temp_gear_change[0]['type']:
            text1 = get_bold_font(22).render(
                f"{item_index} — {sorted_inventory[i].__dict__['name']} (level {sorted_inventory[i].__dict__['level']})",
                True, WHITE)
            text1_rect = text1.get_rect(midleft=(100, HEIGHT))
            HEIGHT = HEIGHT + 23
            SCREEN.blit(text1, text1_rect)
            item_index = item_index + 1
            iteration_rect.append(text1_rect)
            temp_iterable.append(sorted_inventory[i].__dict__['name'])
            temp_gear_change_inventory.append(sorted_inventory[i])
            column_a = column_a + 1
        if column_a == 20:
            break
    HEIGHT2 = 100
    column_b = 0
    for i in range(20, len(sorted_inventory)):
        if sorted_inventory[i].__dict__['type'] == temp_gear_change[0]['type'] and sorted_inventory[i].__dict__[
            'name'] not in temp_iterable:
            text1 = get_bold_font(22).render(
                f"{item_index} — {sorted_inventory[i].__dict__['name']} (level {sorted_inventory[i].__dict__['level']})",
                True, WHITE)
            text1_rect = text1.get_rect(midleft=(550, HEIGHT2))
            HEIGHT2 = HEIGHT2 + 23
            SCREEN.blit(text1, text1_rect)
            item_index = item_index + 1
            iteration_rect.append(text1_rect)
            temp_gear_change_inventory.append(sorted_inventory[i])
            column_b = column_b + 1
        if column_b == 20:
            break
    temp_iterable.clear()

    while True:

        CHANGE_GEAR_MOUSE_POSITION = pygame.mouse.get_pos()
        BUTTONS = main_menu_structure(CHANGE_GEAR_MOUSE_POSITION)

        BACK = Button(image=pygame.image.load("assets/images/Smallest Rect.png"), pos=(180, 600),
                      text_input="BACK", font=get_bold_font(30), base_color="White", hovering_color=BLUE)
        BUTTONS.append(BACK)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                main_menu_structure_events(CHANGE_GEAR_MOUSE_POSITION, BUTTONS)
                if BACK.checkForInput(CHANGE_GEAR_MOUSE_POSITION):
                    player_status()
                    # if consumable_type == 1:
                    #     show_inventory_page_2(1)
                    # else:
                    #     print('page 2')
                    #     show_inventory_page_2(consumable_type)
                # if BACK.checkForInput(INVENTORY_MOUSE_POSITION):
                #     pass
                for i in range(len(iteration_rect)):
                    if iteration_rect[i].collidepoint(CHANGE_GEAR_MOUSE_POSITION):
                        show_item(i, temp_gear_change_inventory[i])

                # if iteration_rect[0].collidepoint(INVENTORY_MOUSE_POSITION):
                #     show_item(sorted_inventory[0])

                # if item_rect1.collidepoint(INVENTORY_MOUSE_POSITION):
                #     pygame.quit()
                #     sys.exit()

        # if counter >= 2:
        for button in BUTTONS:
            button.changeColor(CHANGE_GEAR_MOUSE_POSITION)
            button.update(SCREEN)

        pygame.display.update()


def extras():
    global counter
    SCREEN.blit(BG, (0, 0))
    SCREEN.blit(BATTLE_BOX, (60, 40))

    # Icon Imagens
    SCREEN.blit(CARDS, (150, 100))
    SCREEN.blit(ROULETTE_WHEEL2_TICKET, (250, 100))

    # Icon Texts
    cards_text = get_bold_font(20).render('CARDS', True, WHITE)
    cards_text_rect = cards_text.get_rect(center=(180, 180))
    SCREEN.blit(cards_text, cards_text_rect)

    roulette_text = get_bold_font(20).render('ROULETTE', True, WHITE)
    roulette_text_rect = roulette_text.get_rect(center=(280, 180))
    SCREEN.blit(roulette_text, roulette_text_rect)

    # Collision Points
    cards_rect = ICON_FRAME.get_rect(center=(180, 140))
    roulette_rect = ICON_FRAME.get_rect(center=(280, 140))

    while True:
        EXTRAS_MOUSE_POSITION = pygame.mouse.get_pos()
        BUTTONS = main_menu_structure(EXTRAS_MOUSE_POSITION)

        BACK = Button(image=pygame.image.load("assets/images/Smallest Rect.png"), pos=(770, 600),
                      text_input="NEXT", font=get_bold_font(30), base_color="White", hovering_color=BLUE)
        BUTTONS.append(BACK)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                main_menu_structure_events(EXTRAS_MOUSE_POSITION, BUTTONS)
                if BACK.checkForInput(EXTRAS_MOUSE_POSITION):
                    counter = 0
                    main_menu()
                if cards_rect.collidepoint(EXTRAS_MOUSE_POSITION):
                    cards()
                if roulette_rect.collidepoint(EXTRAS_MOUSE_POSITION):
                    roulette()
            if cards_rect.collidepoint(EXTRAS_MOUSE_POSITION):
                print('cards')
            if roulette_rect.collidepoint(EXTRAS_MOUSE_POSITION):
                print('roulette')

            for button in BUTTONS:
                button.changeColor(EXTRAS_MOUSE_POSITION)
                button.update(SCREEN)

            pygame.display.update()


def cards():
    global counter, last_time_ms

    SCREEN.blit(BG, (0, 0))
    SCREEN.blit(BATTLE_BOX_LARGE, (60, 40))
    # SCREEN.blit(PLAYER_STATUS_BOX, (80, 60))

    # Card Images
    # inventory_cards = [value for elem in cards_list for value in elem.__dict__.values()]
    # if drop['name'] in inventory_cards:
    setter = 0
    width = 100
    height = 100

    while setter < 3:
        for card in range(0, 6):
            SCREEN.blit(SQUIRE_CARD_FRAME, (width, height))
            width += 130
        height += 200
        width = 100
        setter += 1
    SCREEN.blit(SQUIRE_CARD, (940, 100))



    # SCREEN.blit(SQUIRE_CARD, (250, 100))

    while True:
        CARDS_MOUSE_POSITION = pygame.mouse.get_pos()
        # BUTTONS = main_menu_structure(PLAYER_STATUS_MOUSE_POSITION)

        BACK = Button(image=pygame.image.load("assets/images/Smallest Rect.png"), pos=(1110, 610),
                      text_input="BACK", font=get_bold_font(30), base_color="White", hovering_color=BLUE)

        # NO_BUTTON = Button(image=pygame.image.load("images/Smallest Rect.png"), pos=(380, 600),
        #                      text_input="NO", font=get_bold_font(30), base_color="White", hovering_color=BLUE)
        # YES_BUTTON = Button(image=pygame.image.load("images/Smallest Rect.png"), pos=(540, 600),
        #                     text_input="YES", font=get_bold_font(30), base_color="White", hovering_color=BLUE)

        diff_time_ms = int(round(time.time() * 4000)) - last_time_ms

        if diff_time_ms >= 4000:
            counter = counter + 1
            last_time_ms = int(round(time.time() * 4000))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if BACK.checkForInput(CARDS_MOUSE_POSITION):
                    counter = 0
                    extras()
            for button in [BACK]:
                button.changeColor(CARDS_MOUSE_POSITION)
                button.update(SCREEN)
        pygame.display.update()


def roulette():
    global counter, last_time_ms, click_blocking

    SCREEN.blit(BG, (0, 0))
    SCREEN.blit(BATTLE_BOX_LARGE, (60, 40))
    SCREEN.blit(PLAYER_STATUS_BOX, (80, 60))
    SCREEN.blit(ROULETTE_WHEEL2, (SCREEN_WIDTH / 2.5, 100))
    SCREEN.blit(ROULETTE_WHEEL2_ARROW, (SCREEN_WIDTH / 2.5 + 230, 48))

    text1 = get_bold_font(40).render('Roulette Wheel', True, WHITE)
    text2 = get_regular_font(30).render('Feeling lucky?', True, WHITE)
    text3 = get_regular_font(25).render('Sping the wheel of good fortune', True, WHITE)
    text4 = get_regular_font(25).render('and receive powerful items!', True, WHITE)
    text5 = get_bold_font(30).render(f'x {roulette_wheel_ticket.quantity}', True, WHITE)
    WIDTH = SCREEN_WIDTH / 5
    text1_rect = text1.get_rect(center=(WIDTH, 100))
    text2_rect = text2.get_rect(center=(WIDTH, 140))
    text3_rect = text3.get_rect(center=(WIDTH, 200))
    text4_rect = text4.get_rect(center=(WIDTH, 230))
    text5_rect = text5.get_rect(center=(WIDTH + 30, 300))

    SCREEN.blit(text1, text1_rect)
    SCREEN.blit(text2, text2_rect)
    SCREEN.blit(text3, text3_rect)
    SCREEN.blit(text4, text4_rect)
    SCREEN.blit(text5, text5_rect)
    SCREEN.blit(ROULETTE_WHEEL2_TICKET, (WIDTH - 60, 270))

    angle = 0
    roulette_index = 0
    roll = True
    setter = random.randrange(360, 720, 10)
    # PLAYER STATUS
    slice = 360 / 19

    while True:
        HELP_MOUSE_POSITION = pygame.mouse.get_pos()
        # BUTTONS = main_menu_structure(PLAYER_STATUS_MOUSE_POSITION)
        SPIN = Button(image=pygame.image.load("assets/images/Smallest Rect.png"), pos=(WIDTH, 380),
                      text_input="SPIN", font=get_bold_font(30), base_color="White", hovering_color=BLUE)

        BACK = Button(image=pygame.image.load("assets/images/Smallest Rect.png"), pos=(1110, 610),
                      text_input="BACK", font=get_bold_font(30), base_color="White", hovering_color=BLUE)

        # NO_BUTTON = Button(image=pygame.image.load("images/Smallest Rect.png"), pos=(380, 600),
        #                      text_input="NO", font=get_bold_font(30), base_color="White", hovering_color=BLUE)
        # YES_BUTTON = Button(image=pygame.image.load("images/Smallest Rect.png"), pos=(540, 600),
        #                     text_input="YES", font=get_bold_font(30), base_color="White", hovering_color=BLUE)

        diff_time_ms = int(round(time.time() * 4000)) - last_time_ms

        if diff_time_ms >= 4000:
            counter = counter + 1
            last_time_ms = int(round(time.time() * 4000))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if BACK.checkForInput(HELP_MOUSE_POSITION):
                    counter = 0
                    main_menu()
                if SPIN.checkForInput(HELP_MOUSE_POSITION):
                    while click_blocking:
                        if roulette_wheel_ticket.quantity > 0:
                            roulette_wheel_ticket.quantity = roulette_wheel_ticket.quantity + - 1
                            roll = True
                            click_blocking = False
                            while roll:
                                SCREEN.blit(BG, (0, 0))
                                SCREEN.blit(BATTLE_BOX_LARGE, (60, 40))
                                SCREEN.blit(PLAYER_STATUS_BOX, (80, 60))

                                text1 = get_bold_font(40).render('Roulette Wheel', True, WHITE)
                                text2 = get_regular_font(30).render('Feeling lucky?', True, WHITE)
                                text3 = get_regular_font(25).render('Sping the wheel of good fortune', True, WHITE)
                                text4 = get_regular_font(25).render('and receive powerful items!', True, WHITE)
                                text5 = get_bold_font(30).render(f'x {roulette_wheel_ticket.quantity}', True, WHITE)
                                WIDTH = SCREEN_WIDTH / 5
                                text1_rect = text1.get_rect(center=(WIDTH, 100))
                                text2_rect = text2.get_rect(center=(WIDTH, 140))
                                text3_rect = text3.get_rect(center=(WIDTH, 200))
                                text4_rect = text4.get_rect(center=(WIDTH, 230))
                                text5_rect = text5.get_rect(center=(WIDTH + 30, 300))

                                SCREEN.blit(text1, text1_rect)
                                SCREEN.blit(text2, text2_rect)
                                SCREEN.blit(text3, text3_rect)
                                SCREEN.blit(text4, text4_rect)
                                SCREEN.blit(text5, text5_rect)
                                SCREEN.blit(ROULETTE_WHEEL2_TICKET, (WIDTH - 60, 270))

                                rotate_image = pygame.transform.rotate(ROULETTE_WHEEL2, angle)
                                rect = rotate_image.get_rect()
                                pos = (((SCREEN_WIDTH - rect.width) / 2 + 130), ((SCREEN_HEIGHT - rect.height) / 2))
                                SCREEN.blit(rotate_image, pos)
                                SCREEN.blit(ROULETTE_WHEEL2_ARROW, (SCREEN_WIDTH / 2 + 110, 55))
                                pygame.display.flip()
                                angle -= 10
                                # setter = 720
                                if setter == 720:
                                    setter = 710
                                elif setter == 360:
                                    setter = 350
                                if abs(angle) == setter:
                                    roulette_index = math.floor((setter - 360) / slice)
                                    print(f'slice = {slice}')
                                    print(f'setter = {setter}')
                                    print(f'setter - 360 = {setter - 360}')
                                    print(f'index = {roulette_index}')
                                    print(ROULETTE_WHEEL_LIST2[roulette_index])
                                    counter = 0
                                    save_state()
                                    roll = False

        if counter >= 1 and not roll:
            roulette_outcome(ROULETTE_WHEEL_LIST2[roulette_index])

        if roll is True:
            for button in [SPIN, BACK]:
                button.changeColor(HELP_MOUSE_POSITION)
                button.update(SCREEN)
        pygame.display.update()


def roulette_outcome(index):
    global counter, last_time_ms, click_blocking

    reward = ''
    setter = True
    SCREEN.blit(BG, (0, 0))
    SCREEN.blit(BATTLE_BOX_LARGE, (60, 40))
    # SCREEN.blit(pygame.transform.rotate(ROULETTE_WHEEL2, angle), (position))
    print(type(index))
    print(index)
    if index == 19:
        mirror_of_kalandra.quantity += 1
        reward = 'Mirror of Kalandra'
    if index == 18:
        exalted_orb.quantity += 1
        reward = 'Exalted Orb'
    if index == 17:
        elixir.quantity += 1
        reward = 'Elixir'
    if index == 16:
        divine_orb.quantity += 1
        reward = 'Divine Orb'
    if index == 15:
        elixir.quantity += 1
        reward = 'Elixir'
    if index == 14:
        deft_fossil.quantity += 1
        reward = 'Deft Fossil'
    if index == 13:
        elixir.quantity += 1
        reward = 'Elixir'
    if index == 12:
        pristine_fossil.quantity += 1
        reward = 'Pristine Fossil'
    if index == 11:
        elixir.quantity += 1
        reward = 'Elixir'
    if index == 10:
        chaos_orb.quantity += 1
        reward = 'Chaos Orb'
    if index == 9:
        elixir.quantity += 1
        reward = 'Elixir'
    if index == 8:
        serrated_fossil.quantity += 1
        reward = 'Serrated Fossil'
    if index == 7:
        elixir.quantity += 1
        reward = 'Elixir'
    if index == 6:
        divine_orb.quantity += 1
        reward = 'Divine Orb'
    if index == 5:
        elixir.quantity += 1
        reward = 'Elixir'
    if index == 4:
        dense_fossil.quantity += 1
        reward = 'Dense Fossil'
    if index == 3:
        elixir.quantity += 1
        reward = 'Elixir'
    if index == 2:
        chaos_orb.quantity += 1
        reward = 'Chaos Orb'
    if index == 1:
        drop = random.choice(uniques)
        inventory_uniques = [value for elem in inventory for value in elem.__dict__.values()]
        print(drop)
        print(inventory_uniques)
        input('aqui')
        if drop['name'] in inventory_uniques:
            if drop['name'] in uniques_list:
                elixir.quantity += 1
                reward = 'Elixir'
            else:
                elixir.quantity += 1
                reward = 'Elixir'
        else:
            uniques_list.append(drop['name'])
            reward = drop['name']
            new_item = Unique(drop['type'],
                              drop['name'],
                              drop['level'],
                              drop['life'],
                              drop['attack'],
                              drop['defense'],
                              drop['crit_chance'],
                              drop['crit_damage'],
                              drop['magic_find'],
                              drop['rarity'],
                              )
            inventory.append(new_item)
            db.execute("INSERT INTO uniques_list (username, name) VALUES (:username, :name)",
                       username=player.name, name=drop['name'])
            inventory_update(player.name, new_item)
            temp_unique_drop.append(new_item)

    save_state()

    outcome = get_bold_font(40).render(f"You received 1x {reward}!", True, YELLOW)
    outcome_rect = outcome.get_rect(center=(SCREEN_WIDTH / 2, 260))

    while True:
        ROULETTE_OUTCOME_MOUSE_POSITION = pygame.mouse.get_pos()
        # BUTTONS = main_menu_structure(PLAYER_STATUS_MOUSE_POSITION)

        CONTINUE = Button(image=pygame.image.load("assets/images/Smallest Rect.png"), pos=(SCREEN_WIDTH / 2, 360),
                          text_input="CONTINUE", font=get_bold_font(30), base_color="White", hovering_color=BLUE)

        # NO_BUTTON = Button(image=pygame.image.load("images/Smallest Rect.png"), pos=(380, 600),
        #                      text_input="NO", font=get_bold_font(30), base_color="White", hovering_color=BLUE)
        # YES_BUTTON = Button(image=pygame.image.load("images/Smallest Rect.png"), pos=(540, 600),
        #                     text_input="YES", font=get_bold_font(30), base_color="White", hovering_color=BLUE)

        diff_time_ms = int(round(time.time() * 4000)) - last_time_ms

        if diff_time_ms >= 4000:
            counter = counter + 1
            last_time_ms = int(round(time.time() * 4000))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if CONTINUE.checkForInput(ROULETTE_OUTCOME_MOUSE_POSITION):
                    counter = 0
                    click_blocking = True
                    roulette()

        if counter >= 0:
            if setter:
                consumable_drop_sound()
                SCREEN.blit(outcome, outcome_rect)
                setter = False
        if counter >= 2:
            for button in [CONTINUE]:
                button.changeColor(ROULETTE_OUTCOME_MOUSE_POSITION)
                button.update(SCREEN)
        pygame.display.update()


def inventory_update(username, item):
    if len(inventory) == 0:
        pass
    else:

        db.execute(
            "INSERT INTO inventory (username, name, type, level, life, attack, defense, crit_chance,"
            "crit_damage, magic_find, rarity) VALUES (:username, :name, :type, :level, :life, :attack, :defense,"
            ":crit_chance, :crit_damage, :magic_find, :rarity)",
            username=username, name=item.name, type=item.type,
            level=item.level, life=item.life,
            attack=item.attack, defense=item.defense,
            crit_chance=item.crit_chance, crit_damage=item.crit_damage, magic_find=item.magic_find, rarity=item.rarity)


# def card_update(username, card):
#     if len(inventory) == 0:
#         pass
#     else:
#
#         db.execute(
#             "INSERT INTO cards_list (username, type, name, status, image, sound)"
#             "VALUES (:username, :type, :name, :status, :image, :sound)",
#             username=username, type=card.type, name=card.name,
#             status=card.status, image=card.image, sound=card.sound)


def inventory_removal(username, item):
    if len(inventory) == 0:
        pass
    else:

        db.execute(
            "DELETE FROM inventory WHERE username= :username and name = :name",
            username=username, name=item.name)


def save_state():
    username = player.name
    # Player status
    db.execute(
        "UPDATE user_data SET level = :level, experience = :experience, total_life = :total_life, life = :life, attack = :attack, defense = :defense, shaman = :shaman, crit_chance = :crit_chance, crit_damage = :crit_damage, magic_find = :magic_find  WHERE username = :username",
        level=player.level, experience=player.xp, total_life=player.total_life, life=player.life,
        attack=player.attack, defense=player.defense, shaman=player.shaman,
        crit_chance=player.crit_chance, crit_damage=player.crit_damage, magic_find=player.magic_find,
        username=username)

    # Player_Slot
    db.execute("DELETE FROM amulet WHERE username = :username",
               username=username)
    db.execute(
        "INSERT INTO amulet (username, name, type, level, life, attack, defense, crit_chance, crit_damage, magic_find, rarity) VALUES (:username, :name, :type, :level, :life, :attack, :defense, :crit_chance, :crit_damage, :magic_find, :rarity)",
        username=player.name, name=player_slot.amulet['name'], type=player_slot.amulet['type'],
        level=player_slot.amulet['level'], life=player_slot.amulet['life'],
        attack=player_slot.amulet['attack'], defense=player_slot.amulet['defense'],
        crit_chance=player_slot.amulet['crit_chance'], crit_damage=player_slot.amulet['crit_damage'],
        magic_find=player_slot.amulet['magic_find'], rarity=player_slot.amulet['rarity'])
    db.execute("DELETE FROM armor WHERE username = :username",
               username=username)
    db.execute(
        "INSERT INTO armor (username, name, type, level, life, attack, defense, crit_chance, crit_damage, magic_find, rarity) VALUES (:username, :name, :type, :level, :life, :attack, :defense, :crit_chance, :crit_damage, :magic_find, :rarity)",
        username=player.name, name=player_slot.armor['name'], type=player_slot.armor['type'],
        level=player_slot.armor['level'], life=player_slot.armor['life'],
        attack=player_slot.armor['attack'], defense=player_slot.armor['defense'],
        crit_chance=player_slot.armor['crit_chance'], crit_damage=player_slot.armor['crit_damage'],
        magic_find=player_slot.armor['magic_find'], rarity=player_slot.armor['rarity'])
    db.execute("DELETE FROM gloves WHERE username = :username",
               username=username)
    db.execute(
        "INSERT INTO gloves (username, name, type, level, life, attack, defense, crit_chance, crit_damage, magic_find, rarity) VALUES (:username, :name, :type, :level, :life, :attack, :defense, :crit_chance, :crit_damage, :magic_find, :rarity)",
        username=player.name, name=player_slot.gloves['name'], type=player_slot.gloves['type'],
        level=player_slot.gloves['level'], life=player_slot.gloves['life'],
        attack=player_slot.gloves['attack'], defense=player_slot.gloves['defense'],
        crit_chance=player_slot.gloves['crit_chance'], crit_damage=player_slot.gloves['crit_damage'],
        magic_find=player_slot.gloves['magic_find'], rarity=player_slot.gloves['rarity'])
    db.execute("DELETE FROM helmet WHERE username = :username",
               username=username)
    db.execute(
        "INSERT INTO helmet (username, name, type, level, life, attack, defense, crit_chance, crit_damage, magic_find, rarity) VALUES (:username, :name, :type, :level, :life, :attack, :defense, :crit_chance, :crit_damage, :magic_find, :rarity)",
        username=player.name, name=player_slot.helmet['name'], type=player_slot.helmet['type'],
        level=player_slot.helmet['level'], life=player_slot.helmet['life'],
        attack=player_slot.helmet['attack'], defense=player_slot.helmet['defense'],
        crit_chance=player_slot.helmet['crit_chance'], crit_damage=player_slot.helmet['crit_damage'],
        magic_find=player_slot.helmet['magic_find'], rarity=player_slot.helmet['rarity'])
    db.execute("DELETE FROM legs WHERE username = :username",
               username=username)
    db.execute(
        "INSERT INTO legs (username, name, type, level, life, attack, defense, crit_chance, crit_damage, magic_find, rarity) VALUES (:username, :name, :type, :level, :life, :attack, :defense, :crit_chance, :crit_damage, :magic_find, :rarity)",
        username=player.name, name=player_slot.legs['name'], type=player_slot.legs['type'],
        level=player_slot.legs['level'], life=player_slot.legs['life'],
        attack=player_slot.legs['attack'], defense=player_slot.legs['defense'],
        crit_chance=player_slot.legs['crit_chance'], crit_damage=player_slot.legs['crit_damage'],
        magic_find=player_slot.legs['magic_find'], rarity=player_slot.legs['rarity'])
    db.execute("DELETE FROM ring1 WHERE username = :username",
               username=username)
    db.execute(
        "INSERT INTO ring1 (username, name, type, level, life, attack, defense, crit_chance, crit_damage, magic_find, rarity) VALUES (:username, :name, :type, :level, :life, :attack, :defense, :crit_chance, :crit_damage, :magic_find, :rarity)",
        username=player.name, name=player_slot.ring1['name'], type=player_slot.ring1['type'],
        level=player_slot.ring1['level'], life=player_slot.ring1['life'],
        attack=player_slot.ring1['attack'], defense=player_slot.ring1['defense'],
        crit_chance=player_slot.ring1['crit_chance'], crit_damage=player_slot.ring1['crit_damage'],
        magic_find=player_slot.ring1['magic_find'], rarity=player_slot.ring1['rarity'])
    db.execute("DELETE FROM ring2 WHERE username = :username",
               username=username)
    db.execute(
        "INSERT INTO ring2 (username, name, type, level, life, attack, defense, crit_chance, crit_damage, magic_find, rarity) VALUES (:username, :name, :type, :level, :life, :attack, :defense, :crit_chance, :crit_damage, :magic_find, :rarity)",
        username=player.name, name=player_slot.ring2['name'], type=player_slot.ring2['type'],
        level=player_slot.ring2['level'], life=player_slot.ring2['life'],
        attack=player_slot.ring2['attack'], defense=player_slot.ring2['defense'],
        crit_chance=player_slot.ring2['crit_chance'], crit_damage=player_slot.ring2['crit_damage'],
        magic_find=player_slot.ring2['magic_find'], rarity=player_slot.ring2['rarity'])
    db.execute("DELETE FROM second_hand WHERE username = :username",
               username=username)
    db.execute(
        "INSERT INTO second_hand (username, name, type, level, life, attack, defense, crit_chance, crit_damage, magic_find, rarity) VALUES (:username, :name, :type, :level, :life, :attack, :defense, :crit_chance, :crit_damage, :magic_find, :rarity)",
        username=player.name, name=player_slot.second_hand['name'], type=player_slot.second_hand['type'],
        level=player_slot.second_hand['level'], life=player_slot.second_hand['life'],
        attack=player_slot.second_hand['attack'], defense=player_slot.second_hand['defense'],
        crit_chance=player_slot.second_hand['crit_chance'], crit_damage=player_slot.second_hand['crit_damage'],
        magic_find=player_slot.second_hand['magic_find'], rarity=player_slot.second_hand['rarity'])
    db.execute("DELETE FROM weapon WHERE username = :username",
               username=username)
    db.execute(
        "INSERT INTO weapon (username, name, type, level, life, attack, defense, crit_chance, crit_damage, magic_find, rarity) VALUES (:username, :name, :type, :level, :life, :attack, :defense, :crit_chance, :crit_damage, :magic_find, :rarity)",
        username=player.name, name=player_slot.weapon['name'], type=player_slot.weapon['type'],
        level=player_slot.weapon['level'], life=player_slot.weapon['life'],
        attack=player_slot.weapon['attack'], defense=player_slot.weapon['defense'],
        crit_chance=player_slot.weapon['crit_chance'], crit_damage=player_slot.weapon['crit_damage'],
        magic_find=player_slot.weapon['magic_find'], rarity=player_slot.weapon['rarity'])
    db.execute("DELETE FROM boots WHERE username = :username",
               username=username)
    db.execute(
        "INSERT INTO boots (username, name, type, level, life, attack, defense, crit_chance, crit_damage, magic_find, rarity) VALUES (:username, :name, :type, :level, :life, :attack, :defense, :crit_chance, :crit_damage, :magic_find, :rarity)",
        username=player.name, name=player_slot.boots['name'], type=player_slot.boots['type'],
        level=player_slot.boots['level'], life=player_slot.boots['life'],
        attack=player_slot.boots['attack'], defense=player_slot.boots['defense'],
        crit_chance=player_slot.boots['crit_chance'], crit_damage=player_slot.boots['crit_damage'],
        magic_find=player_slot.boots['magic_find'], rarity=player_slot.boots['rarity'])

    # Consumables
    db.execute("UPDATE potion SET quantity = :quantity WHERE username = :username", quantity=potion.quantity,
               username=username)
    db.execute("UPDATE x_potion SET quantity = :quantity WHERE username = :username", quantity=x_potion.quantity,
               username=username)
    db.execute("UPDATE elixir SET quantity = :quantity WHERE username = :username", quantity=elixir.quantity,
               username=username)
    db.execute("UPDATE chaos_orb SET quantity = :quantity WHERE username = :username", quantity=chaos_orb.quantity,
               username=username)
    db.execute("UPDATE divine_orb SET quantity = :quantity WHERE username = :username", quantity=divine_orb.quantity,
               username=username)
    db.execute("UPDATE exalted_orb SET quantity = :quantity WHERE username = :username", quantity=exalted_orb.quantity,
               username=username)
    db.execute("UPDATE mirror_of_kalandra SET quantity = :quantity WHERE username = :username",
               quantity=mirror_of_kalandra.quantity, username=username)
    db.execute("UPDATE roulette_wheel_ticket SET quantity = :quantity WHERE username = :username",
               quantity=roulette_wheel_ticket.quantity, username=username)
    db.execute("UPDATE dense_fossil SET quantity = :quantity WHERE username = :username",
               quantity=dense_fossil.quantity, username=username)
    db.execute("UPDATE serrated_fossil SET quantity = :quantity WHERE username = :username",
               quantity=serrated_fossil.quantity, username=username)
    db.execute("UPDATE pristine_fossil SET quantity = :quantity WHERE username = :username",
               quantity=pristine_fossil.quantity, username=username)
    db.execute("UPDATE deft_fossil SET quantity = :quantity WHERE username = :username",
               quantity=deft_fossil.quantity, username=username)
    db.execute("UPDATE fractured_fossil SET quantity = :quantity WHERE username = :username",
               quantity=fractured_fossil.quantity, username=username)


# def quantity_checker(row_name, instance_attribute, row_zero_attribute):
#
#     if len(row_name) == 0:
#         pass
#     else:
#         instance_attribute = row_zero_attribute


# def card_drop_rate():
#     card_drop_value = random.randint(0, 100)
#
#     if len(list(set(cards_list))) >= 3:
#         pass
#     else:
#         if card_drop_value <= CARD_DROP_RATE + (CARD_DROP_RATE * player.magic_find):
#             drop = random.choice(card_collection)
#             temp_card_drop.append(drop)
#             inventory_cards = [value for elem in cards_list for value in elem.__dict__.values()]
#             if drop['name'] in inventory_cards:
#                 print(f"{drop['name']} já tem")
#                 card_drop_rate()
#             else:
#                 print('add new')
#                 Card.add_card(player.name, drop)




def delve_drop_rate(hoard):
    global drop_quantity

    choice = random.randint(0, 100)
    quantity = random.randint(0, 100)


    if quantity >= 95:
        drop_quantity += 2
    elif 75 <= quantity < 95:
        drop_quantity += 1
    else:
        pass
    if choice >= DELVE_DROP_RATE + (DELVE_DROP_RATE * player.magic_find):
        print(choice)
        pass
    else:
        monster = random.choice(hoard)
        print('entrou aqui 1')
        if monster.delve_drop['name'] == 'Dense Fossil':
            dense_fossil.quantity = dense_fossil.quantity + drop_quantity
            print('entrou aqui 2')
            return monster.delve_drop['name']
        elif monster.delve_drop['name'] == 'Serrated Fossil':
            serrated_fossil.quantity = serrated_fossil.quantity + drop_quantity
            print('entrou aqui 3')
            return monster.delve_drop['name']
        elif monster.delve_drop['name'] == 'Pristine Fossil':
            pristine_fossil.quantity = pristine_fossil.quantity + drop_quantity
            print('entrou aqui 4')
            return monster.delve_drop['name']
        elif monster.delve_drop['name'] == 'Pristine Fossil':
            pristine_fossil.quantity = pristine_fossil.quantity + drop_quantity
            print('entrou aqui 5')
            return monster.delve_drop['name']
        elif monster.delve_drop['name'] == 'Deft Fossil':
            deft_fossil.quantity = deft_fossil.quantity + drop_quantity
            print('entrou aqui 6')
            return monster.delve_drop['name']
        elif monster.delve_drop['name'] == 'Fractured Fossil':
            fractured_fossil.quantity = fractured_fossil.quantity + drop_quantity
            print('entrou aqui 7')
            return monster.delve_drop['name']
        else:
            print('entrou aqui 8')
            pass


def delve_battle_elements_resetter(biome, hoard, i):
    SCREEN.blit(biome, (0, 0))
    # SCREEN.blit(BATTLE_BOX, (60, 40))
    # PLAYER
    SCREEN.blit(player.image, (SCREEN_WIDTH / 2 - 400, 300))
    # ENEMY
    if hoard[i].life > 0:
        image_rect = pygame.image.load(hoard[i].image).get_rect(midbottom=(900, 485))
        SCREEN.blit(pygame.image.load(hoard[i].image), image_rect)

    # CONVERTION
    player_ratio = player.life / player.total_life
    player_life_width = 200 * player_ratio

    hoard_ratio = hoard[i].life / hoard[i].total_life
    hoard_life_width = 200 * hoard_ratio

    text1 = get_regular_font(20).render(f"{player.life}/{player.total_life}", True, WHITE)
    text1_rect = text1.get_rect(center=(SCREEN_WIDTH / 2 - 350, 540))
    text1_5 = get_bold_font(20).render(f"{player.name}", True, WHITE)
    text1_5_rect = text1_5.get_rect(center=(SCREEN_WIDTH / 2 - 350, 565))
    text2 = get_regular_font(20).render(f"{hoard[i].life}/{hoard[i].total_life}", True, WHITE)
    text2_rect = text2.get_rect(center=(SCREEN_WIDTH / 2 + 270, 540))
    text3 = get_bold_font(20).render(f"{hoard[i].name}", True, WHITE)
    text3_rect = text3.get_rect(center=(SCREEN_WIDTH / 2 + 270, 565))
    player_life_bar_rect = pygame.Rect(SCREEN_WIDTH / 2 - 450, 500, 200, 20)  # left/ top / widht / height
    hoard_life_bar_rect = pygame.Rect(SCREEN_WIDTH / 2 + 170, 500, 200, 20)  # left/ top / widht / height
    player_red_life_bar_rect = pygame.Rect(SCREEN_WIDTH / 2 - 450, 500, player_life_width,
                                           20)  # left/ top / widht / height
    hoard_red_life_bar_rect = pygame.Rect(SCREEN_WIDTH / 2 + 170, 500, hoard_life_width, 20)
    pygame.draw.rect(pygame.display.get_surface(), DARK_GREY, player_life_bar_rect)
    pygame.draw.rect(pygame.display.get_surface(), BLUE, player_red_life_bar_rect)
    pygame.draw.rect(pygame.display.get_surface(), DARK_GREY, hoard_life_bar_rect)
    pygame.draw.rect(pygame.display.get_surface(), BLUE, hoard_red_life_bar_rect)
    SCREEN.blit(text1, text1_rect)
    SCREEN.blit(text1_5, text1_5_rect)
    SCREEN.blit(text2, text2_rect)
    SCREEN.blit(text3, text3_rect)
    check_player_life()


def delve_battle(biome, hoard):
    global counter
    for i in range(0, len(hoard)):
        while hoard[i].life > 0:
            # life_bars()
            delve_battle_elements_resetter(biome, hoard, i)
            print(f'enemy = {hoard[i].name}')

            # IF hoard[i] ATTACK IS ZERO
            if hoard[i].attack <= player.defense:
                delve_battle_condition_1(biome, hoard, i)

            # # IF hoard[i] ATTACK IS NOT ZERO
            else:
                print('aqui 4')
                a = crit_chance(player.crit_chance, player.attack, player.crit_damage)
                b = crit_chance(hoard[i].crit_chance, hoard[i].attack, 1.4)
                # PLAYER CRITICAL AND hoard[i] NORMAL ATTACK
                if a > player.attack and b == hoard[i].attack:
                    print('aqui 5')
                    hoard_damage = round(a - hoard[i].defense)
                    counter = 0
                    delve_battle_condition_2a(biome, hoard_damage, hoard, i)

                # PLAYER AND hoard[i] CRITICAL
                elif a > player.attack and b > hoard[i].attack:
                    print('aqui 6')
                    hoard_damage = round(a - hoard[i].defense)
                    player_damage = round(b - player.defense)
                    counter = 0
                    delve_battle_condition_2b(biome, hoard_damage, player_damage, hoard, i)

                # PLAYER NORMAL ATTACK AND hoard[i] CRITICAL
                elif a == player.attack and b > hoard[i].attack:
                    print('aqui 7')
                    hoard_damage = round(player.attack - hoard[i].defense)
                    player_damage = round(b - player.defense)
                    counter = 0
                    delve_battle_condition_2c(biome, hoard_damage, player_damage, hoard, i)

                else:
                    print('aqui 8')
                    hoard_damage = round(player.attack - hoard[i].defense)
                    player_damage = round(hoard[i].attack - player.defense)
                    counter = 0
                    delve_battle_condition_2d(biome, hoard_damage, player_damage, hoard, i)

        else:
            hoard[i].life = 0
            delve_battle_elements_resetter(biome, hoard, i)
            # if hoard[i].life == 0:
            #     SCREEN.fill(0)
            #     SCREEN.blit(BG, (0, 0))
            #     SCREEN.blit(BATTLE_BOX, (60, 40))
            #     # PLAYER
            #     SCREEN.blit(player.image, (130, 300))
    delve_battle_finish(biome, hoard)
    # if hoard[i].life < 0:
    #     hoard[i].life = 0
    #     check_player_life()


# IF ENEMY ATTACK IS ZERO
def delve_battle_condition_1(biome, hoard, i):
    global counter
    player_damage = 0
    a = crit_chance(player.crit_chance, player.attack, player.crit_damage)
    if a > player.attack:
        counter = 0
        delve_battle_condition_1_a(biome, player_damage, a, hoard, i)
    else:
        counter = 0
        delve_battle_condition_1_b(biome, hoard, i, player_damage)


# IF ENEMY ATTACK IS ZERO AND PLAYER ATTACK IS CRITICAL
def delve_battle_condition_1_a(biome, player_damage, a, hoard, i):
    global counter, last_time_ms
    display_delve_depth()
    hoard_damage = round(a - hoard[i].defense)
    hoard[i].life = round(hoard[i].life - hoard_damage)
    player.life = round(player.life - player_damage)
    counter = 0
    c_a = False
    e_a_s = False
    while True:
        text0 = get_regular_font(20).render(f'CRITICAL!', True, WHITE)
        text0_rect = text0.get_rect(center=(910, 220))
        text1 = get_bold_font(70).render(f'{hoard_damage}', True, ORANGE)
        text1_rect = text1.get_rect(center=(910, 260))
        text2 = get_regular_font(20).render(f'MISS!', True, WHITE)
        text2_rect = text2.get_rect(center=(285, 260))

        diff_time_ms = int(round(time.time() * 4000)) - last_time_ms

        if diff_time_ms >= 4000:
            counter = counter + 1
            last_time_ms = int(round(time.time() * 4000))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        if counter == 1:
            SCREEN.blit(text0, text0_rect)
            SCREEN.blit(text1, text1_rect)
            if not c_a:
                critical_attack_sound()
                c_a = True
        if counter == 2:
            SCREEN.blit(text2, text2_rect)
            if not e_a_s:
                enemy_attack_sound()
                e_a_s = True
        if counter == 3:
            counter = 0
            delve_battle(biome, hoard)
        pygame.display.update()


def delve_battle_condition_1_b(biome, hoard, i, player_damage):
    display_delve_depth()
    global last_time_ms, counter
    p_a_s = False
    e_a_s = False
    hoard_damage = round(player.attack - hoard[i].defense)
    hoard[i].life = round(hoard[i].life - hoard_damage)
    player.life = round(player.life - player_damage)

    while True:
        text1 = get_bold_font(50).render(f'{hoard_damage}', True, RED)
        text1_rect = text1.get_rect(center=(910, 260))
        text2 = get_bold_font(20).render(f'MISS!', True, WHITE)
        text2_rect = text2.get_rect(center=(285, 260))

        diff_time_ms = int(round(time.time() * 4000)) - last_time_ms

        if diff_time_ms >= 4000:
            counter = counter + 1
            last_time_ms = int(round(time.time() * 4000))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        if counter == 1:
            SCREEN.blit(text1, text1_rect)
            if not p_a_s:
                critical_attack_sound()
                p_a_s = True
        if counter == 2:
            SCREEN.blit(text2, text2_rect)
            if not e_a_s:
                enemy_attack_sound()
                e_a_s = True
        if counter == 3:
            counter = 0
            delve_battle(biome, hoard)
        pygame.display.update()


# PLAYER CRITICAL AND ENEMY NORMAL ATTACK
def delve_battle_condition_2a(biome, e_damage, hoard, i):
    global counter, last_time_ms
    display_delve_depth()
    player_damage = round(hoard[i].attack - player.defense)
    hoard[i].life = round(hoard[i].life - e_damage)
    player.life = round(player.life - player_damage)
    c_a = False
    e_a_s = False

    while True:
        text0 = get_regular_font(20).render(f'CRITICAL!', True, WHITE)
        text0_rect = text0.get_rect(center=(910, 220))
        text1 = get_bold_font(70).render(f'{e_damage}', True, ORANGE)
        text1_rect = text1.get_rect(center=(910, 260))
        text2 = get_bold_font(50).render(f'{player_damage}', True, RED)
        text2_rect = text2.get_rect(center=(285, 260))

        diff_time_ms = int(round(time.time() * 4000)) - last_time_ms

        if diff_time_ms >= 4000:
            counter = counter + 1
            last_time_ms = int(round(time.time() * 4000))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        if counter == 1:
            SCREEN.blit(text0, text0_rect)
            SCREEN.blit(text1, text1_rect)
            if not c_a:
                critical_attack_sound()
                c_a = True
        if counter == 2:
            SCREEN.blit(text2, text2_rect)
            if not e_a_s:
                enemy_attack_sound()
                e_a_s = True
        if counter == 3:
            counter = 0
            delve_battle(biome, hoard)
        pygame.display.update()


# PLAYER AND ENEMY CRITICAL
def delve_battle_condition_2b(biome, e_damage, p_damage, hoard, i):
    global counter, last_time_ms
    display_delve_depth()
    hoard[i].life = round(hoard[i].life - e_damage)
    player.life = round(player.life - p_damage)
    c_a = False
    c_a_2 = False

    while True:
        text0 = get_regular_font(20).render(f'CRITICAL!', True, WHITE)
        text0_rect = text0.get_rect(center=(910, 220))
        text1 = get_bold_font(70).render(f'{e_damage}', True, ORANGE)
        text1_rect = text1.get_rect(center=(910, 260))
        text1_5 = get_regular_font(20).render(f'CRITICAL!', True, WHITE)
        text1_5_rect = text1_5.get_rect(center=(910, 220))
        text2 = get_bold_font(70).render(f'{p_damage}', True, ORANGE)
        text2_rect = text2.get_rect(center=(285, 260))

        diff_time_ms = int(round(time.time() * 4000)) - last_time_ms

        if diff_time_ms >= 4000:
            counter = counter + 1
            last_time_ms = int(round(time.time() * 4000))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        if counter == 1:
            SCREEN.blit(text0, text0_rect)
            SCREEN.blit(text1, text1_rect)
            if not c_a:
                critical_attack_sound()
                c_a = True
        if counter == 2:
            SCREEN.blit(text1_5, text1_5_rect)
            SCREEN.blit(text2, text2_rect)
            if not c_a_2:
                critical_attack_sound()
                c_a_2 = True
        if counter == 3:
            counter = 0
            delve_battle(biome, hoard)
        pygame.display.update()


# PLAYER NORMAL ATTACK AND ENEMY CRITICAL
def delve_battle_condition_2c(biome, e_damage, p_damage, hoard, i):
    global counter, last_time_ms
    display_delve_depth()
    hoard[i].life = round(hoard[i].life - e_damage)
    player.life = round(player.life - p_damage)
    p_a_s = False
    c_a = False

    while True:
        # text0 = get_regular_font(20).render(f'CRITICAL!', True, WHITE)
        # text0_rect = text0.get_rect(center=(750, 220))
        text1 = get_bold_font(50).render(f'{e_damage}', True, RED)
        text1_rect = text1.get_rect(center=(910, 260))
        text1_5 = get_regular_font(20).render(f'CRITICAL!', True, WHITE)
        text1_5_rect = text1_5.get_rect(center=(910, 220))
        text2 = get_bold_font(70).render(f'{p_damage}', True, ORANGE)
        text2_rect = text2.get_rect(center=(285, 260))

        diff_time_ms = int(round(time.time() * 4000)) - last_time_ms

        if diff_time_ms >= 4000:
            counter = counter + 1
            last_time_ms = int(round(time.time() * 4000))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        if counter == 1:
            SCREEN.blit(text1, text1_rect)
            if not p_a_s:
                player_attack_sound()
                p_a_s = True
        if counter == 2:
            SCREEN.blit(text1_5, text1_5_rect)
            SCREEN.blit(text2, text2_rect)
            if not c_a:
                critical_attack_sound()
                c_a = True
        if counter == 3:
            counter = 0
            delve_battle(biome, hoard)
        pygame.display.update()


# PLAYER AND ENEMY NORMAL ATTACK
def delve_battle_condition_2d(biome, e_damage, p_damage, hoard, i):
    global counter, last_time_ms
    display_delve_depth()
    hoard[i].life = round(hoard[i].life - e_damage)
    player.life = round(player.life - p_damage)
    p_a_s = False
    e_a_s = False

    while True:
        text1 = get_bold_font(50).render(f'{e_damage}', True, RED)
        text1_rect = text1.get_rect(center=(910, 260))
        text2 = get_bold_font(50).render(f'{p_damage}', True, RED)
        text2_rect = text2.get_rect(center=(295, 260))

        diff_time_ms = int(round(time.time() * 4000)) - last_time_ms

        if diff_time_ms >= 4000:
            counter = counter + 1
            last_time_ms = int(round(time.time() * 4000))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        if counter == 1:
            SCREEN.blit(text1, text1_rect)
            if not p_a_s:
                player_attack_sound()
                p_a_s = True
        if counter == 2:
            SCREEN.blit(text2, text2_rect)
            if not e_a_s:
                critical_attack_sound()
                e_a_s = True
        if counter == 3:
            counter = 0
            delve_battle(biome, hoard)
        pygame.display.update()


def delve_battle_finish(biome, hoard):
    global counter, last_time_ms, drop_quantity
    counter = 0
    player.life = player.total_life
    Delve.depth = Delve.depth + 1
    Delve.multiplier = Delve.multiplier + 0.005
    card_drop_rate(player)
    delve_save_state()
    save_state()
    SCREEN.blit(biome, (0, 0))

    depth_setter = False
    encounter_setter = False
    fossil_setter = False
    card_setter = False


    text1 = get_bold_font(40).render(f'You have defeated all enemies of Depth {Delve.depth}!', True, WHITE)
    text1_rect = text1.get_rect(center=(SCREEN_WIDTH / 2, 150))

    text2 = get_bold_font(40).render(f'Your life points were fully restored!', True, WHITE)
    text2_rect = text2.get_rect(center=(SCREEN_WIDTH / 2, 210))

    print('fossil')
    drop = delve_drop_rate(hoard)

    drop_height = 270

    while True:

        DELVE_ENCOUNTER_MOUSE_POSITION = pygame.mouse.get_pos()
        MAIN_MENU = Button(image=pygame.image.load("assets/images/Smallest Rect.png"), pos=(SCREEN_WIDTH / 2 - 180, 500),
                           text_input="MAIN MENU", font=get_bold_font(30), base_color="White", hovering_color=BLUE)
        START_DELVING = Button(image=pygame.image.load("assets/images/Smallest Rect.png"), pos=(SCREEN_WIDTH / 2 + 180, 500),
                               text_input="CONTINUE", font=get_bold_font(30), base_color="White", hovering_color=BLUE)

        diff_time_ms = int(round(time.time() * 4000)) - last_time_ms
        if diff_time_ms >= 4000:
            counter = counter + 1
            last_time_ms = int(round(time.time() * 4000))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if MAIN_MENU.checkForInput(DELVE_ENCOUNTER_MOUSE_POSITION):
                    pygame.mixer.music.fadeout(2)
                    pygame.mixer.music.stop()
                    background_music()
                    main_menu()
                if START_DELVING.checkForInput(DELVE_ENCOUNTER_MOUSE_POSITION):
                    counter = 0
                    delve_encounter()

        if counter >= 0:
            if depth_setter is not True:
                SCREEN.blit(text1, text1_rect)
                depth_setter = True

        if counter == 2:
            if encounter_setter is not True:
                SCREEN.blit(text2, text2_rect)
                encounter_setter = True

        if counter == 3:
            if drop:
                if fossil_setter is not True:
                    counter = 2
                    drop_text = get_bold_font(35).render(f"{drop_quantity}x {drop} dropped!", True, YELLOW)
                    drop_text_rect = drop_text.get_rect(center=(SCREEN_WIDTH / 2, drop_height))
                    SCREEN.blit(drop_text, drop_text_rect)
                    playsound(DROP_1, False)
                    drop_quantity = 1
                    fossil_setter = True
                    drop_height += 40


        if counter == 3:
            if len(temp_card_drop) != 0:
                if card_setter is not True:
                    drop_text2 = get_bold_font(35).render(f"{temp_card_drop[0].__dict__['name']} card dropped!", True, PINK)
                    drop_text2_rect = drop_text2.get_rect(center=(SCREEN_WIDTH / 2, drop_height))
                    SCREEN.blit(drop_text2, drop_text2_rect)
                    playsound(DROP_CONSUMABLE, False)
                    drop_quantity = 1
                    temp_card_drop.clear()
                    card_setter = True

        if counter >= 4:
            for button in [MAIN_MENU, START_DELVING]:
                button.changeColor(DELVE_ENCOUNTER_MOUSE_POSITION)
                button.update(SCREEN)

        pygame.display.update()


def delve_encounter():
    global counter, last_time_ms
    BIOME = random.choice([FROZEN_HOLLOW, FUNGAL_CAVERNS, PETRIFIED_FOREST,
                           ABYSSAL_DEPTHS, MAGMA_FISSURE, SULPHUR_VENTS])
    SCREEN.blit(BIOME, (0, 0))

    clicking_prevention = False
    depth_setter = False
    encounter_setter = False

    text = str(Delve.depth)
    depth = ' '.join(text)

    text1 = get_bold_font(140).render(f"D E P T H  {depth}", True, WHITE)
    text1_rect = text1.get_rect(center=(SCREEN_WIDTH / 2, 200))

    # choice = random.randint(3, 5)
    choice = 1
    hoard = []
    for i in range(0, choice):
        enemy_type_choice = random.choice(list(monster_type))
        enemy_dict = monster_type[enemy_type_choice]
        global enemy
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
                        )
        if Delve.depth < 50 and enemy.level > 20:
            print('rerolling...')
            delve_encounter()
        hoard.append(enemy)
    for i in range(0, len(hoard)):
        hoard[i].life = round(hoard[i].life + hoard[i].life * Delve.multiplier)
        hoard[i].total_life = round(hoard[i].total_life + hoard[i].total_life * Delve.multiplier)
        hoard[i].attack = round(hoard[i].attack + hoard[i].attack * Delve.multiplier)
        hoard[i].defense = round(hoard[i].defense + hoard[i].defense * Delve.multiplier)
        hoard[i].crit_chance = round(hoard[i].crit_chance + hoard[i].crit_chance * Delve.multiplier)

    text2 = get_bold_font(40).render(f"YOU HAVE ENCOUNTERED A HOARD OF {len(hoard)} MONSTERS!", True, WHITE)
    text2_rect = text2.get_rect(center=(SCREEN_WIDTH / 2, 200))

    while True:

        DELVE_ENCOUNTER_MOUSE_POSITION = pygame.mouse.get_pos()
        MAIN_MENU = Button(image=pygame.image.load("assets/images/Smallest Rect.png"), pos=(SCREEN_WIDTH / 2 - 180, 500),
                           text_input="MAIN MENU", font=get_bold_font(30), base_color="White", hovering_color=BLUE)
        START_DELVING = Button(image=pygame.image.load("assets/images/Smallest Rect.png"), pos=(SCREEN_WIDTH / 2 + 180, 500),
                               text_input="ENTER DELVE", font=get_bold_font(30), base_color="White",
                               hovering_color=BLUE)

        diff_time_ms = int(round(time.time() * 4000)) - last_time_ms
        if diff_time_ms >= 4000:
            counter = counter + 1
            last_time_ms = int(round(time.time() * 4000))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN and clicking_prevention is True:
                if MAIN_MENU.checkForInput(DELVE_ENCOUNTER_MOUSE_POSITION):
                    pygame.mixer.music.fadeout(2)
                    pygame.mixer.music.stop()
                    background_music()
                    main_menu()
                if START_DELVING.checkForInput(DELVE_ENCOUNTER_MOUSE_POSITION):
                    counter = 0
                    delve_encounter()

        if counter >= 1:
            if depth_setter is not True:
                SCREEN.blit(text1, text1_rect)
                depth_setter = True

        if counter >= 3:
            if encounter_setter is not True:
                SCREEN.blit(BIOME, (0, 0))
                SCREEN.blit(text2, text2_rect)
                encounter_setter = True

        if counter >= 5:
            clicking_prevention = True
            delve_battle(BIOME, hoard)
            # for button in [MAIN_MENU, START_DELVING]:
            #     button.changeColor(DELVE_ENCOUNTER_MOUSE_POSITION)
            #     button.update(SCREEN)

        pygame.display.update()

    # Delve battle
    # for i in range(0, len(hoard)):
    #     while hoard[i].life > 0:
    #         if hoard[i].attack <= player.defense:
    #             player_damage = 0
    #             a = crit_chance(player.crit_chance, player.attack, player.crit_damage)
    #
    #             if a > player.attack:
    #                 enemy_damage = a - hoard[i].defense
    #                 hoard[i].life = hoard[i].life - enemy_damage
    #                 player.life = player.life - player_damage
    #                 print(f"- CRITICAL HIT! You've attacked {hoard[i].name} and dealt {round(enemy_damage)} damage!")
    #                 critical_attack_sound()
    #                 time.sleep(0.5)
    #                 print(f"- {hoard[i].name} attacked you and dealt {round(player_damage)} damage!")
    #                 enemy_attack_sound()
    #                 time.sleep(0.5)
    #             else:
    #                 enemy_damage = player.attack - hoard[i].defense
    #                 hoard[i].life = hoard[i].life - enemy_damage
    #                 player.life = player.life - player_damage
    #                 print(f"- You've attacked {hoard[i].name} and dealt {round(enemy_damage)} damage!")
    #                 player_attack_sound()
    #                 print(f"- {hoard[i].name} attacked you and dealt {round(player_damage)} damage!")
    #                 enemy_attack_sound()
    #                 time.sleep(0.5)
    #         else:
    #             a = crit_chance(player.crit_chance, player.attack, player.crit_damage)
    #             b = crit_chance(hoard[i].crit_chance, hoard[i].attack, 1.4)
    #
    #             if a > player.attack and b == hoard[i].attack:
    #                 enemy_damage = a - hoard[i].defense
    #                 player_damage = hoard[i].attack - player.defense
    #                 hoard[i].life = hoard[i].life - enemy_damage
    #                 player.life = player.life - player_damage
    #                 print(f"- CRITICAL HIT! You've attacked {hoard[i].name} and dealt {round(enemy_damage)} damage!")
    #                 critical_attack_sound()
    #                 print(f"- {hoard[i].name} attacked you and dealt {round(player_damage)} damage!")
    #                 enemy_attack_sound()
    #                 time.sleep(0.5)
    #             elif a > player.attack and b > hoard[i].attack:
    #                 enemy_damage = a - hoard[i].defense
    #                 player_damage = b - player.defense
    #                 hoard[i].life = hoard[i].life - enemy_damage
    #                 player.life = player.life - player_damage
    #                 print(f"- CRITICAL HIT! You've attacked {hoard[i].name} and dealt {round(enemy_damage)} damage!")
    #                 critical_attack_sound()
    #                 print(f"- CRITICAL HIT! {hoard[i].name} attacked you and dealt {round(player_damage)} damage!")
    #                 critical_attack_sound()
    #
    #             elif a == player.attack and b > hoard[i].attack:
    #                 enemy_damage = player.attack - hoard[i].defense
    #                 player_damage = b - player.defense
    #                 hoard[i].life = hoard[i].life - enemy_damage
    #                 player.life = player.life - player_damage
    #                 print(f"- You've attacked {hoard[i].name} and dealt {round(enemy_damage)} damage!")
    #                 player_attack_sound()
    #                 print(f"- CRITICAL HIT! {hoard[i].name} attacked you and dealt {round(player_damage)} damage!")
    #                 critical_attack_sound()
    #                 time.sleep(0.5)
    #             else:
    #                 enemy_damage = player.attack - hoard[i].defense
    #                 player_damage = hoard[i].attack - player.defense
    #                 hoard[i].life = hoard[i].life - enemy_damage
    #                 player.life = player.life - player_damage
    #                 print(f"- You've attacked {hoard[i].name} and dealt {round(enemy_damage)} damage!")
    #                 player_attack_sound()
    #                 print(f"- {hoard[i].name} attacked you and dealt {round(player_damage)} damage!")
    #                 enemy_attack_sound()
    #                 time.sleep(0.5)
    #     if hoard[i].life < 0:
    #         hoard[i].life = 0
    #     check_player_life()
    #     print(f'\nYour life points: {round(player.life)}/{player.total_life}')
    #     print('-' * DASH)
    #     time.sleep(1)
    # print(f'You have defeated all enemies of depth {Delve.depth}!')
    # print(f'Your life points were fully restored!')
    # print('-' * DASH)
    # time.sleep(2)
    # delve_drop_rate(hoard)
    # player.life = player.total_life
    # Delve.depth = Delve.depth + 1
    # Delve.multiplier = Delve.multiplier + 0.005
    # delve_save_state()
    # save_state()
    # choice = input('Press 1 to continue delving or 2 to return to delve menu: ')
    # if choice == '1':
    #     delve_encounter()
    # elif choice == '2':
    #     delve_menu()
    # else:
    #     print('Wrong option..')
    #     time.sleep(1)
    #     delve_menu()


def delve_menu():
    global counter, last_time_ms
    SCREEN.blit(DELVE_MAIN_BG, (0, 0))
    life_checking_setter = False
    welcome_setter = False

    while True:
        text1 = get_bold_font(40).render('You need to have your life points fully restored before entering delve.',
                                         True, WHITE)
        text1_rect = text1.get_rect(center=(SCREEN_WIDTH / 2, 200))
        text2 = get_bold_font(80).render('WELCOME TO DELVE', True, WHITE)
        text2_rect = text2.get_rect(center=(SCREEN_WIDTH / 2, 300))

        DELVE_MENU_MOUSE_POSITION = pygame.mouse.get_pos()
        # BUTTONS = main_menu_structure(DELVE_MENU_MOUSE_POSITION)
        MAIN_MENU = Button(image=pygame.image.load("assets/images/Smallest Rect.png"), pos=(SCREEN_WIDTH / 2 - 180, 500),
                           text_input="MAIN MENU", font=get_bold_font(30), base_color="White", hovering_color=BLUE)
        START_DELVING = Button(image=pygame.image.load("assets/images/Smallest Rect.png"), pos=(SCREEN_WIDTH / 2 + 180, 500),
                               text_input="ENTER DELVE", font=get_bold_font(30), base_color="White",
                               hovering_color=BLUE)

        diff_time_ms = int(round(time.time() * 4000)) - last_time_ms
        if diff_time_ms >= 4000:
            counter = counter + 1
            last_time_ms = int(round(time.time() * 4000))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if MAIN_MENU.checkForInput(DELVE_MENU_MOUSE_POSITION):
                    pygame.mixer.music.fadeout(2)
                    pygame.mixer.music.stop()
                    background_music()
                    main_menu()
                if START_DELVING.checkForInput(DELVE_MENU_MOUSE_POSITION):
                    counter = 0
                    delve_encounter()

        if counter >= 0:
            if player.life != player.total_life:
                if life_checking_setter is not True:
                    SCREEN.blit(text1, text1_rect)
                    life_checking_setter = True
            else:
                if welcome_setter is not True:
                    SCREEN.blit(text2, text2_rect)
                    welcome_setter = True
        if counter > 1:
            for button in [MAIN_MENU, START_DELVING]:
                button.changeColor(DELVE_MENU_MOUSE_POSITION)
                button.update(SCREEN)

        pygame.display.update()


def delve_save_state():
    db.execute("UPDATE delve SET depth = :depth, multiplier = :multiplier WHERE username = :username",
               username=player.name, depth=Delve.depth, multiplier=Delve.multiplier)


def load_state():
    username = player.name
    rows = db.execute("SELECT * FROM user_data WHERE username = :username",
                      username=username)
    print(rows[0])

    # input('aqui 5')
    player.name = rows[0]['username']
    player.level = rows[0]['level']
    player.xp = rows[0]['experience']
    player.total_life = rows[0]['total_life']
    player.life = rows[0]['life']
    player.attack = rows[0]['attack']
    player.defense = rows[0]['defense']
    player.shaman = rows[0]['shaman']
    player.crit_chance = rows[0]['crit_chance']
    player.crit_damage = rows[0]['crit_damage']
    player.magic_find = rows[0]['magic_find']

    print(player.name, player.level)
    # Inventory
    rows2 = db.execute("SELECT * FROM inventory WHERE username = :username",
                       username=username)

    if len(rows2) < 1:
        pass


    else:
        for i in range(0, len(rows2)):
            new_item = Item(rows2[i]['type'], rows2[i]['name'], rows2[i]['level'],
                            rows2[i]['life'], rows2[i]['attack'],
                            rows2[i]['defense'], rows2[i]['crit_chance'],
                            rows2[i]['crit_damage'], rows2[i]['magic_find'], rows2[i]['rarity'])
            inventory.append(new_item)

    # PlayerSlot
    row_amulet = db.execute("SELECT * FROM amulet WHERE username = :username", username=username)
    player_slot.amulet = row_amulet[0]
    row_armor = db.execute("SELECT * FROM armor WHERE username = :username", username=username)
    player_slot.armor = row_armor[0]
    row_gloves = db.execute("SELECT * FROM gloves WHERE username = :username", username=username)
    player_slot.gloves = row_gloves[0]
    row_helmet = db.execute("SELECT * FROM helmet WHERE username = :username", username=username)
    player_slot.helmet = row_helmet[0]
    row_legs = db.execute("SELECT * FROM legs WHERE username = :username", username=username)
    player_slot.legs = row_legs[0]
    row_ring1 = db.execute("SELECT * FROM ring1 WHERE username = :username", username=username)
    player_slot.ring1 = row_ring1[0]
    row_ring2 = db.execute("SELECT * FROM ring2 WHERE username = :username", username=username)
    player_slot.ring2 = row_ring2[0]
    row_second_hand = db.execute("SELECT * FROM second_hand WHERE username = :username", username=username)
    player_slot.second_hand = row_second_hand[0]
    row_weapon = db.execute("SELECT * FROM weapon WHERE username = :username", username=username)
    player_slot.weapon = row_weapon[0]
    row_boots = db.execute("SELECT * FROM boots WHERE username = :username", username=username)
    player_slot.boots = row_boots[0]

    # Consumables
    row_potion = db.execute("SELECT * FROM potion WHERE username = :username", username=username)
    potion.quantity = row_potion[0]['quantity']
    row_x_potion = db.execute("SELECT * FROM x_potion WHERE username = :username", username=username)
    x_potion.quantity = row_x_potion[0]['quantity']
    row_elixir = db.execute("SELECT * FROM elixir WHERE username = :username", username=username)
    elixir.quantity = row_elixir[0]['quantity']
    row_chaos_orb = db.execute("SELECT * FROM chaos_orb WHERE username = :username", username=username)
    chaos_orb.quantity = row_chaos_orb[0]['quantity']
    row_divine_orb = db.execute("SELECT * FROM divine_orb WHERE username = :username", username=username)
    divine_orb.quantity = row_divine_orb[0]['quantity']
    row_exalted_orb = db.execute("SELECT * FROM exalted_orb WHERE username = :username", username=username)
    exalted_orb.quantity = row_exalted_orb[0]['quantity']
    row_mirror_of_kalandra = db.execute("SELECT * FROM mirror_of_kalandra WHERE username = :username",
                                        username=username)
    mirror_of_kalandra.quantity = row_mirror_of_kalandra[0]['quantity']
    row_dense_fossil = db.execute("SELECT * FROM dense_fossil WHERE username = :username", username=username)
    dense_fossil.quantity = row_dense_fossil[0]['quantity']
    row_serrated_fossil = db.execute("SELECT * FROM serrated_fossil WHERE username = :username", username=username)
    serrated_fossil.quantity = row_serrated_fossil[0]['quantity']
    row_pristine_fossil = db.execute("SELECT * FROM pristine_fossil WHERE username = :username", username=username)
    pristine_fossil.quantity = row_pristine_fossil[0]['quantity']
    row_deft_fossil = db.execute("SELECT * FROM deft_fossil WHERE username = :username", username=username)
    deft_fossil.quantity = row_deft_fossil[0]['quantity']
    row_fractured_fossil = db.execute("SELECT * FROM fractured_fossil WHERE username = :username", username=username)
    fractured_fossil.quantity = row_fractured_fossil[0]['quantity']

    # boss instance
    row_boss_instance = db.execute("SELECT * FROM boss_instance WHERE username = :username", username=username)

    # Uniques_list
    row_uniques_list = db.execute("SELECT * FROM uniques_list WHERE username = :username", username=username)

    for i in range(0, len(row_uniques_list)):
        uniques_list.append(row_uniques_list[i]['name'])

    if row_boss_instance[0]['wiegraf1'] == 0:
        wiegraf1.status = False
    else:
        pass
    if row_boss_instance[0]['dycedarg1'] == 0:
        dycedarg1.status = False
    else:
        pass
    if row_boss_instance[0]['wiegraf2'] == 0:
        wiegraf2.status = False
    else:
        pass
    if row_boss_instance[0]['dycedarg2'] == 0:
        dycedarg2.status = False
    else:
        pass

    # Delve
    delve_rows = db.execute("SELECT * FROM delve WHERE username = :username",
                            username=username)
    Delve.depth = delve_rows[0]['depth']
    Delve.multiplier = delve_rows[0]['multiplier']


def load_username():
    global counter, last_time_ms, player
    username = ''
    input_active = True
    confirm = False

    while True:
        SCREEN.fill(BLACK)
        pygame.display.set_caption("PoETactics")
        LOAD_STATE_MOUSE_POSITION = pygame.mouse.get_pos()

        text1 = get_bold_font(50).render('Please enter your username', True, WHITE)
        menu_rect1 = text1.get_rect(center=(SCREEN_WIDTH / 2, 100))

        text2 = get_bold_font(50).render('Wrong username', True, WHITE)
        menu_rect2 = text2.get_rect(center=(SCREEN_WIDTH / 2, 300))

        CONFIRM = Button(image=pygame.image.load("assets/images/Options Rect.png"), pos=(SCREEN_WIDTH / 2, 450),
                         text_input="CONFIRM", font=get_bold_font(40), base_color="White", hovering_color=PINK)
        SMALL_QUIT_BUTTON = Button(image=pygame.image.load("assets/images/Small Quit Rect.png"), pos=(1870, 40),
                                   text_input="X", font=get_bold_font(40), base_color="White", hovering_color=PINK)

        SCREEN.blit(text1, menu_rect1)

        diff_time_ms = int(round(time.time() * 4000)) - last_time_ms
        if diff_time_ms >= 4000:
            counter = counter + 1
            last_time_ms = int(round(time.time() * 4000))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                input_active = True
                text = ''
                if CONFIRM.checkForInput(LOAD_STATE_MOUSE_POSITION):
                    input_active = False
                    confirm = True
                if SMALL_QUIT_BUTTON.checkForInput(LOAD_STATE_MOUSE_POSITION):
                    pygame.quit()
                    sys.exit()
            elif event.type == pygame.KEYDOWN and input_active:
                if event.key == pygame.K_RETURN or event.key == pygame.K_KP_ENTER:
                    input_active = False
                    confirm = True
                elif event.key == pygame.K_BACKSPACE:
                    username = username[:-1]
                else:
                    username += event.unicode

        username_text = get_regular_font(40).render(username, True, WHITE)
        username_text_rect = username_text.get_rect(center=(SCREEN_WIDTH / 2, 300))
        SCREEN.blit(username_text, username_text_rect)
        for button in [CONFIRM, SMALL_QUIT_BUTTON]:
            button.changeColor(LOAD_STATE_MOUSE_POSITION)
            button.update(SCREEN)
        if confirm:
            try:
                player.name = username
                rows = db.execute("SELECT * FROM users WHERE username = :username",
                                  username=username)
                if username == rows[0]['username']:
                    counter = 0
                    load_state_success()
                if len(rows) != 1:
                    counter = 0
                    wrong_username()
            except:
                counter = 0
                wrong_username()
        pygame.display.update()


def wrong_username():
    pass


def load_state_success():
    global counter, last_time_ms
    load_state()
    while True:
        SCREEN.fill(BLACK)
        pygame.display.set_caption("PoETactics")
        LOAD_STATE_SUCCESS_MOUSE_POSITION = pygame.mouse.get_pos()

        text1 = get_bold_font(50).render(f"Welcome back, {player.name}", True, WHITE)
        menu_rect1 = text1.get_rect(center=(SCREEN_WIDTH / 2, 300))

        SCREEN.blit(text1, menu_rect1)

        NEXT_BUTTON = Button(image=pygame.image.load("assets/images/Next Rect.png"),
                             pos=(SCREEN_WIDTH / 2, SCREEN_HEIGHT - 100),
                             text_input="NEXT", font=get_bold_font(40), base_color="White", hovering_color=PINK)
        SMALL_QUIT_BUTTON = Button(image=pygame.image.load("assets/images/Small Quit Rect.png"), pos=(1600, 40),
                                   text_input="X", font=get_bold_font(40), base_color="White", hovering_color=PINK)

        diff_time_ms = int(round(time.time() * 4000)) - last_time_ms
        if diff_time_ms >= 4000:
            counter = counter + 1
            last_time_ms = int(round(time.time() * 4000))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if NEXT_BUTTON.checkForInput(LOAD_STATE_SUCCESS_MOUSE_POSITION):
                    main_menu()
                if SMALL_QUIT_BUTTON.checkForInput(LOAD_STATE_SUCCESS_MOUSE_POSITION):
                    pygame.quit()
                    sys.exit()

        if counter >= 1:
            SCREEN.blit(text1, menu_rect1)
        if counter >= 3:
            main_menu()
            # for button in [NEXT_BUTTON, SMALL_QUIT_BUTTON]:
            #     button.changeColor(LOAD_STATE_SUCCESS_MOUSE_POSITION)
            #     button.update(SCREEN)
        pygame.display.update()


def register_data_insert(player_name):
    username = player_name
    db.execute(
        "INSERT INTO user_data (username, level, experience, total_life, life, attack, defense, shaman, crit_chance, crit_damage, magic_find) VALUES (:username, :level, :experience, :total_life, :life, :attack, :defense,:shaman, :crit_chance, :crit_damage, :magic_find)",
        username=username, level=player.level, experience=player.xp, total_life=player.total_life, life=player.life,
        attack=player.attack, defense=player.defense, shaman=player.shaman,
        crit_chance=player.crit_chance, crit_damage=player.crit_damage, magic_find=player.magic_find)

    rows = db.execute("SELECT * FROM users WHERE username = :username",
                      username=username)

    player.name = rows[0]['username']

    # Consumables Instance
    db.execute(
        "INSERT INTO potion (username, type, name, value, quantity, rarity, code, sound) VALUES (:username, :type, :name, :value, :quantity, :rarity, :code, :sound)",
        username=player.name, type=potion.type, name=potion.name, value=potion.value, quantity=potion.quantity,
        rarity=potion.rarity, code=potion.code, sound=potion.sound)
    db.execute(
        "INSERT INTO x_potion (username, type, name, value, quantity, rarity, code, sound) VALUES (:username, :type, :name, :value, :quantity, :rarity, :code, :sound)",
        username=player.name, type=x_potion.type, name=x_potion.name, value=x_potion.value, quantity=x_potion.quantity,
        rarity=x_potion.rarity, code=x_potion.code, sound=x_potion.sound)
    db.execute(
        "INSERT INTO elixir (username, type, name, value, quantity, rarity, code, sound) VALUES (:username, :type, :name, :value, :quantity, :rarity, :code, :sound)",
        username=player.name, type=elixir.type, name=elixir.name, value=elixir.value, quantity=elixir.quantity,
        rarity=elixir.rarity, code=elixir.code, sound=elixir.sound)
    db.execute(
        "INSERT INTO chaos_orb (username, type, name, value, quantity, rarity, code, sound) VALUES (:username, :type, :name, :value, :quantity, :rarity, :code, :sound)",
        username=player.name, type=chaos_orb.type, name=chaos_orb.name, value=chaos_orb.value,
        quantity=chaos_orb.quantity,
        rarity=chaos_orb.rarity, code=chaos_orb.code, sound=chaos_orb.sound)
    db.execute(
        "INSERT INTO divine_orb (username, type, name, value, quantity, rarity, code, sound) VALUES (:username, :type, :name, :value, :quantity, :rarity, :code, :sound)",
        username=player.name, type=divine_orb.type, name=divine_orb.name, value=divine_orb.value,
        quantity=divine_orb.quantity,
        rarity=divine_orb.rarity, code=divine_orb.code, sound=divine_orb.sound)
    db.execute(
        "INSERT INTO exalted_orb (username, type, name, value, quantity, rarity, code, sound) VALUES (:username, :type, :name, :value, :quantity, :rarity, :code, :sound)",
        username=player.name, type=exalted_orb.type, name=exalted_orb.name, value=exalted_orb.value,
        quantity=exalted_orb.quantity,
        rarity=exalted_orb.rarity, code=exalted_orb.code, sound=exalted_orb.sound)
    db.execute(
        "INSERT INTO mirror_of_kalandra (username, type, name, value, quantity, rarity, code, sound) VALUES (:username, :type, :name, :value, :quantity, :rarity, :code, :sound)",
        username=player.name, type=mirror_of_kalandra.type, name=mirror_of_kalandra.name,
        value=mirror_of_kalandra.value, quantity=mirror_of_kalandra.quantity,
        rarity=mirror_of_kalandra.rarity, code=mirror_of_kalandra.code, sound=mirror_of_kalandra.sound)
    db.execute(
        "INSERT INTO roulette_wheel_ticket (username, type, name, value, quantity, rarity, code, sound) VALUES (:username, :type, :name, :value, :quantity, :rarity, :code, :sound)",
        username=player.name, type=roulette_wheel_ticket.type, name=roulette_wheel_ticket.name,
        value=roulette_wheel_ticket.value, quantity=roulette_wheel_ticket.quantity,
        rarity=roulette_wheel_ticket.rarity, code=roulette_wheel_ticket.code, sound=roulette_wheel_ticket.sound)

    db.execute(
        "INSERT INTO dense_fossil (username, type, name, value, quantity, rarity, code, sound, attribute) VALUES (:username, :type, :name, :value, :quantity, :rarity, :code, :sound, :attribute)",
        username=player.name, type=dense_fossil.type, name=dense_fossil.name,
        value=dense_fossil.value, quantity=dense_fossil.quantity,
        rarity=dense_fossil.rarity, code=dense_fossil.code, sound=dense_fossil.sound, attribute=dense_fossil.attribute)
    db.execute(
        "INSERT INTO serrated_fossil (username, type, name, value, quantity, rarity, code, sound, attribute) VALUES (:username, :type, :name, :value, :quantity, :rarity, :code, :sound, :attribute)",
        username=player.name, type=serrated_fossil.type, name=serrated_fossil.name,
        value=serrated_fossil.value, quantity=serrated_fossil.quantity,
        rarity=serrated_fossil.rarity, code=serrated_fossil.code, sound=serrated_fossil.sound,
        attribute=serrated_fossil.attribute)
    db.execute(
        "INSERT INTO pristine_fossil (username, type, name, value, quantity, rarity, code, sound, attribute) VALUES (:username, :type, :name, :value, :quantity, :rarity, :code, :sound, :attribute)",
        username=player.name, type=pristine_fossil.type, name=pristine_fossil.name,
        value=pristine_fossil.value, quantity=pristine_fossil.quantity,
        rarity=pristine_fossil.rarity, code=pristine_fossil.code, sound=pristine_fossil.sound,
        attribute=pristine_fossil.attribute)
    db.execute(
        "INSERT INTO deft_fossil (username, type, name, value, quantity, rarity, code, sound, attribute) VALUES (:username, :type, :name, :value, :quantity, :rarity, :code, :sound, :attribute)",
        username=player.name, type=deft_fossil.type, name=deft_fossil.name,
        value=deft_fossil.value, quantity=deft_fossil.quantity,
        rarity=deft_fossil.rarity, code=deft_fossil.code, sound=deft_fossil.sound, attribute=deft_fossil.attribute)
    db.execute(
        "INSERT INTO fractured_fossil (username, type, name, value, quantity, rarity, code, sound, attribute) VALUES (:username, :type, :name, :value, :quantity, :rarity, :code, :sound, :attribute)",
        username=player.name, type=fractured_fossil.type, name=fractured_fossil.name,
        value=fractured_fossil.value, quantity=fractured_fossil.quantity,
        rarity=fractured_fossil.rarity, code=fractured_fossil.code, sound=fractured_fossil.sound,
        attribute=fractured_fossil.attribute)

    # Boss instance
    db.execute(
        "INSERT INTO boss_instance (username, wiegraf1, dycedarg1, wiegraf2, dycedarg2) VALUES (:username, :wiegraf1, :dycedarg1, :wiegraf2, :dycedarg2)",
        username=player.name, wiegraf1=1, dycedarg1=1, wiegraf2=1, dycedarg2=1)

    # Delve instance
    db.execute(
        "INSERT INTO delve (username, depth, multiplier) VALUES (:username, :depth, :multiplier)",
        username=player.name, depth=1, multiplier=0.01)


def register():
    global counter, last_time_ms, player
    username = ''
    input_active = True
    confirm = False

    while True:
        SCREEN.fill(BLACK)
        pygame.display.set_caption("PoeTactics")
        REGISTER_MOUSE_POSITION = pygame.mouse.get_pos()

        text1 = get_bold_font(50).render('Please choose and type a username', True, WHITE)
        menu_rect1 = text1.get_rect(center=(SCREEN_WIDTH / 2, 100))

        text2 = get_bold_font(50).render('Username already exists', True, WHITE)
        menu_rect2 = text2.get_rect(center=(SCREEN_WIDTH / 2, 300))

        CONFIRM = Button(image=pygame.image.load("assets/images/Options Rect.png"), pos=(SCREEN_WIDTH / 2, 450),
                         text_input="CONFIRM", font=get_bold_font(40), base_color="White", hovering_color=PINK)
        SMALL_QUIT_BUTTON = Button(image=pygame.image.load("assets/images/Small Quit Rect.png"), pos=(1870, 40),
                                   text_input="X", font=get_bold_font(40), base_color="White", hovering_color=PINK)

        SCREEN.blit(text1, menu_rect1)

        diff_time_ms = int(round(time.time() * 4000)) - last_time_ms
        if diff_time_ms >= 4000:
            counter = counter + 1
            last_time_ms = int(round(time.time() * 4000))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                input_active = True
                text = ''
                if CONFIRM.checkForInput(REGISTER_MOUSE_POSITION):
                    input_active = False
                    confirm = True
                if SMALL_QUIT_BUTTON.checkForInput(REGISTER_MOUSE_POSITION):
                    pygame.quit()
                    sys.exit()
            elif event.type == pygame.KEYDOWN and input_active:
                if event.key == pygame.K_RETURN or event.key == pygame.K_KP_ENTER:
                    input_active = False
                    confirm = True
                elif event.key == pygame.K_BACKSPACE:
                    username = username[:-1]
                else:
                    username += event.unicode

        username_text = get_regular_font(40).render(username, True, WHITE)
        username_text_rect = username_text.get_rect(center=(SCREEN_WIDTH / 2, 300))
        SCREEN.blit(username_text, username_text_rect)
        for button in [CONFIRM, SMALL_QUIT_BUTTON]:
            button.changeColor(REGISTER_MOUSE_POSITION)
            button.update(SCREEN)
        if confirm:
            try:
                player.name = username
                primary_key = db.execute("INSERT INTO users (username) VALUES (:username)", username=username)
                print('aqui')
                register_data_insert(username)
                counter = 0
                register_username_registered()
            except:
                rows = db.execute("SELECT * FROM users WHERE username = :username",
                                  username=username)
                if username == rows[0]['username']:
                    register_username_already_exists()
        pygame.display.update()


def register_username_registered():
    global counter, last_time_ms

    while True:
        SCREEN.fill(BLACK)
        pygame.display.set_caption("PoeTactics")
        REGISTER_USERNAME_REGISTERED_MOUSE_POSITION = pygame.mouse.get_pos()

        text1 = get_bold_font(50).render(f"You've been registered!, {player.name}", True, WHITE)
        menu_rect1 = text1.get_rect(center=(SCREEN_WIDTH / 2, 300))
        text2 = get_bold_font(30).render('Since usernames are canse-sensitive, make sure', True, WHITE)
        menu_rect2 = text2.get_rect(center=(SCREEN_WIDTH / 2, 400))
        text3 = get_bold_font(30).render('you write yours down to use it correctly later.', True, WHITE)
        menu_rect3 = text3.get_rect(center=(SCREEN_WIDTH / 2, 440))

        SCREEN.blit(text1, menu_rect1)

        NEXT_BUTTON = Button(image=pygame.image.load("assets/images/Next Rect.png"),
                             pos=(SCREEN_WIDTH / 2, SCREEN_HEIGHT - 100),
                             text_input="NEXT", font=get_bold_font(40), base_color="White", hovering_color=PINK)
        SMALL_QUIT_BUTTON = Button(image=pygame.image.load("assets/images/Small Quit Rect.png"), pos=(1600, 40),
                                   text_input="X", font=get_bold_font(40), base_color="White", hovering_color=PINK)

        diff_time_ms = int(round(time.time() * 4000)) - last_time_ms
        if diff_time_ms >= 4000:
            counter = counter + 1
            last_time_ms = int(round(time.time() * 4000))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if NEXT_BUTTON.checkForInput(REGISTER_USERNAME_REGISTERED_MOUSE_POSITION):
                    save_state()
                    counter = 0
                    main_menu()
                if SMALL_QUIT_BUTTON.checkForInput(REGISTER_USERNAME_REGISTERED_MOUSE_POSITION):
                    pygame.quit()
                    sys.exit()

        if counter >= 4:
            SCREEN.blit(text2, menu_rect2)
        if counter >= 4:
            SCREEN.blit(text3, menu_rect3)
        if counter >= 6:
            for button in [NEXT_BUTTON, SMALL_QUIT_BUTTON]:
                button.changeColor(REGISTER_USERNAME_REGISTERED_MOUSE_POSITION)
                button.update(SCREEN)
        pygame.display.update()


def register_username_already_exists():
    global counter, last_time_ms

    while True:
        SCREEN.fill(BLACK)
        pygame.display.set_caption("PoeTactics")

        text_1 = get_bold_font(50).render('Username already exists', True, WHITE)
        menu_rect_1 = text_1.get_rect(center=(SCREEN_WIDTH / 2, 300))

        SCREEN.blit(text_1, menu_rect_1)

        diff_time_ms = int(round(time.time() * 4000)) - last_time_ms
        if diff_time_ms >= 4000:
            counter = counter + 1
            last_time_ms = int(round(time.time() * 4000))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        if counter >= 3:
            register()

        pygame.display.update()

    # print('-' * DASH)
    # print(f"You've been registered!, {player.name}. Since usernames are canse-sensitive,"
    #       f" make sure you write yours down to use it correctly later.")
    # print('-' * DASH)
    # input('Press any key to continue... ')
    # print('-' * DASH)
    # print(f'Welcome to the kingdom of Ivalice, {player.name}!')
    # print('-' * DASH)
    # background_music()
    # time.sleep(2)
    # main_menu()


def login_menu():
    while True:
        SCREEN.fill(BLACK)
        pygame.display.set_caption("PoeTactics")
        LOGIN_MOUSE_POSITION = pygame.mouse.get_pos()

        # text1 = get_bold_font(50).render('LOGIN MENU', True, WHITE)
        # menu_rect1 = text1.get_rect(center=(SCREEN_WIDTH/2, 100))

        NEW_GAME_BUTTON = Button(image=pygame.image.load("assets/images/Options Rect.png"), pos=(SCREEN_WIDTH / 2, 200),
                                 text_input="New game", font=get_bold_font(40), base_color="White", hovering_color=PINK)
        LOAD_GAME_BUTTON = Button(image=pygame.image.load("assets/images/Options Rect.png"), pos=(SCREEN_WIDTH / 2, 350),
                                  text_input="Load game", font=get_bold_font(40), base_color="White",
                                  hovering_color=PINK)
        SMALL_QUIT_BUTTON = Button(image=pygame.image.load("assets/images/Small Quit Rect.png"), pos=(1870, 40),
                                   text_input="X", font=get_bold_font(40), base_color="White", hovering_color=PINK)

        # SCREEN.blit(text1, menu_rect1)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if NEW_GAME_BUTTON.checkForInput(LOGIN_MOUSE_POSITION):
                    register()
                if LOAD_GAME_BUTTON.checkForInput(LOGIN_MOUSE_POSITION):
                    load_username()
                if SMALL_QUIT_BUTTON.checkForInput(LOGIN_MOUSE_POSITION):
                    pygame.quit()
                    sys.exit()
        for button in [NEW_GAME_BUTTON, LOAD_GAME_BUTTON, SMALL_QUIT_BUTTON]:
            button.changeColor(LOGIN_MOUSE_POSITION)
            button.update(SCREEN)

        pygame.display.update()

        # if choice == '1':
        #     register()
        # elif choice == '2':
        #     load_state()
        #     main_menu()
        # else:
        #     print('Wrong option')
        #     time.sleep(1)
        #     login_menu()


def main_menu():
    global counter, last_time_ms
    '''
    REMOVER !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    '''

    username = 'Mizuhara6'
    # username = player.name
    rows = db.execute("SELECT * FROM user_data WHERE username = :username",
                      username=username)
    print(rows[0])

    # input('aqui 5')
    player.name = rows[0]['username']
    player.level = rows[0]['level']
    player.xp = rows[0]['experience']
    player.total_life = rows[0]['total_life']
    player.life = rows[0]['life']
    player.attack = rows[0]['attack']
    player.defense = rows[0]['defense']
    player.shaman = rows[0]['shaman']
    player.crit_chance = rows[0]['crit_chance']
    player.crit_damage = rows[0]['crit_damage']
    player.magic_find = rows[0]['magic_find']

    print(player.name, player.level)
    # Inventory
    rows2 = db.execute("SELECT * FROM inventory WHERE username = :username",
                       username=username)

    if len(rows2) < 1:
        pass


    else:
        for i in range(0, len(rows2)):
            new_item = Item(rows2[i]['type'], rows2[i]['name'], rows2[i]['level'],
                            rows2[i]['life'], rows2[i]['attack'],
                            rows2[i]['defense'], rows2[i]['crit_chance'],
                            rows2[i]['crit_damage'], rows2[i]['magic_find'], rows2[i]['rarity'])
            inventory.append(new_item)

    # Cards List

    rows3 = db.execute("SELECT * FROM cards_list WHERE username = :username",
                       username=username)
    if len(rows3) < 1:
        pass
    else:
        for i in range(0, len(rows3)):
            new_card = Card(rows3[i]['type'], rows3[i]['name'],
                            rows3[i]['status'], rows3[i]['image'],
                            rows3[i]['sound'])
            cards_list.append(new_card)


    # PlayerSlot
    row_amulet = db.execute("SELECT * FROM amulet WHERE username = :username", username=username)
    player_slot.amulet = row_amulet[0]
    row_armor = db.execute("SELECT * FROM armor WHERE username = :username", username=username)
    player_slot.armor = row_armor[0]
    row_gloves = db.execute("SELECT * FROM gloves WHERE username = :username", username=username)
    player_slot.gloves = row_gloves[0]
    row_helmet = db.execute("SELECT * FROM helmet WHERE username = :username", username=username)
    player_slot.helmet = row_helmet[0]
    row_legs = db.execute("SELECT * FROM legs WHERE username = :username", username=username)
    player_slot.legs = row_legs[0]
    row_ring1 = db.execute("SELECT * FROM ring1 WHERE username = :username", username=username)
    player_slot.ring1 = row_ring1[0]
    row_ring2 = db.execute("SELECT * FROM ring2 WHERE username = :username", username=username)
    player_slot.ring2 = row_ring2[0]
    row_second_hand = db.execute("SELECT * FROM second_hand WHERE username = :username", username=username)
    player_slot.second_hand = row_second_hand[0]
    row_weapon = db.execute("SELECT * FROM weapon WHERE username = :username", username=username)
    player_slot.weapon = row_weapon[0]
    row_boots = db.execute("SELECT * FROM boots WHERE username = :username", username=username)
    player_slot.boots = row_boots[0]

    # Consumables
    row_potion = db.execute("SELECT * FROM potion WHERE username = :username", username=username)
    potion.quantity = row_potion[0]['quantity']
    row_x_potion = db.execute("SELECT * FROM x_potion WHERE username = :username", username=username)
    x_potion.quantity = row_x_potion[0]['quantity']
    row_elixir = db.execute("SELECT * FROM elixir WHERE username = :username", username=username)
    elixir.quantity = row_elixir[0]['quantity']
    row_chaos_orb = db.execute("SELECT * FROM chaos_orb WHERE username = :username", username=username)
    chaos_orb.quantity = row_chaos_orb[0]['quantity']
    row_divine_orb = db.execute("SELECT * FROM divine_orb WHERE username = :username", username=username)
    divine_orb.quantity = row_divine_orb[0]['quantity']
    row_exalted_orb = db.execute("SELECT * FROM exalted_orb WHERE username = :username", username=username)
    exalted_orb.quantity = row_exalted_orb[0]['quantity']
    row_mirror_of_kalandra = db.execute("SELECT * FROM mirror_of_kalandra WHERE username = :username",
                                        username=username)
    mirror_of_kalandra.quantity = row_mirror_of_kalandra[0]['quantity']
    row_roulette_wheel_ticket = db.execute("SELECT * FROM roulette_wheel_ticket WHERE username = :username",
                                           username=username)
    roulette_wheel_ticket.quantity = row_roulette_wheel_ticket[0]['quantity']
    row_dense_fossil = db.execute("SELECT * FROM dense_fossil WHERE username = :username", username=username)
    dense_fossil.quantity = row_dense_fossil[0]['quantity']
    row_serrated_fossil = db.execute("SELECT * FROM serrated_fossil WHERE username = :username", username=username)
    serrated_fossil.quantity = row_serrated_fossil[0]['quantity']
    row_pristine_fossil = db.execute("SELECT * FROM pristine_fossil WHERE username = :username", username=username)
    pristine_fossil.quantity = row_pristine_fossil[0]['quantity']
    row_deft_fossil = db.execute("SELECT * FROM deft_fossil WHERE username = :username", username=username)
    deft_fossil.quantity = row_deft_fossil[0]['quantity']
    row_fractured_fossil = db.execute("SELECT * FROM fractured_fossil WHERE username = :username", username=username)
    fractured_fossil.quantity = row_fractured_fossil[0]['quantity']

    # boss instance
    row_boss_instance = db.execute("SELECT * FROM boss_instance WHERE username = :username", username=username)

    # Uniques_list
    row_uniques_list = db.execute("SELECT * FROM uniques_list WHERE username = :username", username=username)

    for i in range(0, len(row_uniques_list)):
        uniques_list.append(row_uniques_list[i]['name'])

    if row_boss_instance[0]['wiegraf1'] == 0:
        wiegraf1.status = False
    else:
        pass
    if row_boss_instance[0]['dycedarg1'] == 0:
        dycedarg1.status = False
    else:
        pass
    if row_boss_instance[0]['wiegraf2'] == 0:
        wiegraf2.status = False
    else:
        pass
    if row_boss_instance[0]['dycedarg2'] == 0:
        dycedarg2.status = False
    else:
        pass

    # Delve
    delve_rows = db.execute("SELECT * FROM delve WHERE username = :username",
                            username=username)
    Delve.depth = delve_rows[0]['depth']
    Delve.multiplier = delve_rows[0]['multiplier']

    '''
      REMOVER !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
      '''

    if player.level != 20 and dycedarg2.status is True:
        while True:
            SCREEN.blit(BG, (0, 0))

            MENU_MOUSE_POSITION = pygame.mouse.get_pos()

            menu_text1 = get_bold_font(80).render("POETACTICS", True, "White")
            menu_text2 = get_bold_font(35).render("THE IDLE RPG ADVENTURE", True, "White")

            menu_rect1 = menu_text1.get_rect(center=(640, 100))
            menu_rect2 = menu_text2.get_rect(center=(640, 160))

            START_BATTLE = Button(image=pygame.image.load("assets/images/ONE_LINE_OPTION.png"), pos=(640, 300),
                                  text_input="EXPLORE", font=get_bold_font(30), base_color="White",
                                  hovering_color=BLUE)
            INVENTORY = Button(image=pygame.image.load("assets/images/ONE_LINE_OPTION.png"), pos=(640, 355),
                               text_input="INVENTORY", font=get_bold_font(30), base_color="White", hovering_color=BLUE)
            CONSUMABLE_ITEMS = Button(image=pygame.image.load("assets/images/ONE_LINE_OPTION.png"), pos=(640, 410),
                                      text_input="CONSUMABLE ITEMS", font=get_bold_font(30), base_color="White",
                                      hovering_color=BLUE)
            PLAYER_STATUS = Button(image=pygame.image.load("assets/images/ONE_LINE_OPTION.png"), pos=(640, 465),
                                   text_input="PLAYER STATUS", font=get_bold_font(30), base_color="White",
                                   hovering_color=BLUE)
            EXTRAS = Button(image=pygame.image.load("assets/images/ONE_LINE_OPTION.png"), pos=(640, 520),
                            text_input="EXTRAS", font=get_bold_font(30), base_color="White",
                            hovering_color=BLUE)
            HELP = Button(image=pygame.image.load("assets/images/ONE_LINE_OPTION.png"), pos=(640, 575),
                          text_input="HELP", font=get_bold_font(30), base_color="White", hovering_color=BLUE)
            QUIT_BUTTON = Button(image=pygame.image.load("assets/images/ONE_LINE_OPTION.png"), pos=(640, 630),
                                 text_input="QUIT", font=get_bold_font(30), base_color="White", hovering_color=BLUE)

            #     print('1   Start Battle\n'
            #           '2   Inventory\n'
            #           '3   Consumable Items\n'
            #           '4   Player Status\n'
            #           '5   Help\n'
            #           '6   Exit Game\n')
            SCREEN.blit(menu_text1, menu_rect1)
            SCREEN.blit(menu_text2, menu_rect2)

            for button in [START_BATTLE, INVENTORY, CONSUMABLE_ITEMS, PLAYER_STATUS, EXTRAS, HELP, QUIT_BUTTON]:
                button.changeColor(MENU_MOUSE_POSITION)
                button.update(SCREEN)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if START_BATTLE.checkForInput(MENU_MOUSE_POSITION):
                        encounter()
                    if INVENTORY.checkForInput(MENU_MOUSE_POSITION):
                        if len(inventory) == 0:
                            pass
                        else:
                            show_inventory_page_1(1)  # options()
                    if CONSUMABLE_ITEMS.checkForInput(MENU_MOUSE_POSITION):
                        show_consumable_items()
                    if PLAYER_STATUS.checkForInput(MENU_MOUSE_POSITION):
                        player_status()  # play()
                    if EXTRAS.checkForInput(MENU_MOUSE_POSITION):
                        counter = 0
                        extras()
                    if HELP.checkForInput(MENU_MOUSE_POSITION):
                        pass  # options()
                    if QUIT_BUTTON.checkForInput(MENU_MOUSE_POSITION):
                        pygame.quit()
                        sys.exit()

            pygame.display.update()
    else:
        while True:
            SCREEN.blit(BG, (0, 0))

            MENU_MOUSE_POSITION = pygame.mouse.get_pos()

            menu_text1 = get_bold_font(80).render("POETACTICS", True, "White")
            menu_text2 = get_bold_font(35).render("THE IDLE RPG ADVENTURE", True, "White")

            menu_rect1 = menu_text1.get_rect(center=(640, 100))
            menu_rect2 = menu_text2.get_rect(center=(640, 160))

            START_BATTLE = Button(image=pygame.image.load("assets/images/ONE_LINE_OPTION.png"), pos=(640, 225),
                                  text_input="EXPLORE", font=get_bold_font(30), base_color="White",
                                  hovering_color=BLUE)
            INVENTORY = Button(image=pygame.image.load("assets/images/ONE_LINE_OPTION.png"), pos=(640, 280),
                               text_input="INVENTORY", font=get_bold_font(30), base_color="White", hovering_color=BLUE)
            CONSUMABLE_ITEMS = Button(image=pygame.image.load("assets/images/ONE_LINE_OPTION.png"), pos=(640, 335),
                                      text_input="CONSUMABLE ITEMS", font=get_bold_font(30), base_color="White",
                                      hovering_color=BLUE)
            PLAYER_STATUS = Button(image=pygame.image.load("assets/images/ONE_LINE_OPTION.png"), pos=(640, 390),
                                   text_input="PLAYER STATUS", font=get_bold_font(30), base_color="White",
                                   hovering_color=BLUE)
            DELVE = Button(image=pygame.image.load("assets/images/ONE_LINE_OPTION.png"), pos=(640, 445),
                           text_input="DELVE", font=get_bold_font(30), base_color="White",
                           hovering_color=BLUE)
            ENDGAME_BOSSES = Button(image=pygame.image.load("assets/images/ONE_LINE_OPTION.png"), pos=(640, 500),
                                    text_input="ENDGAME BOSSES", font=get_bold_font(30), base_color="White",
                                    hovering_color=BLUE)
            EXTRAS = Button(image=pygame.image.load("assets/images/ONE_LINE_OPTION.png"), pos=(640, 555),
                            text_input="EXTRAS", font=get_bold_font(30), base_color="White",
                            hovering_color=BLUE)
            HELP = Button(image=pygame.image.load("assets/images/ONE_LINE_OPTION.png"), pos=(640, 610),
                          text_input="HELP", font=get_bold_font(30), base_color="White", hovering_color=BLUE)
            QUIT_BUTTON = Button(image=pygame.image.load("assets/images/ONE_LINE_OPTION.png"), pos=(640, 665),
                                 text_input="QUIT", font=get_bold_font(30), base_color="White", hovering_color=BLUE)

            #     print('1   Start Battle\n'
            #           '2   Inventory\n'
            #           '3   Consumable Items\n'
            #           '4   Player Status\n'
            #           '5   Help\n'
            #           '6   Exit Game\n')
            SCREEN.blit(menu_text1, menu_rect1)
            SCREEN.blit(menu_text2, menu_rect2)

            for button in [START_BATTLE, INVENTORY, CONSUMABLE_ITEMS, PLAYER_STATUS, EXTRAS, HELP, QUIT_BUTTON,
                           DELVE, ENDGAME_BOSSES]:
                button.changeColor(MENU_MOUSE_POSITION)
                button.update(SCREEN)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if START_BATTLE.checkForInput(MENU_MOUSE_POSITION):
                        encounter()
                    if INVENTORY.checkForInput(MENU_MOUSE_POSITION):
                        if len(inventory) == 0:
                            pass
                        else:
                            show_inventory_page_1(1)  # options()
                    if CONSUMABLE_ITEMS.checkForInput(MENU_MOUSE_POSITION):
                        show_consumable_items()
                    if PLAYER_STATUS.checkForInput(MENU_MOUSE_POSITION):
                        player_status()  # play()
                    if DELVE.checkForInput(MENU_MOUSE_POSITION):
                        pygame.mixer.music.fadeout(2)
                        pygame.mixer.music.stop()
                        delve_music()
                        delve_menu()
                    if ENDGAME_BOSSES.checkForInput(MENU_MOUSE_POSITION):
                        player_status()
                    if EXTRAS.checkForInput(MENU_MOUSE_POSITION):
                        counter = 0
                        extras()
                    if HELP.checkForInput(MENU_MOUSE_POSITION):
                        pass
                    if QUIT_BUTTON.checkForInput(MENU_MOUSE_POSITION):
                        pygame.quit()
                        sys.exit()

            pygame.display.update()

    # if player.level != 20 and dycedarg2.status is True:
    #     print('1   Start Battle\n'
    #           '2   Inventory\n'
    #           '3   Consumable Items\n'
    #           '4   Player Status\n'
    #           '5   Help\n'
    #           '6   Exit Game\n')
    #     choice = (input('Select an option: '))
    #     try:
    #         if choice == '1':
    #             encounter()
    #         elif choice == '2':
    #             show_inventory()
    #         elif choice == '3':
    #             show_consumable_items()
    #         elif choice == '4':
    #             player_status()
    #         elif choice == '5':
    #             player_status()
    #         elif choice == '6':
    #             choice = input('Are you sure you want to exit the game? Press 1 to confirm or 2 to cancel: ')
    #             if choice == '1':
    #                 quit()
    #             elif choice == '2':
    #                 main_menu()
    #         else:
    #             print('Wrong option!')
    #             time.sleep(1)
    #             main_menu()
    #     except ValueError:
    #         main_menu()
    # else:
    #     choice = (input('Select an option:\n'
    #                     '1   Start Battle\n'
    #                     '2   Inventory\n'
    #                     '3   Consumable Items\n'
    #                     '4   Player Status\n'
    #                     '5   Delve\n'
    #                     '6   Endgame Bosses\n'
    #                     '7   Help\n'
    #                     '8   Exit Game\n\n'))
    #     try:
    #         if choice == '1':
    #             encounter()
    #         elif choice == '2':
    #             show_inventory()
    #         elif choice == '3':
    #             show_consumable_items()
    #         elif choice == '4':
    #             player_status()
    #         elif choice == '5':
    #             pygame.mixer.music.fadeout(2)
    #             pygame.mixer.music.stop()
    #             delve_music()
    #             delve_menu()
    #             pygame.mixer.music.fadeout(2)
    #             pygame.mixer.music.stop()
    #             background_music()
    #             main_menu()
    #         elif choice == '6':
    #             main_menu()
    #         elif choice == '7':
    #             main_menu()
    #         elif choice == '8':
    #             choice = input('Are you sure you want to exit the game? Press 1 to confirm or 2 to cancel: ')
    #             if choice == '1':
    #                 quit()
    #             elif choice == '2':
    #                 main_menu()
    #         else:
    #             print('Wrong option!')
    #             time.sleep(1)
    #             main_menu()
    #     except ValueError:
    #         main_menu()


if __name__ == '__main__':
    # Level 1 player instance
    player: Player = Player('unknown', 500, 500, 100, 100, 1, 0, 1, 15, 15, 0, PLAYER)
    player_slot = PlayerSlot(amulet=amulet_type[0],
                             armor=armor_type[0],
                             gloves=gloves_type[0],
                             helmet=helmet_type[0],
                             legs=legs_type[0],
                             ring1=ring_type[0],
                             ring2=ring_type[0],
                             second_hand=second_hand_type[0],
                             weapon=weapon_type[0],
                             boots=boots_type[0])
    # Boss instances:
    wiegraf1 = Character(
        name=characters['Wiegraf 1']['name'],
        total_life=characters['Wiegraf 1']['life'],
        life=characters['Wiegraf 1']['life'],
        attack=characters['Wiegraf 1']['attack'],
        defense=characters['Wiegraf 1']['defense'],
        level=characters['Wiegraf 1']['level'],
        xp=characters['Wiegraf 1']['xp'],
        crit_chance=characters['Wiegraf 1']['crit_chance'],
        status=characters['Wiegraf 1']['status'],
        quote1=characters['Wiegraf 1']['quote1'],
        quote2=characters['Wiegraf 1']['quote2'],
        quote3=characters['Wiegraf 1']['quote3'],
        quote4=characters['Wiegraf 1']['quote4'],
        image=characters['Wiegraf 1']['image']
    )
    dycedarg1 = Character(
        name=characters['Dycedarg 1']['name'],
        total_life=characters['Dycedarg 1']['life'],
        life=characters['Dycedarg 1']['life'],
        attack=characters['Dycedarg 1']['attack'],
        defense=characters['Dycedarg 1']['defense'],
        level=characters['Dycedarg 1']['level'],
        xp=characters['Dycedarg 1']['xp'],
        crit_chance=characters['Dycedarg 1']['crit_chance'],
        status=characters['Dycedarg 1']['status'],
        quote1=characters['Dycedarg 1']['quote1'],
        quote2=characters['Dycedarg 1']['quote2'],
        quote3=characters['Dycedarg 1']['quote3'],
        quote4=characters['Dycedarg 1']['quote4'],
        image=characters['Dycedarg 1']['image']
    )
    wiegraf2 = Character(
        name=characters['Wiegraf 2']['name'],
        total_life=characters['Wiegraf 2']['life'],
        life=characters['Wiegraf 2']['life'],
        attack=characters['Wiegraf 2']['attack'],
        defense=characters['Wiegraf 2']['defense'],
        level=characters['Wiegraf 2']['level'],
        xp=characters['Wiegraf 2']['xp'],
        crit_chance=characters['Wiegraf 2']['crit_chance'],
        status=characters['Wiegraf 2']['status'],
        quote1=characters['Wiegraf 2']['quote1'],
        quote2=characters['Wiegraf 2']['quote2'],
        quote3=characters['Wiegraf 2']['quote3'],
        quote4=characters['Wiegraf 2']['quote4'],
        image=characters['Wiegraf 2']['image']
    )
    dycedarg2 = Character(
        name=characters['Dycedarg 2']['name'],
        total_life=characters['Dycedarg 2']['life'],
        life=characters['Dycedarg 2']['life'],
        attack=characters['Dycedarg 2']['attack'],
        defense=characters['Dycedarg 2']['defense'],
        level=characters['Dycedarg 2']['level'],
        xp=characters['Dycedarg 2']['xp'],
        crit_chance=characters['Dycedarg 2']['crit_chance'],
        status=characters['Dycedarg 2']['status'],
        quote1=characters['Dycedarg 2']['quote1'],
        quote2=characters['Dycedarg 2']['quote2'],
        quote3=characters['Dycedarg 2']['quote3'],
        quote4=characters['Dycedarg 2']['quote4'],
        image=characters['Dycedarg 2']['image']
    )

    # Consumables intances:
    potion = ConsumableItem(consumables['potion']['type'], consumables['potion']['name'],
                            consumables['potion']['value'], consumables['potion']['quantity'],
                            consumables['potion']['rarity'], consumables['potion']['code'],
                            consumables['potion']['sound'])
    hi_potion = ConsumableItem(consumables['hi-potion']['type'], consumables['hi-potion']['name'],
                               consumables['hi-potion']['value'], consumables['hi-potion']['quantity'],
                               consumables['hi-potion']['rarity'], consumables['hi-potion']['code'],
                               consumables['hi-potion']['sound'])
    x_potion = ConsumableItem(consumables['x-potion']['type'], consumables['x-potion']['name'],
                              consumables['x-potion']['value'], consumables['x-potion']['quantity'],
                              consumables['x-potion']['rarity'], consumables['x-potion']['code'],
                              consumables['x-potion']['sound'])
    elixir = ConsumableItem(consumables['elixir']['type'], consumables['elixir']['name'],
                            consumables['elixir']['value'], consumables['elixir']['quantity'],
                            consumables['elixir']['rarity'], consumables['elixir']['code'],
                            consumables['elixir']['sound'])
    chaos_orb = ConsumableItem(consumables['chaos orb']['type'], consumables['chaos orb']['name'],
                               consumables['chaos orb']['value'], consumables['chaos orb']['quantity'],
                               consumables['chaos orb']['rarity'], consumables['chaos orb']['code'],
                               consumables['chaos orb']['sound'])
    divine_orb = ConsumableItem(consumables['divine orb']['type'], consumables['divine orb']['name'],
                                consumables['divine orb']['value'], consumables['divine orb']['quantity'],
                                consumables['divine orb']['rarity'], consumables['divine orb']['code'],
                                consumables['divine orb']['sound'])
    exalted_orb = ConsumableItem(consumables['exalted orb']['type'], consumables['exalted orb']['name'],
                                 consumables['exalted orb']['value'], consumables['exalted orb']['quantity'],
                                 consumables['exalted orb']['rarity'], consumables['exalted orb']['code'],
                                 consumables['exalted orb']['sound'])
    mirror_of_kalandra = ConsumableItem(consumables['mirror of kalandra']['type'],
                                        consumables['mirror of kalandra']['name'],
                                        consumables['mirror of kalandra']['value'],
                                        consumables['mirror of kalandra']['quantity'],
                                        consumables['mirror of kalandra']['rarity'],
                                        consumables['mirror of kalandra']['code'],
                                        consumables['mirror of kalandra']['sound'])
    roulette_wheel_ticket = ConsumableItem(consumables['roulette_wheel_ticket']['type'],
                                           consumables['roulette_wheel_ticket']['name'],
                                           consumables['roulette_wheel_ticket']['value'],
                                           consumables['roulette_wheel_ticket']['quantity'],
                                           consumables['roulette_wheel_ticket']['rarity'],
                                           consumables['roulette_wheel_ticket']['code'],
                                           consumables['roulette_wheel_ticket']['sound'])
    # Fossiles
    dense_fossil = Fossil(consumables['dense fossil']['type'],
                          consumables['dense fossil']['name'],
                          consumables['dense fossil']['value'],
                          consumables['dense fossil']['quantity'],
                          consumables['dense fossil']['rarity'],
                          consumables['dense fossil']['code'],
                          consumables['dense fossil']['sound'],
                          consumables['dense fossil']['attribute'])
    serrated_fossil = Fossil(consumables['serrated fossil']['type'],
                             consumables['serrated fossil']['name'],
                             consumables['serrated fossil']['value'],
                             consumables['serrated fossil']['quantity'],
                             consumables['serrated fossil']['rarity'],
                             consumables['serrated fossil']['code'],
                             consumables['serrated fossil']['sound'],
                             consumables['serrated fossil']['attribute'])
    pristine_fossil = Fossil(consumables['pristine fossil']['type'],
                             consumables['pristine fossil']['name'],
                             consumables['pristine fossil']['value'],
                             consumables['pristine fossil']['quantity'],
                             consumables['pristine fossil']['rarity'],
                             consumables['pristine fossil']['code'],
                             consumables['pristine fossil']['sound'],
                             consumables['pristine fossil']['attribute'])
    deft_fossil = Fossil(consumables['deft fossil']['type'],
                         consumables['deft fossil']['name'],
                         consumables['deft fossil']['value'],
                         consumables['deft fossil']['quantity'],
                         consumables['deft fossil']['rarity'],
                         consumables['deft fossil']['code'],
                         consumables['deft fossil']['sound'],
                         consumables['deft fossil']['attribute'])
    fractured_fossil = Fossil(consumables['fractured fossil']['type'],
                              consumables['fractured fossil']['name'],
                              consumables['fractured fossil']['value'],
                              consumables['fractured fossil']['quantity'],
                              consumables['fractured fossil']['rarity'],
                              consumables['fractured fossil']['code'],
                              consumables['fractured fossil']['sound'],
                              consumables['fractured fossil']['attribute'])
    background_music()

    # login_menu()
    main_menu()
