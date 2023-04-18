import pygame, sys
from settings import *
from button import *
from assets.fonts.fonts import *
from classes import main_menu
from classes import roulette_wheel
from classes import card
from classes import souls


def extras():
    global counter
    SCREEN.blit(BG, (0, 0))
    SCREEN.blit(BATTLE_BOX, (60, 40))

    # Icon Imagens
    SCREEN.blit(CARDS, (150, 100))
    SCREEN.blit(ROULETTE_WHEEL2_TICKET, (250, 100))
    SCREEN.blit(SOULS_ICON_COLORED, (350, 100))

    # Icon Texts
    cards_text = get_bold_font(20).render('CARDS', True, WHITE)
    cards_text_rect = cards_text.get_rect(center=(180, 180))
    SCREEN.blit(cards_text, cards_text_rect)

    roulette_text = get_bold_font(20).render('ROULETTE', True, WHITE)
    roulette_text_rect = roulette_text.get_rect(center=(280, 180))
    SCREEN.blit(roulette_text, roulette_text_rect)

    souls_text = get_bold_font(20).render('SOULS', True, WHITE)
    souls_text_rect = souls_text.get_rect(center=(380, 180))
    SCREEN.blit(souls_text, souls_text_rect)

    # Collision Points
    cards_rect = ICON_FRAME.get_rect(center=(180, 140))
    roulette_rect = ICON_FRAME.get_rect(center=(280, 140))
    souls_rect = ICON_FRAME.get_rect(center=(380, 140))

    while True:
        EXTRAS_MOUSE_POSITION = pygame.mouse.get_pos()
        BUTTONS = main_menu.main_menu_structure(EXTRAS_MOUSE_POSITION)

        BACK = Button(image=pygame.image.load("assets/images/Smallest Rect.png"), pos=(160, 600),
                      text_input="BACK", font=get_bold_font(30), base_color="White", hovering_color=BLUE)
        BUTTONS.append(BACK)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                main_menu.main_menu_structure_events(EXTRAS_MOUSE_POSITION, BUTTONS)
                if BACK.checkForInput(EXTRAS_MOUSE_POSITION):
                    counter = 0
                    main_menu.main_menu()
                if cards_rect.collidepoint(EXTRAS_MOUSE_POSITION):
                    card.cards('cards')
                if roulette_rect.collidepoint(EXTRAS_MOUSE_POSITION):
                    roulette_wheel.roulette()
                if souls_rect.collidepoint(EXTRAS_MOUSE_POSITION):
                    souls.souls_menu()
            if cards_rect.collidepoint(EXTRAS_MOUSE_POSITION):
                print('cards')
            if roulette_rect.collidepoint(EXTRAS_MOUSE_POSITION):
                print('roulette')

            for button in BUTTONS:
                button.changeColor(EXTRAS_MOUSE_POSITION)
                button.update(SCREEN)

            pygame.display.update()