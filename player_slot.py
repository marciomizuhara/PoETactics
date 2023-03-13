from fonts import *
from settings import *
from items.amulets import *
from items.armors import *
from items.boots import *
from items.cards import *
from items.gloves import *
from items.helmets import *
from items.legs import *
from items.rings import *
from items.second_hands import *
from items.weapons import *


class PlayerSlot:

    def __init__(self, amulet, armor, gloves, helmet, legs, ring1, ring2, second_hand, weapon, boots, card):
        self.amulet = amulet
        self.armor = armor
        self.gloves = gloves
        self.helmet = helmet
        self.legs = legs
        self.ring1 = ring1
        self.ring2 = ring2
        self.second_hand = second_hand
        self.weapon = weapon
        self.boots = boots
        self.card = card

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


def show_player_slot(gear_type):
    if gear_type == 'amulet':
        text1 = get_bold_font(35).render(f"{player_slot.amulet['name']}", True, WHITE)
        level_text = get_regular_font(25).render(f"Level {player_slot.amulet['level']}", True, WHITE)
        type_text = get_bold_font(25).render(f"Type: {player_slot.amulet['type']}", True, WHITE)
        life_text = get_bold_font(25).render(f"Life: {player_slot.amulet['life']}", True, WHITE)
        attack_text = get_bold_font(25).render(f"Attack: {player_slot.amulet['attack']}", True, WHITE)
        defense_text = get_bold_font(25).render(f"Defense: {player_slot.amulet['defense']}", True, WHITE)
        crit_chance_text = get_bold_font(25).render(f"Critical Chance: {player_slot.amulet['crit_chance']} %", True,
                                                    WHITE)
        crit_damage_text = get_bold_font(25).render(f"Critical Damage: {player_slot.amulet['crit_damage']} %", True,
                                                    WHITE)
        magic_find_text = get_bold_font(25).render(f"Magic Find: {round(player_slot.amulet['magic_find'] * 100, 2)} %",
                                                   True, WHITE)
        show_player_slot_helper(text1, level_text, type_text, life_text, attack_text, defense_text,
                                crit_chance_text, crit_damage_text, magic_find_text)
    elif gear_type == 'armor':
        text1 = get_bold_font(35).render(f"{player_slot.armor['name']}", True, WHITE)
        level_text = get_regular_font(25).render(f"Level {player_slot.armor['level']}", True, WHITE)
        type_text = get_bold_font(25).render(f"Type: {player_slot.armor['type']}", True, WHITE)
        life_text = get_bold_font(25).render(f"Life: {player_slot.armor['life']}", True, WHITE)
        attack_text = get_bold_font(25).render(f"Attack: {player_slot.armor['attack']}", True, WHITE)
        defense_text = get_bold_font(25).render(f"Defense: {player_slot.armor['defense']}", True, WHITE)
        crit_chance_text = get_bold_font(25).render(f"Critical Chance: {player_slot.armor['crit_chance']} %", True,
                                                    WHITE)
        crit_damage_text = get_bold_font(25).render(f"Critical Damage: {player_slot.armor['crit_damage']} %", True,
                                                    WHITE)
        magic_find_text = get_bold_font(25).render(f"Magic Find: {round(player_slot.armor['magic_find'] * 100, 2)} %",
                                                   True, WHITE)
        show_player_slot_helper(text1, level_text, type_text, life_text, attack_text, defense_text,
                                crit_chance_text, crit_damage_text, magic_find_text)
    elif gear_type == 'card':
        text1 = get_bold_font(35).render(f"{player_slot.card['name']}", True, WHITE)
        level_text = get_regular_font(25).render(f"Level {player_slot.card['level']}", True, WHITE)
        type_text = get_bold_font(25).render(f"Type: {player_slot.card['type']}", True, WHITE)
        life_text = get_bold_font(25).render(f"Life: {player_slot.card['life']}", True, WHITE)
        attack_text = get_bold_font(25).render(f"Attack: {player_slot.card['attack']}", True, WHITE)
        defense_text = get_bold_font(25).render(f"Defense: {player_slot.card['defense']}", True, WHITE)
        crit_chance_text = get_bold_font(25).render(f"Critical Chance: {player_slot.card['crit_chance']} %", True,
                                                    WHITE)
        crit_damage_text = get_bold_font(25).render(f"Critical Damage: {player_slot.card['crit_damage']} %", True,
                                                    WHITE)
        magic_find_text = get_bold_font(25).render(f"Magic Find: {round(player_slot.card['magic_find'] * 100, 2)} %",
                                                   True, WHITE)
        show_player_slot_helper(text1, level_text, type_text, life_text, attack_text, defense_text,
                                crit_chance_text, crit_damage_text, magic_find_text)

    elif gear_type == 'second_hand':
        text1 = get_bold_font(35).render(f"{player_slot.second_hand['name']}", True, WHITE)
        level_text = get_regular_font(25).render(f"Level {player_slot.second_hand['level']}", True, WHITE)
        type_text = get_bold_font(25).render(f"Type: {player_slot.second_hand['type']}", True, WHITE)
        life_text = get_bold_font(25).render(f"Life: {player_slot.second_hand['life']}", True, WHITE)
        attack_text = get_bold_font(25).render(f"Attack: {player_slot.second_hand['attack']}", True, WHITE)
        defense_text = get_bold_font(25).render(f"Defense: {player_slot.second_hand['defense']}", True, WHITE)
        crit_chance_text = get_bold_font(25).render(f"Critical Chance: {player_slot.second_hand['crit_chance']} %",
                                                    True, WHITE)
        crit_damage_text = get_bold_font(25).render(f"Critical Damage: {player_slot.second_hand['crit_damage']} %",
                                                    True, WHITE)
        magic_find_text = get_bold_font(25).render(
            f"Magic Find: {round(player_slot.second_hand['magic_find'] * 100, 2)} %",
            True, WHITE)
        show_player_slot_helper(text1, level_text, type_text, life_text, attack_text, defense_text,
                                crit_chance_text, crit_damage_text, magic_find_text)
    elif gear_type == 'legs':
        text1 = get_bold_font(35).render(f"{player_slot.legs['name']}", True, WHITE)
        level_text = get_regular_font(25).render(f"Level {player_slot.legs['level']}", True, WHITE)
        type_text = get_bold_font(25).render(f"Type: {player_slot.legs['type']}", True, WHITE)
        life_text = get_bold_font(25).render(f"Life: {player_slot.legs['life']}", True, WHITE)
        attack_text = get_bold_font(25).render(f"Attack: {player_slot.legs['attack']}", True, WHITE)
        defense_text = get_bold_font(25).render(f"Defense: {player_slot.legs['defense']}", True, WHITE)
        crit_chance_text = get_bold_font(25).render(f"Critical Chance: {player_slot.legs['crit_chance']} %", True,
                                                    WHITE)
        crit_damage_text = get_bold_font(25).render(f"Critical Damage: {player_slot.legs['crit_damage']} %", True,
                                                    WHITE)
        magic_find_text = get_bold_font(25).render(f"Magic Find: {round(player_slot.legs['magic_find'] * 100, 2)} %",
                                                   True, WHITE)
        show_player_slot_helper(text1, level_text, type_text, life_text, attack_text, defense_text,
                                crit_chance_text, crit_damage_text, magic_find_text)
    elif gear_type == 'gloves':
        text1 = get_bold_font(35).render(f"{player_slot.gloves['name']}", True, WHITE)
        level_text = get_regular_font(25).render(f"Level {player_slot.gloves['level']}", True, WHITE)
        type_text = get_bold_font(25).render(f"Type: {player_slot.gloves['type']}", True, WHITE)
        life_text = get_bold_font(25).render(f"Life: {player_slot.gloves['life']}", True, WHITE)
        attack_text = get_bold_font(25).render(f"Attack: {player_slot.gloves['attack']}", True, WHITE)
        defense_text = get_bold_font(25).render(f"Defense: {player_slot.gloves['defense']}", True, WHITE)
        crit_chance_text = get_bold_font(25).render(f"Critical Chance: {player_slot.gloves['crit_chance']} %", True,
                                                    WHITE)
        crit_damage_text = get_bold_font(25).render(f"Critical Damage: {player_slot.gloves['crit_damage']} %", True,
                                                    WHITE)
        magic_find_text = get_bold_font(25).render(f"Magic Find: {round(player_slot.gloves['magic_find'] * 100, 2)} %",
                                                   True, WHITE)
        show_player_slot_helper(text1, level_text, type_text, life_text, attack_text, defense_text,
                                crit_chance_text, crit_damage_text, magic_find_text)
    elif gear_type == 'boots':
        text1 = get_bold_font(35).render(f"{player_slot.boots['name']}", True, WHITE)
        level_text = get_regular_font(25).render(f"Level {player_slot.boots['level']}", True, WHITE)
        type_text = get_bold_font(25).render(f"Type: {player_slot.boots['type']}", True, WHITE)
        life_text = get_bold_font(25).render(f"Life: {player_slot.boots['life']}", True, WHITE)
        attack_text = get_bold_font(25).render(f"Attack: {player_slot.boots['attack']}", True, WHITE)
        defense_text = get_bold_font(25).render(f"Defense: {player_slot.boots['defense']}", True, WHITE)
        crit_chance_text = get_bold_font(25).render(f"Critical Chance: {player_slot.boots['crit_chance']} %", True,
                                                    WHITE)
        crit_damage_text = get_bold_font(25).render(f"Critical Damage: {player_slot.boots['crit_damage']} %", True,
                                                    WHITE)
        magic_find_text = get_bold_font(25).render(f"Magic Find: {round(player_slot.boots['magic_find'] * 100, 2)} %",
                                                   True, WHITE)
        show_player_slot_helper(text1, level_text, type_text, life_text, attack_text, defense_text,
                                crit_chance_text, crit_damage_text, magic_find_text)
    elif gear_type == 'ring1':
        text1 = get_bold_font(35).render(f"{player_slot.ring1['name']}", True, WHITE)
        level_text = get_regular_font(25).render(f"Level {player_slot.ring1['level']}", True, WHITE)
        type_text = get_bold_font(25).render(f"Type: {player_slot.ring1['type']}", True, WHITE)
        life_text = get_bold_font(25).render(f"Life: {player_slot.ring1['life']}", True, WHITE)
        attack_text = get_bold_font(25).render(f"Attack: {player_slot.ring1['attack']}", True, WHITE)
        defense_text = get_bold_font(25).render(f"Defense: {player_slot.ring1['defense']}", True, WHITE)
        crit_chance_text = get_bold_font(25).render(f"Critical Chance: {player_slot.ring1['crit_chance']} %", True,
                                                    WHITE)
        crit_damage_text = get_bold_font(25).render(f"Critical Damage: {player_slot.ring1['crit_damage']} %", True,
                                                    WHITE)
        magic_find_text = get_bold_font(25).render(f"Magic Find: {round(player_slot.ring1['magic_find'] * 100, 2)} %",
                                                   True, WHITE)
        show_player_slot_helper(text1, level_text, type_text, life_text, attack_text, defense_text,
                                crit_chance_text, crit_damage_text, magic_find_text)

    elif gear_type == 'ring2':
        text1 = get_bold_font(35).render(f"{player_slot.ring2['name']}", True, WHITE)
        level_text = get_regular_font(25).render(f"Level {player_slot.ring2['level']}", True, WHITE)
        type_text = get_bold_font(25).render(f"Type: {player_slot.ring2['type']}", True, WHITE)
        life_text = get_bold_font(25).render(f"Life: {player_slot.ring2['life']}", True, WHITE)
        attack_text = get_bold_font(25).render(f"Attack: {player_slot.ring2['attack']}", True, WHITE)
        defense_text = get_bold_font(25).render(f"Defense: {player_slot.ring2['defense']}", True, WHITE)
        crit_chance_text = get_bold_font(25).render(f"Critical Chance: {player_slot.ring2['crit_chance']} %", True,
                                                    WHITE)
        crit_damage_text = get_bold_font(25).render(f"Critical Damage: {player_slot.ring2['crit_damage']} %", True,
                                                    WHITE)
        magic_find_text = get_bold_font(25).render(f"Magic Find: {round(player_slot.ring2['magic_find'] * 100, 2)} %",
                                                   True, WHITE)
        show_player_slot_helper(text1, level_text, type_text, life_text, attack_text, defense_text,
                                crit_chance_text, crit_damage_text, magic_find_text)
    elif gear_type == 'weapon':
        text1 = get_bold_font(35).render(f"{player_slot.weapon['name']}", True, WHITE)
        level_text = get_regular_font(25).render(f"Level {player_slot.weapon['level']}", True, WHITE)
        type_text = get_bold_font(25).render(f"Type: {player_slot.weapon['type']}", True, WHITE)
        life_text = get_bold_font(25).render(f"Life: {player_slot.weapon['life']}", True, WHITE)
        attack_text = get_bold_font(25).render(f"Attack: {player_slot.weapon['attack']}", True, WHITE)
        defense_text = get_bold_font(25).render(f"Defense: {player_slot.weapon['defense']}", True, WHITE)
        crit_chance_text = get_bold_font(25).render(f"Critical Chance: {player_slot.weapon['crit_chance']} %", True,
                                                    WHITE)
        crit_damage_text = get_bold_font(25).render(f"Critical Damage: {player_slot.weapon['crit_damage']} %", True,
                                                    WHITE)
        magic_find_text = get_bold_font(25).render(f"Magic Find: {round(player_slot.weapon['magic_find'] * 100, 2)} %",
                                                   True, WHITE)
        show_player_slot_helper(text1, level_text, type_text, life_text, attack_text, defense_text,
                                crit_chance_text, crit_damage_text, magic_find_text)

    elif gear_type == 'helmet':
        text1 = get_bold_font(35).render(f"{player_slot.helmet['name']}", True, WHITE)
        level_text = get_regular_font(25).render(f"Level {player_slot.helmet['level']}", True, WHITE)
        type_text = get_bold_font(25).render(f"Type: {player_slot.helmet['type']}", True, WHITE)
        life_text = get_bold_font(25).render(f"Life: {player_slot.helmet['life']}", True, WHITE)
        attack_text = get_bold_font(25).render(f"Attack: {player_slot.helmet['attack']}", True, WHITE)
        defense_text = get_bold_font(25).render(f"Defense: {player_slot.helmet['defense']}", True, WHITE)
        crit_chance_text = get_bold_font(25).render(f"Critical Chance: {player_slot.helmet['crit_chance']} %", True,
                                                    WHITE)
        crit_damage_text = get_bold_font(25).render(f"Critical Damage: {player_slot.helmet['crit_damage']} %", True,
                                                    WHITE)
        magic_find_text = get_bold_font(25).render(f"Magic Find: {round(player_slot.helmet['magic_find'] * 100, 2)} %",
                                                   True, WHITE)
        show_player_slot_helper(text1, level_text, type_text, life_text, attack_text, defense_text,
                                crit_chance_text, crit_damage_text, magic_find_text)


