from classes import player_status_
from classes import player_slot_
from classes import player_
from classes import extras
from button import *
from main import *
from settings import *
from items.cards import *
import random


temp_card_drop = []
cards_list = []
card_counter = 0


class Card:

    def __init__(self, type, name, status, life, attack, defense, crit_chance, crit_damage, magic_find, level, rarity, image, sound):
        self.type = type
        self.name = name
        self.status = status
        self.life = life
        self.attack = attack
        self.defense = defense
        self.crit_chance = crit_chance
        self.crit_damage = crit_damage
        self.magic_find = magic_find
        self.level = level
        self.rarity = rarity
        self.image = image
        self.sound = sound


def equip_card_update_status(card_name):
    # Removing current card status
    # current_card = player_slot.card
    print('slot card', int(player_slot_.player_slot.card['life']))
    print('Total Life com card antigo', player_.player.total_life)
    player_.player.total_life = player_.player.total_life - int(player_slot_.player_slot.card['life'])
    print('Total Life sem card antigo', player_.player.total_life)
    player_.player.attack = player_.player.attack - int(player_slot_.player_slot.card['attack'])
    player_.player.defense = player_.player.defense - int(player_slot_.player_slot.card['defense'])
    player_.player.crit_chance = player_.player.crit_chance - int(player_slot_.player_slot.card['crit_chance'])
    player_.player.crit_damage = player_.player.crit_damage - int(player_slot_.player_slot.card['crit_damage'])
    player_.player.magic_find = player_.player.magic_find - int(player_slot_.player_slot.card['magic_find'])

    # Adding new card status
    new_card = [x for x in cards_list if x.__dict__['name'] == card_name][0].__dict__

    player_.player.total_life = player_.player.total_life + new_card['life']
    print('Total Life com card novo', player_.player.total_life)
    player_.player.attack = player_.player.attack + new_card['attack']
    player_.player.defense = player_.player.defense + new_card['defense']
    player_.player.crit_chance = player_.player.crit_chance + new_card['crit_chance']
    player_.player.crit_damage = player_.player.crit_damage + new_card['crit_damage']
    player_.player.magic_find = player_.player.magic_find + new_card['magic_find']
    player_slot_.player_slot.card = new_card
    player_slot_card_update(player_.player.name, new_card)


def add_card(username, drop):
    new_card = Card(type=drop['type'],
                    name=drop['name'],
                    status=1,
                    life=drop['life'],
                    attack=drop['attack'],
                    defense=drop['defense'],
                    crit_chance=drop['crit_chance'],
                    crit_damage=drop['crit_damage'],
                    magic_find=drop['magic_find'],
                    level=drop['level'],
                    rarity=drop['rarity'],
                    image=drop['image'],
                    sound=drop['sound'],
                    )
    temp_card_drop.append(new_card)
    print('ultimo card variavel global',  temp_card_drop[-1].__dict__['name'])
    cards_list.append(new_card)
    card_list_update(username, new_card)


def card_drop_rate():
    card_drop_value = random.randint(0, 100)
    # inventory_cards = [value for elem in globals_variables.cards_list for value in elem.__dict__.values()]
    inventory_cards = [card.__dict__['name'] for card in cards_list]
    if card_drop_value <= CARD_DROP_RATE + (CARD_DROP_RATE * player_.player.magic_find):
        if len(list(set(cards_list))) >= 18:
            print('card aqui 1')
            pass
        else:
            drop = random.choice(card_collection)
            print('card aqui 2')
            if drop['name'] in inventory_cards:
                print(f"{drop['name']} já tem")
                card_drop_rate()
            else:
                add_card(player_.player.name, drop)
    else:
        pass


