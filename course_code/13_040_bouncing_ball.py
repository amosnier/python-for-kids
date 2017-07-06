import tkinter
import random
#import time

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
        self.canvas.move(self.id, self.dx, self.dy)
        self.check_for_walls()

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

tk = tkinter.Tk()
tk.title("Bounce")
tk.resizable(0, 0)
canvas = tkinter.Canvas(tk, width=500, height=400)
canvas.pack()
tk.update() # necessary for winfo_xxx functions to work

ball = Ball(canvas, 'red', 6)

#i = 0

def handle_timer_event():
    ball.move()
    tk.after(20, handle_timer_event)
#    global i
#    i += 1
#    one_second = 1000 / 20
#    if i >= one_second:
#        print(time.asctime())
#        i = 0

handle_timer_event()
tk.mainloop()

# Alternative in case of timing issues
# Note: it crashes when closing the window!
#while True:
#    ball.move()
#    tk.update_idletasks()
#    tk.update()
#    time.sleep(0.01)
