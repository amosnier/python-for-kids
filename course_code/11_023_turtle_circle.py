import turtle

#turtle.tracer(0, 0)

t = turtle.Pen()

def fill_circle(red, green, blue):
    t.down()
    t.color(red, green, blue)
    t.begin_fill()
    t.circle(50)
    t.end_fill()
    t.up()
        
fill_circle(0, 0, 0)
t.forward(100)
fill_circle(1, 1, 1)
t.forward(100)
fill_circle(1, 0, 0)
t.forward(100)
fill_circle(0, 1, 0)
t.forward(100)
fill_circle(0, 0, 1)
t.forward(100)
fill_circle(0.5, 0, 0)
t.forward(100)
fill_circle(0, 0.5, 0)
t.forward(100)
fill_circle(0, 0, 0.5)
t.forward(100)

turtle.update()
turtle.done()
