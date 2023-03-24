import pygame, sys, random
from settings import *
from assets.fonts.fonts import *
from items.consumables import *
from button import *
from classes import inventory
from classes import main_menu
from classes import player_
from classes import save_load


class ConsumableItem:

    def __init__(self, type, name, value, quantity, rarity, code, sound):
        self.type = type
        self.name = name
        self.value = value
        self.quantity = quantity
        self.rarity = rarity
        self.code = code
        self.sound = sound


class Fossil(ConsumableItem):

    def __init__(self, type, name, value, quantity, rarity, code, sound, attribute):
        super().__init__(type, name, value, quantity, rarity, code, sound)
        self.attribute = attribute


# Consumables intances:
potion = ConsumableItem(consumables['potion']['type'], consumables['potion']['name'],
                        consumables['potion']['value'], consumables['potion']['quantity'],
                        consumables['potion']['rarity'], consumables['potion']['code'],
                        consumables['potion']['sound'])
hi_potion = ConsumableItem(consumables['hi-potion']['type'], consumables['hi-potion']['name'],
                           consumables['hi-potion']['value'], consumables['hi-potion']['quantity'],
                           consumables['hi-potion']['rarity'], consumables['hi-potion']['code'],
                           consumables['hi-potion']['sound'])
x_potion = ConsumableItem(consumables['x-potion']['type'], consumables['x-potion']['name'],
                          consumables['x-potion']['value'], consumables['x-potion']['quantity'],
                          consumables['x-potion']['rarity'], consumables['x-potion']['code'],
                          consumables['x-potion']['sound'])
elixir = ConsumableItem(consumables['elixir']['type'], consumables['elixir']['name'],
                        consumables['elixir']['value'], consumables['elixir']['quantity'],
                        consumables['elixir']['rarity'], consumables['elixir']['code'],
                        consumables['elixir']['sound'])
chaos_orb = ConsumableItem(consumables['chaos orb']['type'], consumables['chaos orb']['name'],
                           consumables['chaos orb']['value'], consumables['chaos orb']['quantity'],
                           consumables['chaos orb']['rarity'], consumables['chaos orb']['code'],
                           consumables['chaos orb']['sound'])
divine_orb = ConsumableItem(consumables['divine orb']['type'], consumables['divine orb']['name'],
                            consumables['divine orb']['value'], consumables['divine orb']['quantity'],
                            consumables['divine orb']['rarity'], consumables['divine orb']['code'],
                            consumables['divine orb']['sound'])
exalted_orb = ConsumableItem(consumables['exalted orb']['type'], consumables['exalted orb']['name'],
                             consumables['exalted orb']['value'], consumables['exalted orb']['quantity'],
                             consumables['exalted orb']['rarity'], consumables['exalted orb']['code'],
                             consumables['exalted orb']['sound'])
mirror_of_kalandra = ConsumableItem(consumables['mirror of kalandra']['type'],
                                    consumables['mirror of kalandra']['name'],
                                    consumables['mirror of kalandra']['value'],
                                    consumables['mirror of kalandra']['quantity'],
                                    consumables['mirror of kalandra']['rarity'],
                                    consumables['mirror of kalandra']['code'],
                                    consumables['mirror of kalandra']['sound'])
roulette_wheel_ticket = ConsumableItem(consumables['roulette_wheel_ticket']['type'],
                                       consumables['roulette_wheel_ticket']['name'],
                                       consumables['roulette_wheel_ticket']['value'],
                                       consumables['roulette_wheel_ticket']['quantity'],
                                       consumables['roulette_wheel_ticket']['rarity'],
                                       consumables['roulette_wheel_ticket']['code'],
                                       consumables['roulette_wheel_ticket']['sound'])

# Fossiles
dense_fossil = Fossil(consumables['dense fossil']['type'],
                      consumables['dense fossil']['name'],
                      consumables['dense fossil']['value'],
                      consumables['dense fossil']['quantity'],
                      consumables['dense fossil']['rarity'],
                      consumables['dense fossil']['code'],
                      consumables['dense fossil']['sound'],
                      consumables['dense fossil']['attribute'])
serrated_fossil = Fossil(consumables['serrated fossil']['type'],
                         consumables['serrated fossil']['name'],
                         consumables['serrated fossil']['value'],
                         consumables['serrated fossil']['quantity'],
                         consumables['serrated fossil']['rarity'],
                         consumables['serrated fossil']['code'],
                         consumables['serrated fossil']['sound'],
                         consumables['serrated fossil']['attribute'])
pristine_fossil = Fossil(consumables['pristine fossil']['type'],
                         consumables['pristine fossil']['name'],
                         consumables['pristine fossil']['value'],
                         consumables['pristine fossil']['quantity'],
                         consumables['pristine fossil']['rarity'],
                         consumables['pristine fossil']['code'],
                         consumables['pristine fossil']['sound'],
                         consumables['pristine fossil']['attribute'])
deft_fossil = Fossil(consumables['deft fossil']['type'],
                     consumables['deft fossil']['name'],
                     consumables['deft fossil']['value'],
                     consumables['deft fossil']['quantity'],
                     consumables['deft fossil']['rarity'],
                     consumables['deft fossil']['code'],
                     consumables['deft fossil']['sound'],
                     consumables['deft fossil']['attribute'])
fractured_fossil = Fossil(consumables['fractured fossil']['type'],
                          consumables['fractured fossil']['name'],
                          consumables['fractured fossil']['value'],
                          consumables['fractured fossil']['quantity'],
                          consumables['fractured fossil']['rarity'],
                          consumables['fractured fossil']['code'],
                          consumables['fractured fossil']['sound'],
                          consumables['fractured fossil']['attribute'])


