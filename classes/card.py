from main import *
import globals_variables


class Card:

    def __init__(self, type, name, life, attack, defense, crit_chance, crit_damage, magic_find, level, rarity, image, sound):
        self.type = type
        self.name = name
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


def card_drop_rate(player):
    card_drop_value = random.randint(0, 100)
    # inventory_cards = [value for elem in globals_variables.cards_list for value in elem.__dict__.values()]
    inventory_cards = [card.__dict__['name'] for card in globals_variables.cards_list]
    if card_drop_value <= CARD_DROP_RATE + (CARD_DROP_RATE * player.magic_find):
        if len(list(set(globals_variables.cards_list))) >= 4:
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


def add_card(username, drop):
    new_card = Card(type=drop['type'],
                    name=drop['name'],
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
    print('new card', new_card)
    globals_variables.temp_card_drop.append(new_card)
    globals_variables.cards_list.append(new_card)
    card_update(username, new_card)


def equip_card_update_status(Card):
    player.total_life = player.total_life + int(Card.life)
    player.attack = player.attack + int(Card.attack)
    player.defense = player.defense + int(Card.defense)
    player.crit_chance = player.crit_chance + int(Card.crit_chance)
    player.crit_damage = player.crit_damage + int(Card.crit_damage)
    player.magic_find = player.magic_find + Card.magic_find


def unequip_card_update_status(Card):
    player.total_life = player.total_life - int(Card.life)
    player.attack = player.attack - int(Card.attack)
    player.defense = player.defense - int(Card.defense)
    player.crit_chance = player.crit_chance - int(Card.crit_chance)
    player.crit_damage = player.crit_damage - int(Card.crit_damage)
    player.magic_find = player.magic_find - Card.magic_find


def card_update(username, card):
    db.execute(
        "INSERT INTO cards_list (username, type, name, life, attack, defense, crit_chance, crit_damage,"
        "magic_find, level, rarity, image, sound)"
        "VALUES (:username, :type, :name, :life, :attack, :defense, :crit_chance, :crit_damage,"
        ":magic_find, :level, :rarity, :image, :sound)",
        username=username, type=card.type, name=card.name, life=card.life, attack=card.attack, defense=card.defense,
        crit_chance=card.crit_chance, crit_damage=card.crit_damage, magic_find=card.magic_find, level=card.level,
        rarity=card.rarity, image=card.image, sound=card.sound)
