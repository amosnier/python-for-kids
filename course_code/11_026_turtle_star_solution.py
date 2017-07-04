import turtle
t = turtle.Pen()

def draw_star(size, nr_points, sharpness, red, green, blue, filled):
    if sharpness < 0:
        sharpness = 0
    if sharpness > 1:
        sharpness = 1
    t.down()
    t.color(red, green, blue)
    if filled == True:
        t.begin_fill()
    angle = 360 / nr_points
    for x in range(0, nr_points):
        t.forward(size)
        point_angle = 90 * (1 + sharpness)
        t.right(point_angle - angle)
        t.forward(size)
        t.left(point_angle)
    if filled == True:
        t.end_fill()
    t.up()
        
draw_star(50, 9, 1, 1, 0, 0, True)
t.forward(200)
draw_star(50, 9, 0.5, 0, 1, 0, True)
t.forward(200)
draw_star(50, 9, 0, 0, 0, 1, True)
t.forward(200)
draw_star(50, 9, 0.9, 1, 1, 0, True)
t.forward(200)

turtle.done()