def confirm_use_consumable_item(item):
    global counter
    SCREEN.blit(BG, (0, 0))
    SCREEN.blit(BATTLE_BOX, (60, 40))
    SCREEN.blit(player_.player.image, (130, 300))
    confirm_text = get_bold_font(40).render(f'Confirm you want to use {item.name}?', True, WHITE)
    confirm_text_rect = confirm_text.get_rect(center=(SCREEN_WIDTH / 2 - 180, 270))
    SCREEN.blit(confirm_text, confirm_text_rect)

    while True:
        CONFIRM_USE_CONSUMABLE_ITEM_MOUSE_POSITION = pygame.mouse.get_pos()
        BUTTONS = main_menu.main_menu_structure(CONFIRM_USE_CONSUMABLE_ITEM_MOUSE_POSITION)
        YES_BUTTON = Button(image=pygame.image.load("assets/images/Smallest Rect.png"), pos=(540, 400),
                            text_input="YES", font=get_bold_font(30), base_color="White", hovering_color=BLUE)
        NO_BUTTON = Button(image=pygame.image.load("assets/images/Smallest Rect.png"), pos=(380, 400),
                           text_input="NO", font=get_bold_font(30), base_color="White", hovering_color=BLUE)
        BUTTONS.extend([YES_BUTTON, NO_BUTTON])

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                main_menu.main_menu_structure_events(CONFIRM_USE_CONSUMABLE_ITEM_MOUSE_POSITION, BUTTONS)
                if YES_BUTTON.checkForInput(CONFIRM_USE_CONSUMABLE_ITEM_MOUSE_POSITION):
                    counter = 0
                    use_consumable_item(item)
                if NO_BUTTON.checkForInput(CONFIRM_USE_CONSUMABLE_ITEM_MOUSE_POSITION):
                    show_consumable_items()
            for button in BUTTONS:
                button.changeColor(CONFIRM_USE_CONSUMABLE_ITEM_MOUSE_POSITION)
                button.update(SCREEN)
        pygame.display.update()