def card_instance_load(username):
    rows3 = db.execute("SELECT * FROM cards_list WHERE username = :username",
                       username=username)
    print(rows3)
    if len(rows3) < 1:
        print('entra aqui se não houver nada no CARD LIST')
        new_card = Card(card_collection[0]['type'], card_collection[0]['name'], 1, card_collection[0]['life'],
                        card_collection[0]['attack'],
                        card_collection[0]['defense'], card_collection[0]['crit_chance'], card_collection[0]['crit_damage'],
                        card_collection[0]['magic_find'], card_collection[0]['level'], card_collection[0]['rarity'], card_collection[0]['image'],
                        card_collection[0]['sound'])
        add_card(username, new_card.__dict__)
        # globals_variables.cards_list.append(new_card)
        # card_list_update(username, new_card)
    else:
        for i in range(0, len(rows3)):
            new_card = Card(rows3[i]['type'], rows3[i]['name'], rows3[i]['status'], rows3[i]['life'],
                            rows3[i]['attack'],
                            rows3[i]['defense'], rows3[i]['crit_chance'], rows3[i]['crit_damage'],
                            rows3[i]['magic_find'], rows3[i]['level'], rows3[i]['rarity'], rows3[i]['image'],
                            rows3[i]['sound'])
            cards_list.append(new_card)
            # card_list_update(username, new_card)


def card_list_update(username, card):
    db.execute(
        "INSERT INTO cards_list (username, type, name, status, life, attack, defense, crit_chance, crit_damage,"
        "magic_find, level, rarity, image, sound)"
        "VALUES (:username, :type, :name, :status, :life, :attack, :defense, :crit_chance, :crit_damage,"
        ":magic_find, :level, :rarity, :image, :sound)",
        username=username, type=card.type, name=card.name, status=card.status, life=card.life, attack=card.attack, defense=card.defense,
        crit_chance=card.crit_chance, crit_damage=card.crit_damage, magic_find=card.magic_find, level=card.level,
        rarity=card.rarity, image=card.image, sound=card.sound)
    row = db.execute("SELECT * FROM card WHERE username = :username",
                     username=username)
    if len(row) < 1:
        card_slot_update(username, card.__dict__)


def card_slot_update(username, card):
    db.execute("DELETE FROM card WHERE name = :name",
               name=card['name'])
    db.execute(
        "INSERT INTO card (username, type, name, status, life, attack, defense, crit_chance, crit_damage,"
        "magic_find, level, rarity, image, sound)"
        "VALUES (:username, :type, :name, :status, :life, :attack, :defense, :crit_chance, :crit_damage,"
        ":magic_find, :level, :rarity, :image, :sound)",
        username=username, type=card['type'], name=card['name'], status=card['status'], life=card['life'],
        attack=card['attack'],
        defense=card['defense'],
        crit_chance=card['crit_chance'], crit_damage=card['crit_damage'], magic_find=card['magic_find'],
        level=card['level'],
        rarity=card['rarity'], image=card['image'], sound=card['sound'])


def player_slot_card_update(username, card):
    row = db.execute("SELECT * FROM card WHERE username = :username",
                     username=username)
    if len(row) < 1:
        card_slot_update(username, card)
    else:
        name = (row[0]['name'])

        db.execute("DELETE FROM card WHERE name = :name",
                   name=name)
        db.execute(
            "INSERT INTO card (username, type, name, status, life, attack, defense, crit_chance, crit_damage,"
            "magic_find, level, rarity, image, sound)"
            "VALUES (:username, :type, :name, :status, :life, :attack, :defense, :crit_chance, :crit_damage,"
            ":magic_find, :level, :rarity, :image, :sound)",
            username=username, type=card['type'], name=card['name'], status=card['status'], life=card['life'], attack=card['attack'],
            defense=card['defense'],
            crit_chance=card['crit_chance'], crit_damage=card['crit_damage'], magic_find=card['magic_find'], level=card['level'],
            rarity=card['rarity'], image=card['image'], sound=card['sound'])
        # card_instance_load(username)


def unequip_card_update_status(card_name):
    pass


def duplicate_prevention(username, card_name):
    rows1 = db.execute("SELECT * FROM cards_list WHERE username = :username",
                       username=username)
    if len(rows1) < 1:
        return 0
    else:
        if rows1[0]['name'] == card_name:
            return 1
        else:
            return 0


