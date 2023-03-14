from assets.music.music import *
from assets.fonts.fonts import *
from settings import *
from classes import main_menu


pygame.init()
clock = pygame.time.Clock()
clock.tick(FPS)


def counter_helper(counter):
    counter_text = get_bold_font(40).render(f'{counter}', True, WHITE)
    counter_text_rect = counter_text.get_rect(center=(SCREEN_WIDTH / 2, 30))
    SCREEN.blit(counter_text, counter_text_rect)

# def bg_box_resetter():
#     SCREEN.blit(BG, (0, 0))
#     SCREEN.blit(BATTLE_BOX, (60, 40))


if __name__ == '__main__':

    background_music()
    # login_menu()
    main_menu.main_menu()
