from settings import *
from fonts import *


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


def shaman():
    player.life += player.shaman
    if player.life > player.total_life:
        player.life = player.total_life
    else:
        pass


def player_level_up():
    global temp_level_up
    next_level = str(player.level + 1)

    if player.xp >= 175000:
        player.xp = 175000
    else:
        player.xp += enemy.xp

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
            battle_finish()


def check_player_life():
    global counter, LAST_TIME_MS
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
            diff_time_ms = int(round(time.time() * 4000)) - LAST_TIME_MS
            if diff_time_ms >= 4000:
                counter = counter + 1
                LAST_TIME_MS = int(round(time.time() * 4000))
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