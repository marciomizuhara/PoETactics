import pygame, time
from cs50 import SQL
from items import amulets, armors, boots, gloves, helmets, legs, rings, second_hands, weapons

db = SQL("sqlite:///../database.db")

# Define player
username = 'Mizuhara1'

slot = input('Insert the slot you want to populate: ')

if slot == 'amulet':
    item = amulets.amulet_type[0]
    db.execute(
        f"INSERT INTO amulet (username, name, type, level, life, attack, defense, crit_chance,"
        "crit_damage, magic_find, rarity, crafted, image) VALUES (:username, :name, :type, :level, :life, :attack, :defense,"
        ":crit_chance, :crit_damage, :magic_find, :rarity, :crafted, :image)",
        username=username, name=item['name'], type=item['type'],
        level=item['level'], life=item['life'],
        attack=item['attack'], defense=item['defense'],
        crit_chance=item['crit_chance'], crit_damage=item['crit_damage'],
        magic_find=item['magic_find'], rarity=item['rarity'], crafted=item['crafted'], image=item['image'])
    print(f'{slot} populated!')

if slot == 'armor':
    item = armors.armor_type[0]
    db.execute(
        f"INSERT INTO armor (username, name, type, level, life, attack, defense, crit_chance,"
        "crit_damage, magic_find, rarity, crafted, image) VALUES (:username, :name, :type, :level, :life, :attack, :defense,"
        ":crit_chance, :crit_damage, :magic_find, :rarity, :crafted, :image)",
        username=username, name=item['name'], type=item['type'],
        level=item['level'], life=item['life'],
        attack=item['attack'], defense=item['defense'],
        crit_chance=item['crit_chance'], crit_damage=item['crit_damage'],
        magic_find=item['magic_find'], rarity=item['rarity'], crafted=item['crafted'], image=item['image'])
    print(f'{slot} populated!')

if slot == 'boots':
    item = boots.boots_type[0]
    db.execute(
        f"INSERT INTO boots (username, name, type, level, life, attack, defense, crit_chance,"
        "crit_damage, magic_find, rarity, crafted, image) VALUES (:username, :name, :type, :level, :life, :attack, :defense,"
        ":crit_chance, :crit_damage, :magic_find, :rarity, :crafted, :image)",
        username=username, name=item['name'], type=item['type'],
        level=item['level'], life=item['life'],
        attack=item['attack'], defense=item['defense'],
        crit_chance=item['crit_chance'], crit_damage=item['crit_damage'],
        magic_find=item['magic_find'], rarity=item['rarity'], crafted=item['crafted'], image=item['image'])
    print(f'{slot} populated!')

if slot == 'gloves':
    item = gloves.gloves_type[0]
    db.execute(
        f"INSERT INTO gloves (username, name, type, level, life, attack, defense, crit_chance,"
        "crit_damage, magic_find, rarity, crafted, image) VALUES (:username, :name, :type, :level, :life, :attack, :defense,"
        ":crit_chance, :crit_damage, :magic_find, :rarity, :crafted, :image)",
        username=username, name=item['name'], type=item['type'],
        level=item['level'], life=item['life'],
        attack=item['attack'], defense=item['defense'],
        crit_chance=item['crit_chance'], crit_damage=item['crit_damage'],
        magic_find=item['magic_find'], rarity=item['rarity'], crafted=item['crafted'], image=item['image'])
    print(f'{slot} populated!')

if slot == 'helmet':
    item = helmets.helmet_type[0]
    db.execute(
        f"INSERT INTO helmet (username, name, type, level, life, attack, defense, crit_chance,"
        "crit_damage, magic_find, rarity, crafted, image) VALUES (:username, :name, :type, :level, :life, :attack, :defense,"
        ":crit_chance, :crit_damage, :magic_find, :rarity, :crafted, :image)",
        username=username, name=item['name'], type=item['type'],
        level=item['level'], life=item['life'],
        attack=item['attack'], defense=item['defense'],
        crit_chance=item['crit_chance'], crit_damage=item['crit_damage'],
        magic_find=item['magic_find'], rarity=item['rarity'], crafted=item['crafted'], image=item['image'])
    print(f'{slot} populated!')

