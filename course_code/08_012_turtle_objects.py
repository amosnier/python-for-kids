# Turtle is the name of a class.
# Several "instances" of that class can live at the same time.

import turtle
bob = turtle.Turtle()
bob.forward(300)
alice = turtle.Turtle()
alice.forward(200)
alice.left(90)
alice.forward(100)
john = turtle.Turtle()
john.forward(200)
john.left(225)
john.forward(100)
turtle.done()
