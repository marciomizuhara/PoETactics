import pygame, sys, random, math
from settings import *
from assets.fonts.fonts import *
from assets.music.music import *
from button import *
from settings import *
from classes import consumable_item_
from classes import drop
from classes import extras
from classes import inventory
from classes import player_
from classes import save_load
from items.uniques import *
from classes import unique


def draw_souls_icon():
    SCREEN.blit(SOULS_ICON, (1020, 633))


def draw_souls_quantity():
    souls_text = get_regular_font(25).render(f" {player_.player.souls}", True, WHITE)
    souls_rect = souls_text.get_rect(midleft=(1065, 653))
    SCREEN.blit(souls_text, souls_rect)


def gain_souls(number):
    player_.player.souls += number


def souls_menu():
    global counter, LAST_TIME_MS

    SCREEN.blit(BG, (0, 0))
    SCREEN.blit(BATTLE_BOX_LARGE, (60, 40))
    # SCREEN.blit(PLAYER_STATUS_BOX, (80, 60))

    draw_dialogue_box(screen=SCREEN, x=110, y=70, width=700,
                            text='Welcome to the Soul Pantheon. \n \n '
                                 'Here you can exchange your souls points to unlock powerful perks and skills.')

    while True:
        HELP_MOUSE_POSITION = pygame.mouse.get_pos()
        # BUTTONS = main_menu_structure(PLAYER_STATUS_MOUSE_POSITION)

        SOUL_SKILL_1 = SoulBox(image=pygame.image.load("assets/images/SOUL_SKILLS_BOX.png"), pos=(460, 220),
                      skill='Soul Reaper 1', description='+ 100% to soul gain permanently', soul_cost='100',
                               soul_icon=SOUL_REAPER_1,
                               skill_font=get_bold_font(20),
                               description_font=get_regular_font(20), soul_cost_font=get_bold_font(25),
                               base_color='White', hovering_color=BLUE)

        SOUL_SKILL_2 = SoulBox(image=pygame.image.load("assets/images/SOUL_SKILLS_BOX.png"), pos=(460, 280),
                               soul_icon=ONE_WITH_THE_NATURE,
                               skill='One with the Nature', description='+ 10% to total life permanently', soul_cost='250',
                               skill_font=get_bold_font(20),
                               description_font=get_regular_font(20), soul_cost_font=get_bold_font(25),
                               base_color='White', hovering_color=BLUE)

        SOUL_SKILL_3 = SoulBox(image=pygame.image.load("assets/images/SOUL_SKILLS_BOX.png"), pos=(460, 340),
                               soul_icon=ASSASSINATION,
                               skill='Assassination',
                               description='+ 10% to attack permanently', soul_cost='270',
                               skill_font=get_bold_font(20),
                               description_font=get_regular_font(20), soul_cost_font=get_bold_font(25),
                               base_color='White', hovering_color=BLUE)


        BACK = Button(image=pygame.image.load("assets/images/Smallest Rect.png"), pos=(1110, 610),
                      text_input="BACK", font=get_bold_font(30), base_color="White", hovering_color=BLUE)

        # NO_BUTTON = Button(image=pygame.image.load("images/Smallest Rect.png"), pos=(380, 600),
        #                      text_input="NO", font=get_bold_font(30), base_color="White", hovering_color=BLUE)
        # YES_BUTTON = Button(image=pygame.image.load("images/Smallest Rect.png"), pos=(540, 600),
        #                     text_input="YES", font=get_bold_font(30), base_color="White", hovering_color=BLUE)

        diff_time_ms = int(round(time.time() * 4000)) - LAST_TIME_MS

        if diff_time_ms >= 4000:
            counter = counter + 1
            LAST_TIME_MS = int(round(time.time() * 4000))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if BACK.checkForInput(HELP_MOUSE_POSITION):
                    counter = 0
                    extras.extras()


        for button in [BACK, SOUL_SKILL_1, SOUL_SKILL_2, SOUL_SKILL_3]:
            button.changeColor(HELP_MOUSE_POSITION)
            button.update(SCREEN)
        pygame.display.update()


