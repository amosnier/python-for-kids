import tkinter

class Ball:
    def __init__(self, canvas, x, y, size, color, step_size):
        self.canvas = canvas
        self.step_size = step_size
        self.id = canvas.create_oval(x, y, x + size, y + size, fill=color)
        self.canvas_width = self.canvas.winfo_width()
        self.canvas_height = self.canvas.winfo_height()
        self.dx = self.step_size
        self.dy = self.step_size
    
    def move(self):
        self.canvas.move(self.id, self.dx, self.dy)
        coords = self.canvas.coords(self.id)
        
    def right_border_reached(self, coords):
        return coords[2] > self.canvas_width
    
    def bottom_border_reached(self, coords):
        return coords[3] > self.canvas_height
    
    def left_border_reached(self, coords):
        return coords[0] < 0

    def top_border_reached(self, coords):
        return coords[1] < 0

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

tk.update() # necessary for winfo_xxx functions to work

ball = Ball(canvas, 100, 100, 25, 'coral', 2)

def handle_timer_event():
    ball.move()
    tk.after(20, handle_timer_event)

handle_timer_event()

tk.mainloop()
