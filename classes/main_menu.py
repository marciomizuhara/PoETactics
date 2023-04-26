import pygame, sys
from button import *
from settings import *
from assets.music.music import *
from assets.fonts.fonts import *
from classes import encounter
from classes import explore
from classes import consumable_item_
from classes import card
from classes import delve
from classes import extras
from classes import inventory
from classes import player_
from classes import player_slot_
from classes import player_status_
from classes import character
from classes import item_
from classes import unique


main_menu_setter = True


# SIDE MENU
def main_menu_structure(mouse):
    # if player_.player.level != 20 and character.dycedarg2.status is True:
    #     EXPLORE = Button(image=pygame.image.load("assets/images/ONE_LINE_OPTION.png"), pos=(1100, 50),
    #                           text_input="EXPLORE", font=get_bold_font(30), base_color="White",
    #                           hovering_color=BLUE)
    #     INVENTORY = Button(image=pygame.image.load("assets/images/ONE_LINE_OPTION.png"), pos=(1100, 105),
    #                        text_input="INVENTORY", font=get_bold_font(30), base_color="White", hovering_color=BLUE)
    #     CONSUMABLE_ITEMS = Button(image=pygame.image.load("assets/images/ONE_LINE_OPTION.png"),
    #                               pos=(SCREEN_WIDTH - 180, 210),
    #                               text_input="CONSUMABLE ITEMS", font=get_bold_font(30), base_color="White",
    #                               hovering_color=BLUE)
    #     PLAYER_STATUS = Button(image=pygame.image.load("assets/images/ONE_LINE_OPTION.png"), pos=(1100, 215),
    #                            text_input="PLAYER STATUS", font=get_bold_font(30), base_color="White",
    #                            hovering_color=BLUE)
    #     EXTRAS = Button(image=pygame.image.load("assets/images/ONE_LINE_OPTION.png"), pos=(1100, 370),
    #                     text_input="EXTRAS", font=get_bold_font(30), base_color="White",
    #                     hovering_color=BLUE)
    #     HELP = Button(image=pygame.image.load("assets/images/ONE_LINE_OPTION.png"), pos=(1100, 325),
    #                   text_input="HELP", font=get_bold_font(30), base_color="White", hovering_color=BLUE)
    #     MAIN_MENU = Button(image=pygame.image.load("assets/images/ONE_LINE_OPTION.png"), pos=(1100, 370),
    #                        text_input="MAIN MENU", font=get_bold_font(30), base_color="White", hovering_color=BLUE)
    #     QUIT_BUTTON = Button(image=pygame.image.load("assets/images/ONE_LINE_OPTION.png"), pos=(1100, 420),
    #                          text_input="QUIT", font=get_bold_font(30), base_color="White", hovering_color=BLUE)
    #     BUTTONS = [EXPLORE, INVENTORY, CONSUMABLE_ITEMS, PLAYER_STATUS, EXTRAS, HELP, MAIN_MENU, QUIT_BUTTON]
    #     return BUTTONS
    # else:
    EXPLORE = Button(image=pygame.image.load("assets/images/ONE_LINE_OPTION.png"), pos=(1100, 50),
                          text_input="EXPLORE", font=get_bold_font(30), base_color="White",
                          hovering_color=BLUE)
    INVENTORY = Button(image=pygame.image.load("assets/images/ONE_LINE_OPTION.png"), pos=(1100, 105),
                       text_input="INVENTORY", font=get_bold_font(30), base_color="White", hovering_color=BLUE)
    CONSUMABLE_ITEMS = Button(image=pygame.image.load("assets/images/ONE_LINE_OPTION.png"), pos=(1100, 160),
                              text_input="CONSUMABLE ITEMS", font=get_bold_font(30), base_color="White",
                              hovering_color=BLUE)
    PLAYER_STATUS = Button(image=pygame.image.load("assets/images/ONE_LINE_OPTION.png"), pos=(1100, 215),
                           text_input="PLAYER STATUS", font=get_bold_font(30), base_color="White",
                           hovering_color=BLUE)
    DELVE = Button(image=pygame.image.load("assets/images/ONE_LINE_OPTION.png"), pos=(1100, 270),
                   text_input="DELVE", font=get_bold_font(30), base_color="White",
                   hovering_color=BLUE)
    ENDGAME_BOSSES = Button(image=pygame.image.load("assets/images/ONE_LINE_OPTION.png"), pos=(1100, 325),
                            text_input="ENDGAME BOSSES", font=get_bold_font(30), base_color="White",
                            hovering_color=BLUE)
    EXTRAS = Button(image=pygame.image.load("assets/images/ONE_LINE_OPTION.png"), pos=(1100, 380),
                    text_input="EXTRAS", font=get_bold_font(30), base_color="White",
                    hovering_color=BLUE)
    HELP = Button(image=pygame.image.load("assets/images/ONE_LINE_OPTION.png"), pos=(1100, 435),
                  text_input="HELP", font=get_bold_font(30), base_color="White", hovering_color=BLUE)
    MAIN_MENU = Button(image=pygame.image.load("assets/images/ONE_LINE_OPTION.png"), pos=(1100, 490),
                       text_input="MAIN MENU", font=get_bold_font(30), base_color="White", hovering_color=BLUE)
    QUIT_BUTTON = Button(image=pygame.image.load("assets/images/ONE_LINE_OPTION.png"), pos=(1100, 545),
                         text_input="QUIT", font=get_bold_font(30), base_color="White", hovering_color=BLUE)
    BUTTONS_LIST = [EXPLORE, INVENTORY, CONSUMABLE_ITEMS, PLAYER_STATUS, DELVE, ENDGAME_BOSSES, EXTRAS, HELP,
                    MAIN_MENU, QUIT_BUTTON]
    return BUTTONS_LIST


