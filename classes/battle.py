import pygame,sys, random
from button import *
from classes import enemy
from assets.music.music import *
from classes import character
from classes import drop
from classes import encounter
from classes import inventory
from classes import main_menu
from classes import player_
from classes import save_load
from assets.fonts.fonts import *
from settings import *


previous_time = pygame.time.get_ticks()
time_counter = 0.0
enemy_setter = True


def increment_time(previous_time, time_counter):
    current_time = pygame.time.get_ticks()
    if current_time - previous_time >= 100:
        time_counter += 0.1
        previous_time = current_time
    return round(previous_time, 2), round(time_counter, 2)


def transform_image_color(image, color):
    width, height = image.get_size()
    width -= 2
    height -= 2
    new_image = pygame.Surface((width, height), pygame.SRCALPHA)
    for x in range(width):
        for y in range(height):
            cor = image.get_at((x, y))
            if cor.a > 0: # verifica se o pixel não é transparente
                new_image.set_at((x, y), (color))
    return new_image


def player_hit_effect(enemy_image, type):
    global time_counter, previous_time
    previous_time, time_counter = increment_time(previous_time, time_counter)
    if type == 'normal' or type == 'critical':
        color = ''
        if type == 'normal':
            color = BLACK
        else:
            color = RED
        if time_counter == 0.0:
            new_image = transform_image_color(pygame.image.load(enemy_image), color)
            image_rect = pygame.image.load(enemy_image).get_rect(midbottom=(750, 500))
            SCREEN.blit(new_image, image_rect)
        if time_counter == 0.1:
            new_image = transform_image_color(pygame.image.load(enemy_image), WHITE)
            image_rect = pygame.image.load(enemy_image).get_rect(midbottom=(750, 500))
            SCREEN.blit(new_image, image_rect)
        if time_counter == 0.2:
            new_image = transform_image_color(pygame.image.load(enemy_image), color)
            image_rect = pygame.image.load(enemy_image).get_rect(midbottom=(750, 500))
            SCREEN.blit(new_image, image_rect)
        if time_counter == 0.3:
            new_image = transform_image_color(pygame.image.load(enemy_image), WHITE)
            image_rect = pygame.image.load(enemy_image).get_rect(midbottom=(750, 500))
            SCREEN.blit(new_image, image_rect)
        if time_counter == 0.4:
            new_image = transform_image_color(pygame.image.load(enemy_image), color)
            image_rect = pygame.image.load(enemy_image).get_rect(midbottom=(750, 500))
            SCREEN.blit(new_image, image_rect)
        if time_counter == 0.5:
            new_image = transform_image_color(pygame.image.load(enemy_image), WHITE)
            image_rect = pygame.image.load(enemy_image).get_rect(midbottom=(750, 500))
            SCREEN.blit(new_image, image_rect)
        if time_counter == 0.6:
            new_image = pygame.image.load(enemy_image)
            image_rect = new_image.get_rect(midbottom=(750, 500))
            SCREEN.blit(new_image, image_rect)
            battle_elements_resetter()
    else:
        pass


def enemy_hit_effect(player_image, type):
    global time_counter, previous_time
    previous_time, time_counter = increment_time(previous_time, time_counter)
    if type == 'normal' or type == 'critical':
        color = ''
        if type == 'normal':
            color = BLACK
        else:
            color = RED

        if color != 0:
            if time_counter == 1.0:
                new_image = transform_image_color(player_image, color)
                image_rect = player_image.get_rect(midbottom=(175, 488))
                SCREEN.blit(new_image, image_rect)
            if time_counter == 1.1:
                new_image = transform_image_color(player_image, WHITE)
                image_rect = player_image.get_rect(midbottom=(175, 488))
                SCREEN.blit(new_image, image_rect)
            if time_counter == 1.2:
                new_image = transform_image_color(player_image, color)
                image_rect = player_image.get_rect(midbottom=(175, 488))
                SCREEN.blit(new_image, image_rect)
            if time_counter == 1.3:
                new_image = transform_image_color(player_image, WHITE)
                image_rect = player_image.get_rect(midbottom=(175, 488))
                SCREEN.blit(new_image, image_rect)
            if time_counter == 1.4:
                new_image = transform_image_color(player_image, color)
                image_rect = player_image.get_rect(midbottom=(175, 488))
                SCREEN.blit(new_image, image_rect)
            if time_counter == 1.5:
                new_image = transform_image_color(player_image, WHITE)
                image_rect = player_image.get_rect(midbottom=(175, 488))
                SCREEN.blit(new_image, image_rect)
            if time_counter == 1.6:
                # new_image = PLAYER
                # image_rect = new_image.get_rect(midbottom=(179, 480))
                # SCREEN.blit(new_image, image_rect)
                SCREEN.blit(player_.player.image, (130, 300))
                battle_elements_resetter()
    else:
        pass



