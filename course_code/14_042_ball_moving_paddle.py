import tkinter
import random
from enum import Enum, auto

class Ball:
    def __init__(self, canvas, color, normal_move):
        self.canvas = canvas
        self.normal_move = normal_move
        self.canvas_width = self.canvas.winfo_width()
        self.canvas_height = self.canvas.winfo_height()
        diameter = 15
        start_x = self.canvas_width / 2
        start_y = self.canvas_height / 4
        self.id = canvas.create_oval(start_x, start_y, start_x + diameter, start_y + diameter, fill=color)
        little_move = normal_move / 3;
        medium_move = little_move * 2
        start_moves = [-normal_move, -medium_move, -little_move, little_move, medium_move, normal_move]
        rand_index = random.randrange(0, len(start_moves))
        self.dx = start_moves[rand_index]
        self.dy = -normal_move

    def move(self):
        self.check_for_walls()
        self.canvas.move(self.id, self.dx, self.dy)

    def check_for_walls(self):
        coords = self.canvas.coords(self.id)
        if coords[0] <= 0:
            self.dx = self.normal_move
        if coords[1] <= 0:
            self.dy = self.normal_move
        if coords[3] >= self.canvas_height:
            self.dy = -self.normal_move
        if coords[2] >= self.canvas_width:
            self.dx = -self.normal_move

class Paddle:
    class Direction(Enum):
        NONE = auto()
        LEFT = auto()
        RIGHT = auto()
        
    def __init__(self, canvas, color, normal_move):
        self.canvas = canvas
        self.normal_move = normal_move
        self.canvas_width = self.canvas.winfo_width()
        self.canvas_height = self.canvas.winfo_height()
        self.size_x = 100
        self.size_y = 10
        start_x = self.canvas_width / 2
        self.id = canvas.create_rectangle(start_x, self.canvas_height - self.size_y, start_x + self.size_x, self.canvas_height, fill=color)
        self.direction = Paddle.Direction.NONE
        self.canvas.bind_all('<KeyPress-Left>', self.on_left_pressed)
        self.canvas.bind_all('<KeyPress-Right>', self.on_right_pressed)
        self.canvas.bind_all('<KeyRelease-Left>', self.on_left_released)
        self.canvas.bind_all('<KeyRelease-Right>', self.on_right_released)
        
    def on_left_pressed(self, event):
        self.direction = Paddle.Direction.LEFT
        
    def on_right_pressed(self, event):
        self.direction = Paddle.Direction.RIGHT
        
    def on_left_released(self, event):
        if self.direction == Paddle.Direction.LEFT:
            self.direction = Paddle.Direction.NONE

    def on_right_released(self, event):
        if self.direction == Paddle.Direction.RIGHT:
            self.direction = Paddle.Direction.NONE

    def move(self):
        if self.direction == Paddle.Direction.LEFT:
            dx = -self.normal_move
        elif self.direction == Paddle.Direction.RIGHT:
            dx = self.normal_move
        else:
            dx = 0
        dx = self.dx_corrected_for_walls(dx)
        self.canvas.move(self.id, dx, 0)

    def dx_corrected_for_walls(self, dx):
        coords = self.canvas.coords(self.id)
        new_dx = max(dx, -coords[0])
        new_dx = min(new_dx, self.canvas_width - coords[2])
        return new_dx

tk = tkinter.Tk()
tk.title("Bounce")
tk.resizable(0, 0)
canvas = tkinter.Canvas(tk, width=500, height=400)
canvas.pack()
tk.update() # necessary for winfo_xxx functions to work

ball = Ball(canvas, 'red', 6)
paddle = Paddle(canvas, 'blue', 4)

def handle_timer_event():
    ball.move()
    paddle.move()
    tk.after(20, handle_timer_event)

handle_timer_event()
tk.mainloop()
