import sys
import character
from button import *
from delve import *
from player_ import player
from player_slot import *


def main_menu_structure(mouse):
    if player.level != 20 and character.dycedarg2.status is True:
        START_BATTLE = Button(image=pygame.image.load("assets/images/ONE_LINE_OPTION.png"), pos=(1100, 50),
                              text_input="EXPLORE", font=get_bold_font(30), base_color="White",
                              hovering_color=BLUE)
        INVENTORY = Button(image=pygame.image.load("assets/images/ONE_LINE_OPTION.png"), pos=(1100, 105),
                           text_input="INVENTORY", font=get_bold_font(30), base_color="White", hovering_color=BLUE)
        CONSUMABLE_ITEMS = Button(image=pygame.image.load("assets/images/ONE_LINE_OPTION.png"),
                                  pos=(SCREEN_WIDTH - 180, 210),
                                  text_input="CONSUMABLE ITEMS", font=get_bold_font(30), base_color="White",
                                  hovering_color=BLUE)
        PLAYER_STATUS = Button(image=pygame.image.load("assets/images/ONE_LINE_OPTION.png"), pos=(1100, 215),
                               text_input="PLAYER STATUS", font=get_bold_font(30), base_color="White",
                               hovering_color=BLUE)
        EXTRAS = Button(image=pygame.image.load("assets/images/ONE_LINE_OPTION.png"), pos=(1100, 370),
                        text_input="EXTRAS", font=get_bold_font(30), base_color="White",
                        hovering_color=BLUE)
        HELP = Button(image=pygame.image.load("assets/images/ONE_LINE_OPTION.png"), pos=(1100, 325),
                      text_input="HELP", font=get_bold_font(30), base_color="White", hovering_color=BLUE)
        MAIN_MENU = Button(image=pygame.image.load("assets/images/ONE_LINE_OPTION.png"), pos=(1100, 370),
                           text_input="MAIN MENU", font=get_bold_font(30), base_color="White", hovering_color=BLUE)
        QUIT_BUTTON = Button(image=pygame.image.load("assets/images/ONE_LINE_OPTION.png"), pos=(1100, 420),
                             text_input="QUIT", font=get_bold_font(30), base_color="White", hovering_color=BLUE)
        BUTTONS = [START_BATTLE, INVENTORY, CONSUMABLE_ITEMS, PLAYER_STATUS, EXTRAS, HELP, MAIN_MENU, QUIT_BUTTON]
        return BUTTONS
    else:
        START_BATTLE = Button(image=pygame.image.load("assets/images/ONE_LINE_OPTION.png"), pos=(1100, 50),
                              text_input="EXPLORE", font=get_bold_font(30), base_color="White",
                              hovering_color=BLUE)
        INVENTORY = Button(image=pygame.image.load("assets/images/ONE_LINE_OPTION.png"), pos=(1100, 105),
                           text_input="INVENTORY", font=get_bold_font(30), base_color="White", hovering_color=BLUE)
        CONSUMABLE_ITEMS = Button(image=pygame.image.load("assets/images/ONE_LINE_OPTION.png"), pos=(1100, 160),
                                  text_input="CONSUMABLE ITEMS", font=get_bold_font(30), base_color="White",
                                  hovering_color=BLUE)
        PLAYER_STATUS = Button(image=pygame.image.load("assets/images/ONE_LINE_OPTION.png"), pos=(1100, 215),
                               text_input="PLAYER STATUS", font=get_bold_font(30), base_color="White",
                               hovering_color=BLUE)
        DELVE = Button(image=pygame.image.load("assets/images/ONE_LINE_OPTION.png"), pos=(1100, 270),
                       text_input="DELVE", font=get_bold_font(30), base_color="White",
                       hovering_color=BLUE)
        ENDGAME_BOSSES = Button(image=pygame.image.load("assets/images/ONE_LINE_OPTION.png"), pos=(1100, 325),
                                text_input="ENDGAME BOSSES", font=get_bold_font(30), base_color="White",
                                hovering_color=BLUE)
        EXTRAS = Button(image=pygame.image.load("assets/images/ONE_LINE_OPTION.png"), pos=(1100, 380),
                        text_input="EXTRAS", font=get_bold_font(30), base_color="White",
                        hovering_color=BLUE)
        HELP = Button(image=pygame.image.load("assets/images/ONE_LINE_OPTION.png"), pos=(1100, 435),
                      text_input="HELP", font=get_bold_font(30), base_color="White", hovering_color=BLUE)
        MAIN_MENU = Button(image=pygame.image.load("assets/images/ONE_LINE_OPTION.png"), pos=(1100, 490),
                           text_input="MAIN MENU", font=get_bold_font(30), base_color="White", hovering_color=BLUE)
        QUIT_BUTTON = Button(image=pygame.image.load("assets/images/ONE_LINE_OPTION.png"), pos=(1100, 545),
                             text_input="QUIT", font=get_bold_font(30), base_color="White", hovering_color=BLUE)
        BUTTONS_LIST = [START_BATTLE, INVENTORY, CONSUMABLE_ITEMS, PLAYER_STATUS, DELVE, ENDGAME_BOSSES, EXTRAS, HELP,
                        MAIN_MENU, QUIT_BUTTON]
        return BUTTONS_LIST


def main_menu_structure_events(mouse, buttons):
    if player.level == 20:
        if buttons[0].checkForInput(mouse):
            from battle import encounter
            encounter()
        if buttons[1].checkForInput(mouse):
            from main import show_inventory_page_1
            show_inventory_page_1(1)
        if buttons[2].checkForInput(mouse):
            from main import show_consumable_items
            show_consumable_items()
        if buttons[3].checkForInput(mouse):
            from player_status import player_status
            player_status()
        if buttons[4].checkForInput(mouse):
            pygame.mixer.music.fadeout(2)
            pygame.mixer.music.stop()
            from assets.music.music import delve_music
            delve_music()
            from delve import delve_menu
            delve_menu()
            delve_menu()
        if buttons[5].checkForInput(mouse):
            # bosses
            pass
        if buttons[6].checkForInput(mouse):
            from extras import extras
            extras()  # help
        if buttons[7].checkForInput(mouse):
            # help
            pass
        if buttons[8].checkForInput(mouse):
            from main import main_menu
            main_menu()
        if buttons[9].checkForInput(mouse):
            print('aqui 2')
            pygame.quit()
            sys.exit()
    else:
        if buttons[0].checkForInput(mouse):
            from battle import encounter
            encounter()
        if buttons[1].checkForInput(mouse):
            from main import show_inventory_page_1
            show_inventory_page_1(1)
        if buttons[2].checkForInput(mouse):
            from main import show_consumable_items
            show_consumable_items()
        if buttons[3].checkForInput(mouse):
            from player_status import player_status
            player_status()
        if buttons[4].checkForInput(mouse):
            from extras import extras
            extras()
        if buttons[5].checkForInput(mouse):
            pygame.quit()
            sys.exit()


