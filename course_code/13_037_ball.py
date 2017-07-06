import tkinter

tk = tkinter.Tk()

tk.title("Bounce")
tk.resizable(0, 0)
width = 500
height = 400
canvas = tkinter.Canvas(tk, width=width, height=height)
canvas.pack()

ball = canvas.create_oval(10, 10, 25, 25, fill='red')

tk.mainloop()
