class Hero():
    def __init__(self, name, health, armor):
        self.name = name
        self.health = health
        self.armor = armor
    def print_info(self):
        print('Уровень здоровья:', self.health)
        print('Уровень брони:', self.armor, '\n')
