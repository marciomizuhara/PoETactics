from main import *
import globals_variables
import random


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
    globals_variables.temp_card_drop.append(new_card)
    print('ultimo card variavel global',  globals_variables.temp_card_drop[-1].__dict__['name'])
    globals_variables.cards_list.append(new_card)
    card_list_update(username, new_card)


def card_drop_rate(player):
    card_drop_value = random.randint(0, 100)
    # inventory_cards = [value for elem in globals_variables.cards_list for value in elem.__dict__.values()]
    inventory_cards = [card.__dict__['name'] for card in globals_variables.cards_list]
    if card_drop_value <= CARD_DROP_RATE + (CARD_DROP_RATE * player.magic_find):
        if len(list(set(globals_variables.cards_list))) >= 18:
            print('card aqui 1')
            pass
        else:
            drop = random.choice(card_collection)
            print('card aqui 2')
            if drop['name'] in inventory_cards:
                print(f"{drop['name']} já tem")
                card_drop_rate(player)
            else:
                add_card(player.name, drop)
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
            globals_variables.cards_list.append(new_card)
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


