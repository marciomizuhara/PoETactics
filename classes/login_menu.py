import pygame,sys
from assets.fonts.fonts import *
from settings import *
from button import *
from classes import new_player
from classes import save_load


def login_menu():
    while True:
        SCREEN.fill(BLACK)
        pygame.display.set_caption("PoeTactics")
        LOGIN_MOUSE_POSITION = pygame.mouse.get_pos()

        # text1 = get_bold_font(50).render('LOGIN MENU', True, WHITE)
        # menu_rect1 = text1.get_rect(center=(SCREEN_WIDTH/2, 100))

        NEW_GAME_BUTTON = Button(image=pygame.image.load("assets/images/Options Rect.png"), pos=(SCREEN_WIDTH / 2, 200),
                                 text_input="New game", font=get_bold_font(40), base_color="White", hovering_color=PINK)
        LOAD_GAME_BUTTON = Button(image=pygame.image.load("assets/images/Options Rect.png"),
                                  pos=(SCREEN_WIDTH / 2, 350),
                                  text_input="Load game", font=get_bold_font(40), base_color="White",
                                  hovering_color=PINK)
        SMALL_QUIT_BUTTON = Button(image=pygame.image.load("assets/images/Small Quit Rect.png"), pos=(1870, 40),
                                   text_input="X", font=get_bold_font(40), base_color="White", hovering_color=PINK)

        # SCREEN.blit(text1, menu_rect1)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if NEW_GAME_BUTTON.checkForInput(LOGIN_MOUSE_POSITION):
                    new_player.register()
                if LOAD_GAME_BUTTON.checkForInput(LOGIN_MOUSE_POSITION):
                    save_load.load_username()
                if SMALL_QUIT_BUTTON.checkForInput(LOGIN_MOUSE_POSITION):
                    pygame.quit()
                    sys.exit()
        for button in [NEW_GAME_BUTTON, LOAD_GAME_BUTTON, SMALL_QUIT_BUTTON]:
            button.changeColor(LOGIN_MOUSE_POSITION)
            button.update(SCREEN)

        pygame.display.update()