import pygame, sys
from assets.fonts.fonts import *
from button import *
from settings import *
from classes import character
from classes import consumable_item_
from classes import delve
from classes import inventory
from classes import item_
from classes import main_menu
from classes import player_
from classes import player_slot_
from classes import unique


def load_state():
    username = player_.player.name
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

    print(player_.player.name, player_.player.level)
    # Inventory
    rows2 = db.execute("SELECT * FROM inventory WHERE username = :username",
                       username=username)

    if len(rows2) < 1:
        pass


    else:
        for i in range(0, len(rows2)):
            new_item = item_.Item(rows2[i]['type'], rows2[i]['name'], rows2[i]['level'],
                            rows2[i]['life'], rows2[i]['attack'],
                            rows2[i]['defense'], rows2[i]['crit_chance'],
                            rows2[i]['crit_damage'], rows2[i]['magic_find'], rows2[i]['rarity'], rows[i]['image'])
            inventory.inventory.append(new_item)

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
    row_dense_fossil = db.execute("SELECT * FROM dense_fossil WHERE username = :username", username=username)
    consumable_item_.dense_fossil.quantity = row_dense_fossil[0]['quantity']
    row_serrated_fossil = db.execute("SELECT * FROM serrated_fossil WHERE username = :username", username=username)
    consumable_item_.serrated_fossil.quantity = row_serrated_fossil[0]['quantity']
    row_pristine_fossil = db.execute("SELECT * FROM pristine_fossil WHERE username = :username", username=username)
    consumable_item_.pristine_fossil.quantity = row_pristine_fossil[0]['quantity']
    row_deft_fossil = db.execute("SELECT * FROM deft_fossil WHERE username = :username", username=username)
    consumable_item_.deft_fossil.quantity = row_deft_fossil[0]['quantity']
    row_fractured_fossil = db.execute("SELECT * FROM fractured_fossil WHERE username = :username", username=username)
    consumable_item_.fractured_fossil.quantity = row_fractured_fossil[0]['quantity']

    # boss instance
    row_boss_instance = db.execute("SELECT * FROM boss_instance WHERE username = :username", username=username)

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


