import tkinter

class Ball:
    def __init__(self, canvas, x, y, size, color, step_size):
        self.canvas = canvas
        self.step_size = step_size
        self.id = canvas.create_oval(x, y, x + size, y + size, fill=color)
    
    def move(self):
        self.canvas.move(self.id, self.step_size, self.step_size)        


tk = tkinter.Tk()

tk.title("Bounce")
tk.resizable(0, 0)
# Keep the window on the top
tk.wm_attributes("-topmost", 1)
canvas = tkinter.Canvas(tk, width=500, height=400)
# Remove border. Apparently no effect on Linux, but good on Mac
canvas.configure(bd=0)
# Make the 0 horizontal and vertical line apparent
canvas.configure(highlightthickness=0)
canvas.pack()

ball1 = Ball(canvas, 100, 100, 25, 'coral', 5)
ball2 = Ball(canvas, 0, 100, 25, 'turquoise', 2)
ball3 = Ball(canvas, 100, 0, 25, 'violet', 3)

def handle_timer_event():
    ball1.move()
    ball2.move()
    ball3.move()
    tk.after(20, handle_timer_event)

handle_timer_event()

tk.mainloop()
