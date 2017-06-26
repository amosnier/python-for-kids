def greet(name):
    print('Hello, %s!' % name)

greet('Loïc')
greet('Freja')
greet('Jalle')
greet('Liam')

def accumulated_pocket_money(week_money, nr_weeks, spent_per_week):
    left_per_week = week_money - spent_per_week
    return left_per_week * nr_weeks

def print_accumulated(week_money = 100, nr_weeks = 52, spent_per_week = 0):
    print("Accumulated money for %s weeks: %s" % (nr_weeks, accumulated_pocket_money(week_money, nr_weeks, spent_per_week)))

print_accumulated(20, 52)
print_accumulated(100, 4)
print_accumulated(100, 4, 20)
print_accumulated()
#print(left_per_week)

name = 'Peter' # Global variable
def greet_name():
    print('Hello, %s!' % name)
greet_name()

def angles(nr_angles):
    angle_step = 360.0 / nr_angles
    angle = 0
    angle_list = []
    for i in range(0, nr_angles):
        angle_list.append(angle)
        angle += angle_step
    return angle_list

def print_angles(nr_angles = 8):
    print('List of angles for %s steps: %s' % (nr_angles, angles(nr_angles)))

print_angles()
print_angles(10)
print_angles(16)
