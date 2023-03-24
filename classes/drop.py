import random
from settings import *
from classes import consumable_item_
from classes import item_
from classes import inventory
from classes import player_
from classes import player_slot_
from classes import unique
from items.amulets import *
from items.armors import *
from items.boots import *
from items.gloves import *
from items.helmets import *
from items.legs import *
from items.rings import *
from items.second_hands import *
from items.gear_type import *
from items.uniques import *
from items.weapons import *


temp_gear_drop = []
temp_unique_drop = []
temp_consumable_drop = []
temp_ticket_drop = []
drop_quantity = 1


def gear_drop_rate():
    drop_rate_value = random.randint(0, 100)
    if drop_rate_value <= GEAR_DROP_RATE + (GEAR_DROP_RATE * player_.player.magic_find):
        if len(inventory.inventory) >= 150:
            pass
        else:
            enemy_gear_drop()
    else:
        pass


def enemy_gear_drop():
    drop = random.choice(gear_type)
    item_type = []
    """
    UNDER DEVELOPMENT
    """
    # MAKE SURE ITEM DROPPED DOES NOT EXCEED 2 COPIES OF A SAME ITEM IN THE INVENTORY:
    # temp_duplicates = []
    # for item in inventory:
    #     if item_type[0]['name'] == item_.__dict__['name']:
    #         temp_duplicates.append(item_.__dict__['name'])
    # try:
    #     if item_type[0]['name'] in temp_duplicates and temp_duplicates.count(item_type[0]['name']) >= 2:
    #         temp_duplicates.clear()
    #         enemy_gear_drop()
    # except:
    #     pass
    # temp_duplicates.clear()
    """
    UNDER DEVELOPMENT
    """
    if drop == 'weapon':
        item_drop = item_.item_level_random_setter(weapon_type)
        item_type.append(item_drop)
    elif drop == 'amulet':
        item_drop = item_.item_level_random_setter(amulet_type)
        item_type.append(item_drop)
    elif drop == 'armor':
        item_drop = item_.item_level_random_setter(armor_type)
        item_type.append(item_drop)
    elif drop == 'boots':
        item_drop = item_.item_level_random_setter(boots_type)
        item_type.append(item_drop)
    elif drop == 'gloves':
        item_drop = item_.item_level_random_setter(gloves_type)
        item_type.append(item_drop)
    elif drop == 'helmet':
        item_drop = item_.item_level_random_setter(helmet_type)
        item_type.append(item_drop)
    elif drop == 'legs':
        item_drop = item_.item_level_random_setter(legs_type)
        item_type.append(item_drop)
    elif drop == 'ring':
        item_drop = item_.item_level_random_setter(ring_type)
        item_type.append(item_drop)
    elif drop == 'second_hand':
        item_drop = item_.item_level_random_setter(second_hand_type)
        item_type.append(item_drop)
    else:
        pass

    new_item = item_.Item(item_type[0]['type'],
                    item_type[0]['name'],
                    item_type[0]['level'],
                    item_type[0]['life'],
                    item_type[0]['attack'],
                    item_type[0]['defense'],
                    item_type[0]['crit_chance'],
                    item_type[0]['crit_damage'],
                    item_type[0]['magic_find'],
                    item_type[0]['rarity'],
                    item_type[0]['crafted'],
                    item_type[0]['image'],
                    )

    inventory.inventory.append(new_item)
    temp_gear_drop.append(new_item)
    inventory.inventory_update(player_.player.name, new_item)
    inventory.inventory_limit()


def consumable_drop_rate():
    consumable_drop_rate_value = random.randint(0, 100)
    print(f'com magic find {CONSUMABLE_DROP_RATE + (player_.player.magic_find * 100)}')
    if consumable_drop_rate_value <= CONSUMABLE_DROP_RATE + (CONSUMABLE_DROP_RATE * player_.player.magic_find):
        enemy_consumable_drop()
    else:
        pass


