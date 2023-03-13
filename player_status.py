from levels_xp import *
from card import *
from player_ import player
from player_slot import player_slot
from fonts import *

globals_variables.global_containers()


def player_status():
    globals_variables.temp_gear_change_inventory.clear()
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
    SCREEN.blit(CARD, (SCREEN_WIDTH / 2 - 30, 600))

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
    card_rect = AMULET.get_rect(center=(SCREEN_WIDTH / 2, 620))

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
                    from main import main_menu
                    main_menu()
                if CHANGE.checkForInput(PLAYER_STATUS_MOUSE_POSITION):
                    globals_variables.temp_gear_change_inventory.clear()
                    counter = 0
                    change_gear()
            if weapon_rect.collidepoint(PLAYER_STATUS_MOUSE_POSITION):
                SCREEN.blit(PLAYER_STATUS_BOX, (80, 60))
                SCREEN.blit(gear_slot, gear_slot_rect)
                globals_variables.temp_gear_change.clear()
                globals_variables.temp_gear_change.append(player_slot.weapon)
                show_player_slot('weapon')

            if amulet_rect.collidepoint(PLAYER_STATUS_MOUSE_POSITION):
                SCREEN.blit(PLAYER_STATUS_BOX, (80, 60))
                SCREEN.blit(gear_slot, gear_slot_rect)
                globals_variables.temp_gear_change.clear()
                globals_variables.temp_gear_change.append(player_slot.amulet)
                show_player_slot('amulet')

            if armor_rect.collidepoint(PLAYER_STATUS_MOUSE_POSITION):
                SCREEN.blit(PLAYER_STATUS_BOX, (80, 60))
                SCREEN.blit(gear_slot, gear_slot_rect)
                globals_variables.temp_gear_change.clear()
                globals_variables.temp_gear_change.append(player_slot.armor)
                show_player_slot('armor')

            if boots_rect.collidepoint(PLAYER_STATUS_MOUSE_POSITION):
                SCREEN.blit(PLAYER_STATUS_BOX, (80, 60))
                SCREEN.blit(gear_slot, gear_slot_rect)
                globals_variables.temp_gear_change.clear()
                globals_variables.temp_gear_change.append(player_slot.boots)
                show_player_slot('boots')

            if gloves_rect.collidepoint(PLAYER_STATUS_MOUSE_POSITION):
                SCREEN.blit(PLAYER_STATUS_BOX, (80, 60))
                SCREEN.blit(gear_slot, gear_slot_rect)
                globals_variables.temp_gear_change.clear()
                globals_variables.temp_gear_change.append(player_slot.gloves)
                show_player_slot('gloves')

            if helmet_rect.collidepoint(PLAYER_STATUS_MOUSE_POSITION):
                SCREEN.blit(PLAYER_STATUS_BOX, (80, 60))
                SCREEN.blit(gear_slot, gear_slot_rect)
                globals_variables.temp_gear_change.clear()
                globals_variables.temp_gear_change.append(player_slot.helmet)
                show_player_slot('helmet')

            if legs_rect.collidepoint(PLAYER_STATUS_MOUSE_POSITION):
                SCREEN.blit(PLAYER_STATUS_BOX, (80, 60))
                SCREEN.blit(gear_slot, gear_slot_rect)
                globals_variables.temp_gear_change.clear()
                globals_variables.temp_gear_change.append(player_slot.legs)
                show_player_slot('legs')

            if ring1_rect.collidepoint(PLAYER_STATUS_MOUSE_POSITION):
                SCREEN.blit(PLAYER_STATUS_BOX, (80, 60))
                SCREEN.blit(gear_slot, gear_slot_rect)
                globals_variables.temp_gear_change.clear()
                globals_variables.temp_gear_change.append(player_slot.ring1)
                show_player_slot('ring1')

            if ring2_rect.collidepoint(PLAYER_STATUS_MOUSE_POSITION):
                SCREEN.blit(PLAYER_STATUS_BOX, (80, 60))
                SCREEN.blit(gear_slot, gear_slot_rect)
                globals_variables.temp_gear_change.clear()
                globals_variables.temp_gear_change.append(player_slot.ring2)
                show_player_slot('ring2')

            if second_hand_rect.collidepoint(PLAYER_STATUS_MOUSE_POSITION):
                SCREEN.blit(PLAYER_STATUS_BOX, (80, 60))
                SCREEN.blit(gear_slot, gear_slot_rect)
                globals_variables.temp_gear_change.clear()
                globals_variables.temp_gear_change.append(player_slot.second_hand)
                show_player_slot('second_hand')

            if card_rect.collidepoint(PLAYER_STATUS_MOUSE_POSITION):
                SCREEN.blit(PLAYER_STATUS_BOX, (80, 60))
                SCREEN.blit(gear_slot, gear_slot_rect)
                globals_variables.temp_gear_change.clear()
                globals_variables.temp_gear_change.append(player_slot.card)
                show_player_slot('card')

            for button in [BACK, CHANGE]:
                button.changeColor(PLAYER_STATUS_MOUSE_POSITION)
                button.update(SCREEN)
            pygame.display.update()


def change_gear():
    if globals_variables.temp_gear_change[0]['type'] == 'card':
        cards_screen('player_status')
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
            if sorted_inventory[i].__dict__['type'] == globals_variables.temp_gear_change[0]['type']:
                text1 = get_bold_font(22).render(
                    f"{item_index} — {sorted_inventory[i].__dict__['name']} (level {sorted_inventory[i].__dict__['level']})",
                    True, WHITE)
                text1_rect = text1.get_rect(midleft=(100, HEIGHT))
                HEIGHT = HEIGHT + 23
                SCREEN.blit(text1, text1_rect)
                item_index = item_index + 1
                iteration_rect.append(text1_rect)
                temp_iterable.append(sorted_inventory[i].__dict__['name'])
                globals_variables.temp_gear_change_inventory.append(sorted_inventory[i])
                column_a = column_a + 1
            if column_a == 20:
                break
        HEIGHT2 = 100
        column_b = 0
        for i in range(20, len(sorted_inventory)):
            if sorted_inventory[i].__dict__['type'] == globals_variables.temp_gear_change[0]['type'] and sorted_inventory[i].__dict__[
                'name'] not in temp_iterable:
                text1 = get_bold_font(22).render(
                    f"{item_index} — {sorted_inventory[i].__dict__['name']} (level {sorted_inventory[i].__dict__['level']})",
                    True, WHITE)
                text1_rect = text1.get_rect(midleft=(550, HEIGHT2))
                HEIGHT2 = HEIGHT2 + 23
                SCREEN.blit(text1, text1_rect)
                item_index = item_index + 1
                iteration_rect.append(text1_rect)
                globals_variables.temp_gear_change_inventory.append(sorted_inventory[i])
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
                            show_item(i, globals_variables.temp_gear_change_inventory[i])

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