def main_menu_structure_events(mouse, buttons):
    # if player_.player.level == 20:
    if buttons[0].checkForInput(mouse):
        explore.explore()
    if buttons[1].checkForInput(mouse):
        inventory.show_inventory_page_1(1)
    if buttons[2].checkForInput(mouse):
        consumable_item_.show_consumable_items()
    if buttons[3].checkForInput(mouse):
        player_status_.player_status()
    if buttons[4].checkForInput(mouse):
        pygame.mixer.music.fadeout(2)
        pygame.mixer.music.stop()
        delve_music()
        delve.delve_menu()
        delve.delve_menu()
    if buttons[5].checkForInput(mouse):
        # bosses
        print('bosses')
    if buttons[6].checkForInput(mouse):
        extras.extras()
    if buttons[7].checkForInput(mouse):
        print('help')
    if buttons[8].checkForInput(mouse):
        main_menu()
    if buttons[9].checkForInput(mouse):
        pygame.quit()
        sys.exit()
    # else:
    #     if buttons[0].checkForInput(mouse):
    #         explore.explore()
    #     if buttons[1].checkForInput(mouse):
    #         inventory.show_inventory_page_1(1)
    #     if buttons[2].checkForInput(mouse):
    #         consumable_item_.show_consumable_items()
    #     if buttons[3].checkForInput(mouse):
    #         player_status_.player_status()
    #     if buttons[4].checkForInput(mouse):
    #         print('not available')
    #     if buttons[5].checkForInput(mouse):
    #         print('not available')
    #     if buttons[6].checkForInput(mouse):
    #         extras.extras()
    #     if buttons[7].checkForInput(mouse):
    #         print('help')
    #     if buttons[8].checkForInput(mouse):
    #         main_menu()
    #     if buttons[9].checkForInput(mouse):
    #         pygame.quit()
    #         sys.exit()


