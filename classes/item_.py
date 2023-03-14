import random
from classes import player_
from items.gear_type import *


class Item:

    def __init__(self, type, name, level, life, attack, defense, crit_chance, crit_damage, magic_find, rarity, image):
        self.type = type
        self.name = name
        self.level = level
        self.life = life
        self.attack = attack
        self.defense = defense
        self.crit_chance = crit_chance
        self.crit_damage = crit_damage
        self.magic_find = magic_find
        self.rarity = rarity
        self.image = image


def item_level_random_setter(gear_type):
    filtered_dict = (
        [x for x in gear_type if x['level'] > player_.player.level - 2 and x['level'] < player_.player.level + 2 and x['level'] > 1])
    filtered_drop = random.choice(filtered_dict)
    if filtered_drop['level'] > 25:
        filtered_drop['level'] = 25
    elif filtered_drop['level'] <= 1:
        filtered_drop['level'] = 2
    elif filtered_drop['level'] is None:
        filtered_drop['level'] = player_.player.level
    return filtered_drop