def show_dialogue(character):
    print(f'{character.name}')
    # global counter, LAST_TIME_MS
    height = 100
    character_setter = False
    quote1_setter = False
    quote2_setter = False
    quote3_setter = False
    quote4_setter = False

    SCREEN.blit(BG, (0, 0))
    SCREEN.blit(BATTLE_BOX, (60, 40))

    # PLAYER
    SCREEN.blit(player_.player.image, (130, 300))
    # ENEMY
    image_rect = pygame.image.load(enemy.image).get_rect(midbottom=(750, 500))
    SCREEN.blit(pygame.image.load(enemy.image), image_rect)

    player_.display_level_xp()
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
                        battle.battle()
                    else:
                        print('entrou char morto')
                        character.status = False
                        username = player_.player.name
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
                        battle.battle_elements_resetter()
                        battle.battle_finish()

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
    boss_music()
    show_dialogue(boss_instance)


def battle_elements_resetter():
    global enemy_setter
    SCREEN.blit(BG, (0, 0))
    SCREEN.blit(BATTLE_BOX, (60, 40))
    # PLAYER
    SCREEN.blit(player_.player.image, (130, 300))
    # ENEMY
    if encounter.enemy.life >= 0:
        image_rect = pygame.image.load(encounter.enemy.image).get_rect(midbottom=(750, 500))
        SCREEN.blit(pygame.image.load(encounter.enemy.image), image_rect)

    if player_.player.life < 0:
        player_.player.life = 0

    # CONVERTION
    player_ratio = player_.player.life / player_.player.total_life
    player_life_width = 200 * player_ratio

    enemy_ratio = encounter.enemy.life / encounter.enemy.total_life
    enemy_life_width = 200 * enemy_ratio
    if encounter.enemy.life < 0:
        encounter.enemy.life = 0
    text1 = get_regular_font(20).render(f"{round(player_.player.life)}/{player_.player.total_life}", True, WHITE)
    text1_rect = text1.get_rect(midleft=(100, 540))
    text1_5 = get_bold_font(20).render(f"{player_.player.name}", True, WHITE)
    text1_5_rect = text1_5.get_rect(midleft=(100, 570))
    text2 = get_regular_font(20).render(f"{round(encounter.enemy.life)}/{encounter.enemy.total_life}", True, WHITE)
    text2_rect = text2.get_rect(midright=(830, 540))
    text3 = get_bold_font(20).render(f"{encounter.enemy.name}", True, WHITE)
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


