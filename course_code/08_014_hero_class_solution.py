class Hero:
    def __init__(self, name, health = 100, wealth = 500, race = 'hero'):
        self.name = name
        self.max_health = health
        self.health = health
        self.race = race
        self.wealth = wealth
    def report_health(self):
        print("%s: my health is %s" % (self.name, self.health))
    def report_wealth(self):
        print("%s: my wealth is %s" % (self.name, self.wealth))
    def greet(self):
        print("Hi, my name is %s, and I am a hero!" % self.name)
        self.info_race()
        self.report_health()
        self.report_wealth()
    def info_race(self):
        print("%s: actually, I am a(n) %s!" % (self.name, self.race))
    def hit(self, points):
        if (self.health > points):
            self.health -= points
        else:
            self.health = 0
    def heal(self, points):
        self.health += points
        if (self.health > self.max_health):
            self.health = self.max_health
    def spend(self, amount):
        if (self.wealth > amount):
            self.wealth -= amount
        else:
            self.wealth = 0
    def earn(self, amount):
        self.wealth += amount

bob = Hero('Bob')
bob.greet()
print()

class Elf(Hero):
    def __init__(self, name):
        Hero.__init__(self, name, 75, race = 'elf')
    def greet(self):
        Hero.greet(self)
        
bob = Elf("Bob")
bob.greet()
print()

class Dwarf(Hero):
    def __init__(self, name):
        Hero.__init__(self, name, 200, race = 'dwarf')
    def greet(self):
        Hero.greet(self)

alice = Dwarf("Alice")
alice.greet()
print()

class Human(Hero):
    def __init__(self, name):
        Hero.__init__(self, name, race = 'human')
    def greet(self):
        Hero.greet(self)

john = Human("John")
john.greet()
print()

bob.hit(10)
bob.report_health()
bob.heal(100)
bob.report_health()
print()

john.spend(100)
john.report_wealth()
john.earn(20000)
john.report_wealth()
