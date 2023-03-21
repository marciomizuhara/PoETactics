class Enemy:

    def __init__(self, name, total_life, life, attack, defense, level, xp, crit_chance, essence):
        self.name = name
        self.total_life = total_life
        self.life = life
        self.attack = attack
        self.defense = defense
        self.level = level
        self.xp = xp
        self.crit_chance = crit_chance
        self.essence = False
