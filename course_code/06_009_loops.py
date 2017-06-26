print(list(range(0, 5)))
for x in range(0, 5):
    print("Loops repeat things.")
    print("Hello,", x)
lang_list = ['Python', 'C', 'C++', 'Java', 'Javascript']
for lang in lang_list:
    print("I love programming in", lang)
for lang in lang_list:
    print("I love programming in", lang)
    print("Actually, I wish I knew how to program in", lang)

x = 0
x += 1
print(x)
x += 2
print(x)

cards = list(range(1, 11)) + ['jack', 'queen', 'king']
print(cards)
nr_combinations = 0
for card1 in cards:
    print("Combinations for card one =", card1)
    for card2 in cards:
        nr_combinations += 1
        print("Combination %s: %s and %s" % (nr_combinations, card1, card2))

week_money = 20
accumulated = 0
for week in range(1, 53):
    accumulated += week_money
    print("week %s: %s" % (week, accumulated))
print("total =", week_money * 52)

accumulated = 0
week = 0
while accumulated < 2000:
    week += 1
    accumulated += week_money
    print("week %s: %s" % (week, accumulated))

accumulated = 0
week = 0
while True:
    week += 1
    accumulated += week_money
    print("week %s: %s" % (week, accumulated))
    if accumulated >= 2000:
        break

x = 45
y = 80
while x < 50 and y < 100:
    x += 1
    y += 1
    print(x, y)
