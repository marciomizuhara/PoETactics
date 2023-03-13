import consumable_item
from character import *
from player_status import *
from unique import *
from levels_xp import *
from items.amulets import *
from items.armors import *
from items.boots import *
from items.gloves import *
from items.helmets import *
from items.legs import *
from items.rings import *
from items.second_hands import *
from items.gear_type import *
from items.uniques import *
from items.weapons import *
from battle import *
from roulette_wheel import *
from inventory import *

pygame.init()
clock = pygame.time.Clock()
clock.tick(FPS)




# Importing globals
globals_variables.global_containers()

# Temp variables
temp_gear_drop = []

temp_unique_drop = []
temp_consumable_drop = []
temp_ticket_drop = []
# temp_card_drop = []

temp_level_up = False


# Main containers


# cards_list = []

main_menu_setter = True

def counter_helper(counter):
    counter_text = get_bold_font(40).render(f'{counter}', True, WHITE)
    counter_text_rect = counter_text.get_rect(center=(SCREEN_WIDTH / 2, 30))
    SCREEN.blit(counter_text, counter_text_rect)


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





def show_item(item_index, item):
    ITEM_IMAGE = pygame.transform.scale(pygame.image.load(item.image), (200, 200))
    print(item.name, item.image)
    SCREEN.blit(BG, (0, 0))
    SCREEN.blit(BATTLE_BOX, (60, 40))
    SCREEN.blit(ITEM_IMAGE, (500, 200))

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
    global counter, LAST_TIME_MS
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

        diff_time_ms = int(round(time.time() * 4000)) - LAST_TIME_MS
        if diff_time_ms >= 4000:
            counter = counter + 1
            LAST_TIME_MS = int(round(time.time() * 4000))

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
                            if sorted_inventory[i].__dict__['rarity'] == 'unique':
                                fossil_reforge_cannot_reforge(sorted_inventory[i].__dict__, 1, consumable_type)
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
                            if sorted_inventory[i].__dict__['rarity'] == 'unique':
                                fossil_reforge_cannot_reforge(sorted_inventory[i].__dict__, 2, consumable_type)
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
                            if sorted_inventory[i].__dict__['rarity'] == 'unique':
                                fossil_reforge_cannot_reforge(sorted_inventory[i].__dict__, 3, consumable_type)
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
                            if sorted_inventory[i].__dict__['rarity'] == 'unique':
                                fossil_reforge_cannot_reforge(sorted_inventory[i].__dict__, 4, consumable_type)
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








def draw_player_level_up():
    global temp_level_up, counter, LAST_TIME_MS
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

            CONTINUE = Button(image=pygame.image.load("assets/images/Smallest Rect.png"),
                              pos=(SCREEN_WIDTH / 2 - 180, 550),
                              text_input="CONTINUE", font=get_bold_font(30), base_color="White", hovering_color=BLUE)

            diff_time_ms = int(round(time.time() * 4000)) - LAST_TIME_MS
            if diff_time_ms >= 4000:
                counter = counter + 1
                LAST_TIME_MS = int(round(time.time() * 4000))

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
                    item_type[0]['image'],
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
                                  drop['image'],
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
    global LAST_TIME_MS, counter, slot_item

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
                        to_inventory['rarity'],
                        to_inventory['image']
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
                        to_inventory['rarity'],
                        to_inventory['image']
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
                        to_inventory['rarity'],
                        to_inventory['image']
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

        diff_time_ms = int(round(time.time() * 4000)) - LAST_TIME_MS
        if diff_time_ms >= 4000:
            counter = counter + 1
            LAST_TIME_MS = int(round(time.time() * 4000))

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
    global counter, LAST_TIME_MS
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

        diff_time_ms = int(round(time.time() * 4000)) - LAST_TIME_MS

        if diff_time_ms >= 4000:
            counter = counter + 1
            LAST_TIME_MS = int(round(time.time() * 4000))
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


