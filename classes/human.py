from classes.enemy import Enemy


class Human(Enemy):

    def __init__(self, name, total_life, life, attack, defense, level, xp, crit_chance, image, essence):
        super().__init__(name, total_life, life, attack, defense, level, xp, crit_chance, essence)
        self.image = image
