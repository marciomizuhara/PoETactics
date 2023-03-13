import sys
from settings import *
from fonts import *
from inventory import *
from button import *


def game_over():
    global counter, LAST_TIME_MS
    SCREEN.fill(BLACK)
    life_checking_setter = False
    welcome_setter = False

    while True:
        SCREEN.fill(BLACK)
        pygame.display.set_caption("PoETactics")
        GAME_OVER_MOUSE_POSITION = pygame.mouse.get_pos()

        text1 = get_bold_font(100).render(f"GAME OVER!", True, RED)
        menu_rect1 = text1.get_rect(center=(SCREEN_WIDTH / 2, 300))

        SCREEN.blit(text1, menu_rect1)

        CONTINUE = Button(image=pygame.image.load("assets/images/Next Rect.png"),
                          pos=(SCREEN_WIDTH / 2, SCREEN_HEIGHT - 200),
                          text_input="CONTINUE", font=get_bold_font(40), base_color="White", hovering_color=PINK)

        diff_time_ms = int(round(time.time() * 4000)) - LAST_TIME_MS
        if diff_time_ms >= 4000:
            counter = counter + 1
            LAST_TIME_MS = int(round(time.time() * 4000))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if CONTINUE.checkForInput(GAME_OVER_MOUSE_POSITION):
                    inventory.clear()
                    from main import login_menu
                    login_menu()

        if counter >= 1:
            SCREEN.blit(text1, menu_rect1)
        if counter >= 2:
            for button in [CONTINUE]:
                button.changeColor(GAME_OVER_MOUSE_POSITION)
                button.update(SCREEN)

        pygame.display.update()