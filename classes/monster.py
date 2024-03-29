from classes.enemy import Enemy


class Monster(Enemy):

    def __init__(self, name, total_life, life, attack, defense, level, xp, crit_chance, delve_drop, image, essence):
        super().__init__(name, total_life, life, attack, defense, level, xp, crit_chance, essence)
        self.delve_drop = delve_drop
        self.image = image