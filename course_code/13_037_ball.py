import tkinter

tk = tkinter.Tk()

tk.title("Bounce")
tk.resizable(0, 0)

width = 500
height = 400
canvas = tkinter.Canvas(tk, width=width, height=height)
# Remove border. Apparently no effect on Linux, but good on Mac
canvas.configure(bd=0)
# Make the 0 horizontal and vertical line apparent
canvas.configure(highlightthickness=0)
canvas.pack()

ball = canvas.create_oval(10, 10, 25, 25, fill='red')

tk.mainloop()
