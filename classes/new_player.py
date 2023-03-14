import pygame,sys
from settings import *
from assets.fonts.fonts import *
from button import *
from classes import consumable_item_
from classes import player_
from classes import save_load


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
                player_.player.name = username
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

        text1 = get_bold_font(50).render(f"You've been registered!, {player_.player.name}", True, WHITE)
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
                    save_load.save_state()
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
        

def register_data_insert(player_name):
    username = player_name
    db.execute(
        "INSERT INTO user_data (username, level, experience, total_life, life, attack, defense, shaman, crit_chance, crit_damage, magic_find) VALUES (:username, :level, :experience, :total_life, :life, :attack, :defense,:shaman, :crit_chance, :crit_damage, :magic_find)",
        username=username, level=player_.player.level, experience=player_.player.xp, total_life=player_.player.total_life, life=player_.player.life,
        attack=player_.player.attack, defense=player_.player.defense, shaman=player_.player.shaman,
        crit_chance=player_.player.crit_chance, crit_damage=player_.player.crit_damage, magic_find=player_.player.magic_find)

    rows = db.execute("SELECT * FROM users WHERE username = :username",
                      username=username)

    player_.player.name = rows[0]['username']

    # Consumables Instance
    db.execute(
        "INSERT INTO potion (username, type, name, value, quantity, rarity, code, sound) VALUES (:username, :type, :name, :value, :quantity, :rarity, :code, :sound)",
        username=player_.player.name, type=consumable_item_.potion.type, name=consumable_item_.potion.name, value=consumable_item_.potion.value, quantity=consumable_item_.potion.quantity,
        rarity=consumable_item_.potion.rarity, code=consumable_item_.potion.code, sound=consumable_item_.potion.sound)
    db.execute(
        "INSERT INTO x_potion (username, type, name, value, quantity, rarity, code, sound) VALUES (:username, :type, :name, :value, :quantity, :rarity, :code, :sound)",
        username=player_.player.name, type=consumable_item_.x_potion.type, name=consumable_item_.x_potion.name, value=consumable_item_.x_potion.value, quantity=consumable_item_.x_potion.quantity,
        rarity=consumable_item_.x_potion.rarity, code=consumable_item_.x_potion.code, sound=consumable_item_.x_potion.sound)
    db.execute(
        "INSERT INTO elixir (username, type, name, value, quantity, rarity, code, sound) VALUES (:username, :type, :name, :value, :quantity, :rarity, :code, :sound)",
        username=player_.player.name, type=consumable_item_.elixir.type, name=consumable_item_.elixir.name, value=consumable_item_.elixir.value, quantity=consumable_item_.elixir.quantity,
        rarity=consumable_item_.elixir.rarity, code=consumable_item_.elixir.code, sound=consumable_item_.elixir.sound)
    db.execute(
        "INSERT INTO chaos_orb (username, type, name, value, quantity, rarity, code, sound) VALUES (:username, :type, :name, :value, :quantity, :rarity, :code, :sound)",
        username=player_.player.name, type=consumable_item_.chaos_orb.type, name=consumable_item_.chaos_orb.name, value=consumable_item_.chaos_orb.value,
        quantity=consumable_item_.chaos_orb.quantity,
        rarity=consumable_item_.chaos_orb.rarity, code=consumable_item_.chaos_orb.code, sound=consumable_item_.chaos_orb.sound)
    db.execute(
        "INSERT INTO divine_orb (username, type, name, value, quantity, rarity, code, sound) VALUES (:username, :type, :name, :value, :quantity, :rarity, :code, :sound)",
        username=player_.player.name, type=consumable_item_.divine_orb.type, name=consumable_item_.divine_orb.name, value=consumable_item_.divine_orb.value,
        quantity=consumable_item_.divine_orb.quantity,
        rarity=consumable_item_.divine_orb.rarity, code=consumable_item_.divine_orb.code, sound=consumable_item_.divine_orb.sound)
    db.execute(
        "INSERT INTO exalted_orb (username, type, name, value, quantity, rarity, code, sound) VALUES (:username, :type, :name, :value, :quantity, :rarity, :code, :sound)",
        username=player_.player.name, type=consumable_item_.exalted_orb.type, name=consumable_item_.exalted_orb.name, value=consumable_item_.exalted_orb.value,
        quantity=consumable_item_.exalted_orb.quantity,
        rarity=consumable_item_.exalted_orb.rarity, code=consumable_item_.exalted_orb.code, sound=consumable_item_.exalted_orb.sound)
    db.execute(
        "INSERT INTO consumable_item_.mirror_of_kalandra. (username, type, name, value, quantity, rarity, code, sound) VALUES (:username, :type, :name, :value, :quantity, :rarity, :code, :sound)",
        username=player_.player.name, type=consumable_item_.mirror_of_kalandra.type, name=consumable_item_.mirror_of_kalandra.name,
        value=consumable_item_.mirror_of_kalandra.value, quantity=consumable_item_.mirror_of_kalandra.quantity,
        rarity=consumable_item_.mirror_of_kalandra.rarity, code=consumable_item_.mirror_of_kalandra.code, sound=consumable_item_.mirror_of_kalandra.sound)
    db.execute(
        "INSERT INTO consumable_item_.roulette_wheel_ticket. (username, type, name, value, quantity, rarity, code, sound) VALUES (:username, :type, :name, :value, :quantity, :rarity, :code, :sound)",
        username=player_.player.name, type=consumable_item_.roulette_wheel_ticket.type, name=consumable_item_.roulette_wheel_ticket.name,
        value=consumable_item_.roulette_wheel_ticket.value, quantity=consumable_item_.roulette_wheel_ticket.quantity,
        rarity=consumable_item_.roulette_wheel_ticket.rarity, code=consumable_item_.roulette_wheel_ticket.code, sound=consumable_item_.roulette_wheel_ticket.sound)

    db.execute(
        "INSERT INTO dense_fossil (username, type, name, value, quantity, rarity, code, sound, attribute) VALUES (:username, :type, :name, :value, :quantity, :rarity, :code, :sound, :attribute)",
        username=player_.player.name, type=consumable_item_.dense_fossil.type, name=consumable_item_.dense_fossil.name,
        value=consumable_item_.dense_fossil.value, quantity=consumable_item_.dense_fossil.quantity,
        rarity=consumable_item_.dense_fossil.rarity, code=consumable_item_.dense_fossil.code, sound=consumable_item_.dense_fossil.sound, attribute=consumable_item_.dense_fossil.attribute)
    db.execute(
        "INSERT INTO serrated_fossil (username, type, name, value, quantity, rarity, code, sound, attribute) VALUES (:username, :type, :name, :value, :quantity, :rarity, :code, :sound, :attribute)",
        username=player_.player.name, type=consumable_item_.serrated_fossil.type, name=consumable_item_.serrated_fossil.name,
        value=consumable_item_.serrated_fossil.value, quantity=consumable_item_.serrated_fossil.quantity,
        rarity=consumable_item_.serrated_fossil.rarity, code=consumable_item_.serrated_fossil.code, sound=consumable_item_.serrated_fossil.sound,
        attribute=consumable_item_.serrated_fossil.attribute)
    db.execute(
        "INSERT INTO pristine_fossil (username, type, name, value, quantity, rarity, code, sound, attribute) VALUES (:username, :type, :name, :value, :quantity, :rarity, :code, :sound, :attribute)",
        username=player_.player.name, type=consumable_item_.pristine_fossil.type, name=consumable_item_.pristine_fossil.name,
        value=consumable_item_.pristine_fossil.value, quantity=consumable_item_.pristine_fossil.quantity,
        rarity=consumable_item_.pristine_fossil.rarity, code=consumable_item_.pristine_fossil.code, sound=consumable_item_.pristine_fossil.sound,
        attribute=consumable_item_.pristine_fossil.attribute)
    db.execute(
        "INSERT INTO deft_fossil (username, type, name, value, quantity, rarity, code, sound, attribute) VALUES (:username, :type, :name, :value, :quantity, :rarity, :code, :sound, :attribute)",
        username=player_.player.name, type=consumable_item_.deft_fossil.type, name=consumable_item_.deft_fossil.name,
        value=consumable_item_.deft_fossil.value, quantity=consumable_item_.deft_fossil.quantity,
        rarity=consumable_item_.deft_fossil.rarity, code=consumable_item_.deft_fossil.code, sound=consumable_item_.deft_fossil.sound, attribute=consumable_item_.deft_fossil.attribute)
    db.execute(
        "INSERT INTO fractured_fossil (username, type, name, value, quantity, rarity, code, sound, attribute) VALUES (:username, :type, :name, :value, :quantity, :rarity, :code, :sound, :attribute)",
        username=player_.player.name, type=consumable_item_.fractured_fossil.type, name=consumable_item_.fractured_fossil.name,
        value=consumable_item_.fractured_fossil.value, quantity=consumable_item_.fractured_fossil.quantity,
        rarity=consumable_item_.fractured_fossil.rarity, code=consumable_item_.fractured_fossil.code, sound=consumable_item_.fractured_fossil.sound,
        attribute=consumable_item_.fractured_fossil.attribute)

    # Boss instance
    db.execute(
        "INSERT INTO boss_instance (username, wiegraf1, dycedarg1, wiegraf2, dycedarg2) VALUES (:username, :wiegraf1, :dycedarg1, :wiegraf2, :dycedarg2)",
        username=player_.player.name, wiegraf1=1, dycedarg1=1, wiegraf2=1, dycedarg2=1)

    # Delve instance
    db.execute(
        "INSERT INTO delve (username, depth, multiplier) VALUES (:username, :depth, :multiplier)",
        username=player_.player.name, depth=1, multiplier=0.01)