def roulette_outcome(index):
    global counter, LAST_TIME_MS, click_blocking

    reward = ''
    setter = True
    SCREEN.blit(BG, (0, 0))
    SCREEN.blit(BATTLE_BOX_LARGE, (60, 40))
    # SCREEN.blit(pygame.transform.rotate(ROULETTE_WHEEL2, angle), (position))
    print(type(index))
    print(index)
    if index == 19:
        consumable_item_.mirror_of_kalandra.quantity += 1
        reward = 'Mirror of Kalandra'
    if index == 18:
        consumable_item_.exalted_orb.quantity += 1
        reward = 'Exalted Orb'
    if index == 17:
        consumable_item_.elixir.quantity += 1
        reward = 'Elixir'
    if index == 16:
        consumable_item_.divine_orb.quantity += 1
        reward = 'Divine Orb'
    if index == 15:
        consumable_item_.elixir.quantity += 1
        reward = 'Elixir'
    if index == 14:
        consumable_item_.deft_fossil.quantity += 1
        reward = 'Deft Fossil'
    if index == 13:
        consumable_item_.elixir.quantity += 1
        reward = 'Elixir'
    if index == 12:
        consumable_item_.pristine_fossil.quantity += 1
        reward = 'Pristine Fossil'
    if index == 11:
        consumable_item_.elixir.quantity += 1
        reward = 'Elixir'
    if index == 10:
        consumable_item_.chaos_orb.quantity += 1
        reward = 'Chaos Orb'
    if index == 9:
        consumable_item_.elixir.quantity += 1
        reward = 'Elixir'
    if index == 8:
        consumable_item_.serrated_fossil.quantity += 1
        reward = 'Serrated Fossil'
    if index == 7:
        consumable_item_.elixir.quantity += 1
        reward = 'Elixir'
    if index == 6:
        consumable_item_.divine_orb.quantity += 1
        reward = 'Divine Orb'
    if index == 5:
        consumable_item_.elixir.quantity += 1
        reward = 'Elixir'
    if index == 4:
        consumable_item_.dense_fossil.quantity += 1
        reward = 'Dense Fossil'
    if index == 3:
        consumable_item_.elixir.quantity += 1
        reward = 'Elixir'
    if index == 2:
        consumable_item_.chaos_orb.quantity += 1
        reward = 'Chaos Orb'
    if index == 1:
        new_drop = random.choice(uniques)
        inventory_uniques = [value for elem in inventory.inventory for value in elem.__dict__.values()]
        print(new_drop)
        print(inventory_uniques)
        input('aqui')
        if new_drop['name'] in inventory_uniques:
            if new_drop['name'] in unique.uniques_list:
                consumable_item_.elixir.quantity += 1
                reward = 'Elixir'
            else:
                consumable_item_.elixir.quantity += 1
                reward = 'Elixir'
        else:
            unique.uniques_list.append(new_drop['name'])
            reward = new_drop['name']
            new_item = unique.Unique(new_drop['type'],
                              new_drop['name'],
                              new_drop['level'],
                              new_drop['life'],
                              new_drop['attack'],
                              new_drop['defense'],
                              new_drop['crit_chance'],
                              new_drop['crit_damage'],
                              new_drop['magic_find'],
                              new_drop['rarity'],
                              new_drop['image'],
                              )
            inventory.inventory.append(new_item)
            db.execute("INSERT INTO uniques_list (username, name) VALUES (:username, :name)",
                       username=player_.player.name, name=new_drop['name'])
            inventory.inventory_update(player_.player.name, new_item)
            new_drop.temp_unique_new_drop.append(new_item)

    save_load.save_state()

    outcome = get_bold_font(40).render(f"You received 1x {reward}!", True, YELLOW)
    outcome_rect = outcome.get_rect(center=(SCREEN_WIDTH / 2, 260))

    while True:
        ROULETTE_OUTCOME_MOUSE_POSITION = pygame.mouse.get_pos()
        # BUTTONS = main_menu_structure(PLAYER_STATUS_MOUSE_POSITION)

        CONTINUE = Button(image=pygame.image.load("assets/images/Smallest Rect.png"), pos=(SCREEN_WIDTH / 2, 360),
                          text_input="CONTINUE", font=get_bold_font(30), base_color="White", hovering_color=BLUE)

        # NO_BUTTON = Button(image=pygame.image.load("images/Smallest Rect.png"), pos=(380, 600),
        #                      text_input="NO", font=get_bold_font(30), base_color="White", hovering_color=BLUE)
        # YES_BUTTON = Button(image=pygame.image.load("images/Smallest Rect.png"), pos=(540, 600),
        #                     text_input="YES", font=get_bold_font(30), base_color="White", hovering_color=BLUE)

        diff_time_ms = int(round(time.time() * 4000)) - LAST_TIME_MS

        if diff_time_ms >= 4000:
            counter = counter + 1
            LAST_TIME_MS = int(round(time.time() * 4000))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if CONTINUE.checkForInput(ROULETTE_OUTCOME_MOUSE_POSITION):
                    counter = 0
                    click_blocking = True
                    roulette()

        if counter >= 0:
            if setter:
                consumable_drop_sound()
                SCREEN.blit(outcome, outcome_rect)
                setter = False
        if counter >= 2:
            for button in [CONTINUE]:
                button.changeColor(ROULETTE_OUTCOME_MOUSE_POSITION)
                button.update(SCREEN)
        pygame.display.update()