def draw_equipped_card(card_equipped):
    if card_equipped['name'] == 'Squire':
        SCREEN.blit(SQUIRE_CARD, (940, 100))
    if card_equipped['name'] == 'Chemist':
        SCREEN.blit(CHEMIST_CARD, (940, 100))
    if card_equipped['name'] == 'Knight':
        SCREEN.blit(KNIGHT_CARD, (940, 100))
    if card_equipped['name'] == 'Archer':
        SCREEN.blit(ARCHER_CARD, (940, 100))
    if card_equipped['name'] == 'Priest':
        SCREEN.blit(PRIEST_CARD, (940, 100))
    if card_equipped['name'] == 'Wizard':
        SCREEN.blit(WIZARD_CARD, (940, 100))
    if card_equipped['name'] == 'Monk':
        SCREEN.blit(MONK_CARD, (940, 100))
    if card_equipped['name'] == 'Thief':
        SCREEN.blit(THIEF_CARD, (940, 100))
    if card_equipped['name'] == 'Oracle':
        SCREEN.blit(ORACLE_CARD, (940, 100))
    if card_equipped['name'] == 'Time Mage':
        SCREEN.blit(TIME_MAGE_CARD, (940, 100))
    if card_equipped['name'] == 'Geomancer':
        SCREEN.blit(GEOMANCER_CARD, (940, 100))
    if card_equipped['name'] == 'Lancer':
        SCREEN.blit(LANCER_CARD, (940, 100))
    if card_equipped['name'] == 'Mediator':
        SCREEN.blit(MEDIATOR_CARD, (940, 100))
    if card_equipped['name'] == 'Summoner':
        SCREEN.blit(SUMMONER_CARD, (940, 100))
    if card_equipped['name'] == 'Samurai':
        SCREEN.blit(SAMURAI_CARD, (940, 100))
    if card_equipped['name'] == 'Ninja':
        SCREEN.blit(NINJA_CARD, (940, 100))
    if card_equipped['name'] == 'Calculator':
        SCREEN.blit(CALCULATOR_CARD, (940, 100))
    if card_equipped['name'] == 'Bard/Dancer':
        SCREEN.blit(BARD_DANCER_CARD, (940, 100))


