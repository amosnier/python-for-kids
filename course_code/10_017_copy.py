class Character:
    def __init__(self, name):
        self.name = name
        self.health = 100
    def hit(self, points):
        self.health -= points

bob = Character('Bob')
alice = bob
print(bob.health)
print(alice.health)
print()

bob.hit(20)
print(bob.health)
print(alice.health)
print()

import copy
alice = copy.copy(bob)
bob.hit(20)
print(bob.health)
print(alice.health)
print()

characters1 = [bob, alice]
characters2 = copy.copy(characters1)

bob.hit(20)
print(characters1[0].health)
print(characters1[1].health)
print(characters2[0].health)
print(characters2[1].health)
print()

characters1.append(bob)
print(characters1)
print(characters2)
print()
