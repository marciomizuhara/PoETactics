import sys, pygame
from assets.fonts.fonts import *
from classes import card
from classes import consumable_item_
from classes import item_
from classes import main_menu
from classes import player_
from classes import player_slot_
from classes import player_status_
from classes import save_load
from settings import *
from button import *


inventory = []
temp_gear_change = []
temp_gear_change_inventory = []


def change_gear():
    global temp_gear_change, temp_gear_change_inventory
    if temp_gear_change[0]['type'] == 'card':
        card.cards('player_status')
    else:
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
            BUTTONS = main_menu.main_menu_structure(CHANGE_GEAR_MOUSE_POSITION)

            BACK = Button(image=pygame.image.load("assets/images/Smallest Rect.png"), pos=(180, 600),
                          text_input="BACK", font=get_bold_font(30), base_color="White", hovering_color=BLUE)
            BUTTONS.append(BACK)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    main_menu.main_menu_structure_events(CHANGE_GEAR_MOUSE_POSITION, BUTTONS)
                    if BACK.checkForInput(CHANGE_GEAR_MOUSE_POSITION):
                        player_status_.player_status()
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



def equip_update_status(item):
    player_.player.total_life = player_.player.total_life + int(item.life)
    player_.player.attack = player_.player.attack + int(item.attack)
    player_.player.defense = player_.player.defense + int(item.defense)
    player_.player.crit_chance = player_.player.crit_chance + int(item.crit_chance)
    player_.player.crit_damage = player_.player.crit_damage + int(item.crit_damage)
    player_.player.magic_find = player_.player.magic_find + item.magic_find


def unequip_update_status(item):
    player_.player.total_life = player_.player.total_life - int(item.life)
    player_.player.attack = player_.player.attack - int(item.attack)
    player_.player.defense = player_.player.defense - int(item.defense)
    player_.player.crit_chance = player_.player.crit_chance - int(item.crit_chance)
    player_.player.crit_damage = player_.player.crit_damage - int(item.crit_damage)
    player_.player.magic_find = player_.player.magic_find - item.magic_find


def delete_item_confirmation(item_index, item):
    global counter
    SCREEN.blit(BG, (0, 0))
    SCREEN.blit(BATTLE_BOX, (60, 40))
    player_.display_level_xp()

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
        BUTTONS = main_menu.main_menu_structure(DELETE_ITEM_CONFIRMATION_MOUSE_POSITION)
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
                main_menu.main_menu_structure_events(DELETE_ITEM_CONFIRMATION_MOUSE_POSITION, BUTTONS)
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
    player_.display_level_xp()
    delete_setter = False
    row = db.execute("SELECT * FROM inventory WHERE username = :username AND name = :name AND level = :level",
                     username=player_.player.name,
                     name=item.__dict__['name'],
                     level=item.__dict__['level'])
    id = (row[0]['id'])
    db.execute("DELETE FROM inventory WHERE id = :id",
               id=id)
    inventory.clear()
    save_load.save_state()

    save_load.load_state()

    temp_level_up = False
    while True:
        confirm_text1 = get_bold_font(40).render(
            f"{item.__dict__['name']} level {item.__dict__['level']} deleted!", True, RED)
        confirm_text1_rect = confirm_text1.get_rect(center=(SCREEN_WIDTH / 2 - 180, 280))

        DELETE_ITEM_MOUSE_POSITION = pygame.mouse.get_pos()
        BUTTONS = main_menu.main_menu_structure(DELETE_ITEM_MOUSE_POSITION)
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
                main_menu.main_menu_structure_events(DELETE_ITEM_MOUSE_POSITION, BUTTONS)
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
        BUTTONS = main_menu.main_menu_structure(ITEM_DISP_MOUSE_POSITION)
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
                main_menu.main_menu_structure_events(ITEM_DISP_MOUSE_POSITION, BUTTONS)
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


