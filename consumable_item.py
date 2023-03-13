from items.consumables import *
class ConsumableItem:

    def __init__(self, type, name, value, quantity, rarity, code, sound):
        self.type = type
        self.name = name
        self.value = value
        self.quantity = quantity
        self.rarity = rarity
        self.code = code
        self.sound = sound


# Consumables intances:
potion = ConsumableItem(consumables['potion']['type'], consumables['potion']['name'],
                        consumables['potion']['value'], consumables['potion']['quantity'],
                        consumables['potion']['rarity'], consumables['potion']['code'],
                        consumables['potion']['sound'])
hi_potion = ConsumableItem(consumables['hi-potion']['type'], consumables['hi-potion']['name'],
                           consumables['hi-potion']['value'], consumables['hi-potion']['quantity'],
                           consumables['hi-potion']['rarity'], consumables['hi-potion']['code'],
                           consumables['hi-potion']['sound'])
x_potion = ConsumableItem(consumables['x-potion']['type'], consumables['x-potion']['name'],
                          consumables['x-potion']['value'], consumables['x-potion']['quantity'],
                          consumables['x-potion']['rarity'], consumables['x-potion']['code'],
                          consumables['x-potion']['sound'])
elixir = ConsumableItem(consumables['elixir']['type'], consumables['elixir']['name'],
                        consumables['elixir']['value'], consumables['elixir']['quantity'],
                        consumables['elixir']['rarity'], consumables['elixir']['code'],
                        consumables['elixir']['sound'])
chaos_orb = ConsumableItem(consumables['chaos orb']['type'], consumables['chaos orb']['name'],
                           consumables['chaos orb']['value'], consumables['chaos orb']['quantity'],
                           consumables['chaos orb']['rarity'], consumables['chaos orb']['code'],
                           consumables['chaos orb']['sound'])
divine_orb = ConsumableItem(consumables['divine orb']['type'], consumables['divine orb']['name'],
                            consumables['divine orb']['value'], consumables['divine orb']['quantity'],
                            consumables['divine orb']['rarity'], consumables['divine orb']['code'],
                            consumables['divine orb']['sound'])
exalted_orb = ConsumableItem(consumables['exalted orb']['type'], consumables['exalted orb']['name'],
                             consumables['exalted orb']['value'], consumables['exalted orb']['quantity'],
                             consumables['exalted orb']['rarity'], consumables['exalted orb']['code'],
                             consumables['exalted orb']['sound'])
mirror_of_kalandra = ConsumableItem(consumables['mirror of kalandra']['type'],
                                    consumables['mirror of kalandra']['name'],
                                    consumables['mirror of kalandra']['value'],
                                    consumables['mirror of kalandra']['quantity'],
                                    consumables['mirror of kalandra']['rarity'],
                                    consumables['mirror of kalandra']['code'],
                                    consumables['mirror of kalandra']['sound'])
roulette_wheel_ticket = ConsumableItem(consumables['roulette_wheel_ticket']['type'],
                                       consumables['roulette_wheel_ticket']['name'],
                                       consumables['roulette_wheel_ticket']['value'],
                                       consumables['roulette_wheel_ticket']['quantity'],
                                       consumables['roulette_wheel_ticket']['rarity'],
                                       consumables['roulette_wheel_ticket']['code'],
                                       consumables['roulette_wheel_ticket']['sound'])
