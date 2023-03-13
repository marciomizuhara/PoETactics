from card import *
from fossil import *
from monster import *
from player_ import *
import globals_variables
from settings import *


#GLOBALS
DELVE_DROP_RATE = 100




class Delve:
    depth = 1
    multiplier = 0.005

    def __init__(self, mobs):
        self.mobs = mobs


def delve_menu():
    global counter, LAST_TIME_MS
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
        MAIN_MENU = Button(image=pygame.image.load("assets/images/Smallest Rect.png"),
                           pos=(SCREEN_WIDTH / 2 - 180, 500),
                           text_input="MAIN MENU", font=get_bold_font(30), base_color="White", hovering_color=BLUE)
        START_DELVING = Button(image=pygame.image.load("assets/images/Smallest Rect.png"),
                               pos=(SCREEN_WIDTH / 2 + 180, 500),
                               text_input="ENTER DELVE", font=get_bold_font(30), base_color="White",
                               hovering_color=BLUE)

        diff_time_ms = int(round(time.time() * 4000)) - LAST_TIME_MS
        if diff_time_ms >= 4000:
            counter = counter + 1
            LAST_TIME_MS = int(round(time.time() * 4000))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if MAIN_MENU.checkForInput(DELVE_MENU_MOUSE_POSITION):
                    pygame.mixer.music.fadeout(2)
                    pygame.mixer.music.stop()
                    from assets.music.music import background_music
                    background_music()
                    from main import main_menu
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


def display_delve_depth():
    level_text = get_regular_font(25).render(f"DEPTH: {Delve.depth}", True, WHITE)
    level_rect = level_text.get_rect(midright=(1260, 630))
    life_text = get_regular_font(25).render(f"Life Points: {player.life}/{player.total_life}", True, WHITE)
    life_rect = life_text.get_rect(midright=(1260, 660))
    SCREEN.blit(level_text, level_rect)
    SCREEN.blit(life_text, life_rect)


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
    from battle import crit_chance
    a = crit_chance(player.crit_chance, player.attack, player.crit_damage)
    if a > player.attack:
        counter = 0
        delve_battle_condition_1_a(biome, player_damage, a, hoard, i)
    else:
        counter = 0
        delve_battle_condition_1_b(biome, hoard, i, player_damage)


# IF ENEMY ATTACK IS ZERO AND PLAYER ATTACK IS CRITICAL
def delve_battle_condition_1_a(biome, player_damage, a, hoard, i):
    global counter, LAST_TIME_MS
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

        diff_time_ms = int(round(time.time() * 4000)) - LAST_TIME_MS

        if diff_time_ms >= 4000:
            counter = counter + 1
            LAST_TIME_MS = int(round(time.time() * 4000))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        if counter == 1:
            SCREEN.blit(text0, text0_rect)
            SCREEN.blit(text1, text1_rect)
            if not c_a:
                from assets.music.music import critical_attack_sound
                critical_attack_sound()
                c_a = True
        if counter == 2:
            SCREEN.blit(text2, text2_rect)
            if not e_a_s:
                from assets.music.music import enemy_attack_sound
                enemy_attack_sound()
                e_a_s = True
        if counter == 3:
            counter = 0
            delve_battle(biome, hoard)
        pygame.display.update()


def delve_battle_condition_1_b(biome, hoard, i, player_damage):
    display_delve_depth()
    global LAST_TIME_MS, counter
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

        diff_time_ms = int(round(time.time() * 4000)) - LAST_TIME_MS

        if diff_time_ms >= 4000:
            counter = counter + 1
            LAST_TIME_MS = int(round(time.time() * 4000))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        if counter == 1:
            SCREEN.blit(text1, text1_rect)
            if not p_a_s:
                from assets.music.music import critical_attack_sound
                critical_attack_sound()
                p_a_s = True
        if counter == 2:
            SCREEN.blit(text2, text2_rect)
            if not e_a_s:
                from assets.music.music import enemy_attack_sound
                enemy_attack_sound()
                e_a_s = True
        if counter == 3:
            counter = 0
            delve_battle(biome, hoard)
        pygame.display.update()


# PLAYER CRITICAL AND ENEMY NORMAL ATTACK
def delve_battle_condition_2a(biome, e_damage, hoard, i):
    global counter, LAST_TIME_MS
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

        diff_time_ms = int(round(time.time() * 4000)) - LAST_TIME_MS

        if diff_time_ms >= 4000:
            counter = counter + 1
            LAST_TIME_MS = int(round(time.time() * 4000))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        if counter == 1:
            SCREEN.blit(text0, text0_rect)
            SCREEN.blit(text1, text1_rect)
            if not c_a:
                from assets.music.music import critical_attack_sound
                critical_attack_sound()
                c_a = True
        if counter == 2:
            SCREEN.blit(text2, text2_rect)
            if not e_a_s:
                from assets.music.music import enemy_attack_sound
                enemy_attack_sound()
                e_a_s = True
        if counter == 3:
            counter = 0
            delve_battle(biome, hoard)
        pygame.display.update()


