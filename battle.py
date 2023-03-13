import random, sys
import player_
import character
import levels_xp
from assets.music.music import *
from button import *
from monster import *
from fonts import *
from player_ import player
from enemies.enemy_type import *
from enemies.humans import *
from enemies.monsters import *
from main_menu_structure import *
from human import *
from settings import *


def crit_chance(character_crit_chance, character_attack, character_critdamage):
    crit_chance_random = random.randint(1, 100)
    if crit_chance_random <= character_crit_chance:
        random2 = random.randint(10, character_attack // 2)
        crit_damage = int((character_attack + random2) + (character_critdamage / character_attack * 100))
        return crit_damage
    else:
        return character_attack


def boss_battle(boss_instance):
    global counter
    boss_music()
    show_dialogue(boss_instance)


def show_dialogue(character):
    print(f'{character.name}')
    global counter, LAST_TIME_MS
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

    levels_xp.display_level_xp()
    while True:
        QUOTING_MOUSE_POSITION = pygame.mouse.get_pos()
        CONTINUE = Button(image=pygame.image.load("assets/images/Smallest Rect.png"), pos=(SCREEN_WIDTH / 2 - 180, 590),
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
        if enemy in [character.wiegraf1, character.wiegraf2, character.dycedarg1, character.dycedarg2]:
            show_dialogue(enemy)
        if enemy.life == 0:
            SCREEN.fill(0)
            SCREEN.blit(BG, (0, 0))
            SCREEN.blit(BATTLE_BOX, (60, 40))
            # PLAYER
            SCREEN.blit(player.image, (130, 300))
            player_.player_level_up()
            battle_finish()
            # battle_elements_resetter()


# IF ENEMY ATTACK IS ZERO AND PLAYER ATTACK IS CRITICAL
def battle_condition_1_a(player_damage, a):
    global counter, LAST_TIME_MS
    levels_xp.display_level_xp()
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
    levels_xp.display_level_xp()
    global LAST_TIME_MS, counter
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

        diff_time_ms = int(round(time.time() * 4000)) - LAST_TIME_MS

        if diff_time_ms >= 4000:
            counter = counter + 1
            LAST_TIME_MS = int(round(time.time() * 4000))
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
    global counter, LAST_TIME_MS
    levels_xp.display_level_xp()
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

        diff_time_ms = int(round(time.time() * 4000)) - LAST_TIME_MS

        if diff_time_ms >= 4000:
            counter = counter + 1
            LAST_TIME_MS = int(round(time.time() * 4000))
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
    global counter, LAST_TIME_MS
    levels_xp.display_level_xp()
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

        diff_time_ms = int(round(time.time() * 4000)) - LAST_TIME_MS

        if diff_time_ms >= 4000:
            counter = counter + 1
            LAST_TIME_MS = int(round(time.time() * 4000))
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
    global counter, LAST_TIME_MS
    levels_xp.display_level_xp()
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

        diff_time_ms = int(round(time.time() * 4000)) - LAST_TIME_MS

        if diff_time_ms >= 4000:
            counter = counter + 1
            LAST_TIME_MS = int(round(time.time() * 4000))
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
    global counter, LAST_TIME_MS
    levels_xp.display_level_xp()
    enemy.life = enemy.life - e_damage
    player.life = player.life - p_damage
    p_a_s = False
    e_a_s = False
    while True:
        text1 = get_bold_font(50).render(f'{e_damage}', True, RED)
        text1_rect = text1.get_rect(center=(750, 260))
        text2 = get_bold_font(50).render(f'{p_damage}', True, RED)
        text2_rect = text2.get_rect(center=(180, 260))

        diff_time_ms = int(round(time.time() * 4000)) - LAST_TIME_MS

        if diff_time_ms >= 4000:
            counter = counter + 1
            LAST_TIME_MS = int(round(time.time() * 4000))
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
    global counter, LAST_TIME_MS, DROP_HEIGHT, drop_quantity
    check_player_life()
    player_.shaman()
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
    levels_xp.display_level_xp()
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

        diff_time_ms = int(round(time.time() * 4000)) - LAST_TIME_MS
        if diff_time_ms >= 4000:
            counter = counter + 1
            LAST_TIME_MS = int(round(time.time() * 4000))

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
    player_.check_player_life()


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
        if player.level == 5 and character.wiegraf1.status is True:
            enemy = character.wiegraf1
            boss_battle(character.wiegraf1)
        elif player.level == 10 and character.dycedarg1.status is True:
            enemy = character.dycedarg1
            boss_battle(character.dycedarg1)
        elif player.level == 15 and character.wiegraf2.status is True:
            enemy = character.wiegraf2
            boss_battle(character.wiegraf2)
        elif player.level == 20 and character.dycedarg2.status is True:
            enemy = character.dycedarg2
            boss_battle(character.dycedarg2)
        else:
            pass
    battle_elements_resetter()
    levels_xp.display_level_xp()
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

        diff_time_ms = int(round(time.time() * 4000)) - LAST_TIME_MS
        if diff_time_ms >= 4000:
            counter = counter + 1
            LAST_TIME_MS = int(round(time.time() * 4000))

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