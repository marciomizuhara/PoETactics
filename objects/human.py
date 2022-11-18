from objects.enemy import Enemy


class Human(Enemy):

    def __init__(self, name, total_life, life, attack, defense, level, xp, crit_chance, image):
        super().__init__(name, total_life, life, attack, defense, level, xp, crit_chance)
        self.image = image