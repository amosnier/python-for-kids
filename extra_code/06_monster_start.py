class Monster:
    def __init__(self, name, race = 'Monster', health = 100):
        self.name = name
        self.max_health = health
        self.health = health
        self.race = race
        
    def greet(self):
        print('Hello, my name is %s and I am a monster of race %s' % (self.name, self.race))

monster1 = Monster('John', 'orc')
monster1.greet()

monster2 = Monster('Carl', 'zombie')
monster2.greet()

bob = Monster('Bob', 'creeper')
bob.greet()

alice = Monster('Alice', 'ghast')
alice.greet()

dokemonduck = Monster('Dokemonduck', 'blaze')
dokemonduck.greet()
