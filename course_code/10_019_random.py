import random

print(random.randint(1, 100))
print(random.randint(100, 1000))
print(random.randint(1000, 5000))
print()

desserts = ['ice cream', 'pancakes', 'brownies', 'cookies', 'candy']
print(random.choice(desserts))
random.shuffle(desserts)
print(desserts)
print()

number = random.randint(1, 100)
print('Guess a number between 1 and 100')
while True:
    guess = input()
    i = int(guess)
    if i == number:
        print('You guessed right')
        break
    elif i < number:
        print('Try higher')
    elif i > number:
        print('Try lower')
