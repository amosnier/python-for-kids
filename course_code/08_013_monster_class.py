class Monster:
    def __init__(self, name, health = 100, race = 'monster'):
        self.name = name
        self.max_health = health
        self.health = health
        self.race = race
    def report_health(self):
        print("%s: my health is %s" % (self.name, self.health))
    def greet(self):
        print("Hi, my name is %s, and I am a monster!" % self.name)
        self.info_race()
        self.report_health()
    def info_race(self):
        print("%s: actually, I am a %s!" % (self.name, self.race))
    def hit(self, points):
        if (self.health > points):
            self.health -= points
        else:
            self.health = 0
    def heal(self, points):
        self.health += points
        if (self.health > self.max_health):
            self.health = self.max_health

bob = Monster('Bob')
bob.greet()
print()

class Zombie(Monster):
    def __init__(self, name):
        Monster.__init__(self, name, 75, 'zombie')
        
bob = Zombie("Bob")
bob.greet()
print()

class Goblin(Monster):
    def __init__(self, name):
        Monster.__init__(self, name, 200, 'goblin')

alice = Goblin("Alice")
alice.greet()
print()

class Troll(Monster):
    def __init__(self, name):
        Monster.__init__(self, name, race = 'troll')

john = Troll("John")
john.greet()
print()

bob.hit(10)
bob.report_health()
bob.heal(100)
bob.report_health()