def use_consumable_item(item):
    global counter, LAST_TIME_MS
    SCREEN.blit(BG, (0, 0))
    SCREEN.blit(BATTLE_BOX, (60, 40))
    SCREEN.blit(player_.player.image, (130, 300))
    potion_setter = False
    hi_potion_setter = False
    x_potion_setter = False
    elixir_setter = False
    chaos_orb_setter = False
    divine_orb_setter = False
    exalted_orb_setter = False
    mirror_of_kalandra_setter = False

    if item.name == 'Potion' and item.quantity > 0:
        player_.player.life = player_.player.life + potion.value
        potion.quantity = potion.quantity - 1
        if player_.player.life > player_.player.total_life:
            player_.player.life = player_.player.total_life
    if item.name == 'Hi-Potion' and item.quantity > 0:
        player_.player.life = player_.player.life + hi_potion.value
        hi_potion.quantity = hi_potion.quantity - 1
        if player_.player.life > player_.player.total_life:
            player_.player.life = player_.player.total_life
    if item.name == 'X-Potion' and item.quantity > 0:
        player_.player.life = player_.player.life + x_potion.value
        x_potion.quantity = x_potion.quantity - 1
        if player_.player.life > player_.player.total_life:
            player_.player.life = player_.player.total_life
    if item.name == 'Elixir' and item.quantity > 0:
        player_.player.life = player_.player.total_life
        elixir.quantity = elixir.quantity - 1
    if item.name == 'Chaos Orb' and item.quantity > 0:
        player_.player.attack = player_.player.attack + chaos_orb.value
        chaos_orb.quantity = chaos_orb.quantity - 1
    if item.name == 'Divine Orb' and item.quantity > 0:
        player_.player.defense = player_.player.defense + divine_orb.value
        divine_orb.quantity = divine_orb.quantity - 1
    if item.name == 'Exalted Orb' and item.quantity > 0:
        player_.player.total_life = player_.player.total_life + exalted_orb.value
        exalted_orb.quantity = exalted_orb.quantity - 1
    if item.name == 'Mirror of Kalandra' and item.quantity > 0:
        player_.player.total_life = player_.player.total_life + int(mirror_of_kalandra.value.split(', ')[0])
        player_.player.attack = player_.player.attack + int(mirror_of_kalandra.value.split(', ')[1])
        player_.player.defense = player_.player.defense + int(mirror_of_kalandra.value.split(', ')[2])
        mirror_of_kalandra.quantity = mirror_of_kalandra.quantity - 1
    if item.name == 'Dense Fossil' and item.quantity > 0:
        pass
    if item.name == 'Serrated Fossil' and item.quantity > 0:
        pass
    if item.name == 'Pristine Fossil' and item.quantity > 0:
        pass
    if item.name == 'Deft Fossil' and item.quantity > 0:
        pass
    if item.name == 'Fractured Fossil' and item.quantity > 0:
        pass

    save_load.save_state()
    counter = 0
    while True:
        USE_CONSUMABLE_ITEM_CONFIRMATION_MOUSE_POSITION = pygame.mouse.get_pos()

        potion_text = get_bold_font(40).render(f'You restored {potion.value} life points!', True, YELLOW)
        potion_text_rect = potion_text.get_rect(center=(SCREEN_WIDTH / 2 - 180, 260))
        hi_potion_text = get_bold_font(40).render(f'You restored {hi_potion.value} life points!', True, YELLOW)
        hi_potion_text_rect = hi_potion_text.get_rect(center=(SCREEN_WIDTH / 2 - 180, 260))
        x_potion_text = get_bold_font(40).render(f'You restored {x_potion.value} life points!', True, YELLOW)
        x_potion_text_rect = x_potion_text.get_rect(center=(SCREEN_WIDTH / 2 - 180, 260))
        elixir_text = get_bold_font(40).render(f'You restored all your life points!', True, YELLOW)
        elixir_text_rect = elixir_text.get_rect(center=(SCREEN_WIDTH / 2 - 180, 260))
        chaos_orb_text = get_bold_font(40).render(f'Your permanently added +{chaos_orb.value} to your attack!', True,
                                                  YELLOW)
        chaos_orb_text_rect = chaos_orb_text.get_rect(center=(SCREEN_WIDTH / 2 - 180, 260))
        divine_orb_text = get_bold_font(40).render(f'Your permanently added +{divine_orb.value} to your defense!', True,
                                                   YELLOW)
        divine_orb_text_rect = divine_orb_text.get_rect(center=(SCREEN_WIDTH / 2 - 180, 260))
        exalted_orb_text = get_bold_font(40).render(f'Your permanently added +{exalted_orb.value} to your life points!',
                                                    True, YELLOW)
        exalted_orb_text_rect = exalted_orb_text.get_rect(center=(SCREEN_WIDTH / 2 - 180, 260))
        mirror_text1 = get_bold_font(40).render(f"Your permanently added +{(mirror_of_kalandra.value.split(', ')[0])} "
                                                f"to your life points,", True, YELLOW)
        mirror_text1_rect = mirror_text1.get_rect(center=(SCREEN_WIDTH / 2 - 180, 220))
        mirror_text2 = get_bold_font(40).render(f"+{(mirror_of_kalandra.value.split(', ')[1])} to your attack and "
                                                f"+{(mirror_of_kalandra.value.split(', ')[2])} to your defense!", True,
                                                YELLOW)
        mirror_text2_rect = mirror_text2.get_rect(center=(SCREEN_WIDTH / 2 - 180, 275))

        BUTTONS = main_menu.main_menu_structure(USE_CONSUMABLE_ITEM_CONFIRMATION_MOUSE_POSITION)
        CONTINUE = Button(image=pygame.image.load("assets/images/Smallest Rect.png"), pos=(SCREEN_WIDTH / 2 - 180, 400),
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
                main_menu.main_menu_structure_events(USE_CONSUMABLE_ITEM_CONFIRMATION_MOUSE_POSITION, BUTTONS)
                if CONTINUE.checkForInput(USE_CONSUMABLE_ITEM_CONFIRMATION_MOUSE_POSITION):
                    counter = 0
                    show_consumable_items()

        if counter >= 0 and item.name == 'Potion':
            if not potion_setter:
                SCREEN.blit(potion_text, potion_text_rect)
                potion_setter = True
        if counter >= 0 and item.name == 'Hi-Potion':
            if not hi_potion_setter:
                SCREEN.blit(hi_potion_text, hi_potion_text_rect)
                hi_potion_setter = True
        if counter >= 0 and item.name == 'X-Potion':
            if not x_potion_setter:
                SCREEN.blit(x_potion_text, x_potion_text_rect)
                x_potion_setter = True
        if counter >= 0 and item.name == 'Elixir':
            if not elixir_setter:
                SCREEN.blit(elixir_text, elixir_text_rect)
                elixir_setter = True
        if counter >= 0 and item.name == 'Chaos Orb':
            if not chaos_orb_setter:
                SCREEN.blit(chaos_orb_text, chaos_orb_text_rect)
                chaos_orb_setter = True
        if counter >= 0 and item.name == 'Divine Orb':
            if not divine_orb_setter:
                SCREEN.blit(divine_orb_text, divine_orb_text_rect)
                divine_orb_setter = True
        if counter >= 0 and item.name == 'Exalted Orb':
            if not exalted_orb_setter:
                SCREEN.blit(exalted_orb_text, exalted_orb_text_rect)
                exalted_orb_setter = True
        if counter >= 0 and item.name == 'Mirror of Kalandra':
            if not mirror_of_kalandra_setter:
                SCREEN.blit(mirror_text1, mirror_text1_rect)
                SCREEN.blit(mirror_text2, mirror_text2_rect)
                mirror_of_kalandra_setter = True

        if counter >= 1:
            for button in BUTTONS:
                button.changeColor(USE_CONSUMABLE_ITEM_CONFIRMATION_MOUSE_POSITION)
                button.update(SCREEN)

        pygame.display.update()


def show_consumable_items():
    global INPUT_TEXT
    SCREEN.blit(BG, (0, 0))
    SCREEN.blit(CONSUMABLES_GRID, (60, 40))
    SCREEN.blit(player_.player.image, (130, 300))
    player_.display_level_xp()
    # Items images
    if potion.quantity != 0:
        SCREEN.blit(POTION, (310, 120))
    else:
        SCREEN.blit(G_POTION, (310, 120))
    potion_quantity_text = get_bold_font(20).render(f'{potion.quantity}', True, WHITE)
    potion_quantity_text_rect = potion_quantity_text.get_rect(midleft=(290, 115))
    SCREEN.blit(potion_quantity_text, potion_quantity_text_rect)

    if hi_potion.quantity != 0:
        SCREEN.blit(HI_POTION, (420, 120))
    else:
        SCREEN.blit(G_HI_POTION, (420, 120))
    hi_potion_quantity_text = get_bold_font(20).render(f'{hi_potion.quantity}', True, WHITE)
    hi_potion_quantity_text_rect = hi_potion_quantity_text.get_rect(midleft=(400, 115))
    SCREEN.blit(hi_potion_quantity_text, hi_potion_quantity_text_rect)

    if x_potion.quantity != 0:
        SCREEN.blit(X_POTION, (525, 120))
    else:
        SCREEN.blit(G_X_POTION, (525, 120))
    x_potion_quantity_text = get_bold_font(20).render(f'{x_potion.quantity}', True, WHITE)
    x_potion_quantity_text_rect = x_potion_quantity_text.get_rect(midleft=(505, 115))
    SCREEN.blit(x_potion_quantity_text, x_potion_quantity_text_rect)

    if elixir.quantity != 0:
        SCREEN.blit(ELIXIR, (635, 120))
    else:
        SCREEN.blit(G_ELIXIR, (635, 120))
    elixir_quantity_text = get_bold_font(20).render(f'{elixir.quantity}', True, WHITE)
    elixir_quantity_text_rect = elixir_quantity_text.get_rect(midleft=(615, 115))
    SCREEN.blit(elixir_quantity_text, elixir_quantity_text_rect)

    if chaos_orb.quantity != 0:
        SCREEN.blit(CHAOS_ORB, (745, 120))
    else:
        SCREEN.blit(G_CHAOS_ORB, (745, 120))
    chaos_orb_quantity_text = get_bold_font(20).render(f'{chaos_orb.quantity}', True, WHITE)
    chaos_orb_quantity_text_rect = chaos_orb_quantity_text.get_rect(midleft=(725, 115))
    SCREEN.blit(chaos_orb_quantity_text, chaos_orb_quantity_text_rect)

    if divine_orb.quantity != 0:
        SCREEN.blit(DIVINE_ORB, (305, 225))
    else:
        SCREEN.blit(G_DIVINE_ORB, (305, 225))
    divine_orb_quantity_text = get_bold_font(20).render(f'{divine_orb.quantity}', True, WHITE)
    divine_orb_quantity_text_rect = divine_orb_quantity_text.get_rect(midleft=(290, 220))
    SCREEN.blit(divine_orb_quantity_text, divine_orb_quantity_text_rect)

    if exalted_orb.quantity != 0:
        SCREEN.blit(EXALTED_ORB, (410, 225))
    else:
        SCREEN.blit(G_EXALTED_ORB, (410, 225))
    exalted_orb_quantity_text = get_bold_font(20).render(f'{exalted_orb.quantity}', True, WHITE)
    exalted_orb_quantity_text_rect = exalted_orb_quantity_text.get_rect(midleft=(400, 220))
    SCREEN.blit(exalted_orb_quantity_text, exalted_orb_quantity_text_rect)

    if mirror_of_kalandra.quantity != 0:
        SCREEN.blit(MIRROR_OF_KALANDRA, (520, 220))
    else:
        SCREEN.blit(G_MIRROR_OF_KALANDRA, (520, 220))
    mirror_of_kalandra_quantity_text = get_bold_font(20).render(f'{mirror_of_kalandra.quantity}', True, WHITE)
    mirror_of_kalandra_quantity_text_rect = mirror_of_kalandra_quantity_text.get_rect(midleft=(505, 220))
    SCREEN.blit(mirror_of_kalandra_quantity_text, mirror_of_kalandra_quantity_text_rect)

    if roulette_wheel_ticket.quantity != 0:
        SCREEN.blit(ROULETTE_WHEEL2_TICKET, (630, 320))
    else:
        SCREEN.blit(G_ROULETTE_WHEEL2_TICKET, (630, 320))
    roulette_wheel_ticket_text = get_bold_font(20).render(f'{roulette_wheel_ticket.quantity}', True, WHITE)
    roulette_wheel_ticket_text_rect = roulette_wheel_ticket_text.get_rect(midleft=(615, 325))
    SCREEN.blit(roulette_wheel_ticket_text, roulette_wheel_ticket_text_rect)

    if dense_fossil.quantity != 0:
        SCREEN.blit(DENSE_FOSSIL, (630, 220))
    else:
        SCREEN.blit(G_DENSE_FOSSIL, (630, 220))
    dense_fossil_quantity_text = get_bold_font(20).render(f'{dense_fossil.quantity}', True, WHITE)
    dense_fossil_quantity_text_rect = dense_fossil_quantity_text.get_rect(midleft=(615, 220))
    SCREEN.blit(dense_fossil_quantity_text, dense_fossil_quantity_text_rect)

    if serrated_fossil.quantity != 0:
        SCREEN.blit(SERRATED_FOSSIL, (740, 220))
    else:
        SCREEN.blit(G_SERRATED_FOSSIL, (740, 220))
    serrated_fossil_quantity_text = get_bold_font(20).render(f'{serrated_fossil.quantity}', True, WHITE)
    serrated_fossil_quantity_text_rect = serrated_fossil_quantity_text.get_rect(midleft=(725, 220))
    SCREEN.blit(serrated_fossil_quantity_text, serrated_fossil_quantity_text_rect)

    if pristine_fossil.quantity != 0:
        SCREEN.blit(PRISTINE_FOSSIL, (295, 320))
    else:
        SCREEN.blit(G_PRISTINE_FOSSIL, (295, 320))
    pristine_fossil_quantity_text = get_bold_font(20).render(f'{pristine_fossil.quantity}', True, WHITE)
    pristine_fossil_quantity_text_rect = pristine_fossil_quantity_text.get_rect(midleft=(290, 325))
    SCREEN.blit(pristine_fossil_quantity_text, pristine_fossil_quantity_text_rect)

    if deft_fossil.quantity != 0:
        SCREEN.blit(DEFT_FOSSIL, (405, 320))
    else:
        SCREEN.blit(G_DEFT_FOSSIL, (405, 320))
    deft_fossil_quantity_text = get_bold_font(20).render(f'{deft_fossil.quantity}', True, WHITE)
    deft_fossil_quantity_text_rect = deft_fossil_quantity_text.get_rect(midleft=(400, 325))
    SCREEN.blit(deft_fossil_quantity_text, deft_fossil_quantity_text_rect)

    if fractured_fossil.quantity != 0:
        SCREEN.blit(FRACTURED_FOSSIL, (515, 320))
    else:
        SCREEN.blit(G_FRACTURED_FOSSIL, (515, 320))
    fractured_fossil_quantity_text = get_bold_font(20).render(f'{fractured_fossil.quantity}', True, WHITE)
    fractured_fossil_quantity_text_rect = fractured_fossil_quantity_text.get_rect(midleft=(505, 325))
    SCREEN.blit(fractured_fossil_quantity_text, fractured_fossil_quantity_text_rect)

    potion_rect = POTION.get_rect(center=(330, 150))
    hi_potion_rect = HI_POTION.get_rect(center=(440, 150))
    x_potion_rect = X_POTION.get_rect(center=(545, 150))
    elixir_rect = ELIXIR.get_rect(center=(670, 150))
    chaos_orb_rect = CHAOS_ORB.get_rect(center=(780, 150))
    divine_orb_rect = DIVINE_ORB.get_rect(center=(330, 260))
    exalted_orb_rect = EXALTED_ORB.get_rect(center=(440, 260))
    mirror_of_kalandra_rect = MIRROR_OF_KALANDRA.get_rect(center=(540, 260))
    roulette_wheel_ticket_rect = ROULETTE_WHEEL2_TICKET.get_rect(center=(650, 350))
    dense_fossil_rect = DENSE_FOSSIL.get_rect(center=(650, 260))
    serrated_fossil_rect = SERRATED_FOSSIL.get_rect(center=(765, 260))
    pristine_fossil_rect = PRISTINE_FOSSIL.get_rect(center=(320, 350))
    deft_fossil_rect = DEFT_FOSSIL.get_rect(center=(420, 350))
    fractured_fossil_rect = FRACTURED_FOSSIL.get_rect(center=(520, 350))

    INPUT_TEXT = ''

    while True:

        SHOW_CONSUMABLES_MOUSE_POSITION = pygame.mouse.get_pos()
        BUTTONS = main_menu.main_menu_structure(SHOW_CONSUMABLES_MOUSE_POSITION)

        BOX = Box(image=pygame.image.load("assets/images/CONSUMABLE_ONE_LINE_BOX.png"), pos=(550, 600),
                  text_input=INPUT_TEXT, font=get_bold_font(20), base_color="White", hovering_color=BLUE)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                main_menu.main_menu_structure_events(SHOW_CONSUMABLES_MOUSE_POSITION, BUTTONS)
                if potion_rect.collidepoint(SHOW_CONSUMABLES_MOUSE_POSITION):
                    if potion.quantity > 0:
                        confirm_use_consumable_item(potion)
                if hi_potion_rect.collidepoint(SHOW_CONSUMABLES_MOUSE_POSITION):
                    if hi_potion.quantity > 0:
                        confirm_use_consumable_item(hi_potion)
                if x_potion_rect.collidepoint(SHOW_CONSUMABLES_MOUSE_POSITION):
                    if x_potion.quantity > 0:
                        confirm_use_consumable_item(x_potion)
                if elixir_rect.collidepoint(SHOW_CONSUMABLES_MOUSE_POSITION):
                    if elixir.quantity > 0:
                        confirm_use_consumable_item(elixir)
                if chaos_orb_rect.collidepoint(SHOW_CONSUMABLES_MOUSE_POSITION):
                    if chaos_orb.quantity > 0:
                        confirm_use_consumable_item(chaos_orb)
                if divine_orb_rect.collidepoint(SHOW_CONSUMABLES_MOUSE_POSITION):
                    if divine_orb.quantity > 0:
                        confirm_use_consumable_item(divine_orb)
                if exalted_orb_rect.collidepoint(SHOW_CONSUMABLES_MOUSE_POSITION):
                    if exalted_orb.quantity > 0:
                        confirm_use_consumable_item(exalted_orb)
                if mirror_of_kalandra_rect.collidepoint(SHOW_CONSUMABLES_MOUSE_POSITION):
                    if mirror_of_kalandra.quantity > 0:
                        confirm_use_consumable_item(mirror_of_kalandra)
                if roulette_wheel_ticket_rect.collidepoint(SHOW_CONSUMABLES_MOUSE_POSITION):
                    if roulette_wheel_ticket.quantity > 0:
                        roulette()
                if dense_fossil_rect.collidepoint(SHOW_CONSUMABLES_MOUSE_POSITION):
                    if dense_fossil.quantity > 0:
                        inventory.show_inventory_page_1(dense_fossil)
                if serrated_fossil_rect.collidepoint(SHOW_CONSUMABLES_MOUSE_POSITION):
                    if serrated_fossil.quantity > 0:
                        inventory.show_inventory_page_1(serrated_fossil)
                if pristine_fossil_rect.collidepoint(SHOW_CONSUMABLES_MOUSE_POSITION):
                    if pristine_fossil.quantity > 0:
                        inventory.show_inventory_page_1(pristine_fossil)
                if deft_fossil_rect.collidepoint(SHOW_CONSUMABLES_MOUSE_POSITION):
                    if deft_fossil.quantity > 0:
                        inventory.show_inventory_page_1(deft_fossil)
                if fractured_fossil_rect.collidepoint(SHOW_CONSUMABLES_MOUSE_POSITION):
                    if fractured_fossil.quantity > 0:
                        inventory.show_inventory_page_1(fractured_fossil)
            if potion_rect.collidepoint(SHOW_CONSUMABLES_MOUSE_POSITION):
                BOX.update(screen=SCREEN)
                INPUT_TEXT = f"{potion.name}: Restores {potion.value} life points"

            if hi_potion_rect.collidepoint(SHOW_CONSUMABLES_MOUSE_POSITION):
                BOX.update(screen=SCREEN)
                INPUT_TEXT = f"{hi_potion.name}: Restores {hi_potion.value} life points"

            if x_potion_rect.collidepoint(SHOW_CONSUMABLES_MOUSE_POSITION):
                BOX.update(screen=SCREEN)
                INPUT_TEXT = f"{x_potion.name}: Restores {x_potion.value} life points"

            if elixir_rect.collidepoint(SHOW_CONSUMABLES_MOUSE_POSITION):
                BOX.update(screen=SCREEN)
                INPUT_TEXT = f"{elixir.name}: Restores full life points"

            if chaos_orb_rect.collidepoint(SHOW_CONSUMABLES_MOUSE_POSITION):
                BOX.update(screen=SCREEN)
                INPUT_TEXT = f"{chaos_orb.name}: Permanently adds +{chaos_orb.value} to player's attack"

            if divine_orb_rect.collidepoint(SHOW_CONSUMABLES_MOUSE_POSITION):
                BOX.update(screen=SCREEN)
                INPUT_TEXT = f"{divine_orb.name}: Permanently adds +{divine_orb.value} to player's defense"

            if exalted_orb_rect.collidepoint(SHOW_CONSUMABLES_MOUSE_POSITION):
                BOX.update(screen=SCREEN)
                INPUT_TEXT = f"{exalted_orb.name}: Permanently adds +{exalted_orb.value} to player's total life"

            if mirror_of_kalandra_rect.collidepoint(SHOW_CONSUMABLES_MOUSE_POSITION):
                BOX.update(screen=SCREEN)
                INPUT_TEXT = f"{mirror_of_kalandra.name}: +{mirror_of_kalandra.value.split()[0]} to total life, " \
                             f"+{mirror_of_kalandra.value.split()[1]} to attack, +{mirror_of_kalandra.value.split()[2]} to defense"
            if roulette_wheel_ticket_rect.collidepoint(SHOW_CONSUMABLES_MOUSE_POSITION):
                BOX.update(screen=SCREEN)
                INPUT_TEXT = f"{roulette_wheel_ticket.name}: You can try your luck at the Roulette Wheel"
            if dense_fossil_rect.collidepoint(SHOW_CONSUMABLES_MOUSE_POSITION):
                BOX.update(screen=SCREEN)
                INPUT_TEXT = f"{dense_fossil.name}: Unpredicably reforges the defense value of an item"

            if serrated_fossil_rect.collidepoint(SHOW_CONSUMABLES_MOUSE_POSITION):
                BOX.update(screen=SCREEN)
                INPUT_TEXT = f"{serrated_fossil.name}: Unpredicably reforges the attack value of an item"

            if pristine_fossil_rect.collidepoint(SHOW_CONSUMABLES_MOUSE_POSITION):
                BOX.update(screen=SCREEN)
                INPUT_TEXT = f"{pristine_fossil.name}: Unpredicably reforges the life value of an item"

            if deft_fossil_rect.collidepoint(SHOW_CONSUMABLES_MOUSE_POSITION):
                BOX.update(screen=SCREEN)
                INPUT_TEXT = f"{deft_fossil.name}: Unpredicably reforges the critical damage value of an item"

            if fractured_fossil_rect.collidepoint(SHOW_CONSUMABLES_MOUSE_POSITION):
                BOX.update(screen=SCREEN)
                INPUT_TEXT = f"{fractured_fossil.name}: Unpredicably reforges all values of an item"

            if not potion_rect.collidepoint(SHOW_CONSUMABLES_MOUSE_POSITION) and not hi_potion_rect.collidepoint(
                    SHOW_CONSUMABLES_MOUSE_POSITION) and not x_potion_rect.collidepoint(
                SHOW_CONSUMABLES_MOUSE_POSITION) and not elixir_rect.collidepoint(
                SHOW_CONSUMABLES_MOUSE_POSITION) and not chaos_orb_rect.collidepoint(
                SHOW_CONSUMABLES_MOUSE_POSITION) and not divine_orb_rect.collidepoint(
                SHOW_CONSUMABLES_MOUSE_POSITION) and not exalted_orb_rect.collidepoint(
                SHOW_CONSUMABLES_MOUSE_POSITION) and not mirror_of_kalandra_rect.collidepoint(
                SHOW_CONSUMABLES_MOUSE_POSITION) and not pristine_fossil_rect.collidepoint(
                SHOW_CONSUMABLES_MOUSE_POSITION) and not dense_fossil_rect.collidepoint(
                SHOW_CONSUMABLES_MOUSE_POSITION) and not serrated_fossil_rect.collidepoint(
                SHOW_CONSUMABLES_MOUSE_POSITION) and not pristine_fossil_rect.collidepoint(
                SHOW_CONSUMABLES_MOUSE_POSITION) and not deft_fossil_rect.collidepoint(
                SHOW_CONSUMABLES_MOUSE_POSITION) and not fractured_fossil_rect.collidepoint(
                SHOW_CONSUMABLES_MOUSE_POSITION) and not roulette_wheel_ticket_rect.collidepoint(
                SHOW_CONSUMABLES_MOUSE_POSITION):
                BOX.update(screen=SCREEN)
                INPUT_TEXT = f""

            for button in BUTTONS:
                button.changeColor(SHOW_CONSUMABLES_MOUSE_POSITION)
                button.update(SCREEN)
        pygame.display.update()


def use_fossil(fossil, item_index, item):
    # item_index = 1
    SCREEN.blit(BG, (0, 0))
    SCREEN.blit(BATTLE_BOX, (60, 40))
    player_.display_level_xp()
    confirm_text1 = get_bold_font(35).render(f'Confirm you want to reforge it with {fossil.name}?', True, WHITE)
    confirm_text1_rect = confirm_text1.get_rect(center=(SCREEN_WIDTH / 2 - 180, 480))
    text2 = get_bold_font(25).render(f'(1% chance for the item to get destroyed)', True, WHITE)
    text2_rect = text2.get_rect(center=(SCREEN_WIDTH / 2 - 180, 520))

    text1 = get_bold_font(40).render(f"{item.name}", True, WHITE)
    level_text = get_regular_font(30).render(f"Level {item.level}", True, WHITE)
    type_text = get_bold_font(30).render(f"Type: {item.type}", True, WHITE)
    life_text = get_bold_font(30).render(f"Life: {item.life}", True, WHITE)
    attack_text = get_bold_font(30).render(f"Attack: {item.attack}", True, WHITE)
    defense_text = get_bold_font(30).render(f"Defense: {item.defense}", True, WHITE)
    crit_chance_text = get_bold_font(30).render(f"Critical Chance: {item.crit_chance} %", True, WHITE)
    crit_damage_text = get_bold_font(30).render(f"Critical Damage: {item.crit_damage} %", True, WHITE)
    magic_find_text = get_bold_font(30).render(f"Magic Find: {round(item.magic_find * 100, 2)} %", True, WHITE)
    WIDTH = 806 / 2
    text1_rect = text1.get_rect(center=(WIDTH, 90))
    level_text_rect = level_text.get_rect(center=(WIDTH, 130))
    type_text_rect = type_text.get_rect(midleft=(100, 160))
    life_text_rect = life_text.get_rect(midleft=(100, 200))
    attack_text_rect = attack_text.get_rect(midleft=(100, 240))
    defense_text_rect = defense_text.get_rect(midleft=(100, 280))
    crit_chance_text_rect = crit_chance_text.get_rect(midleft=(100, 320))
    crit_damage_text_rect = crit_damage_text.get_rect(midleft=(100, 360))
    magic_find_text_rect = magic_find_text.get_rect(midleft=(100, 400))
    SCREEN.blit(text1, text1_rect)
    SCREEN.blit(type_text, type_text_rect)
    SCREEN.blit(level_text, level_text_rect)
    SCREEN.blit(life_text, life_text_rect)
    SCREEN.blit(attack_text, attack_text_rect)
    SCREEN.blit(defense_text, defense_text_rect)
    SCREEN.blit(crit_chance_text, crit_chance_text_rect)
    SCREEN.blit(crit_damage_text, crit_damage_text_rect)
    SCREEN.blit(magic_find_text, magic_find_text_rect)

    SCREEN.blit(confirm_text1, confirm_text1_rect)
    SCREEN.blit(text2, text2_rect)

    while True:
        USE_FOSSIL_MOUSE_POSITION = pygame.mouse.get_pos()
        BUTTONS = main_menu.main_menu_structure(USE_FOSSIL_MOUSE_POSITION)
        NO_BUTTON = Button(image=pygame.image.load("assets/images/Smallest Rect.png"), pos=(380, 600),
                           text_input="NO", font=get_bold_font(30), base_color="White", hovering_color=BLUE)
        YES_BUTTON = Button(image=pygame.image.load("assets/images/Smallest Rect.png"), pos=(540, 600),
                            text_input="YES", font=get_bold_font(30), base_color="White", hovering_color=BLUE)
        BUTTONS.extend([NO_BUTTON, YES_BUTTON])

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                main_menu.main_menu_structure_events(USE_FOSSIL_MOUSE_POSITION, BUTTONS)
                if YES_BUTTON.checkForInput(USE_FOSSIL_MOUSE_POSITION):
                    fossil_reforge(fossil, item_index, item)
                if NO_BUTTON.checkForInput(USE_FOSSIL_MOUSE_POSITION):
                    show_consumable_items()

        for button in BUTTONS:
            button.changeColor(USE_FOSSIL_MOUSE_POSITION)
            button.update(SCREEN)
        pygame.display.update()


def fossil_reforge(fossil, item_index, item_to_reforge):
    choice = random.randint(0, 100)
    fossil.quantity = fossil.quantity - 1
    old_item_name = item_to_reforge.__dict__['name']
    old_item_level = item_to_reforge.__dict__['level']
    print(choice)
    if choice <= 99:
        if fossil.name == 'Dense Fossil':
            number = random.randint(dense_fossil.value // 2, dense_fossil.value)
            item_to_reforge.__dict__['defense'] = item_to_reforge.__dict__['defense'] + number
            item_to_reforge.__dict__['level'] = item_to_reforge.__dict__['level'] + 1
            item_to_reforge.__dict__['crafted'] = 1
            # if item_to_reforge.__dict__['name']:
            #     pass
            # else:
            #     item_to_reforge.__dict__['name'] = '*' + item_to_reforge.__dict__['name']
            fossil_reforge_success(fossil, item_index, old_item_name, old_item_level, item_to_reforge)
        elif fossil.name == 'Serrated Fossil':
            number = random.randint(serrated_fossil.value // 2, serrated_fossil.value)
            item_to_reforge.__dict__['attack'] = item_to_reforge.__dict__['attack'] + number
            item_to_reforge.__dict__['level'] = item_to_reforge.__dict__['level'] + 1
            item_to_reforge.__dict__['crafted'] = 1
            # if '*' in item_to_reforge.__dict__['name']:
            #     pass
            # else:
            #     item_to_reforge.__dict__['name'] = '*' + item_to_reforge.__dict__['name']
            fossil_reforge_success(fossil, item_index, old_item_name, old_item_level, item_to_reforge)
        elif fossil.name == 'Pristine Fossil':
            number = random.randint(pristine_fossil.value // 2, pristine_fossil.value)
            item_to_reforge.__dict__['life'] = item_to_reforge.__dict__['life'] + number
            item_to_reforge.__dict__['level'] = item_to_reforge.__dict__['level'] + 1
            item_to_reforge.__dict__['crafted'] = 1
            # if '*' in item_to_reforge.__dict__['name']:
            #     pass
            # else:
            #     item_to_reforge.__dict__['name'] = '*' + item_to_reforge.__dict__['name']
            # fossil_reforge_success(fossil, item_index, old_item_name, old_item_level, item_to_reforge)
        elif fossil.name == 'Deft Fossil':
            number = random.randint(deft_fossil.value // 2, deft_fossil.value)
            item_to_reforge.__dict__['crit_damage'] = item_to_reforge.__dict__['crit_damage'] + number
            item_to_reforge.__dict__['level'] = item_to_reforge.__dict__['level'] + 1
            item_to_reforge.__dict__['crafted'] = 1
            # if '*' in item_to_reforge.__dict__['name']:
            #     pass
            # else:
            #     item_to_reforge.__dict__['name'] = '*' + item_to_reforge.__dict__['name']
            fossil_reforge_success(fossil, item_index, old_item_name, old_item_level, item_to_reforge)
        elif fossil.name == 'Fractured Fossil':
            number = random.randint(fractured_fossil.value // 2, fractured_fossil.value)
            item_to_reforge.__dict__['life'] = item_to_reforge.__dict__['life'] + number
            item_to_reforge.__dict__['attack'] = item_to_reforge.__dict__['attack'] + number
            item_to_reforge.__dict__['defense'] = item_to_reforge.__dict__['defense'] + number
            item_to_reforge.__dict__['crit_chance'] = item_to_reforge.__dict__['crit_chance'] + number
            item_to_reforge.__dict__['crit_damage'] = item_to_reforge.__dict__['crit_damage'] + number
            item_to_reforge.__dict__['level'] = item_to_reforge.__dict__['level'] + 1
            item_to_reforge.__dict__['crafted'] = 1
            # if '*' in item_to_reforge.__dict__['name']:
            #     pass
            # else:
            #     item_to_reforge.__dict__['name'] = '*' + item_to_reforge.__dict__['name']
            fossil_reforge_success(fossil, item_index, old_item_name, old_item_level, item_to_reforge)
        else:
            pass

    else:
        fossil_reforge_failure(item_index, item_to_reforge)


def fossil_reforge_success(fossil, item_index, old_item_name, old_item_level, new_item):
    SCREEN.blit(BG, (0, 0))
    SCREEN.blit(BATTLE_BOX, (60, 40))
    player_.display_level_xp()
    reforged_item_update(item_index, old_item_name, old_item_level, new_item)
    confirm_text1 = get_bold_font(35).render(
        f"{new_item.__dict__['name']} level {new_item.__dict__['level']} was reforged", True, YELLOW)
    confirm_text1_rect = confirm_text1.get_rect(center=(SCREEN_WIDTH / 2 - 180, 520))
    # text2 = get_bold_font(25).render(f'(10% chance for the item to get destroyed)', True, WHITE)
    # text2_rect = text2.get_rect(center=(SCREEN_WIDTH / 2 - 180, 520))
    SCREEN.blit(confirm_text1, confirm_text1_rect)

    text1 = get_bold_font(40).render(f"{new_item.name}", True, WHITE)
    level_text = get_regular_font(30).render(f"Level {new_item.level}", True, WHITE)
    type_text = get_bold_font(30).render(f"Type: {new_item.type}", True, WHITE)
    life_text = get_bold_font(30).render(f"Life: {new_item.life}", True, WHITE)
    attack_text = get_bold_font(30).render(f"Attack: {new_item.attack}", True, WHITE)
    defense_text = get_bold_font(30).render(f"Defense: {new_item.defense}", True, WHITE)
    crit_chance_text = get_bold_font(30).render(f"Critical Chance: {new_item.crit_chance} %", True, WHITE)
    crit_damage_text = get_bold_font(30).render(f"Critical Damage: {new_item.crit_damage} %", True, WHITE)
    magic_find_text = get_bold_font(30).render(f"Magic Find: {round(new_item.magic_find * 100, 2)} %", True, WHITE)
    text1_rect = text1.get_rect(center=(SCREEN_WIDTH / 2 - 200, 100))
    level_text_rect = level_text.get_rect(center=(SCREEN_WIDTH / 2 - 200, 140))
    type_text_rect = type_text.get_rect(center=(SCREEN_WIDTH / 2 - 200, 190))
    life_text_rect = life_text.get_rect(center=(SCREEN_WIDTH / 2 - 200, 230))
    attack_text_rect = attack_text.get_rect(center=(SCREEN_WIDTH / 2 - 200, 270))
    defense_text_rect = defense_text.get_rect(center=(SCREEN_WIDTH / 2 - 200, 310))
    crit_chance_text_rect = crit_chance_text.get_rect(center=(SCREEN_WIDTH / 2 - 200, 350))
    crit_damage_text_rect = crit_damage_text.get_rect(center=(SCREEN_WIDTH / 2 - 200, 390))
    magic_find_text_rect = magic_find_text.get_rect(center=(SCREEN_WIDTH / 2 - 200, 430))
    SCREEN.blit(text1, text1_rect)
    SCREEN.blit(type_text, type_text_rect)
    SCREEN.blit(level_text, level_text_rect)
    SCREEN.blit(life_text, life_text_rect)
    SCREEN.blit(attack_text, attack_text_rect)
    SCREEN.blit(defense_text, defense_text_rect)
    SCREEN.blit(crit_chance_text, crit_chance_text_rect)
    SCREEN.blit(crit_damage_text, crit_damage_text_rect)
    SCREEN.blit(magic_find_text, magic_find_text_rect)

    while True:
        USE_FOSSIL_MOUSE_POSITION = pygame.mouse.get_pos()
        BUTTONS = main_menu.main_menu_structure(USE_FOSSIL_MOUSE_POSITION)
        CONTINUE = Button(image=pygame.image.load("assets/images/Smallest Rect.png"), pos=(SCREEN_WIDTH / 2 - 180, 590),
                          text_input="CONTINUE", font=get_bold_font(30), base_color="White", hovering_color=BLUE)
        BUTTONS.append(CONTINUE)

        # NO_BUTTON = Button(image=pygame.image.load("images/Smallest Rect.png"), pos=(380, 600),
        #                      text_input="NO", font=get_bold_font(30), base_color="White", hovering_color=BLUE)
        # YES_BUTTON = Button(image=pygame.image.load("images/Smallest Rect.png"), pos=(540, 600),
        #                     text_input="YES", font=get_bold_font(30), base_color="White", hovering_color=BLUE)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                main_menu.main_menu_structure_events(USE_FOSSIL_MOUSE_POSITION, BUTTONS)
                if CONTINUE.checkForInput(USE_FOSSIL_MOUSE_POSITION):
                    show_consumable_items()

        for button in BUTTONS:
            button.changeColor(USE_FOSSIL_MOUSE_POSITION)
            button.update(SCREEN)
        pygame.display.update()


def fossil_reforge_failure(item_index, item_to_reforge):
    SCREEN.blit(BG, (0, 0))
    SCREEN.blit(BATTLE_BOX, (60, 40))
    player_.display_level_xp()
    row = db.execute("SELECT * FROM inventory WHERE username = :username AND name = :name AND level = :level",
                     username=player_.player.name,
                     name=item_to_reforge.__dict__['name'],
                     level=item_to_reforge.__dict__['level'])
    id = (row[0]['id'])
    db.execute("DELETE FROM inventory WHERE id = :id",
               id=id)

    text1 = get_bold_font(40).render(
        f"{item_to_reforge.__dict__['name']} {item_to_reforge.__dict__['level']} was destroyed!", True, RED)
    text1_rect = text1.get_rect(center=(SCREEN_WIDTH / 2 - 180, 250))
    SCREEN.blit(text1, text1_rect)
    # inventory.remove(item_index)
    inventory.inventory.clear()
    save_load.save_state()
    # inventory_update(player.name, item_to_reforge)
    save_load.load_state()
    while True:
        FOSSIL_REFORGE_FAILURE_MOUSE_POSITION = pygame.mouse.get_pos()
        BUTTONS = main_menu.main_menu_structure(FOSSIL_REFORGE_FAILURE_MOUSE_POSITION)
        CONTINUE = Button(image=pygame.image.load("assets/images/Smallest Rect.png"), pos=(SCREEN_WIDTH / 2 - 180, 550),
                          text_input="CONTINUE", font=get_bold_font(30), base_color="White", hovering_color=BLUE)
        BUTTONS.append(CONTINUE)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                main_menu.main_menu_structure_events(FOSSIL_REFORGE_FAILURE_MOUSE_POSITION, BUTTONS)
                if CONTINUE.checkForInput(FOSSIL_REFORGE_FAILURE_MOUSE_POSITION):
                    show_consumable_items()

        for button in BUTTONS:
            button.changeColor(FOSSIL_REFORGE_FAILURE_MOUSE_POSITION)
            button.update(SCREEN)
        pygame.display.update()


def fossil_reforge_cannot_reforge(item, inventory_page, consumable_type):
    SCREEN.blit(BG, (0, 0))
    SCREEN.blit(BATTLE_BOX, (60, 40))
    player_.display_level_xp()
    confirm_text1 = get_bold_font(35).render(
        f"Unique items cannot be reforged!", True, YELLOW)
    confirm_text1_rect = confirm_text1.get_rect(center=(SCREEN_WIDTH / 2 - 180, 320))
    # text2 = get_bold_font(25).render(f'(10% chance for the item to get destroyed)', True, WHITE)
    # text2_rect = text2.get_rect(center=(SCREEN_WIDTH / 2 - 180, 520))
    SCREEN.blit(confirm_text1, confirm_text1_rect)

    while True:
        USE_FOSSIL_MOUSE_POSITION = pygame.mouse.get_pos()
        BUTTONS = main_menu.main_menu_structure(USE_FOSSIL_MOUSE_POSITION)
        BACK = Button(image=pygame.image.load("assets/images/Smallest Rect.png"), pos=(SCREEN_WIDTH / 2 - 180, 390),
                      text_input="BACK", font=get_bold_font(30), base_color="White", hovering_color=BLUE)
        BUTTONS.append(BACK)

        # NO_BUTTON = Button(image=pygame.image.load("images/Smallest Rect.png"), pos=(380, 600),
        #                      text_input="NO", font=get_bold_font(30), base_color="White", hovering_color=BLUE)
        # YES_BUTTON = Button(image=pygame.image.load("images/Smallest Rect.png"), pos=(540, 600),
        #                     text_input="YES", font=get_bold_font(30), base_color="White", hovering_color=BLUE)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                main_menu.main_menu_structure_events(USE_FOSSIL_MOUSE_POSITION, BUTTONS)
                if BACK.checkForInput(USE_FOSSIL_MOUSE_POSITION):
                    if inventory_page == 1:
                        inventory.show_inventory_page_1(consumable_type)
                    elif inventory_page == 2:
                        inventory.show_inventory_page_2(consumable_type)
                    elif inventory_page == 3:
                        inventory.show_inventory_page_3(consumable_type)
                    elif inventory_page == 4:
                        inventory.show_inventory_page_4(consumable_type)

        for button in BUTTONS:
            button.changeColor(USE_FOSSIL_MOUSE_POSITION)
            button.update(SCREEN)
        pygame.display.update()


def reforged_item_update(item_index, old_item_name, old_item_level, new_item):
    row = db.execute("SELECT * FROM inventory WHERE username = :username AND name = :name AND level = :level",
                     username=player_.player.name, name=old_item_name, level=old_item_level)
    id = (row[0]['id'])
    db.execute("DELETE FROM inventory WHERE id = :id",
               id=id)
    db.execute(
        "INSERT INTO inventory (username, name, type, level, life, attack, defense, crit_chance, crit_damage, magic_find, rarity, crafted, image)"
        "VALUES (:username, :name, :type, :level, :life, :attack, :defense, :crit_chance, :crit_damage, :magic_find, :rarity, :crafted, :image)",
        username=player_.player.name,
        name=new_item.__dict__['name'],
        type=new_item.__dict__['type'],
        level=new_item.__dict__['level'],
        life=new_item.__dict__['life'],
        attack=new_item.__dict__['attack'],
        defense=new_item.__dict__['defense'],
        crit_chance=new_item.__dict__['crit_chance'],
        crit_damage=new_item.__dict__['crit_damage'],
        magic_find=new_item.__dict__['magic_find'],
        rarity=new_item.__dict__['rarity'],
        crafted=new_item.__dict__['crafted'],
        image=new_item.__dict__['image'])
