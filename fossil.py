from consumable_item import ConsumableItem
from items.consumables import *


class Fossil(ConsumableItem):

    def __init__(self, type, name, value, quantity, rarity, code, sound, attribute):
        super().__init__(type, name, value, quantity, rarity, code, sound)
        self.attribute = attribute


# Fossiles
dense_fossil = Fossil(consumables['dense fossil']['type'],
                      consumables['dense fossil']['name'],
                      consumables['dense fossil']['value'],
                      consumables['dense fossil']['quantity'],
                      consumables['dense fossil']['rarity'],
                      consumables['dense fossil']['code'],
                      consumables['dense fossil']['sound'],
                      consumables['dense fossil']['attribute'])
serrated_fossil = Fossil(consumables['serrated fossil']['type'],
                         consumables['serrated fossil']['name'],
                         consumables['serrated fossil']['value'],
                         consumables['serrated fossil']['quantity'],
                         consumables['serrated fossil']['rarity'],
                         consumables['serrated fossil']['code'],
                         consumables['serrated fossil']['sound'],
                         consumables['serrated fossil']['attribute'])
pristine_fossil = Fossil(consumables['pristine fossil']['type'],
                         consumables['pristine fossil']['name'],
                         consumables['pristine fossil']['value'],
                         consumables['pristine fossil']['quantity'],
                         consumables['pristine fossil']['rarity'],
                         consumables['pristine fossil']['code'],
                         consumables['pristine fossil']['sound'],
                         consumables['pristine fossil']['attribute'])
deft_fossil = Fossil(consumables['deft fossil']['type'],
                     consumables['deft fossil']['name'],
                     consumables['deft fossil']['value'],
                     consumables['deft fossil']['quantity'],
                     consumables['deft fossil']['rarity'],
                     consumables['deft fossil']['code'],
                     consumables['deft fossil']['sound'],
                     consumables['deft fossil']['attribute'])
fractured_fossil = Fossil(consumables['fractured fossil']['type'],
                          consumables['fractured fossil']['name'],
                          consumables['fractured fossil']['value'],
                          consumables['fractured fossil']['quantity'],
                          consumables['fractured fossil']['rarity'],
                          consumables['fractured fossil']['code'],
                          consumables['fractured fossil']['sound'],
                          consumables['fractured fossil']['attribute'])