import turtle
turtle.clearscreen()
t = turtle.Turtle()

#turtle.tracer(0, 0)

t.fillcolor(0.9, 0.9, 0.6)

t.begin_fill()

for i in range(0, 5):
    t.forward(100)
    t.right(144)
    
t.end_fill()

t.up()
t.backward(200)
t.down()

t.fillcolor(0.7, 0.95, 0.7)

t.begin_fill()

for i in range(0, 5):
    t.forward(100)
    t.left(72)
    
t.end_fill()

t.up()
t.right(90)
t.forward(200)
t.down()

t.fillcolor(0.7, 0.9, 0)

t.begin_fill()

for i in range(0, 6):
    t.forward(100)
    t.left(60)
    
t.end_fill()

t.up()
t.left(90)
t.forward(500)
t.down()

t.fillcolor(0.95, 0, 0.5)

t.begin_fill()

for i in range(100, 0, -1):
    t.forward(i)
    t.left(60)
    
t.end_fill()

t.up()
t.left(60)
t.backward(300)
t.down()

t.fillcolor(0.80, 0, 0.7)

t.begin_fill()

for i in range(60, 120):
    t.forward(180 - i)
    t.left(i)
    
t.end_fill()

turtle.update()
