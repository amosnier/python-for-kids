import turtle

#turtle.tracer(0, 0)

t = turtle.Pen()

t.up()
t.backward(300)
t.down()

for x in range(1, 5):
    t.forward(50)
    t.left(90)

t.up()
t.backward(150)
t.down()

for x in range(1, 9):
    t.forward(100)
    t.right(135)
        
t.up()
t.forward(400)
t.down()

for x in range(1, 73):
    t.forward(200)
    t.right(95)
        
t.up()
t.forward(300)
t.down()

for x in range(1, 73):
    t.forward(400)
    t.right(175)
        
t.up()
t.backward(100)
t.left(90)
t.forward(100)
t.down()

for x in range(1, 19):
    t.forward(100)
    if x % 2 == 0:
        t.left(175)
    else:
        t.right(135)
        
turtle.update()
turtle.done()
