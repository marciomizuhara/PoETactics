from objects.enemy import Enemy


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