def save_state():
    username = player_.player.name
    # Player status
    db.execute(
        "UPDATE user_data SET level = :level, experience = :experience, total_life = :total_life, life = :life, attack = :attack, defense = :defense, shaman = :shaman, crit_chance = :crit_chance, crit_damage = :crit_damage, magic_find = :magic_find  WHERE username = :username",
        level=player_.player.level, experience=player_.player.xp, total_life=player_.player.total_life, life=player_.player.life,
        attack=player_.player.attack, defense=player_.player.defense, shaman=player_.player.shaman,
        crit_chance=player_.player.crit_chance, crit_damage=player_.player.crit_damage, magic_find=player_.player.magic_find,
        username=username)

    # Player_Slot
    db.execute("DELETE FROM amulet WHERE username = :username",
               username=username)
    db.execute(
        "INSERT INTO amulet (username, name, type, level, life, attack, defense, crit_chance, crit_damage, magic_find, rarity, image) VALUES (:username, :name, :type, :level, :life, :attack, :defense, :crit_chance, :crit_damage, :magic_find, :rarity, :image)",
        username=player_.player.name, name=player_slot_.player_slot.amulet['name'], type=player_slot_.player_slot.amulet['type'],
        level=player_slot_.player_slot.amulet['level'], life=player_slot_.player_slot.amulet['life'],
        attack=player_slot_.player_slot.amulet['attack'], defense=player_slot_.player_slot.amulet['defense'],
        crit_chance=player_slot_.player_slot.amulet['crit_chance'], crit_damage=player_slot_.player_slot.amulet['crit_damage'],
        magic_find=player_slot_.player_slot.amulet['magic_find'], rarity=player_slot_.player_slot.amulet['rarity'], image=player_slot_.player_slot.amulet['image'])
    db.execute("DELETE FROM armor WHERE username = :username",
               username=username)
    db.execute(
        "INSERT INTO armor (username, name, type, level, life, attack, defense, crit_chance, crit_damage, magic_find, rarity, image) VALUES (:username, :name, :type, :level, :life, :attack, :defense, :crit_chance, :crit_damage, :magic_find, :rarity, :image)",
        username=player_.player.name, name=player_slot_.player_slot.armor['name'], type=player_slot_.player_slot.armor['type'],
        level=player_slot_.player_slot.armor['level'], life=player_slot_.player_slot.armor['life'],
        attack=player_slot_.player_slot.armor['attack'], defense=player_slot_.player_slot.armor['defense'],
        crit_chance=player_slot_.player_slot.armor['crit_chance'], crit_damage=player_slot_.player_slot.armor['crit_damage'],
        magic_find=player_slot_.player_slot.armor['magic_find'], rarity=player_slot_.player_slot.armor['rarity'], image=player_slot_.player_slot.armor['image'])
    db.execute("DELETE FROM gloves WHERE username = :user"
               "name",
               username=username)
    db.execute(
        "INSERT INTO gloves (username, name, type, level, life, attack, defense, crit_chance, crit_damage, magic_find, rarity, image) VALUES (:username, :name, :type, :level, :life, :attack, :defense, :crit_chance, :crit_damage, :magic_find, :rarity, :image)",
        username=player_.player.name, name=player_slot_.player_slot.gloves['name'], type=player_slot_.player_slot.gloves['type'],
        level=player_slot_.player_slot.gloves['level'], life=player_slot_.player_slot.gloves['life'],
        attack=player_slot_.player_slot.gloves['attack'], defense=player_slot_.player_slot.gloves['defense'],
        crit_chance=player_slot_.player_slot.gloves['crit_chance'], crit_damage=player_slot_.player_slot.gloves['crit_damage'],
        magic_find=player_slot_.player_slot.gloves['magic_find'], rarity=player_slot_.player_slot.gloves['rarity'], image=player_slot_.player_slot.gloves['image'])
    db.execute("DELETE FROM helmet WHERE username = :username",
               username=username)
    db.execute(
        "INSERT INTO helmet (username, name, type, level, life, attack, defense, crit_chance, crit_damage, magic_find, rarity, image) VALUES (:username, :name, :type, :level, :life, :attack, :defense, :crit_chance, :crit_damage, :magic_find, :rarity, :image)",
        username=player_.player.name, name=player_slot_.player_slot.helmet['name'], type=player_slot_.player_slot.helmet['type'],
        level=player_slot_.player_slot.helmet['level'], life=player_slot_.player_slot.helmet['life'],
        attack=player_slot_.player_slot.helmet['attack'], defense=player_slot_.player_slot.helmet['defense'],
        crit_chance=player_slot_.player_slot.helmet['crit_chance'], crit_damage=player_slot_.player_slot.helmet['crit_damage'],
        magic_find=player_slot_.player_slot.helmet['magic_find'], rarity=player_slot_.player_slot.helmet['rarity'], image=player_slot_.player_slot.helmet['image'])
    db.execute("DELETE FROM legs WHERE username = :username",
               username=username)
    db.execute(
        "INSERT INTO legs (username, name, type, level, life, attack, defense, crit_chance, crit_damage, magic_find, rarity, image) VALUES (:username, :name, :type, :level, :life, :attack, :defense, :crit_chance, :crit_damage, :magic_find, :rarity, :image)",
        username=player_.player.name, name=player_slot_.player_slot.legs['name'], type=player_slot_.player_slot.legs['type'],
        level=player_slot_.player_slot.legs['level'], life=player_slot_.player_slot.legs['life'],
        attack=player_slot_.player_slot.legs['attack'], defense=player_slot_.player_slot.legs['defense'],
        crit_chance=player_slot_.player_slot.legs['crit_chance'], crit_damage=player_slot_.player_slot.legs['crit_damage'],
        magic_find=player_slot_.player_slot.legs['magic_find'], rarity=player_slot_.player_slot.legs['rarity'], image=player_slot_.player_slot.legs['image'])
    db.execute("DELETE FROM ring1 WHERE username = :username",
               username=username)
    db.execute(
        "INSERT INTO ring1 (username, name, type, level, life, attack, defense, crit_chance, crit_damage, magic_find, rarity, image) VALUES (:username, :name, :type, :level, :life, :attack, :defense, :crit_chance, :crit_damage, :magic_find, :rarity, :image)",
        username=player_.player.name, name=player_slot_.player_slot.ring1['name'], type=player_slot_.player_slot.ring1['type'],
        level=player_slot_.player_slot.ring1['level'], life=player_slot_.player_slot.ring1['life'],
        attack=player_slot_.player_slot.ring1['attack'], defense=player_slot_.player_slot.ring1['defense'],
        crit_chance=player_slot_.player_slot.ring1['crit_chance'], crit_damage=player_slot_.player_slot.ring1['crit_damage'],
        magic_find=player_slot_.player_slot.ring1['magic_find'], rarity=player_slot_.player_slot.ring1['rarity'], image=player_slot_.player_slot.ring1['image'])
    db.execute("DELETE FROM ring2 WHERE username = :username",
               username=username)
    db.execute(
        "INSERT INTO ring2 (username, name, type, level, life, attack, defense, crit_chance, crit_damage, magic_find, rarity, image) VALUES (:username, :name, :type, :level, :life, :attack, :defense, :crit_chance, :crit_damage, :magic_find, :rarity, :image)",
        username=player_.player.name, name=player_slot_.player_slot.ring2['name'], type=player_slot_.player_slot.ring2['type'],
        level=player_slot_.player_slot.ring2['level'], life=player_slot_.player_slot.ring2['life'],
        attack=player_slot_.player_slot.ring2['attack'], defense=player_slot_.player_slot.ring2['defense'],
        crit_chance=player_slot_.player_slot.ring2['crit_chance'], crit_damage=player_slot_.player_slot.ring2['crit_damage'],
        magic_find=player_slot_.player_slot.ring2['magic_find'], rarity=player_slot_.player_slot.ring2['rarity'], image=player_slot_.player_slot.ring2['image'])
    db.execute("DELETE FROM second_hand WHERE username = :username",
               username=username)
    db.execute(
        "INSERT INTO second_hand (username, name, type, level, life, attack, defense, crit_chance, crit_damage, magic_find, rarity, image) VALUES (:username, :name, :type, :level, :life, :attack, :defense, :crit_chance, :crit_damage, :magic_find, :rarity, :image)",
        username=player_.player.name, name=player_slot_.player_slot.second_hand['name'], type=player_slot_.player_slot.second_hand['type'],
        level=player_slot_.player_slot.second_hand['level'], life=player_slot_.player_slot.second_hand['life'],
        attack=player_slot_.player_slot.second_hand['attack'], defense=player_slot_.player_slot.second_hand['defense'],
        crit_chance=player_slot_.player_slot.second_hand['crit_chance'], crit_damage=player_slot_.player_slot.second_hand['crit_damage'],
        magic_find=player_slot_.player_slot.second_hand['magic_find'], rarity=player_slot_.player_slot.second_hand['rarity'], image=player_slot_.player_slot.second_hand['image'])
    db.execute("DELETE FROM weapon WHERE username = :username",
               username=username)
    db.execute(
        "INSERT INTO weapon (username, name, type, level, life, attack, defense, crit_chance, crit_damage, magic_find, rarity, image) VALUES (:username, :name, :type, :level, :life, :attack, :defense, :crit_chance, :crit_damage, :magic_find, :rarity, :image)",
        username=player_.player.name, name=player_slot_.player_slot.weapon['name'], type=player_slot_.player_slot.weapon['type'],
        level=player_slot_.player_slot.weapon['level'], life=player_slot_.player_slot.weapon['life'],
        attack=player_slot_.player_slot.weapon['attack'], defense=player_slot_.player_slot.weapon['defense'],
        crit_chance=player_slot_.player_slot.weapon['crit_chance'], crit_damage=player_slot_.player_slot.weapon['crit_damage'],
        magic_find=player_slot_.player_slot.weapon['magic_find'], rarity=player_slot_.player_slot.weapon['rarity'], image=player_slot_.player_slot.weapon['image'])
    db.execute("DELETE FROM boots WHERE username = :username",
               username=username)
    db.execute(
        "INSERT INTO boots (username, name, type, level, life, attack, defense, crit_chance, crit_damage, magic_find, rarity, image) VALUES (:username, :name, :type, :level, :life, :attack, :defense, :crit_chance, :crit_damage, :magic_find, :rarity, :image)",
        username=player_.player.name, name=player_slot_.player_slot.boots['name'], type=player_slot_.player_slot.boots['type'],
        level=player_slot_.player_slot.boots['level'], life=player_slot_.player_slot.boots['life'],
        attack=player_slot_.player_slot.boots['attack'], defense=player_slot_.player_slot.boots['defense'],
        crit_chance=player_slot_.player_slot.boots['crit_chance'], crit_damage=player_slot_.player_slot.boots['crit_damage'],
        magic_find=player_slot_.player_slot.boots['magic_find'], rarity=player_slot_.player_slot.boots['rarity'], image=player_slot_.player_slot.boots['image'])

    # Consumables
    db.execute("UPDATE potion SET quantity = :quantity WHERE username = :username", quantity=consumable_item_.potion.quantity,
               username=username)
    db.execute("UPDATE x_potion SET quantity = :quantity WHERE username = :username", quantity=consumable_item_.x_potion.quantity,
               username=username)
    db.execute("UPDATE elixir SET quantity = :quantity WHERE username = :username", quantity=consumable_item_.elixir.quantity,
               username=username)
    db.execute("UPDATE chaos_orb SET quantity = :quantity WHERE username = :username", quantity=consumable_item_.chaos_orb.quantity,
               username=username)
    db.execute("UPDATE divine_orb SET quantity = :quantity WHERE username = :username", quantity=consumable_item_.divine_orb.quantity,
               username=username)
    db.execute("UPDATE exalted_orb SET quantity = :quantity WHERE username = :username", quantity=consumable_item_.exalted_orb.quantity,
               username=username)
    db.execute("UPDATE mirror_of_kalandra SET quantity = :quantity WHERE username = :username",
               quantity=consumable_item_.mirror_of_kalandra.quantity, username=username)
    db.execute("UPDATE roulette_wheel_ticket SET quantity = :quantity WHERE username = :username",
               quantity=consumable_item_.roulette_wheel_ticket.quantity, username=username)
    db.execute("UPDATE dense_fossil SET quantity = :quantity WHERE username = :username",
               quantity=consumable_item_.dense_fossil.quantity, username=username)
    db.execute("UPDATE serrated_fossil SET quantity = :quantity WHERE username = :username",
               quantity=consumable_item_.serrated_fossil.quantity, username=username)
    db.execute("UPDATE pristine_fossil SET quantity = :quantity WHERE username = :username",
               quantity=consumable_item_.pristine_fossil.quantity, username=username)
    db.execute("UPDATE deft_fossil SET quantity = :quantity WHERE username = :username",
               quantity=consumable_item_.deft_fossil.quantity, username=username)
    db.execute("UPDATE fractured_fossil SET quantity = :quantity WHERE username = :username",
               quantity=consumable_item_.fractured_fossil.quantity, username=username)


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