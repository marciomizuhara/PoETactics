import pygame, random
from assets.fonts.fonts import *
from assets.music.music import *
from classes import encounter
from classes import player_
from classes import player_status_
from settings import *
from classes import battle


ESSENCE_DROP_RATE = 0
essences_applied = []


class Essence:
    def __init__(self, name, attribute, modifier):
        self.name = name
        self.attribute = attribute
        self.modifier = modifier


essences_list = [
    Essence("Essence of Contempt", "attack", 0.5),
    Essence("Essence of Dread", "defense", 0.5),
    Essence("Essence of Fear", "life", 0.5),
    Essence("Essence of Loathing", "crit_chance", 0.5),
]


def essence_effect(enemy_image):
    new_image = battle.transform_image_color(pygame.image.load(enemy_image), PINK)
    new_image.set_alpha(70)
    return new_image


def apply_essence(enemy):
    essence = random.choice(essences_list)
    if essence.name == 'Essence of Contempt':
        enemy.attack += round(enemy.attack * essence.modifier)
    elif essence.name == 'Essence of Dread':
        enemy.defense += round(enemy.defense * essence.modifier)
    elif essence.name == 'Essence of Fear':
        enemy.total_life += round(enemy.total_life + essence.modifier)
        enemy.life = enemy.total_life
    elif essence.name == 'Essence of Loathing':
        enemy.crit_chance += round(enemy.crit_chance + essence.modifier)
    essences_applied.append(essence)
    if len(essences_applied) < 4:
        roll = random.randint(0, 100)
        if roll <= 70:
            apply_essence(enemy)
    return enemy


def is_essence(enemy):
    roll = random.randint(0, 100)
    print(roll)
    if roll <= ESSENCE_DROP_RATE:
        enemy = apply_essence(enemy)
        enemy.essence = True
        essence_encounter_sound()
        return enemy
    else:
        return enemy