def fossil_reforge_cannot_reforge(item, inventory_page, consumable_type):
    SCREEN.blit(BG, (0, 0))
    SCREEN.blit(BATTLE_BOX, (60, 40))
    display_level_xp()
    confirm_text1 = get_bold_font(35).render(
        f"Unique items cannot be reforged!", True, YELLOW)
    confirm_text1_rect = confirm_text1.get_rect(center=(SCREEN_WIDTH / 2 - 180, 320))
    # text2 = get_bold_font(25).render(f'(10% chance for the item to get destroyed)', True, WHITE)
    # text2_rect = text2.get_rect(center=(SCREEN_WIDTH / 2 - 180, 520))
    SCREEN.blit(confirm_text1, confirm_text1_rect)


    while True:
        USE_FOSSIL_MOUSE_POSITION = pygame.mouse.get_pos()
        BUTTONS = main_menu_structure(USE_FOSSIL_MOUSE_POSITION)
        BACK = Button(image=pygame.image.load("assets/images/Smallest Rect.png"), pos=(SCREEN_WIDTH / 2 - 180, 390),
                          text_input="BACK", font=get_bold_font(30), base_color="White", hovering_color=BLUE)
        BUTTONS.append(BACK)

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
                if BACK.checkForInput(USE_FOSSIL_MOUSE_POSITION):
                    if inventory_page == 1:
                        show_inventory_page_1(consumable_type)
                    elif inventory_page == 2:
                        show_inventory_page_2(consumable_type)
                    elif inventory_page == 3:
                        show_inventory_page_3(consumable_type)
                    elif inventory_page == 4:
                        show_inventory_page_4(consumable_type)

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
        "INSERT INTO inventory (username, name, type, level, life, attack, defense, crit_chance, crit_damage, magic_find, rarity, image)"
        "VALUES (:username, :name, :type, :level, :life, :attack, :defense, :crit_chance, :crit_damage, :magic_find, :rarity, :image)",
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
        rarity=new_item.__dict__['rarity'],
        image = new_item.__dict__['image'])


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








# def show_dialogue(character, quote):
#     global counter, LAST_TIME_MS
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
#         diff_time_ms = int(round(time.time() * 4000)) - LAST_TIME_MS
#         if diff_time_ms >= 4000:
#             counter = counter + 1
#             LAST_TIME_MS = int(round(time.time() * 4000))
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






