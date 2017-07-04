import tkinter
import time

tk = tkinter.Tk()

canvas = tkinter.Canvas(tk, width = 500, height = 500)
canvas.pack()

triangle = canvas.create_polygon(10, 10, 10, 60, 50, 35)
print(triangle)
for x in range(0, 60):
   canvas.move(triangle, 5, 0)
   tk.update()
   time.sleep(0.05)

tk.mainloop()