# PLAYER AND ENEMY CRITICAL
def delve_battle_condition_2b(biome, e_damage, p_damage, hoard, i):
    global counter, LAST_TIME_MS
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

        diff_time_ms = int(round(time.time() * 4000)) - LAST_TIME_MS

        if diff_time_ms >= 4000:
            counter = counter + 1
            LAST_TIME_MS = int(round(time.time() * 4000))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        if counter == 1:
            SCREEN.blit(text0, text0_rect)
            SCREEN.blit(text1, text1_rect)
            if not c_a:
                from assets.music.music import critical_attack_sound
                critical_attack_sound()
                c_a = True
        if counter == 2:
            SCREEN.blit(text1_5, text1_5_rect)
            SCREEN.blit(text2, text2_rect)
            if not c_a_2:
                from assets.music.music import critical_attack_sound
                critical_attack_sound()
                c_a_2 = True
        if counter == 3:
            counter = 0
            delve_battle(biome, hoard)
        pygame.display.update()


# PLAYER NORMAL ATTACK AND ENEMY CRITICAL
def delve_battle_condition_2c(biome, e_damage, p_damage, hoard, i):
    global counter, LAST_TIME_MS
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

        diff_time_ms = int(round(time.time() * 4000)) - LAST_TIME_MS

        if diff_time_ms >= 4000:
            counter = counter + 1
            LAST_TIME_MS = int(round(time.time() * 4000))
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
                from assets.music.music import critical_attack_sound
                critical_attack_sound()
                c_a = True
        if counter == 3:
            counter = 0
            delve_battle(biome, hoard)
        pygame.display.update()


# PLAYER AND ENEMY NORMAL ATTACK
def delve_battle_condition_2d(biome, e_damage, p_damage, hoard, i):
    global counter, LAST_TIME_MS
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

        diff_time_ms = int(round(time.time() * 4000)) - LAST_TIME_MS

        if diff_time_ms >= 4000:
            counter = counter + 1
            LAST_TIME_MS = int(round(time.time() * 4000))
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
                from assets.music.music import critical_attack_sound
                critical_attack_sound()
                e_a_s = True
        if counter == 3:
            counter = 0
            delve_battle(biome, hoard)
        pygame.display.update()


def delve_battle_finish(biome, hoard):
    global counter, LAST_TIME_MS, drop_quantity, cards_list, temp_card_drop
    counter = 0
    player.life = player.total_life
    Delve.depth = Delve.depth + 1
    Delve.multiplier = Delve.multiplier + 0.005
    from card import card_drop_rate
    card_drop_rate(player)
    delve_save_state()
    from main import save_state
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
        MAIN_MENU = Button(image=pygame.image.load("assets/images/Smallest Rect.png"),
                           pos=(SCREEN_WIDTH / 2 - 180, 500),
                           text_input="MAIN MENU", font=get_bold_font(30), base_color="White", hovering_color=BLUE)
        START_DELVING = Button(image=pygame.image.load("assets/images/Smallest Rect.png"),
                               pos=(SCREEN_WIDTH / 2 + 180, 500),
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
                if MAIN_MENU.checkForInput(DELVE_ENCOUNTER_MOUSE_POSITION):
                    pygame.mixer.music.fadeout(2)
                    pygame.mixer.music.stop()
                    from assets.music.music import background_music
                    background_music()
                    from main import main_menu
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
            if len(globals_variables.temp_card_drop) != 0:
                if card_setter is not True:
                    drop_text2 = get_bold_font(35).render(
                        f"{globals_variables.temp_card_drop[0].__dict__['name']} card dropped!", True, PINK)
                    drop_text2_rect = drop_text2.get_rect(center=(SCREEN_WIDTH / 2, drop_height))
                    SCREEN.blit(drop_text2, drop_text2_rect)
                    playsound(DROP_CONSUMABLE, False)
                    drop_quantity = 1
                    globals_variables.temp_card_drop.clear()
                    card_setter = True

        if counter >= 4:
            for button in [MAIN_MENU, START_DELVING]:
                button.changeColor(DELVE_ENCOUNTER_MOUSE_POSITION)
                button.update(SCREEN)

        pygame.display.update()


def delve_encounter():
    global counter, LAST_TIME_MS
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
        MAIN_MENU = Button(image=pygame.image.load("assets/images/Smallest Rect.png"),
                           pos=(SCREEN_WIDTH / 2 - 180, 500),
                           text_input="MAIN MENU", font=get_bold_font(30), base_color="White", hovering_color=BLUE)
        START_DELVING = Button(image=pygame.image.load("assets/images/Smallest Rect.png"),
                               pos=(SCREEN_WIDTH / 2 + 180, 500),
                               text_input="ENTER DELVE", font=get_bold_font(30), base_color="White",
                               hovering_color=BLUE)

        diff_time_ms = int(round(time.time() * 4000)) - LAST_TIME_MS
        if diff_time_ms >= 4000:
            counter = counter + 1
            LAST_TIME_MS = int(round(time.time() * 4000))

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