def inventory_update(username, item):
    if len(inventory) == 0:
        pass
    else:

        db.execute(
            "INSERT INTO inventory (username, name, type, level, life, attack, defense, crit_chance,"
            "crit_damage, magic_find, rarity, image) VALUES (:username, :name, :type, :level, :life, :attack, :defense,"
            ":crit_chance, :crit_damage, :magic_find, :rarity, :image)",
            username=username, name=item.name, type=item.type,
            level=item.level, life=item.life,
            attack=item.attack, defense=item.defense,
            crit_chance=item.crit_chance, crit_damage=item.crit_damage,
            magic_find=item.magic_find, rarity=item.rarity, image=item.image)


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
        "INSERT INTO amulet (username, name, type, level, life, attack, defense, crit_chance, crit_damage, magic_find, rarity, image) VALUES (:username, :name, :type, :level, :life, :attack, :defense, :crit_chance, :crit_damage, :magic_find, :rarity, :image)",
        username=player.name, name=player_slot.amulet['name'], type=player_slot.amulet['type'],
        level=player_slot.amulet['level'], life=player_slot.amulet['life'],
        attack=player_slot.amulet['attack'], defense=player_slot.amulet['defense'],
        crit_chance=player_slot.amulet['crit_chance'], crit_damage=player_slot.amulet['crit_damage'],
        magic_find=player_slot.amulet['magic_find'], rarity=player_slot.amulet['rarity'], image=player_slot.amulet['image'])
    db.execute("DELETE FROM armor WHERE username = :username",
               username=username)
    db.execute(
        "INSERT INTO armor (username, name, type, level, life, attack, defense, crit_chance, crit_damage, magic_find, rarity, image) VALUES (:username, :name, :type, :level, :life, :attack, :defense, :crit_chance, :crit_damage, :magic_find, :rarity, :image)",
        username=player.name, name=player_slot.armor['name'], type=player_slot.armor['type'],
        level=player_slot.armor['level'], life=player_slot.armor['life'],
        attack=player_slot.armor['attack'], defense=player_slot.armor['defense'],
        crit_chance=player_slot.armor['crit_chance'], crit_damage=player_slot.armor['crit_damage'],
        magic_find=player_slot.armor['magic_find'], rarity=player_slot.armor['rarity'], image=player_slot.armor['image'])
    db.execute("DELETE FROM gloves WHERE username = :user"
               "name",
               username=username)
    db.execute(
        "INSERT INTO gloves (username, name, type, level, life, attack, defense, crit_chance, crit_damage, magic_find, rarity, image) VALUES (:username, :name, :type, :level, :life, :attack, :defense, :crit_chance, :crit_damage, :magic_find, :rarity, :image)",
        username=player.name, name=player_slot.gloves['name'], type=player_slot.gloves['type'],
        level=player_slot.gloves['level'], life=player_slot.gloves['life'],
        attack=player_slot.gloves['attack'], defense=player_slot.gloves['defense'],
        crit_chance=player_slot.gloves['crit_chance'], crit_damage=player_slot.gloves['crit_damage'],
        magic_find=player_slot.gloves['magic_find'], rarity=player_slot.gloves['rarity'], image=player_slot.gloves['image'])
    db.execute("DELETE FROM helmet WHERE username = :username",
               username=username)
    db.execute(
        "INSERT INTO helmet (username, name, type, level, life, attack, defense, crit_chance, crit_damage, magic_find, rarity, image) VALUES (:username, :name, :type, :level, :life, :attack, :defense, :crit_chance, :crit_damage, :magic_find, :rarity, :image)",
        username=player.name, name=player_slot.helmet['name'], type=player_slot.helmet['type'],
        level=player_slot.helmet['level'], life=player_slot.helmet['life'],
        attack=player_slot.helmet['attack'], defense=player_slot.helmet['defense'],
        crit_chance=player_slot.helmet['crit_chance'], crit_damage=player_slot.helmet['crit_damage'],
        magic_find=player_slot.helmet['magic_find'], rarity=player_slot.helmet['rarity'], image=player_slot.helmet['image'])
    db.execute("DELETE FROM legs WHERE username = :username",
               username=username)
    db.execute(
        "INSERT INTO legs (username, name, type, level, life, attack, defense, crit_chance, crit_damage, magic_find, rarity, image) VALUES (:username, :name, :type, :level, :life, :attack, :defense, :crit_chance, :crit_damage, :magic_find, :rarity, :image)",
        username=player.name, name=player_slot.legs['name'], type=player_slot.legs['type'],
        level=player_slot.legs['level'], life=player_slot.legs['life'],
        attack=player_slot.legs['attack'], defense=player_slot.legs['defense'],
        crit_chance=player_slot.legs['crit_chance'], crit_damage=player_slot.legs['crit_damage'],
        magic_find=player_slot.legs['magic_find'], rarity=player_slot.legs['rarity'], image=player_slot.legs['image'])
    db.execute("DELETE FROM ring1 WHERE username = :username",
               username=username)
    db.execute(
        "INSERT INTO ring1 (username, name, type, level, life, attack, defense, crit_chance, crit_damage, magic_find, rarity, image) VALUES (:username, :name, :type, :level, :life, :attack, :defense, :crit_chance, :crit_damage, :magic_find, :rarity, :image)",
        username=player.name, name=player_slot.ring1['name'], type=player_slot.ring1['type'],
        level=player_slot.ring1['level'], life=player_slot.ring1['life'],
        attack=player_slot.ring1['attack'], defense=player_slot.ring1['defense'],
        crit_chance=player_slot.ring1['crit_chance'], crit_damage=player_slot.ring1['crit_damage'],
        magic_find=player_slot.ring1['magic_find'], rarity=player_slot.ring1['rarity'], image=player_slot.ring1['image'])
    db.execute("DELETE FROM ring2 WHERE username = :username",
               username=username)
    db.execute(
        "INSERT INTO ring2 (username, name, type, level, life, attack, defense, crit_chance, crit_damage, magic_find, rarity, image) VALUES (:username, :name, :type, :level, :life, :attack, :defense, :crit_chance, :crit_damage, :magic_find, :rarity, :image)",
        username=player.name, name=player_slot.ring2['name'], type=player_slot.ring2['type'],
        level=player_slot.ring2['level'], life=player_slot.ring2['life'],
        attack=player_slot.ring2['attack'], defense=player_slot.ring2['defense'],
        crit_chance=player_slot.ring2['crit_chance'], crit_damage=player_slot.ring2['crit_damage'],
        magic_find=player_slot.ring2['magic_find'], rarity=player_slot.ring2['rarity'], image=player_slot.ring2['image'])
    db.execute("DELETE FROM second_hand WHERE username = :username",
               username=username)
    db.execute(
        "INSERT INTO second_hand (username, name, type, level, life, attack, defense, crit_chance, crit_damage, magic_find, rarity, image) VALUES (:username, :name, :type, :level, :life, :attack, :defense, :crit_chance, :crit_damage, :magic_find, :rarity, :image)",
        username=player.name, name=player_slot.second_hand['name'], type=player_slot.second_hand['type'],
        level=player_slot.second_hand['level'], life=player_slot.second_hand['life'],
        attack=player_slot.second_hand['attack'], defense=player_slot.second_hand['defense'],
        crit_chance=player_slot.second_hand['crit_chance'], crit_damage=player_slot.second_hand['crit_damage'],
        magic_find=player_slot.second_hand['magic_find'], rarity=player_slot.second_hand['rarity'], image=player_slot.second_hand['image'])
    db.execute("DELETE FROM weapon WHERE username = :username",
               username=username)
    db.execute(
        "INSERT INTO weapon (username, name, type, level, life, attack, defense, crit_chance, crit_damage, magic_find, rarity, image) VALUES (:username, :name, :type, :level, :life, :attack, :defense, :crit_chance, :crit_damage, :magic_find, :rarity, :image)",
        username=player.name, name=player_slot.weapon['name'], type=player_slot.weapon['type'],
        level=player_slot.weapon['level'], life=player_slot.weapon['life'],
        attack=player_slot.weapon['attack'], defense=player_slot.weapon['defense'],
        crit_chance=player_slot.weapon['crit_chance'], crit_damage=player_slot.weapon['crit_damage'],
        magic_find=player_slot.weapon['magic_find'], rarity=player_slot.weapon['rarity'], image=player_slot.weapon['image'])
    db.execute("DELETE FROM boots WHERE username = :username",
               username=username)
    db.execute(
        "INSERT INTO boots (username, name, type, level, life, attack, defense, crit_chance, crit_damage, magic_find, rarity, image) VALUES (:username, :name, :type, :level, :life, :attack, :defense, :crit_chance, :crit_damage, :magic_find, :rarity, :image)",
        username=player.name, name=player_slot.boots['name'], type=player_slot.boots['type'],
        level=player_slot.boots['level'], life=player_slot.boots['life'],
        attack=player_slot.boots['attack'], defense=player_slot.boots['defense'],
        crit_chance=player_slot.boots['crit_chance'], crit_damage=player_slot.boots['crit_damage'],
        magic_find=player_slot.boots['magic_find'], rarity=player_slot.boots['rarity'], image=player_slot.boots['image'])

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
                            rows2[i]['crit_damage'], rows2[i]['magic_find'], rows2[i]['rarity'], rows[i]['image'])
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
    global counter, LAST_TIME_MS, player
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

        diff_time_ms = int(round(time.time() * 4000)) - LAST_TIME_MS
        if diff_time_ms >= 4000:
            counter = counter + 1
            LAST_TIME_MS = int(round(time.time() * 4000))

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
    global counter, LAST_TIME_MS
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

        diff_time_ms = int(round(time.time() * 4000)) - LAST_TIME_MS
        if diff_time_ms >= 4000:
            counter = counter + 1
            LAST_TIME_MS = int(round(time.time() * 4000))

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
    global counter, LAST_TIME_MS, player
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

        diff_time_ms = int(round(time.time() * 4000)) - LAST_TIME_MS
        if diff_time_ms >= 4000:
            counter = counter + 1
            LAST_TIME_MS = int(round(time.time() * 4000))

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
    global counter, LAST_TIME_MS

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

        diff_time_ms = int(round(time.time() * 4000)) - LAST_TIME_MS
        if diff_time_ms >= 4000:
            counter = counter + 1
            LAST_TIME_MS = int(round(time.time() * 4000))

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
    global counter, LAST_TIME_MS

    while True:
        SCREEN.fill(BLACK)
        pygame.display.set_caption("PoeTactics")

        text_1 = get_bold_font(50).render('Username already exists', True, WHITE)
        menu_rect_1 = text_1.get_rect(center=(SCREEN_WIDTH / 2, 300))

        SCREEN.blit(text_1, menu_rect_1)

        diff_time_ms = int(round(time.time() * 4000)) - LAST_TIME_MS
        if diff_time_ms >= 4000:
            counter = counter + 1
            LAST_TIME_MS = int(round(time.time() * 4000))

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
        LOAD_GAME_BUTTON = Button(image=pygame.image.load("assets/images/Options Rect.png"),
                                  pos=(SCREEN_WIDTH / 2, 350),
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


def main_menu():
    global counter, LAST_TIME_MS, main_menu_setter

    if main_menu_setter:
        print('main menu setter ')
        # print('dycegadr2 ', dycedarg2.__dict__)
        '''
        REMOVER !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
        '''
        from character import set_boss_instances
        wiegraf1, wiegraf2, dycedard1, dycedarg2 = set_boss_instances()
        username = 'Mizuhara1'
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
            print('rows 2 aqui', rows2)
            for i in range(0, len(rows2)):
                new_item = Item(rows2[i]['type'], rows2[i]['name'], rows2[i]['level'],
                                rows2[i]['life'], rows2[i]['attack'],
                                rows2[i]['defense'], rows2[i]['crit_chance'],
                                rows2[i]['crit_damage'], rows2[i]['magic_find'], rows2[i]['rarity'], rows2[i]['image'])
                inventory.append(new_item)


        # Cards List
        card_instance_load(player.name)

        # duplicate = duplicate_prevention(player.name, 'Squire')
        # if duplicate == 0:
        #     print('não tem card, tem q addar')
        #     add_card(player.name, card_collection[0])

        # rows3 = db.execute("SELECT * FROM cards_list WHERE username = :username",
        #                    username=username)
        # if len(rows3) < 1:
        #     pass
        # else:
        #     for i in range(0, len(rows3)):
        #         new_card = Card(rows3[i]['type'], rows3[i]['name'], rows3[i]['status'], rows3[i]['life'],
        #                         rows3[i]['attack'],
        #                         rows3[i]['defense'], rows3[i]['crit_chance'], rows3[i]['crit_damage'],
        #                         rows3[i]['magic_find'], rows3[i]['level'], rows3[i]['rarity'], rows3[i]['image'],
        #                         rows3[i]['sound'])
        #         globals_variables.cards_list.append(new_card)
        # print('inicialização de cards', globals_variables.cards_list)

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
        row_card = db.execute("SELECT * FROM card WHERE username = :username", username=username)
        player_slot.card = row_card[0]
        # Consumables
        row_potion = db.execute("SELECT * FROM potion WHERE username = :username", username=username)
        consumable_item.potion.quantity = row_potion[0]['quantity']
        row_x_potion = db.execute("SELECT * FROM x_potion WHERE username = :username", username=username)
        consumable_item.x_potion.quantity = row_x_potion[0]['quantity']
        row_elixir = db.execute("SELECT * FROM elixir WHERE username = :username", username=username)
        consumable_item.elixir.quantity = row_elixir[0]['quantity']
        row_chaos_orb = db.execute("SELECT * FROM chaos_orb WHERE username = :username", username=username)
        consumable_item.chaos_orb.quantity = row_chaos_orb[0]['quantity']
        row_divine_orb = db.execute("SELECT * FROM divine_orb WHERE username = :username", username=username)
        consumable_item.divine_orb.quantity = row_divine_orb[0]['quantity']
        row_exalted_orb = db.execute("SELECT * FROM exalted_orb WHERE username = :username", username=username)
        consumable_item.exalted_orb.quantity = row_exalted_orb[0]['quantity']
        row_mirror_of_kalandra = db.execute("SELECT * FROM mirror_of_kalandra WHERE username = :username",
                                            username=username)
        consumable_item.mirror_of_kalandra.quantity = row_mirror_of_kalandra[0]['quantity']
        row_roulette_wheel_ticket = db.execute("SELECT * FROM roulette_wheel_ticket WHERE username = :username",
                                               username=username)
        consumable_item.roulette_wheel_ticket.quantity = row_roulette_wheel_ticket[0]['quantity']
        row_dense_fossil = db.execute("SELECT * FROM dense_fossil WHERE username = :username", username=username)
        dense_fossil.quantity = row_dense_fossil[0]['quantity']
        row_serrated_fossil = db.execute("SELECT * FROM serrated_fossil WHERE username = :username", username=username)
        serrated_fossil.quantity = row_serrated_fossil[0]['quantity']
        row_pristine_fossil = db.execute("SELECT * FROM pristine_fossil WHERE username = :username", username=username)
        pristine_fossil.quantity = row_pristine_fossil[0]['quantity']
        row_deft_fossil = db.execute("SELECT * FROM deft_fossil WHERE username = :username", username=username)
        deft_fossil.quantity = row_deft_fossil[0]['quantity']
        row_fractured_fossil = db.execute("SELECT * FROM fractured_fossil WHERE username = :username",
                                          username=username)
        fractured_fossil.quantity = row_fractured_fossil[0]['quantity']

        # boss instance
        row_boss_instance = db.execute("SELECT * FROM boss_instance WHERE username = :username", username=username)

        # card instance
        # row_card_instance = db.execute("SELECT * FROM card_instance WHERE username = :username", username=username)

        # Uniques_list
        row_uniques_list = db.execute("SELECT * FROM uniques_list WHERE username = :username", username=username)

        for i in range(0, len(row_uniques_list)):
            uniques_list.append(row_uniques_list[i]['name'])
        load_boss_instances(player.name)
        # if row_boss_instance[0]['wiegraf1'] == 0:
        #     wiegraf1.status = False
        # else:
        #     pass
        # if row_boss_instance[0]['dycedarg1'] == 0:
        #     dycedarg1.status = False
        # else:
        #     pass
        # if row_boss_instance[0]['wiegraf2'] == 0:
        #     wiegraf2.status = False
        # else:
        #     pass
        # if row_boss_instance[0]['dycedarg2'] == 0:
        #     dycedarg2.status = False
        # else:
        #     pass

        # Delve
        delve_rows = db.execute("SELECT * FROM delve WHERE username = :username",
                                username=username)
        Delve.depth = delve_rows[0]['depth']
        Delve.multiplier = delve_rows[0]['multiplier']

        '''
          REMOVER !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
          '''
        main_menu_setter = False
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
                        from battle import encounter
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



if __name__ == '__main__':
    background_music()

    # login_menu()
    main_menu()
