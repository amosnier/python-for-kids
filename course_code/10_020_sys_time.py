import sys
print(sys.version)

def print_numbers(max_number):
    for x in range(0, max_number):
        print(x)

import time
t = time.time()
print_numbers(1000)
print(t)
print("The function print_numbers took %s seconds to run" % (time.time() - t))
print()

print(time.asctime())
print(time.localtime())
print(time.localtime().tm_year)
print(time.localtime().tm_mon)
print()

for x in range(0, 6):
    print(x)
    time.sleep(1)
print()

