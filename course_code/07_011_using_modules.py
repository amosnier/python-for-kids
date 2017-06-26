import time
print(time.asctime())

#import sys
#name = sys.stdin.readline() # does not work with IPython under SPyder
def greet():
    name = input("What's your name? ")
    age = input("How old are you? ")
    print("Hello %s, you are %s years old." % (name, age))
    
for i in range(0,5):
    greet()
