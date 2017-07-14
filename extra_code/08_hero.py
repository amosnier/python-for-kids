class Hero:
    def __init__(self, name, race = 'hero', health = 100, wealth = 500):
        self.name = name
        self.max_health = health
        self.health = health
        self.race = race
        self.wealth = wealth
        
    def greet(self):
        print('Hello, my name is %s and I am a hero of race %s, my health is %s' % (self.name, self.race, self.health))

    def report_health(self):
        print('%s, health: %s' % (self.name, self.health))

    def hit(self, points):
        if (self.health > points):
            self.health -= points
        else:
            self.health = 0

    def heal(self, points):
        self.health += points
        if (self.health > self.max_health):
            self.health = self.max_health

    def report_wealth(self):
        print('%s, wealth: %s' % (self.name, self.wealth))

    def spend(self, coins):
            self.wealth -= coins

    def earn(self, coins):
        self.wealth += coins

class Dwarf(Hero):
    def __init__(self, name):
        Hero.__init__(self, name, 'dwarf', 150, 300)

class Human(Hero):
    def __init__(self, name):
        Hero.__init__(self, name, 'human', 150)

class Elf(Hero):
    def __init__(self, name):
        Hero.__init__(self, name, 'elf', 200, 700)

john = Hero('John')
john.greet()
john.report_wealth()

hero2 = Dwarf('Carl')
hero2.greet()
hero2.report_wealth()

bob = Human('Bob')
bob.greet()
bob.report_wealth()

dokemonduck = Elf('Dokemonduck')
dokemonduck.greet()
dokemonduck.report_wealth()

bob.hit(200)
bob.report_health()
bob.heal(20)
bob.report_health()

bob.spend(100)
bob.report_wealth()
bob.spend(1000)
bob.report_wealth()
bob.earn(700)
bob.report_wealth()
