import tkinter

tk = tkinter.Tk()
tk.title('Mr. Stickman races for the exit')
tk.resizable(0, 0)
canvas = tkinter.Canvas(tk, width=500, height=500)
canvas.pack()
tk.update()
background = tkinter.PhotoImage(file='gif/background.gif')
w = background.width()
h = background.height()
for x in range(0, 5):
    for y in range(0, 5):
        canvas.create_image(x * w, y * h, image=background, anchor='nw')

tk.mainloop()
