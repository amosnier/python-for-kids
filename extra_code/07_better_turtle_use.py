import turtle
turtle.clearscreen()
t = turtle.Turtle()

turtle.tracer(0, 0)

t.up()
t.goto(-350, 100)
t.down()

t.fillcolor('violet')

t.begin_fill()

for i in range(100, 0, -1):
    angle = 145
    t.forward(angle * i / 20)
    t.right(angle)
    
t.end_fill()

t.hideturtle()

turtle.update()
