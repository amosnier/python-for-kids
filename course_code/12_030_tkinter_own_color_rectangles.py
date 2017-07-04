import tkinter
import random

tk = tkinter.Tk()

width = 500
height = 500

canvas = tkinter.Canvas(tk, width = width, height = 500)
canvas.pack()

def draw_random_rectangle(fill_color):
    x1 = random.randint(1, width)
    y1 = random.randrange(1, height)
    x2 = x1 + random.randint(0, width - x1)
    y2 = y1 + random.randint(0, height - y1)
    canvas.create_rectangle(x1, y1, x2, y2, fill=fill_color)

#import tkinter.colorchooser
#tkinter.colorchooser.askcolor()

draw_random_rectangle('#fc7619')
draw_random_rectangle('#d961d9')
draw_random_rectangle('#79ffd9')
    
tk.mainloop()