def show_player_slot_helper(text1, level_text, type_text, life_text, attack_text, defense_text,
                            crit_chance_text, crit_damage_text, magic_find_text):
    text1_rect = text1.get_rect(midleft=(100, 160))
    level_text_rect = level_text.get_rect(midleft=(100, 200))
    type_text_rect = type_text.get_rect(midleft=(100, 260))
    life_text_rect = life_text.get_rect(midleft=(100, 300))
    attack_text_rect = attack_text.get_rect(midleft=(100, 340))
    defense_text_rect = defense_text.get_rect(midleft=(100, 380))
    crit_chance_text_rect = crit_chance_text.get_rect(midleft=(100, 420))
    crit_damage_text_rect = crit_damage_text.get_rect(midleft=(100, 460))
    magic_find_text_rect = magic_find_text.get_rect(midleft=(100, 500))
    SCREEN.blit(text1, text1_rect)
    SCREEN.blit(type_text, type_text_rect)
    SCREEN.blit(level_text, level_text_rect)
    SCREEN.blit(life_text, life_text_rect)
    SCREEN.blit(attack_text, attack_text_rect)
    SCREEN.blit(defense_text, defense_text_rect)
    SCREEN.blit(crit_chance_text, crit_chance_text_rect)
    SCREEN.blit(crit_damage_text, crit_damage_text_rect)
    SCREEN.blit(magic_find_text, magic_find_text_rect)