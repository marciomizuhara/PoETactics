from settings import *
from classes.player_slot_ import PlayerSlot
from assets.fonts.fonts import *

from classes import battle
from classes import enemy
from classes import encounter

from assets.music.music import *
from items.amulets import *
from items.armors import *
from items.boots import *
from items.cards import *
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
from levels_xp import *
temp_level_up = False


class Player:
    def __init__(self, name, total_life, life, attack, defense, level, xp, shaman, crit_chance, crit_damage,
                 magic_find, image):
        self.name = name
        self.total_life = total_life
        self.life = life
        self.attack = attack
        self.defense = defense
        self.level = level
        self.xp = xp
        self.shaman = shaman
        self.crit_chance = crit_chance
        self.crit_damage = crit_damage
        self.magic_find = magic_find
        self.image = image


# Level 1 player instance
player: Player = Player('unknown', 500, 500, 100, 100, 1, 0, 1, 15, 15, 0, PLAYER)
# player = Player('unknown', 500, 500, 100, 100, 1, 0, 1, 15, 15, 0, PLAYER)



def player_level_up():
    global temp_level_up
    next_level = str(player.level + 1)

    if player.xp >= 175000:
        player.xp = 175000
    else:
        player.xp += encounter.enemy.xp

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
            battle.battle_finish()


def draw_player_level_up():
    global temp_level_up, counter, LAST_TIME_MS
    level_up_sound_setter = False
    if temp_level_up is True:
        battle.battle_elements_resetter()
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
                        battle.battle_finish()

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


def shaman():
    print('shaman', player.life)
    player.life += player.shaman
    if player.life > player.total_life:
        player.life = player.total_life
    else:
        pass