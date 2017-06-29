print(abs(-10))
print(abs(10))
print()

def is_large(x):
#    return x > 10000 or x < -10000
    return abs(x) > 10000

print(is_large(0))
print(is_large(5))
print(is_large(20000))
print(is_large(-100000))
print()

# A boolean is True or False
# When converting objects to a boolean, pretty much anything that is
# not zero or empty is True.

print(bool(0))
print(bool(1))
print(bool(-1))
print(bool(-10000))
print()

print(bool([]))
print(bool(['This', 'list', 'is', 'not', 'empty']))
print()

print(len(''))
print(len('Longer string'))
print(len([1, 2, 3]))
print()

s = ''
#while len(s) == 0:
#while not len(s):
#while not s:
#    s = input("Enter something: ")
print(s)
print()

# What can I do on a list
print(dir([]))
print()

# Let's try
l1 = []
l1.append(1)
print(l1)
l1.extend([1, 2])
print(l1)
l2 = l1
l3 = l1.copy()
l1.clear()
print(l1)
print(l2)
print(l3)
print(l3.count(1))
print(l3.index(2))
print(l3.index(1))
l3.insert(1, 3)
print(l3)
l3.reverse()
print(l3)
l3.sort()
print(l3)
l1 = l3.copy()
print(l3.pop())
print(l3.pop())
print(l3)
print(l1)
l1.remove(1)
print(l1)
l1.remove(1)
print(l1)
print()

print(float('123.456'))
#print(int('123.456'))
print(int(float('123.456')))
print()

print(min(3, 4))
print(max(3, 4))
print(min(['Great', 'a', 'bli', 'bla']))
print(max(['Great', 'a', 'bli', 'bla']))
print(max('String'))
print()

print(range(0, 5))
print(list(range(0, 5)))
print(list(range(0, 30, 2)))
print(list(range(30, 0, -2)))
print()

print(sum([2, 3, 5]))
print(sum(range(0, 6)))
print()