def cards(previous_screen):
    global counter, LAST_TIME_MS, confirmation_counter
    hovering_card = True
    equipped_text = get_bold_font(30).render('Equipped', True, WHITE)
    equipped_text_rect = equipped_text.get_rect(center=(1063, 465))

    # SCREEN.blit(PLAYER_STATUS_BOX, (80, 60))

    # Card Images
    # inventory_cards = [value for elem in cards_list for value in elem.__dict__.values()]
    # if drop['name'] in inventory_cards:
    setter = 0
    width = 100
    height = 100
    counter = 0
    CARD_LIST = [SQUIRE_CARD_FRAME, CHEMIST_CARD_FRAME, KNIGHT_CARD_FRAME, ARCHER_CARD_FRAME,
                 PRIEST_CARD_FRAME, WIZARD_CARD_FRAME, MONK_CARD_FRAME, THIEF_CARD_FRAME,
                 ORACLE_CARD_FRAME, TIME_MAGE_CARD_FRAME, GEOMANCER_CARD_FRAME, LANCER_CARD_FRAME,
                 SQUIRE_CARD_FRAME, CHEMIST_CARD_FRAME, SQUIRE_CARD_FRAME, CHEMIST_CARD_FRAME,
                 SQUIRE_CARD_FRAME, CHEMIST_CARD_FRAME]
    while setter < 3:
        for card in range(0, 6):
            SCREEN.blit(CARD_LIST[counter], (width, height))
            width += 130
            counter += 1
        height += 150
        width = 100
        setter += 1
    # SCREEN.blit(CHEMIST_CARD, (940, 100))

    card_names = [x.__dict__['name'] for x in cards_list]



    squire_rect = SQUIRE_CARD_FRAME.get_rect(center=(140, 160))
    chemist_rect = CHEMIST_CARD_FRAME.get_rect(center=(270, 160))
    knight_rect = KNIGHT_CARD_FRAME.get_rect(center=(400, 160))
    archer_rect = ARCHER_CARD_FRAME.get_rect(center=(530, 160))
    priest_rect = PRIEST_CARD_FRAME.get_rect(center=(660, 160))
    wizard_rect = WIZARD_CARD_FRAME.get_rect(center=(790, 160))
    monk_rect = MONK_CARD_FRAME.get_rect(center=(140, 310))
    thief_rect = THIEF_CARD_FRAME.get_rect(center=(270, 310))
    oracle_rect = ORACLE_CARD_FRAME.get_rect(center=(400, 310))
    time_mage_rect = TIME_MAGE_CARD_FRAME.get_rect(center=(530, 310))
    geomancer_rect = GEOMANCER_CARD_FRAME.get_rect(center=(660, 310))
    lancer_rect = LANCER_CARD_FRAME.get_rect(center=(790, 310))
    mediator_rect = MEDIATOR_CARD_FRAME.get_rect(center=(140, 460))
    summoner_rect = SUMMONER_CARD_FRAME.get_rect(center=(270, 460))
    samurai_rect = SAMURAI_CARD_FRAME.get_rect(center=(400, 460))
    ninja_rect = NINJA_CARD_FRAME.get_rect(center=(530, 460))
    calculator_rect = CALCULATOR_CARD_FRAME.get_rect(center=(660, 460))
    bard_dancer_rect = BARD_DANCER_CARD_FRAME.get_rect(center=(790, 460))
    cards_obtained = [x.__dict__['name'] for x in cards_list]
    # SCREEN.blit(SQUIRE_CARD, (250, 100))
    equipped_confirmation = False
    while True:
        CARDS_MOUSE_POSITION = pygame.mouse.get_pos()
        SCREEN.blit(BG, (0, 0))
        SCREEN.blit(BATTLE_BOX_LARGE, (60, 40))
        # SCREEN.blit(CARD_EQUIPPED, (940, 440))
        if squire_rect.colliderect(squire_rect) or not chemist_rect.collidepoint(
                CARDS_MOUSE_POSITION) or not knight_rect.collidepoint(
            CARDS_MOUSE_POSITION) or not archer_rect.collidepoint(
            CARDS_MOUSE_POSITION) or not priest_rect.collidepoint(
            CARDS_MOUSE_POSITION) or not wizard_rect.collidepoint(
            CARDS_MOUSE_POSITION) or not monk_rect.collidepoint(
            CARDS_MOUSE_POSITION) or not thief_rect.collidepoint(
            CARDS_MOUSE_POSITION) or not oracle_rect.collidepoint(
            CARDS_MOUSE_POSITION) or not time_mage_rect.collidepoint(
            CARDS_MOUSE_POSITION) or not geomancer_rect.collidepoint(
            CARDS_MOUSE_POSITION) or not lancer_rect.collidepoint(
            CARDS_MOUSE_POSITION) or not mediator_rect.collidepoint(
            CARDS_MOUSE_POSITION) or not summoner_rect.collidepoint(
            CARDS_MOUSE_POSITION) or not samurai_rect.collidepoint(
            CARDS_MOUSE_POSITION) or not ninja_rect.collidepoint(
            CARDS_MOUSE_POSITION) or not calculator_rect.collidepoint(
            CARDS_MOUSE_POSITION) or not bard_dancer_rect.collidepoint(CARDS_MOUSE_POSITION):
            hovering_card = True
            draw_equipped_card(player_slot_.player_slot.card)


        # if not squire_rect.colliderect(squire_rect) or not chemist_rect.collidepoint(
        #         CARDS_MOUSE_POSITION) or not knight_rect.collidepoint(
        #     CARDS_MOUSE_POSITION) or not archer_rect.collidepoint(
        #     CARDS_MOUSE_POSITION) or not priest_rect.collidepoint(
        #     CARDS_MOUSE_POSITION) or not wizard_rect.collidepoint(
        #     CARDS_MOUSE_POSITION) or not monk_rect.collidepoint(
        #     CARDS_MOUSE_POSITION) or not thief_rect.collidepoint(
        #     CARDS_MOUSE_POSITION) or not oracle_rect.collidepoint(
        #     CARDS_MOUSE_POSITION) or not time_mage_rect.collidepoint(
        #     CARDS_MOUSE_POSITION) or not geomancer_rect.collidepoint(
        #     CARDS_MOUSE_POSITION) or not lancer_rect.collidepoint(
        #     CARDS_MOUSE_POSITION) or not mediator_rect.collidepoint(
        #     CARDS_MOUSE_POSITION) or not summoner_rect.collidepoint(
        #     CARDS_MOUSE_POSITION) or not samurai_rect.collidepoint(
        #     CARDS_MOUSE_POSITION) or not ninja_rect.collidepoint(
        #     CARDS_MOUSE_POSITION) or not calculator_rect.collidepoint(
        #     CARDS_MOUSE_POSITION) or not bard_dancer_rect.collidepoint(CARDS_MOUSE_POSITION) and hovering_card:
        #         card_equipped = player_slot_.player_slot.card
        #
        #         hovering_card = False

        if 'Squire' in card_names:
            SCREEN.blit(SQUIRE, (100, 100))
        if 'Chemist' in card_names:
            SCREEN.blit(CHEMIST, (230, 100))
        if 'Knight' in card_names:
            SCREEN.blit(KNIGHT, (360, 100))
        if 'Archer' in card_names:
            SCREEN.blit(ARCHER, (490, 100))
        if 'Priest' in card_names:
            SCREEN.blit(PRIEST, (620, 100))
        if 'Wizard' in card_names:
            SCREEN.blit(WIZARD, (750, 100))
        if 'Monk' in card_names:
            SCREEN.blit(MONK, (100, 250))
        if 'Thief' in card_names:
            SCREEN.blit(THIEF, (230, 250))
        if 'Oracle' in card_names:
            SCREEN.blit(ORACLE, (360, 250))
        if 'Time Mage' in card_names:
            SCREEN.blit(TIME_MAGE, (490, 250))
        if 'Geomancer' in card_names:
            SCREEN.blit(GEOMANCER, (620, 250))
        if 'Lancer' in card_names:
            SCREEN.blit(LANCER, (750, 250))
        if 'Mediator' in card_names:
            SCREEN.blit(MEDIATOR, (100, 400))
        if 'Summoner' in card_names:
            SCREEN.blit(SUMMONER, (230, 400))
        if 'Samurai' in card_names:
            SCREEN.blit(SAMURAI, (360, 400))
        if 'Ninja' in card_names:
            SCREEN.blit(NINJA, (490, 400))
        if 'Calculator' in card_names:
            SCREEN.blit(CALCULATOR, (620, 400))
        if 'Bard/Dancer' in card_names:
            SCREEN.blit(BARD_DANCER, (750, 400))


        # BUTTONS = main_menu_structure(PLAYER_STATUS_MOUSE_POSITION)
        # EQUIP = Button(image=pygame.image.load("assets/images/ONE_LINE_CARD_BOX.png"), pos=(1063, 460),
        #                    text_input="EQUIP", font=get_bold_font(30), base_color="White", hovering_color=BLUE)
        BACK = Button(image=pygame.image.load("assets/images/Smallest Rect.png"), pos=(160, 610),
                      text_input="BACK", font=get_bold_font(30), base_color="White", hovering_color=BLUE)

        # NO_BUTTON = Button(image=pygame.image.load("images/Smallest Rect.png"), pos=(380, 600),
        #                      text_input="NO", font=get_bold_font(30), base_color="White", hovering_color=BLUE)
        # YES_BUTTON = Button(image=pygame.image.load("images/Smallest Rect.png"), pos=(540, 600),
        #                     text_input="YES", font=get_bold_font(30), base_color="White", hovering_color=BLUE)

        diff_time_ms = int(round(time.time() * 4000)) - LAST_TIME_MS

        if diff_time_ms >= 4000:
            counter += 1
            confirmation_counter += 1
            print('confirmation counter', confirmation_counter)
            LAST_TIME_MS = int(round(time.time() * 4000))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if BACK.checkForInput(CARDS_MOUSE_POSITION):
                    counter = 0
                    if previous_screen == 'player_status':
                        player_status_.player_status()
                    else:
                        extras.extras()
                if squire_rect.collidepoint(CARDS_MOUSE_POSITION)  and 'Squire' in cards_obtained:
                    equip_card_update_status('Squire')
                    card_change_sound()
                    confirmation_counter = 0
                    equipped_confirmation = True
                if chemist_rect.collidepoint(CARDS_MOUSE_POSITION) and 'Chemist' in cards_obtained:
                    equip_card_update_status('Chemist')
                    card_change_sound()
                    confirmation_counter = 0
                    equipped_confirmation = True
                if knight_rect.collidepoint(CARDS_MOUSE_POSITION) and 'Knight' in cards_obtained:
                    equip_card_update_status('Knight')
                    card_change_sound()
                    confirmation_counter = 0
                    equipped_confirmation = True
                if archer_rect.collidepoint(CARDS_MOUSE_POSITION) and 'Archer' in cards_obtained:
                    equip_card_update_status('Archer')
                    card_change_sound()
                    confirmation_counter = 0
                    equipped_confirmation = True
                if priest_rect.collidepoint(CARDS_MOUSE_POSITION) and 'Priest' in cards_obtained:
                    equip_card_update_status('Priest')
                    card_change_sound()
                    confirmation_counter = 0
                    equipped_confirmation = True
                if wizard_rect.collidepoint(CARDS_MOUSE_POSITION) and 'Wizard' in cards_obtained:
                    equip_card_update_status('Wizard')
                    card_change_sound()
                    confirmation_counter = 0
                    equipped_confirmation = True
                if monk_rect.collidepoint(CARDS_MOUSE_POSITION) and 'Monk' in cards_obtained:
                    equip_card_update_status('Monk')
                    card_change_sound()
                    confirmation_counter = 0
                    equipped_confirmation = True
                if thief_rect.collidepoint(CARDS_MOUSE_POSITION) and 'Thief' in cards_obtained:
                    equip_card_update_status('Thief')
                    card_change_sound()
                    confirmation_counter = 0
                    equipped_confirmation = True
                if oracle_rect.collidepoint(CARDS_MOUSE_POSITION) and 'Oracle' in cards_obtained:
                    equip_card_update_status('Oracle')
                    card_change_sound()
                    confirmation_counter = 0
                    equipped_confirmation = True
                if time_mage_rect.collidepoint(CARDS_MOUSE_POSITION) and 'Time Mage' in cards_obtained:
                    equip_card_update_status('Time Mage')
                    card_change_sound()
                    confirmation_counter = 0
                    equipped_confirmation = True
                if geomancer_rect.collidepoint(CARDS_MOUSE_POSITION) and 'Geomancer' in cards_obtained:
                    equip_card_update_status('Geomancer')
                    card_change_sound()
                    confirmation_counter = 0
                    equipped_confirmation = True
                if lancer_rect.collidepoint(CARDS_MOUSE_POSITION) and 'Lancer' in cards_obtained:
                    equip_card_update_status('Lancer')
                    card_change_sound()
                    confirmation_counter = 0
                    equipped_confirmation = True
                if mediator_rect.collidepoint(CARDS_MOUSE_POSITION) and 'Mediator' in cards_obtained:
                    equip_card_update_status('Mediator')
                    card_change_sound()
                    confirmation_counter = 0
                    equipped_confirmation = True
                if summoner_rect.collidepoint(CARDS_MOUSE_POSITION) and 'Summoner' in cards_obtained:
                    equip_card_update_status('Summoner')
                    card_change_sound()
                    confirmation_counter = 0
                    equipped_confirmation = True
                if samurai_rect.collidepoint(CARDS_MOUSE_POSITION) and 'Samurai' in cards_obtained:
                    equip_card_update_status('Samurai')
                    card_change_sound()
                    confirmation_counter = 0
                    equipped_confirmation = True
                if ninja_rect.collidepoint(CARDS_MOUSE_POSITION) and 'Ninja' in cards_obtained:
                    equip_card_update_status('Ninja')
                    card_change_sound()
                    confirmation_counter = 0
                    equipped_confirmation = True
                if calculator_rect.collidepoint(CARDS_MOUSE_POSITION) and 'Calculator' in cards_obtained:
                    equip_card_update_status('Calculator')
                    card_change_sound()
                    confirmation_counter = 0
                    equipped_confirmation = True
                if bard_dancer_rect.collidepoint(CARDS_MOUSE_POSITION) and 'Bard/Dancer' in cards_obtained:
                    equip_card_update_status('Bard/Dancer')
                    card_change_sound()
                    confirmation_counter = 0
                    equipped_confirmation = True

            if squire_rect.collidepoint(CARDS_MOUSE_POSITION) and 'Squire' in card_names:
                # print('squire')
                # print(globals_variables.cards_list[0])

                SCREEN.blit(SQUIRE_CARD, (940, 100))


            if chemist_rect.collidepoint(CARDS_MOUSE_POSITION) and 'Chemist' in card_names:
                # print('chemist')

                SCREEN.blit(CHEMIST_CARD, (940, 100))
                hovering_card = True
            if knight_rect.collidepoint(CARDS_MOUSE_POSITION) and 'Knight' in card_names:
                # print('knight')

                SCREEN.blit(KNIGHT_CARD, (940, 100))
            if archer_rect.collidepoint(CARDS_MOUSE_POSITION) and 'Archer' in card_names:
                # print('archer')

                SCREEN.blit(ARCHER_CARD, (940, 100))
            if priest_rect.collidepoint(CARDS_MOUSE_POSITION) and 'Priest' in card_names:
                # print('priest')

                SCREEN.blit(PRIEST_CARD, (940, 100))
            if wizard_rect.collidepoint(CARDS_MOUSE_POSITION) and 'Wizard' in card_names:
                # print('wizard')

                SCREEN.blit(WIZARD_CARD, (940, 100))
            if monk_rect.collidepoint(CARDS_MOUSE_POSITION) and 'Monk' in card_names:
                # print('monk')

                SCREEN.blit(MONK_CARD, (940, 100))
            if thief_rect.collidepoint(CARDS_MOUSE_POSITION) and 'Thief' in card_names:
                # print('thief')

                SCREEN.blit(THIEF_CARD, (940, 100))
            if oracle_rect.collidepoint(CARDS_MOUSE_POSITION) and 'Oracle' in card_names:
                # print('oracle')

                SCREEN.blit(ORACLE_CARD, (940, 100))
            if time_mage_rect.collidepoint(CARDS_MOUSE_POSITION) and 'Time Mage' in card_names:
                # print('time mage')

                SCREEN.blit(TIME_MAGE_CARD, (940, 100))
            if geomancer_rect.collidepoint(CARDS_MOUSE_POSITION) and 'Geomancer' in card_names:
                # print('geomancer')

                SCREEN.blit(GEOMANCER_CARD, (940, 100))
            if lancer_rect.collidepoint(CARDS_MOUSE_POSITION) and 'Lancer' in card_names:
                # print('lancer')

                SCREEN.blit(LANCER_CARD, (940, 100))
            if mediator_rect.collidepoint(CARDS_MOUSE_POSITION) and 'Mediator' in card_names:
                # print('mediator')

                SCREEN.blit(MEDIATOR_CARD, (940, 100))
            if summoner_rect.collidepoint(CARDS_MOUSE_POSITION) and 'Summoner' in card_names:
                # print('summoner')

                SCREEN.blit(SUMMONER_CARD, (940, 100))
            if samurai_rect.collidepoint(CARDS_MOUSE_POSITION) and 'Samurai' in card_names:
                # print('samurai')

                SCREEN.blit(SAMURAI_CARD, (940, 100))
            if ninja_rect.collidepoint(CARDS_MOUSE_POSITION) and 'Ninja' in card_names:
                # print('ninja')
                SCREEN.blit(NINJA_CARD, (940, 100))
            if calculator_rect.collidepoint(CARDS_MOUSE_POSITION) and 'Calculator' in card_names:
                # print('calculator')
                SCREEN.blit(CALCULATOR_CARD, (940, 100))
            if bard_dancer_rect.collidepoint(CARDS_MOUSE_POSITION) and 'Bard/Dancer' in card_names:
                # print('bard/dancer')
                SCREEN.blit(BARD_DANCER_CARD, (940, 100))

        if equipped_confirmation and confirmation_counter >= 0:
            card = f'{player_slot_.player_slot.card["name"]} equipped!'
            show_confirmation_message(card, WHITE, 40, 600, 600)
        if confirmation_counter == 3:
            confirmation_counter = 0
            equipped_confirmation = False
        for button in [BACK]:
            button.changeColor(CARDS_MOUSE_POSITION)
            button.update(SCREEN)
        pygame.display.update()


def show_confirmation_message(message, color, size, x, y):
    text = get_bold_font(size).render(message, True, color)
    rect = text.get_rect()
    rect.center = (x, y)
    SCREEN.blit(text, rect)
    # pygame.display.update()