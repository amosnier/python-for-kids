import tkinter

tk = tkinter.Tk()

canvas = tkinter.Canvas(tk, width = 500, height = 500)
canvas.pack()

canvas.create_polygon(1, 1, 101, 1, 201, 101, 201, 201, fill = 'orange', outline = 'black')

tk.mainloop()
