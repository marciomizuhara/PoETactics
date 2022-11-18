from objects.consumable_item import ConsumableItem


class Fossil(ConsumableItem):

    def __init__(self, type, name, value, quantity, rarity, code, sound, attribute):
        super().__init__(type, name, value, quantity, rarity, code, sound)
        self.attribute = attribute