def enemy_consumable_drop():
    global drop_quantity

    drop = random.randint(0, 100)
    quantity = random.randint(0, 100)
    ticket_drop = random.randint(0, 100)

    if quantity >= 95:
        drop_quantity += 2
    elif 75 <= quantity < 95:
        drop_quantity += 1
    else:
        pass

    if 0 <= drop < 70:
        if 10 < player_.player.level < 15:
            consumable_item_.hi_potion.quantity += drop_quantity
            temp_consumable_drop.append(consumable_item_.hi_potion)
        elif 15 <= player_.player.level < 18:
            consumable_item_.x_potion.quantity += drop_quantity
            temp_consumable_drop.append(consumable_item_.x_potion)
        elif 18 <= player_.player.level < 20:
            drop2 = random.randint(0, 100)
            if drop2 < 50:
                consumable_item_.x_potion.quantity += drop_quantity
                temp_consumable_drop.append(consumable_item_.x_potion)
            else:
                consumable_item_.elixir.quantity += drop_quantity
                temp_consumable_drop.append(consumable_item_.elixir)
        elif player_.player.level == 20:
            consumable_item_.elixir.quantity += drop_quantity
            temp_consumable_drop.append(consumable_item_.elixir)
        else:
            consumable_item_.potion.quantity += drop_quantity
            temp_consumable_drop.append(consumable_item_.potion)
            # consumable_item_.mirror_of_kalandra.quantity = consumable_item_.mirror_of_kalandra.quantity + 1
            # temp_consumable_drop.append(consumable_item_.mirror_of_kalandra)
    elif 70 <= drop < 78:
        consumable_item_.hi_potion.quantity += drop_quantity
        temp_consumable_drop.append(consumable_item_.hi_potion)
    elif 78 <= drop < 85:
        consumable_item_.x_potion.quantity += drop_quantity
        temp_consumable_drop.append(consumable_item_.x_potion)
    elif 85 <= drop < 91:
        consumable_item_.elixir.quantity += drop_quantity
        temp_consumable_drop.append(consumable_item_.elixir)
    elif 91 <= drop < 94:
        consumable_item_.chaos_orb.quantity += drop_quantity
        temp_consumable_drop.append(consumable_item_.chaos_orb)
    elif 94 <= drop < 97:
        consumable_item_.divine_orb.quantity += drop_quantity
        temp_consumable_drop.append(consumable_item_.divine_orb)
    elif 97 <= drop <= 99:
        consumable_item_.exalted_orb.quantity += drop_quantity
        temp_consumable_drop.append(consumable_item_.exalted_orb)
    else:
        random2 = random.randint(0, 100)
        if random2 <= 80:
            consumable_item_.exalted_orb.quantity += drop_quantity
            temp_consumable_drop.append(consumable_item_.exalted_orb)
        else:
            consumable_item_.mirror_of_kalandra.quantity += 1
            temp_consumable_drop.append(consumable_item_.mirror_of_kalandra)
    if ticket_drop < TICKET_DROP_RATE:
        consumable_item_.roulette_wheel_ticket.quantity += 1
        temp_ticket_drop.append(consumable_item_.roulette_wheel_ticket)


def unique_drop_rate():
    drop_rate_value = random.randint(0, 100)
    if len(list(set(unique.uniques_list))) >= 9:
        pass
    else:
        if drop_rate_value <= UNIQUE_DROP_RATE + (UNIQUE_DROP_RATE * player_.player.magic_find):
            drop = random.choice(uniques)
            inventory_uniques = [value for elem in inventory.inventory for value in elem.__dict__.values()]
            if drop['name'] in inventory_uniques:
                if drop['name'] in unique.uniques_list:
                    pass
                else:
                    unique.uniques_list.append(drop['name'])
                unique_drop_rate()
            elif drop['name'] == player_slot_.player_slot.amulet['name'] or drop['name'] == player_slot_.player_slot.armor['name'] or drop[
                'name'] == \
                    player_slot_.player_slot.boots['name'] or drop['name'] == player_slot_.player_slot.gloves['name'] or drop['name'] == \
                    player_slot_.player_slot.helmet['name'] or drop['name'] == player_slot_.player_slot.legs['name'] or drop['name'] == \
                    player_slot_.player_slot.ring1['name'] or drop['name'] == player_slot_.player_slot.ring2['name'] or drop['name'] == \
                    player_slot_.player_slot.second_hand['name'] or drop['name'] == player_slot_.player_slot.weapon['name']:
                if drop['name'] in unique.uniques_list:
                    pass
                else:
                    unique.uniques_list.append(drop['name'])
                unique_drop_rate()
            else:
                new_item = unique.Unique(drop['type'],
                                  drop['name'],
                                  drop['level'],
                                  drop['life'],
                                  drop['attack'],
                                  drop['defense'],
                                  drop['crit_chance'],
                                  drop['crit_damage'],
                                  drop['magic_find'],
                                  drop['rarity'],
                                  drop['crafted'],
                                  drop['image'],
                                  )
                if drop['name'] in unique.uniques_list:
                    pass
                else:
                    unique.uniques_list.append(drop['name'])
                inventory.inventory.append(new_item)
                db.execute("INSERT INTO uniques_list (username, name) VALUES (:username, :name)",
                           username=player_.player.name, name=drop['name'])
                inventory.inventory_update(player_.player.name, new_item)
                temp_unique_drop.append(new_item)