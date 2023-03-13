from enemies.characters import *
from enemy import Enemy


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


def set_boss_instances():
    global wiegraf1, dycedarg1, wiegraf2, dycedarg2
    wiegraf1 = Character(
                name=characters['Wiegraf 1']['name'],
                total_life=characters['Wiegraf 1']['life'],
                life=characters['Wiegraf 1']['life'],
                attack=characters['Wiegraf 1']['attack'],
                defense=characters['Wiegraf 1']['defense'],
                level=characters['Wiegraf 1']['level'],
                xp=characters['Wiegraf 1']['xp'],
                crit_chance=characters['Wiegraf 1']['crit_chance'],
                status=characters['Wiegraf 1']['status'],
                quote1=characters['Wiegraf 1']['quote1'],
                quote2=characters['Wiegraf 1']['quote2'],
                quote3=characters['Wiegraf 1']['quote3'],
                quote4=characters['Wiegraf 1']['quote4'],
                image=characters['Wiegraf 1']['image']
            )
    dycedarg1 = Character(
        name=characters['Dycedarg 1']['name'],
        total_life=characters['Dycedarg 1']['life'],
        life=characters['Dycedarg 1']['life'],
        attack=characters['Dycedarg 1']['attack'],
        defense=characters['Dycedarg 1']['defense'],
        level=characters['Dycedarg 1']['level'],
        xp=characters['Dycedarg 1']['xp'],
        crit_chance=characters['Dycedarg 1']['crit_chance'],
        status=characters['Dycedarg 1']['status'],
        quote1=characters['Dycedarg 1']['quote1'],
        quote2=characters['Dycedarg 1']['quote2'],
        quote3=characters['Dycedarg 1']['quote3'],
        quote4=characters['Dycedarg 1']['quote4'],
        image=characters['Dycedarg 1']['image']
    )
    wiegraf2 = Character(
        name=characters['Wiegraf 2']['name'],
        total_life=characters['Wiegraf 2']['life'],
        life=characters['Wiegraf 2']['life'],
        attack=characters['Wiegraf 2']['attack'],
        defense=characters['Wiegraf 2']['defense'],
        level=characters['Wiegraf 2']['level'],
        xp=characters['Wiegraf 2']['xp'],
        crit_chance=characters['Wiegraf 2']['crit_chance'],
        status=characters['Wiegraf 2']['status'],
        quote1=characters['Wiegraf 2']['quote1'],
        quote2=characters['Wiegraf 2']['quote2'],
        quote3=characters['Wiegraf 2']['quote3'],
        quote4=characters['Wiegraf 2']['quote4'],
        image=characters['Wiegraf 2']['image']
    )
    dycedarg2 = Character(
        name=characters['Dycedarg 2']['name'],
        total_life=characters['Dycedarg 2']['life'],
        life=characters['Dycedarg 2']['life'],
        attack=characters['Dycedarg 2']['attack'],
        defense=characters['Dycedarg 2']['defense'],
        level=characters['Dycedarg 2']['level'],
        xp=characters['Dycedarg 2']['xp'],
        crit_chance=characters['Dycedarg 2']['crit_chance'],
        status=characters['Dycedarg 2']['status'],
        quote1=characters['Dycedarg 2']['quote1'],
        quote2=characters['Dycedarg 2']['quote2'],
        quote3=characters['Dycedarg 2']['quote3'],
        quote4=characters['Dycedarg 2']['quote4'],
        image=characters['Dycedarg 2']['image']
    )
    return wiegraf1, dycedarg1, wiegraf2, dycedarg2


def load_boss_instances(username):
    # boss instance
    row_boss_instance = db.execute("SELECT * FROM boss_instance WHERE username = :username", username=username)
    if row_boss_instance[0]['wiegraf1'] == 0:
        wiegraf1.status = False
    else:
        pass
    if row_boss_instance[0]['dycedarg1'] == 0:
        dycedarg1.status = False
    else:
        pass
    if row_boss_instance[0]['wiegraf2'] == 0:
        wiegraf2.status = False
    else:
        pass
    if row_boss_instance[0]['dycedarg2'] == 0:
        dycedarg2.status = False
    else:
        pass