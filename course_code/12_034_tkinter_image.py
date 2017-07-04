import tkinter

tk = tkinter.Tk()

canvas = tkinter.Canvas(tk, width = 500, height = 500)
canvas.pack()

image = tkinter.PhotoImage(file = 'gif/example.gif')
canvas.create_image(1, 1, anchor = tkinter.NW, image = image)

tk.mainloop()