def main_menu():
    global counter, LAST_TIME_MS, main_menu_setter

    if main_menu_setter:
        print('main menu setter ')

        '''
        REMOVER !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
        '''

        username = 'Mizuhara1'
        # username = player.name
        rows = db.execute("SELECT * FROM user_data WHERE username = :username",
                          username=username)
        print(rows[0])

        # input('aqui 5')
        player_.player.name = rows[0]['username']
        player_.player.level = rows[0]['level']
        player_.player.xp = rows[0]['experience']
        player_.player.total_life = rows[0]['total_life']
        player_.player.life = rows[0]['life']
        player_.player.attack = rows[0]['attack']
        player_.player.defense = rows[0]['defense']
        player_.player.shaman = rows[0]['shaman']
        player_.player.crit_chance = rows[0]['crit_chance']
        player_.player.crit_damage = rows[0]['crit_damage']
        player_.player.magic_find = rows[0]['magic_find']
        player_.player.souls = rows[0]['souls']

        print(player_.player.name, player_.player.level)
        # Inventory
        rows2 = db.execute("SELECT * FROM inventory WHERE username = :username",
                           username=username)

        if len(rows2) < 1:
            pass


        else:
            print('rows 2 aqui', rows2)
            for i in range(0, len(rows2)):
                new_item = item_.Item(rows2[i]['type'], rows2[i]['name'], rows2[i]['level'],
                                rows2[i]['life'], rows2[i]['attack'],
                                rows2[i]['defense'], rows2[i]['crit_chance'],
                                rows2[i]['crit_damage'], rows2[i]['magic_find'], rows2[i]['rarity'],
                                rows2[i]['crafted'], rows2[i]['image'])
                inventory.inventory.append(new_item)

        # Card
        card.card_instance_load(player_.player.name)

        # PlayerSlot
        row_amulet = db.execute("SELECT * FROM amulet WHERE username = :username", username=username)
        player_slot_.player_slot.amulet = row_amulet[0]
        row_armor = db.execute("SELECT * FROM armor WHERE username = :username", username=username)
        player_slot_.player_slot.armor = row_armor[0]
        row_gloves = db.execute("SELECT * FROM gloves WHERE username = :username", username=username)
        player_slot_.player_slot.gloves = row_gloves[0]
        row_helmet = db.execute("SELECT * FROM helmet WHERE username = :username", username=username)
        player_slot_.player_slot.helmet = row_helmet[0]
        row_legs = db.execute("SELECT * FROM legs WHERE username = :username", username=username)
        player_slot_.player_slot.legs = row_legs[0]
        row_ring1 = db.execute("SELECT * FROM ring1 WHERE username = :username", username=username)
        player_slot_.player_slot.ring1 = row_ring1[0]
        row_ring2 = db.execute("SELECT * FROM ring2 WHERE username = :username", username=username)
        player_slot_.player_slot.ring2 = row_ring2[0]
        row_second_hand = db.execute("SELECT * FROM second_hand WHERE username = :username", username=username)
        player_slot_.player_slot.second_hand = row_second_hand[0]
        row_weapon = db.execute("SELECT * FROM weapon WHERE username = :username", username=username)
        player_slot_.player_slot.weapon = row_weapon[0]
        row_boots = db.execute("SELECT * FROM boots WHERE username = :username", username=username)
        player_slot_.player_slot.boots = row_boots[0]
        row_card = db.execute("SELECT * FROM card WHERE username = :username", username=username)
        player_slot_.player_slot.card = row_card[0]
        # Consumables
        row_potion = db.execute("SELECT * FROM potion WHERE username = :username", username=username)
        consumable_item_.potion.quantity = row_potion[0]['quantity']
        row_x_potion = db.execute("SELECT * FROM x_potion WHERE username = :username", username=username)
        consumable_item_.x_potion.quantity = row_x_potion[0]['quantity']
        row_elixir = db.execute("SELECT * FROM elixir WHERE username = :username", username=username)
        consumable_item_.elixir.quantity = row_elixir[0]['quantity']
        row_chaos_orb = db.execute("SELECT * FROM chaos_orb WHERE username = :username", username=username)
        consumable_item_.chaos_orb.quantity = row_chaos_orb[0]['quantity']
        row_divine_orb = db.execute("SELECT * FROM divine_orb WHERE username = :username", username=username)
        consumable_item_.divine_orb.quantity = row_divine_orb[0]['quantity']
        row_exalted_orb = db.execute("SELECT * FROM exalted_orb WHERE username = :username", username=username)
        consumable_item_.exalted_orb.quantity = row_exalted_orb[0]['quantity']
        row_mirror_of_kalandra = db.execute("SELECT * FROM mirror_of_kalandra WHERE username = :username",
                                            username=username)
        consumable_item_.mirror_of_kalandra.quantity = row_mirror_of_kalandra[0]['quantity']
        row_roulette_wheel_ticket = db.execute("SELECT * FROM roulette_wheel_ticket WHERE username = :username",
                                               username=username)
        consumable_item_.roulette_wheel_ticket.quantity = row_roulette_wheel_ticket[0]['quantity']
        row_dense_fossil = db.execute("SELECT * FROM dense_fossil WHERE username = :username", username=username)
        consumable_item_.dense_fossil.quantity = row_dense_fossil[0]['quantity']
        row_serrated_fossil = db.execute("SELECT * FROM serrated_fossil WHERE username = :username", username=username)
        consumable_item_.serrated_fossil.quantity = row_serrated_fossil[0]['quantity']
        row_pristine_fossil = db.execute("SELECT * FROM pristine_fossil WHERE username = :username", username=username)
        consumable_item_.pristine_fossil.quantity = row_pristine_fossil[0]['quantity']
        row_deft_fossil = db.execute("SELECT * FROM deft_fossil WHERE username = :username", username=username)
        consumable_item_.deft_fossil.quantity = row_deft_fossil[0]['quantity']
        row_fractured_fossil = db.execute("SELECT * FROM fractured_fossil WHERE username = :username",
                                          username=username)
        consumable_item_.fractured_fossil.quantity = row_fractured_fossil[0]['quantity']

        # boss instance
        row_boss_instance = db.execute("SELECT * FROM boss_instance WHERE username = :username", username=username)

        # card instance
        # row_card_instance = db.execute("SELECT * FROM card_instance WHERE username = :username", username=username)

        # Uniques_list
        row_uniques_list = db.execute("SELECT * FROM uniques_list WHERE username = :username", username=username)

        for i in range(0, len(row_uniques_list)):
            unique.uniques_list.append(row_uniques_list[i]['name'])

        if row_boss_instance[0]['wiegraf1'] == 0:
            character.wiegraf1.status = False
        else:
            pass
        if row_boss_instance[0]['dycedarg1'] == 0:
            character.dycedarg1.status = False
        else:
            pass
        if row_boss_instance[0]['wiegraf2'] == 0:
            character.wiegraf2.status = False
        else:
            pass
        if row_boss_instance[0]['dycedarg2'] == 0:
            character.dycedarg2.status = False
        else:
            pass

        # Delve
        delve_rows = db.execute("SELECT * FROM delve WHERE username = :username",
                                username=username)
        delve.Delve.depth = delve_rows[0]['depth']
        delve.Delve.multiplier = delve_rows[0]['multiplier']
        print('aqui', player_.player.life)
        '''
          REMOVER !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
          '''
        main_menu_setter = False

    # MAIN MENU
    if player_.player.level != 20 and character.dycedarg2.status is True:
        while True:
            SCREEN.blit(BG, (0, 0))

            MENU_MOUSE_POSITION = pygame.mouse.get_pos()

            menu_text1 = get_bold_font(80).render("POETACTICS", True, "White")
            menu_text2 = get_bold_font(35).render("THE IDLE RPG ADVENTURE", True, "White")

            menu_rect1 = menu_text1.get_rect(center=(640, 100))
            menu_rect2 = menu_text2.get_rect(center=(640, 160))

            EXPLORE = Button(image=pygame.image.load("assets/images/ONE_LINE_OPTION.png"), pos=(640, 300),
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

            SCREEN.blit(menu_text1, menu_rect1)
            SCREEN.blit(menu_text2, menu_rect2)

            for button in [EXPLORE, INVENTORY, CONSUMABLE_ITEMS, PLAYER_STATUS, EXTRAS, HELP, QUIT_BUTTON]:
                button.changeColor(MENU_MOUSE_POSITION)
                button.update(SCREEN)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if EXPLORE.checkForInput(MENU_MOUSE_POSITION):
                        explore.explore()
                    if INVENTORY.checkForInput(MENU_MOUSE_POSITION):
                        if len(inventory.inventory) == 0:
                            pass
                        else:
                            inventory.show_inventory_page_1(1)  # options()
                    if CONSUMABLE_ITEMS.checkForInput(MENU_MOUSE_POSITION):
                        consumable_item_.show_consumable_items()
                    if PLAYER_STATUS.checkForInput(MENU_MOUSE_POSITION):
                        player_status_.player_status()  # play()
                    if EXTRAS.checkForInput(MENU_MOUSE_POSITION):
                        counter = 0
                        extras.extras()
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

            EXPLORE = Button(image=pygame.image.load("assets/images/ONE_LINE_OPTION.png"), pos=(640, 225),
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

            for button in [EXPLORE, INVENTORY, CONSUMABLE_ITEMS, PLAYER_STATUS, EXTRAS, HELP, QUIT_BUTTON,
                           DELVE, ENDGAME_BOSSES]:
                button.changeColor(MENU_MOUSE_POSITION)
                button.update(SCREEN)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if EXPLORE.checkForInput(MENU_MOUSE_POSITION):
                        explore.explore()
                    if INVENTORY.checkForInput(MENU_MOUSE_POSITION):
                        if len(inventory.inventory) == 0:
                            pass
                        else:
                            inventory.show_inventory_page_1(1)  # options()
                    if CONSUMABLE_ITEMS.checkForInput(MENU_MOUSE_POSITION):
                        consumable_item_.show_consumable_items()
                    if PLAYER_STATUS.checkForInput(MENU_MOUSE_POSITION):
                        player_status_.player_status()  # play()
                    if DELVE.checkForInput(MENU_MOUSE_POSITION):
                        pygame.mixer.music.fadeout(2)
                        pygame.mixer.music.stop()
                        delve_music()
                        delve.delve_menu()
                    if ENDGAME_BOSSES.checkForInput(MENU_MOUSE_POSITION):
                       pass
                    if EXTRAS.checkForInput(MENU_MOUSE_POSITION):
                        counter = 0
                        extras.extras()
                    if HELP.checkForInput(MENU_MOUSE_POSITION):
                        pass
                    if QUIT_BUTTON.checkForInput(MENU_MOUSE_POSITION):
                        pygame.quit()
                        sys.exit()

            pygame.display.update()