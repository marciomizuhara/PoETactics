from settings import *
from classes.player_slot import PlayerSlot
from items.amulets import *
from items.armors import *
from items.boots import *
from items.cards import *
from items.consumables import *
from items.gear_type import *
from items.gloves import *
from items.helmets import *
from items.legs import *
from items.rings import *
from items.second_hands import *
from items.gear_type import *
from items.uniques import *
from items.weapons import *


class Player:
    def __init__(self, name, total_life, life, attack, defense, level, xp, shaman, crit_chance, crit_damage,
                 magic_find, image):
        self.name = name
        self.total_life = total_life
        self.life = life
        self.attack = attack
        self.defense = defense
        self.level = level
        self.xp = xp
        self.shaman = shaman
        self.crit_chance = crit_chance
        self.crit_damage = crit_damage
        self.magic_find = magic_find
        self.image = image


# Level 1 player instance
player: Player = Player('unknown', 500, 500, 100, 100, 1, 0, 1, 15, 15, 0, PLAYER)
# player = Player('unknown', 500, 500, 100, 100, 1, 0, 1, 15, 15, 0, PLAYER)
player_slot = PlayerSlot(amulet=amulet_type[0],
                         armor=armor_type[0],
                         gloves=gloves_type[0],
                         helmet=helmet_type[0],
                         legs=legs_type[0],
                         ring1=ring_type[0],
                         ring2=ring_type[0],
                         second_hand=second_hand_type[0],
                         weapon=weapon_type[0],
                         boots=boots_type[0],
                         card=card_collection[0])