from main import *
import globals_variables


class Card:

    def __init__(self, type, name, status, image, sound):
        self.type = type
        self.name = name
        self.status = status
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
                    status=drop['status'],
                    image=drop['image'],
                    sound=drop['sound'],
                    )
    print('new card', new_card)
    globals_variables.temp_card_drop.append(new_card)
    globals_variables.cards_list.append(new_card)
    card_update(username, new_card)


def card_update(username, card):
    db.execute(
        "INSERT INTO cards_list (username, type, name, status, image, sound)"
        "VALUES (:username, :type, :name, :status, :image, :sound)",
        username=username, type=card.type, name=card.name,
        status=card.status, image=card.image, sound=card.sound)
