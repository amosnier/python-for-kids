import tkinter

tk = tkinter.Tk()

canvas = tkinter.Canvas(tk, width = 500, height = 500)
canvas.pack()

canvas.create_line(1, 1, 500, 500)
canvas.create_rectangle(10, 10, 50, 50)
canvas.create_rectangle(70, 10, 300, 50)
canvas.create_rectangle(10, 70, 50, 500)

tk.mainloop()
