import tkinter

tk = tkinter.Tk()

canvas = tkinter.Canvas(tk, width = 500, height = 500)
canvas.pack()

canvas.create_arc(1, 1, 500, 500, extent = 359.99, style = tkinter.ARC)
canvas.create_arc(51, 51, 450, 450, extent = 180, style = tkinter.ARC)
canvas.create_arc(101, 101, 400, 400, extent = 90, style = tkinter.ARC)
canvas.create_arc(151, 151, 350, 350, extent = 45, style = tkinter.ARC)
canvas.create_arc(51, 251, 450, 450, extent = 359.99, style = tkinter.ARC)

tk.mainloop()