def ring_slot_confirmation(item_index, item):
    SCREEN.blit(BG, (0, 0))
    SCREEN.blit(BATTLE_BOX, (60, 40))

    # Ring slot 1
    ring1 = get_bold_font(30).render(f"{player_slot_.player_slot.ring1['name']}", True, WHITE)
    level_ring1 = get_regular_font(20).render(f"level {player_slot_.player_slot.ring1['level']}", True, WHITE)
    type_ring1 = get_bold_font(20).render(f"Type: {player_slot_.player_slot.ring1['type']}", True, WHITE)
    life_ring1 = get_bold_font(20).render(f"Life: {player_slot_.player_slot.ring1['life']}", True, WHITE)
    attack_ring1 = get_bold_font(20).render(f"Attack: {player_slot_.player_slot.ring1['attack']}", True, WHITE)
    defense_ring1 = get_bold_font(20).render(f"Defense: {player_slot_.player_slot.ring1['defense']}", True, WHITE)
    crit_chance_ring1 = get_bold_font(20).render(f"Critical Chance: {round((player_slot_.player_slot.ring1['crit_chance']), 2)} %",
                                                 True, WHITE)
    crit_damage_ring1 = get_bold_font(20).render(f"Critical Damage: {round((player_slot_.player_slot.ring1['crit_damage']), 2)} %",
                                                 True, WHITE)
    magic_find_ring1 = get_bold_font(20).render(f"Magic Find: {round((player_slot_.player_slot.ring1['magic_find'] * 100), 2)} %",
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
    ring2 = get_bold_font(30).render(f"{player_slot_.player_slot.ring2['name']}", True, WHITE)
    level_ring2 = get_regular_font(20).render(f"level {player_slot_.player_slot.ring2['level']}", True, WHITE)
    type_ring2 = get_bold_font(20).render(f"Type: {player_slot_.player_slot.ring2['type']}", True, WHITE)
    life_ring2 = get_bold_font(20).render(f"Life: {player_slot_.player_slot.ring2['life']}", True, WHITE)
    attack_ring2 = get_bold_font(20).render(f"Attack: {player_slot_.player_slot.ring2['attack']}", True, WHITE)
    defense_ring2 = get_bold_font(20).render(f"Defense: {player_slot_.player_slot.ring2['defense']}", True, WHITE)
    crit_chance_ring2 = get_bold_font(20).render(f"Critical Chance: {round((player_slot_.player_slot.ring2['crit_chance']), 2)} %",
                                                 True, WHITE)
    crit_damage_ring2 = get_bold_font(20).render(f"Critical Damage: {round((player_slot_.player_slot.ring2['crit_damage']), 2)} %",
                                                 True, WHITE)
    magic_find_ring2 = get_bold_font(20).render(f"Magic Find: {round((player_slot_.player_slot.ring1['magic_find'] * 100), 2)} %",
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
        BUTTONS = main_menu.main_menu_structure(ITEM_DISP_MOUSE_POSITION)
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
                main_menu.main_menu_structure_events(ITEM_DISP_MOUSE_POSITION, BUTTONS)
                if RING_SLOT_1.checkForInput(ITEM_DISP_MOUSE_POSITION):
                    equip_item(item_index, item, 1)
                if RING_SLOT_2.checkForInput(ITEM_DISP_MOUSE_POSITION):
                    equip_item(item_index, item, 2)

        for button in BUTTONS:
            button.changeColor(ITEM_DISP_MOUSE_POSITION)
            button.update(SCREEN)

        pygame.display.update()


def item_type_confirmation(item_index, item):
    global counter
    if item.type == 'ring':
        ring_slot_confirmation(item_index, item)
    else:
        equip_item(item_index, item, 0)


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
        slot_item = getattr(player_slot_.player_slot, item.type + '1')
    elif ring_slot == 2:
        slot_item = getattr(player_slot_.player_slot, item.type + '2')
    elif ring_slot == 0:
        slot_item = getattr(player_slot_.player_slot, item.type)

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
        BUTTONS = main_menu.main_menu_structure(EQUIP_ITEM_MOUSE_POSITION)
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
                main_menu.main_menu_structure_events(EQUIP_ITEM_MOUSE_POSITION, BUTTONS)
                if YES_BUTTON.checkForInput(EQUIP_ITEM_MOUSE_POSITION):
                    counter = 0
                    item_equipped_confirmation(item_index, item, ring_slot)
                if NO_BUTTON.checkForInput(EQUIP_ITEM_MOUSE_POSITION):
                    show_item(item_index, item)

        for button in BUTTONS:
            button.changeColor(EQUIP_ITEM_MOUSE_POSITION)
            button.update(SCREEN)

        pygame.display.update()


def inventory_limit():
    limit = 150
    if len(inventory) >= limit:
        to_remove = sorted(inventory, key=lambda x: (x.level, x.type), reverse=True).pop(-1)
        row = db.execute("SELECT * FROM inventory WHERE username = :username AND name = :name AND level = :level",
                         username=player_.player.name, name=to_remove.name, level=to_remove.level)
        id = (row[0]['id'])
        db.execute("DELETE FROM inventory WHERE id = :id",
                   id=id)


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


def inventory_removal(username, item):
    if len(inventory) == 0:
        pass
    else:

        db.execute(
            "DELETE FROM inventory WHERE username= :username and name = :name",
            username=username, name=item.name)


def item_equipped_confirmation(item_index, item, ring_slot):
    global LAST_TIME_MS, counter, slot_item

    if ring_slot == 1:
        slot_item = getattr(player_slot_.player_slot, item.type + '1')
    elif ring_slot == 2:
        slot_item = getattr(player_slot_.player_slot, item.type + '2')
    elif ring_slot == 0:
        slot_item = getattr(player_slot_.player_slot, item.type)
    item_type = item.type
    print(f'item type {item_type}')
    print(ring_slot)
    if slot_item is None:
        pass
        # setattr(player_slot, item_type, item)
        # inventory.remove(item)
        # inventory_removal(player.name, item)
        # item = getattr(player_slot_.player_slot, item_type)
        # counter = 0
        # item_equipped_confirmation(item_index, item)

    elif ring_slot == 1:
        to_inventory = getattr(player_slot_.player_slot, item_type + '1')
        new_item = item_.Item(to_inventory['type'],
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
        inventory_removal(player_.playername, item)
        player_slot_.player_slot.ring1 = item.__dict__
        equip_update_status(item)
        print(f"{item.__dict__['name']} level {item.__dict__['level']} equipped!")
        save_load.save_state()
    elif ring_slot == 2:
        to_inventory = getattr(player_slot_.player_slot, item_type + '2')
        new_item = item_.Item(to_inventory['type'],
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
        inventory_removal(player_.player.name, item)
        player_slot_.player_slot.ring2 = item.__dict__
        equip_update_status(item)
        print(f"{item.__dict__['name']} level {item.__dict__['level']} equipped!")
        save_load.save_state()
    else:
        to_inventory = getattr(player_slot_.player_slot, item_type)
        new_item = item_.Item(to_inventory['type'],
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
        inventory_update(player_.player.name, new_item)
        # slot
        unequip_update_status(new_item)
        setattr(player_slot_.player_slot, item_type, item.__dict__)
        print(f"{item.__dict__['name']} level {item.__dict__['level']} equipped!")

        # status
        equip_update_status(item)
        # removal from inventory list
        inventory.remove(item)

        # removal from database
        inventory_removal(player_.player.name, item)
        save_load.save_state()

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
        BUTTONS = main_menu.main_menu_structure(INVENTORY_MOUSE_POSITION)

        NEXT = Button(image=pygame.image.load("assets/images/Smallest Rect.png"), pos=(770, 600),
                      text_input="NEXT", font=get_bold_font(30), base_color="White", hovering_color=BLUE)
        BUTTONS.append(NEXT)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                main_menu.main_menu_structure_events(INVENTORY_MOUSE_POSITION, BUTTONS)
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
                                consumable_item_.fossil_reforge_cannot_reforge(sorted_inventory[i].__dict__, 1, consumable_type)
                            else:
                                consumable_item_.use_fossil(consumable_type, i, sorted_inventory[i])
            # BOTAR DESTAQUE NO ITEM HOVERADO
            # for i in range(len(iteration_rect)):
            #     if iteration_rect[i].collidepoint(INVENTORY_MOUSE_POSITION):
            #         pass

        for button in BUTTONS:
            button.changeColor(INVENTORY_MOUSE_POSITION)
            button.update(SCREEN)

        pygame.display.update()


def show_inventory_page_2(consumable_type):
    item_index = 41
    SCREEN.blit(BG, (0, 0))
    SCREEN.blit(BATTLE_BOX, (60, 40))
    player_.display_level_xp()
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
        BUTTONS = main_menu.main_menu_structure(INVENTORY_MOUSE_POSITION)

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
                main_menu.main_menu_structure_events(INVENTORY_MOUSE_POSITION, BUTTONS)
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
    player_.display_level_xp()
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
        BUTTONS = main_menu.main_menu_structure(INVENTORY_MOUSE_POSITION)

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
                main_menu.main_menu_structure_events(INVENTORY_MOUSE_POSITION, BUTTONS)
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
    player_.display_level_xp()
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
        BUTTONS = main_menu.main_menu_structure(INVENTORY_MOUSE_POSITION)

        BACK = Button(image=pygame.image.load("assets/images/Smallest Rect.png"), pos=(160, 600),
                      text_input="BACK", font=get_bold_font(30), base_color="White", hovering_color=BLUE)

        BUTTONS.extend([BACK])

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                main_menu.main_menu_structure_events(INVENTORY_MOUSE_POSITION, BUTTONS)
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

