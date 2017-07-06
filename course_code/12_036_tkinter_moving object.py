import tkinter

tk = tkinter.Tk()

canvas = tkinter.Canvas(tk, width = 500, height = 500)
canvas.pack()

triangle = canvas.create_polygon(10, 10, 10, 60, 50, 35)

canvas.itemconfig(triangle, fill = 'blue', outline = 'red')

def move_triangle(event):
    if event.keysym == 'Up':
        canvas.move(triangle, 0, -3)
    if event.keysym == 'Down':
        canvas.move(triangle, 0, 3)
    if event.keysym == 'Left':
        canvas.move(triangle, -3, 0)
    if event.keysym == 'Right':
        canvas.move(triangle, 3, 0)

canvas.bind_all('<KeyPress-Up>', move_triangle)
canvas.bind_all('<KeyPress-Down>', move_triangle)
canvas.bind_all('<KeyPress-Left>', move_triangle)
canvas.bind_all('<KeyPress-Right>', move_triangle)

tk.mainloop()
