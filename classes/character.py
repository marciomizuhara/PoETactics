from classes.enemy import Enemy
from enemies import characters
print(characters.characters_list)


class Character(Enemy):

    def __init__(self, name, total_life, life, attack, defense, level, xp, crit_chance, status, quote1, quote2, quote3,
                 quote4, image):
        super().__init__(name, total_life, life, attack, defense, level, xp, crit_chance)
        self.status = status
        self.quote1 = quote1
        self.quote2 = quote2
        self.quote3 = quote3
        self.quote4 = quote4
        self.image = image


# Boss instances:
wiegraf1 = Character(
    name=characters.characters_list['Wiegraf 1']['name'],
    total_life=characters.characters_list['Wiegraf 1']['life'],
    life=characters.characters_list['Wiegraf 1']['life'],
    attack=characters.characters_list['Wiegraf 1']['attack'],
    defense=characters.characters_list['Wiegraf 1']['defense'],
    level=characters.characters_list['Wiegraf 1']['level'],
    xp=characters.characters_list['Wiegraf 1']['xp'],
    crit_chance=characters.characters_list['Wiegraf 1']['crit_chance'],
    status=characters.characters_list['Wiegraf 1']['status'],
    quote1=characters.characters_list['Wiegraf 1']['quote1'],
    quote2=characters.characters_list['Wiegraf 1']['quote2'],
    quote3=characters.characters_list['Wiegraf 1']['quote3'],
    quote4=characters.characters_list['Wiegraf 1']['quote4'],
    image=characters.characters_list['Wiegraf 1']['image']
)
dycedarg1 = Character(
    name=characters.characters_list['Dycedarg 1']['name'],
    total_life=characters.characters_list['Dycedarg 1']['life'],
    life=characters.characters_list['Dycedarg 1']['life'],
    attack=characters.characters_list['Dycedarg 1']['attack'],
    defense=characters.characters_list['Dycedarg 1']['defense'],
    level=characters.characters_list['Dycedarg 1']['level'],
    xp=characters.characters_list['Dycedarg 1']['xp'],
    crit_chance=characters.characters_list['Dycedarg 1']['crit_chance'],
    status=characters.characters_list['Dycedarg 1']['status'],
    quote1=characters.characters_list['Dycedarg 1']['quote1'],
    quote2=characters.characters_list['Dycedarg 1']['quote2'],
    quote3=characters.characters_list['Dycedarg 1']['quote3'],
    quote4=characters.characters_list['Dycedarg 1']['quote4'],
    image=characters.characters_list['Dycedarg 1']['image']
)
wiegraf2 = Character(
    name=characters.characters_list['Wiegraf 2']['name'],
    total_life=characters.characters_list['Wiegraf 2']['life'],
    life=characters.characters_list['Wiegraf 2']['life'],
    attack=characters.characters_list['Wiegraf 2']['attack'],
    defense=characters.characters_list['Wiegraf 2']['defense'],
    level=characters.characters_list['Wiegraf 2']['level'],
    xp=characters.characters_list['Wiegraf 2']['xp'],
    crit_chance=characters.characters_list['Wiegraf 2']['crit_chance'],
    status=characters.characters_list['Wiegraf 2']['status'],
    quote1=characters.characters_list['Wiegraf 2']['quote1'],
    quote2=characters.characters_list['Wiegraf 2']['quote2'],
    quote3=characters.characters_list['Wiegraf 2']['quote3'],
    quote4=characters.characters_list['Wiegraf 2']['quote4'],
    image=characters.characters_list['Wiegraf 2']['image']
)
dycedarg2 = Character(
    name=characters.characters_list['Dycedarg 2']['name'],
    total_life=characters.characters_list['Dycedarg 2']['life'],
    life=characters.characters_list['Dycedarg 2']['life'],
    attack=characters.characters_list['Dycedarg 2']['attack'],
    defense=characters.characters_list['Dycedarg 2']['defense'],
    level=characters.characters_list['Dycedarg 2']['level'],
    xp=characters.characters_list['Dycedarg 2']['xp'],
    crit_chance=characters.characters_list['Dycedarg 2']['crit_chance'],
    status=characters.characters_list['Dycedarg 2']['status'],
    quote1=characters.characters_list['Dycedarg 2']['quote1'],
    quote2=characters.characters_list['Dycedarg 2']['quote2'],
    quote3=characters.characters_list['Dycedarg 2']['quote3'],
    quote4=characters.characters_list['Dycedarg 2']['quote4'],
    image=characters.characters_list['Dycedarg 2']['image']
)