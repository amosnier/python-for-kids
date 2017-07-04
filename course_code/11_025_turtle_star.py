import turtle
t = turtle.Pen()

def draw_star(size, red, green, blue, filled):
    t.down()
    t.color(red, green, blue)
    if filled == True:
        t.begin_fill()
    for x in range(1, 19):
        t.forward(size)
        if x % 2 == 0:
            t.left(175)
        else:
            t.right(135)
    if filled == True:
        t.end_fill()
    t.up()
        
draw_star(100, 1, 0, 0, True)
t.forward(200)
draw_star(50, 0.5, 0.5, 0, True)
t.forward(200)

turtle.done()
