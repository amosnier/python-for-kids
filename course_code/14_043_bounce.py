import tkinter
import random

class Ball:
    def __init__(self, canvas, color, normal_move, paddle):
        self.canvas = canvas
        self.paddle = paddle
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
        self.hit_bottom = False

    def move(self):
        self.canvas.move(self.id, self.dx, self.dy)
        self.check_for_paddle()
        self.check_for_walls()

    def check_for_walls(self):
        coords = self.canvas.coords(self.id)
        if coords[0] <= 0:
            self.dx = self.normal_move
        if coords[1] <= 0:
            self.dy = self.normal_move
        if coords[2] >= self.canvas_width:
            self.dx = -self.normal_move
        if coords[3] >= self.canvas_height:
            self.hit_bottom = True
            
    def check_for_paddle(self):
        coords = self.canvas.coords(self.id)
        paddle_coords = self.paddle.coords()
        if (coords[0] >= paddle_coords[0] and coords[2] <= paddle_coords[2] and
            coords[3] >= paddle_coords[1] and coords[3] <= paddle_coords[3]):
            self.dy = -self.normal_move

class Paddle:
    def __init__(self, canvas, color, normal_move):
        self.canvas = canvas
        self.normal_move = normal_move
        self.canvas_width = self.canvas.winfo_width()
        self.canvas_height = self.canvas.winfo_height()
        self.size_x = 100
        self.size_y = 10
        start_x = self.canvas_width / 2
        start_y = self.canvas_height - 50
        self.id = canvas.create_rectangle(start_x, start_y, start_x + self.size_x, start_y + self.size_y, fill=color)
        self.canvas.bind_all('<KeyPress-Left>', self.turn_left)
        self.canvas.bind_all('<KeyPress-Right>', self.turn_right)
        self.dx = 0
        
    def turn_left(self, event):
        self.dx = -self.normal_move
            
    def turn_right(self, event):
        self.dx = self.normal_move

    def move(self):
        self.check_for_walls()
        self.canvas.move(self.id, self.dx, 0)

    def check_for_walls(self):
        coords = self.canvas.coords(self.id)
        if (coords[0] + self.dx) <= 0 or (coords[2] + self.dx) >= self.canvas_width:
            self.dx = 0

    def coords(self):
        return self.canvas.coords(self.id)

tk = tkinter.Tk()
tk.title("Bounce")
tk.resizable(0, 0)
canvas = tkinter.Canvas(tk, width=500, height=400)
canvas.pack()
tk.update() # necessary for winfo_xxx functions to work

paddle = Paddle(canvas, 'blue', 4)
ball = Ball(canvas, 'red', 6, paddle)

def handle_timer_event():
    if not ball.hit_bottom:
        ball.move()
        paddle.move()
    tk.after(20, handle_timer_event)

handle_timer_event()
tk.mainloop()
