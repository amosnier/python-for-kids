class Monster:
    def __init__(self, name, race = 'monster', health = 100):
        self.name = name
        self.max_health = health
        self.health = health
        self.race = race
        
    def greet(self):
        print('Hello, my name is %s and I am a monster of race %s, my health is %s' % (self.name, self.race, self.health))

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

class Zombie(Monster):
    def __init__(self, name):
        Monster.__init__(self, name, 'zombie', 150)

class Creeper(Monster):
    def __init__(self, name):
        Monster.__init__(self, name, 'creeper', 150)

class Ghast(Monster):
    def __init__(self, name):
        Monster.__init__(self, name, 'ghast', 100)
        self.invisible = False
    def make_invisible(self):
        self.invisible = True
    def report_invisible(self):
        if self.invisible:
            print('%s is invisible' % self.name)
        else:
            print('%s is not invisible' % self.name)

class Blaze(Monster):
    def __init__(self, name):
        Monster.__init__(self, name, 'blaze', 200)

monster1 = Monster('John')
monster1.greet()

monster2 = Zombie('Carl')
monster2.greet()

bob = Creeper('Bob')
bob.greet()

alice = Ghast('Alice')
alice.greet()

dokemonduck = Blaze('Dokemonduck')
dokemonduck.greet()

alice.hit(25)
alice.report_health()
alice.report_invisible()
alice.make_invisible()
alice.report_invisible()

bob.hit(200)
bob.report_health()
bob.heal(20)
bob.report_health()
