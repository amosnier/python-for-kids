import turtle
t = turtle.Turtle()

def draw_polygon_or_star(x, y, n, fc, pc, star):
    t.up()
    t.goto(x, y)
    t.setheading(0)
    t.down()
    
    t.fillcolor(fc)
    t.pencolor(pc)
    angle = 360 / n
    length = 100 / n * 5
    if star:
        angle *= 2
    else:
        length /= 2
    t.begin_fill()
    for i in range(0, n):
        t.forward(length)
        t.left(angle)
    t.end_fill()


#draw_polygon_or_star(-100, 0, 5, 'lightgreen', 'red', True)
#draw_polygon_or_star(100, 0, 7, 'lightblue', 'red', True)
#draw_polygon_or_star(0, -200, 9, 'violet', 'red', True)
#draw_polygon_or_star(0, 200, 11, 'blue', 'red', True)
#
#draw_polygon_or_star(-200, 0, 5, 'lightgreen', 'red', False)
#draw_polygon_or_star(200, 0, 7, 'lightblue', 'red', False)
#draw_polygon_or_star(-200, -200, 9, 'violet', 'red', False)
#draw_polygon_or_star(200, 200, 11, 'blue', 'red', False)

draw_polygon_or_star(0, -100, 20, 'red', 'red', False)
draw_polygon_or_star(0, 0, 20, 'green', 'red', False)
draw_polygon_or_star(0, 100, 20, 'blue', 'red', False)


turtle.done()
