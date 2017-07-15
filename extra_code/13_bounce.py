import tkinter
from enum import Enum, auto

class Ball:
    def __init__(self, canvas, racket, x, y, size, color, step_size):
        self.canvas = canvas
        self.step_size = step_size
        self.id = canvas.create_oval(x, y, x + size, y + size, fill=color)
        self.canvas_width = self.canvas.winfo_width()
        self.canvas_height = self.canvas.winfo_height()
        self.dx = self.step_size
        self.dy = self.step_size
        self.racket = racket
        self.lost = False
        self.x = x
        self.y = y
        self.size = size

        canvas.bind_all('<KeyPress-space>', self.on_space_pressed)

    def on_space_pressed(self, event):
        if self.lost:
            self.canvas.coords(self.id, self.x, self.y, self.x + self.size, self.y + self.size)
            self.lost = False

    def move(self):
        self.canvas.move(self.id, self.dx, self.dy)
        coords = self.canvas.coords(self.id)
        racket_coords = self.racket.coords()
        if self.racket_reached(coords, racket_coords):
            self.dy = -self.step_size
        if self.right_border_reached(coords):
            self.dx = -self.step_size
        if self.bottom_border_reached(coords):
            self.lost = True
        if self.left_border_reached(coords):
            self.dx = self.step_size
        if self.top_border_reached(coords):
            self.dy = self.step_size

    def right_border_reached(self, coords):
        return coords[2] > self.canvas_width

    def bottom_border_reached(self, coords):
        return coords[3] > self.canvas_height

    def left_border_reached(self, coords):
        return coords[0] < 0

    def top_border_reached(self, coords):
        return coords[1] < 0

    def racket_reached(self, ball_coords, racket_coords):
        return ball_coords[3] > racket_coords[1] and ball_coords[2] > racket_coords[0] and  ball_coords[0] < racket_coords[2]

    def is_lost(self):
        return self.lost

class Racket:
    class Direction(Enum):
        NONE = auto()
        LEFT = auto()
        RIGHT = auto()

    def __init__(self, canvas, x, y, x_size, y_size, color, step_size):
        self.canvas = canvas
        self.step_size = step_size
        self.id = canvas.create_rectangle(x, y, x + x_size, y + y_size, fill=color)
        self.canvas_width = self.canvas.winfo_width()
        self.direction = Racket.Direction.NONE

        canvas.bind_all('<KeyPress-Left>', self.on_left_pressed)
        canvas.bind_all('<KeyPress-Right>', self.on_right_pressed)
        canvas.bind_all('<KeyRelease-Left>', self.on_left_released)
        canvas.bind_all('<KeyRelease-Right>', self.on_right_released)

    def on_left_pressed(self, event):
        self.direction = Racket.Direction.LEFT

    def on_right_pressed(self, event):
        self.direction = Racket.Direction.RIGHT

    def on_left_released(self, event):
        if self.direction == Racket.Direction.LEFT:
            self.direction = Racket.Direction.NONE

    def on_right_released(self, event):
        if self.direction == Racket.Direction.RIGHT:
            self.direction = Racket.Direction.NONE

    def move(self):
        dx = 0
        if self.direction == Racket.Direction.LEFT:
            dx = -self.step_size
        elif self.direction == Racket.Direction.RIGHT:
            dx = self.step_size
        self.canvas.move(self.id, dx, 0)

    def coords(self):
        return self.canvas.coords(self.id)

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

racket = Racket(canvas, 250, 370, 80, 10, 'lightgreen', 3)
ball = Ball(canvas, racket, 100, 100, 15, 'coral', 5)

def handle_timer_event():
    if not ball.is_lost():
        ball.move()
        racket.move()
    tk.after(20, handle_timer_event)

handle_timer_event()

tk.mainloop()