def crit_chance(character_crit_chance, character_attack, character_critdamage):
    crit_chance_random = random.randint(1, 100)
    if crit_chance_random <= character_crit_chance:
        random2 = random.randint(10, character_attack // 2)
        crit_damage = int((character_attack + random2) + (character_critdamage / character_attack * 100))
        return crit_damage
    else:
        return character_attack


def battle():
    global enemy_setter
    if encounter.enemy.life > 0 and enemy_setter is True:
        # life_bars()
        battle_elements_resetter()

        # IF ENEMY ATTACK IS ZERO
        if encounter.enemy.attack <= player_.player.defense:
            battle_condition_1()

        # # IF ENEMY ATTACK IS NOT ZERO
        else:
            a = crit_chance(player_.player.crit_chance, player_.player.attack, player_.player.crit_damage)
            b = crit_chance(encounter.enemy.crit_chance, encounter.enemy.attack, 1.4)
            # PLAYER CRITICAL AND ENEMY NORMAL ATTACK
            if a > player_.player.attack and b == encounter.enemy.attack:
                enemy_damage = a - encounter.enemy.defense
                counter = 0
                battle_condition_2a(enemy_damage)

            # PLAYER AND ENEMY CRITICAL
            elif a > player_.player.attack and b > encounter.enemy.attack:
                enemy_damage = a - encounter.enemy.defense
                player_damage = b - player_.player.defense
                counter = 0
                battle_condition_2b(enemy_damage, player_damage)

            # PLAYER NORMAL ATTACK AND ENEMY CRITICAL
            elif a == player_.player.attack and b > encounter.enemy.attack:
                enemy_damage = player_.player.attack - encounter.enemy.defense
                player_damage = b - player_.player.defense
                counter = 0
                battle_condition_2c(enemy_damage, player_damage)

            else:
                enemy_damage = player_.player.attack - encounter.enemy.defense
                player_damage = encounter.enemy.attack - player_.player.defense
                counter = 0
                battle_condition_2d(enemy_damage, player_damage)

    else:
        encounter.enemy.life = 0
        enemy_setter = False
        # battle_elements_resetter()
        if enemy in [character.wiegraf1, character.wiegraf2, character.dycedarg1, character.dycedarg2]:
            show_dialogue(enemy)
        if encounter.enemy.life == 0:
            battle_finish()
            # battle_elements_resetter()


# IF ENEMY ATTACK IS ZERO AND PLAYER ATTACK IS CRITICAL
def battle_condition_1_a(player_damage, a):
    print('1a')
    global LAST_TIME_MS, counter, previous_time, time_counter
    player_.display_level_xp()
    enemy_damage = a - encounter.enemy.defense
    encounter.enemy.life = encounter.enemy.life - enemy_damage
    player_.player.life = player_.player.life - player_damage
    counter = 0
    c_a = False
    e_a_s = False
    previous_time, time_counter = pygame.time.get_ticks(), 0.0
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

            player_hit_effect(encounter.enemy.image, 'critical')

            # SCREEN.blit(transform_image_color(pygame.image.load(encounter.enemy.image), BLACK), (130, 300))
            # print(transform_image_color(encounter.enemy.image, BLACK))

        if counter == 2:
            SCREEN.blit(text2, text2_rect)
            if not e_a_s:
                enemy_attack_sound()
                e_a_s = True
            enemy_hit_effect(time_counter, PLAYER, 'zero')
        if counter == 3:
            counter = 0
            battle()
        pygame.display.update()


# IF ENEMY ATTACK IS ZERO AND PLAYER ATTACK IS NORMAL
def battle_condition_1_b(player_damage):
    print('1b')
    global LAST_TIME_MS, counter, previous_time, time_counter
    player_.display_level_xp()
    p_a_s = False
    e_a_s = False
    enemy_damage = player_.player.attack - encounter.enemy.defense
    encounter.enemy.life = encounter.enemy.life - enemy_damage
    player_.player.life = player_.player.life - player_damage
    counter = 0
    previous_time, time_counter = pygame.time.get_ticks(), 0.0
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
            player_hit_effect(encounter.enemy.image, 'normal')

        if counter == 2:
            if not e_a_s:
                SCREEN.blit(text2, text2_rect)
                enemy_attack_sound()
                e_a_s = True
            enemy_hit_effect(time_counter, PLAYER, 'zero')
        if counter == 3:
            counter = 0
            battle()
        pygame.display.update()


# IF ENEMY ATTACK IS ZERO
def battle_condition_1():
    global counter
    player_damage = 0
    a = crit_chance(player_.player.crit_chance, player_.player.attack, player_.player.crit_damage)
    if a > player_.player.attack:
        counter = 0
        battle_condition_1_a(player_damage, a)
    else:
        counter = 0
        battle_condition_1_b(player_damage)


# PLAYER CRITICAL AND ENEMY NORMAL ATTACK
def battle_condition_2a(e_damage):
    global counter, LAST_TIME_MS, previous_time, time_counter
    player_.display_level_xp()
    player_damage = encounter.enemy.attack - player_.player.defense
    encounter.enemy.life = encounter.enemy.life - e_damage
    player_.player.life = player_.player.life - player_damage
    c_a = False
    e_a_s = False
    previous_time, time_counter = pygame.time.get_ticks(), 0.0
    print('2a')
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
            player_hit_effect(encounter.enemy.image, 'critical')
        if counter == 2:
            if not e_a_s:
                SCREEN.blit(text2, text2_rect)
                enemy_attack_sound()
                e_a_s = True
            enemy_hit_effect(PLAYER, 'normal')
        if counter == 3:
            counter = 0
            battle()
        pygame.display.update()


# PLAYER AND ENEMY CRITICAL
def battle_condition_2b(e_damage, p_damage):
    print('2b')
    global counter, LAST_TIME_MS
    player_.display_level_xp()
    encounter.enemy.life = encounter.enemy.life - e_damage
    player_.player.life = player_.player.life - p_damage
    c_a = False
    c_a_2 = False
    previous_time, time_counter = pygame.time.get_ticks(), 0.0
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
            player_hit_effect(encounter.enemy.image, 'normal')
        if counter == 2:
            if not c_a_2:
                SCREEN.blit(text1_5, text1_5_rect)
                SCREEN.blit(text2, text2_rect)
                critical_attack_sound()
                c_a_2 = True
            enemy_hit_effect(PLAYER, 'normal')
        if counter == 3:
            counter = 0
            battle()
        pygame.display.update()


# PLAYER NORMAL ATTACK AND ENEMY CRITICAL
def battle_condition_2c(e_damage, p_damage):
    print('2c')
    global counter, LAST_TIME_MS, previous_time, time_counter
    player_.display_level_xp()
    encounter.enemy.life = encounter.enemy.life - e_damage
    player_.player.life = player_.player.life - p_damage
    p_a_s = False
    c_a = False
    previous_time, time_counter = pygame.time.get_ticks(), 0.0
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
            player_hit_effect(encounter.enemy.image, 'normal')
        if counter == 2:
            if not c_a:
                SCREEN.blit(text1_5, text1_5_rect)
                SCREEN.blit(text2, text2_rect)
                critical_attack_sound()
                c_a = True
            enemy_hit_effect(PLAYER, 'critical')
        if counter == 3:
            counter = 0
            battle()
        pygame.display.update()


# PLAYER AND ENEMY NORMAL ATTACK
def battle_condition_2d(e_damage, p_damage):
    print('2d')
    global counter, LAST_TIME_MS, previous_time, time_counter
    player_.display_level_xp()
    encounter.enemy.life = encounter.enemy.life - e_damage
    player_.player.life = player_.player.life - p_damage
    counter = 0
    p_a_s = False
    e_a_s = False
    previous_time, time_counter = pygame.time.get_ticks(), 0.0
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
            player_hit_effect(encounter.enemy.image, 'normal')
        if counter == 2:
            if not e_a_s:
                SCREEN.blit(text2, text2_rect)
                critical_attack_sound()
                e_a_s = True
            enemy_hit_effect(PLAYER, 'normal')
        if counter == 3:
            counter = 0
            battle()
        pygame.display.update()


def battle_finish():
    global counter, LAST_TIME_MS, DROP_HEIGHT, drop_quantity, enemy_setter
    player_.check_player_life()
    player_.shaman()
    drop.gear_drop_rate()
    drop.unique_drop_rate()
    drop.consumable_drop_rate()
    # player_level_up()
    player_.draw_player_level_up()
    save_load.save_state()

    if encounter.enemy.name == 'Wiegraf':
        character.wiegraf1.status = False
    elif encounter.enemy.name == 'Dycedarg':
        character.dycedarg1.status = False
    elif encounter.enemy.name == 'Wiegraf, Corpse Brigade Head':
        character.wiegraf2.status = False
    elif encounter.enemy.name == 'Dycedarg, the Betrayer God':
        character.dycedarg2.status = False
    else:
        pass
    battle_elements_resetter()
    player_.display_level_xp()
    SCREEN.fill(0)
    SCREEN.blit(BG, (0, 0))
    SCREEN.blit(BATTLE_BOX, (60, 40))
    # PLAYER
    SCREEN.blit(player_.player.image, (130, 300))
    player_.player_level_up()
    enemy_setter = True
    counter = 0
    text1 = get_bold_font(30).render(
        f"You've defeated level {encounter.enemy.level} {encounter.enemy.name} and gained {encounter.enemy.xp} xp points!", True, "White")
    text1_rect = text1.get_rect(center=(440, 100))
    SCREEN.blit(text1, text1_rect)
    text2 = get_regular_font(25).render(f"Your shaman healed you {player_.player.shaman} life points!", True, "White")
    text2_rect = text2.get_rect(center=(440, 170))
    SCREEN.blit(text2, text2_rect)
    drop_setter = False
    unique_setter = False
    consumable_setter = False
    ticket_setter = False
    while True:
        # battle_elements_resetter()
        BATTLE_FINISH_MOUSE_POSITION = pygame.mouse.get_pos()
        BUTTONS = main_menu.main_menu_structure(BATTLE_FINISH_MOUSE_POSITION)
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
                main_menu.main_menu_structure_events(BATTLE_FINISH_MOUSE_POSITION, BUTTONS)
                if CONTINUE.checkForInput(BATTLE_FINISH_MOUSE_POSITION):
                    DROP_HEIGHT = 210
                    counter = 0
                    encounter.encounter()

        if counter == 1:
            if len(drop.temp_gear_drop) != 0:
                if drop_setter is False:
                    if len(inventory.inventory) >= 150:
                        gear_drop_text = get_bold_font(35).render(f"[INVENTORY FULL! Get rid of unwanted gear first!]",
                                                                  True, YELLOW)
                    else:
                        gear_drop_text = get_bold_font(35).render(f"{drop.temp_gear_drop[-1].__dict__['name']} level "
                                                                  f"{drop.temp_gear_drop[-1].__dict__['level']} dropped!",
                                                                  True,
                                                                  YELLOW)
                    gear_drop_text_rect = gear_drop_text.get_rect(center=(440, DROP_HEIGHT))
                    SCREEN.blit(gear_drop_text, gear_drop_text_rect)
                    gear_drop_sound()
                    # playsound(DROP_1, True)
                    drop.temp_gear_drop.clear()
                    DROP_HEIGHT = DROP_HEIGHT + 40
                    drop_setter = True
                    counter = 0

        if counter == 1:
            if len(drop.temp_unique_drop) != 0:
                if unique_setter is False:
                    unique_drop_text = get_bold_font(35).render(f"{drop.temp_unique_drop[-1].__dict__['name']} level "
                                                                f"{drop.temp_unique_drop[-1].__dict__['level']} dropped!",
                                                                True,
                                                                ORANGE)
                    unique_drop_text_rect = unique_drop_text.get_rect(center=(440, DROP_HEIGHT))
                    SCREEN.blit(unique_drop_text, unique_drop_text_rect)
                    gear_drop_sound()
                    # playsound(DROP_1, False)
                    drop.temp_unique_drop.clear()
                    DROP_HEIGHT = DROP_HEIGHT + 40
                    unique_setter = True
                    counter = 0

        if counter == 1:
            if len(drop.temp_consumable_drop) != 0:
                if consumable_setter is False:
                    consumable_drop_text = get_bold_font(35).render(
                        f"{drop.drop_quantity}x {drop.temp_consumable_drop[-1].__dict__['name']} dropped!",
                        True, CYAN)
                    consumable_drop_text_rect = consumable_drop_text.get_rect(center=(440, DROP_HEIGHT))
                    SCREEN.blit(consumable_drop_text, consumable_drop_text_rect)
                    consumable_drop_sound()
                    drop.temp_consumable_drop.clear()
                    drop_quantity = 1
                    consumable_setter = True
                    counter = 0
        if counter == 1:
            if len(drop.temp_ticket_drop) != 0:
                if ticket_setter is False:
                    DROP_HEIGHT = DROP_HEIGHT + 40
                    ticket_drop_text = get_bold_font(35).render(
                        f"{drop.temp_ticket_drop[-1].__dict__['name']} dropped!",
                        True, PINK)
                    ticket_drop_text_rect = ticket_drop_text.get_rect(center=(440, DROP_HEIGHT))
                    SCREEN.blit(ticket_drop_text, ticket_drop_text_rect)
                    consumable_drop_sound()
                    # playsound(temp_ticket_drop[0].__dict__['sound'], False)
                    drop.temp_ticket_drop.clear()
                    ticket_setter = True
                    counter = 0

        if counter >= 1:
            DROP_HEIGHT = 210

        for button in BUTTONS:
            button.changeColor(BATTLE_FINISH_MOUSE_POSITION)
            button.update(SCREEN)

        pygame.display.update()