if slot == 'legs':
    item = legs.legs_type[0]
    db.execute(
        f"INSERT INTO legs (username, name, type, level, life, attack, defense, crit_chance,"
        "crit_damage, magic_find, rarity, crafted, image) VALUES (:username, :name, :type, :level, :life, :attack, :defense,"
        ":crit_chance, :crit_damage, :magic_find, :rarity, :crafted, :image)",
        username=username, name=item['name'], type=item['type'],
        level=item['level'], life=item['life'],
        attack=item['attack'], defense=item['defense'],
        crit_chance=item['crit_chance'], crit_damage=item['crit_damage'],
        magic_find=item['magic_find'], rarity=item['rarity'], crafted=item['crafted'], image=item['image'])
    print(f'{slot} populated!')

if slot == 'ring1':
    item = rings.ring_type[0]
    db.execute(
        f"INSERT INTO ring1 (username, name, type, level, life, attack, defense, crit_chance,"
        "crit_damage, magic_find, rarity, crafted, image) VALUES (:username, :name, :type, :level, :life, :attack, :defense,"
        ":crit_chance, :crit_damage, :magic_find, :rarity, :crafted, :image)",
        username=username, name=item['name'], type=item['type'],
        level=item['level'], life=item['life'],
        attack=item['attack'], defense=item['defense'],
        crit_chance=item['crit_chance'], crit_damage=item['crit_damage'],
        magic_find=item['magic_find'], rarity=item['rarity'], crafted=item['crafted'], image=item['image'])
    print(f'{slot} populated!')

if slot == 'ring2':
    item = rings.ring_type[0]
    db.execute(
        f"INSERT INTO ring2 (username, name, type, level, life, attack, defense, crit_chance,"
        "crit_damage, magic_find, rarity, crafted, image) VALUES (:username, :name, :type, :level, :life, :attack, :defense,"
        ":crit_chance, :crit_damage, :magic_find, :rarity, :crafted, :image)",
        username=username, name=item['name'], type=item['type'],
        level=item['level'], life=item['life'],
        attack=item['attack'], defense=item['defense'],
        crit_chance=item['crit_chance'], crit_damage=item['crit_damage'],
        magic_find=item['magic_find'], rarity=item['rarity'], crafted=item['crafted'], image=item['image'])
    print(f'{slot} populated!')

if slot == 'second_hand':
    item = second_hands.second_hand_type[0]
    db.execute(
        f"INSERT INTO second_hand (username, name, type, level, life, attack, defense, crit_chance,"
        "crit_damage, magic_find, rarity, crafted, image) VALUES (:username, :name, :type, :level, :life, :attack, :defense,"
        ":crit_chance, :crit_damage, :magic_find, :rarity, :crafted, :image)",
        username=username, name=item['name'], type=item['type'],
        level=item['level'], life=item['life'],
        attack=item['attack'], defense=item['defense'],
        crit_chance=item['crit_chance'], crit_damage=item['crit_damage'],
        magic_find=item['magic_find'], rarity=item['rarity'], crafted=item['crafted'], image=item['image'])
    print(f'{slot} populated!')

if slot == 'weapon':
    item = weapons.weapon_type[0]
    db.execute(
        f"INSERT INTO weapon (username, name, type, level, life, attack, defense, crit_chance,"
        "crit_damage, magic_find, rarity, crafted, image) VALUES (:username, :name, :type, :level, :life, :attack, :defense,"
        ":crit_chance, :crit_damage, :magic_find, :rarity, :crafted, :image)",
        username=username, name=item['name'], type=item['type'],
        level=item['level'], life=item['life'],
        attack=item['attack'], defense=item['defense'],
        crit_chance=item['crit_chance'], crit_damage=item['crit_damage'],
        magic_find=item['magic_find'], rarity=item['rarity'], crafted=item['crafted'], image=item['image'])
    print(f'{slot} populated!')