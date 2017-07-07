import tkinter
import time
from enum import Enum, auto

tk = tkinter.Tk()

class Man:
    class Direction(Enum):
        NONE = auto()
        LEFT = auto()
        RIGHT = auto()
        
    def __init__(self, canvas, normal_move):
        self.canvas = canvas
        self.normal_move = normal_move
        self.canvas_width = self.canvas.winfo_width()
        self.canvas_height = self.canvas.winfo_height()
        self.size_x = 100
        self.size_y = 10
        start_x = self.canvas_width / 2
        start_y = self.canvas_height
        self.left_images = [tkinter.PhotoImage(file='gif/stick-L1.gif'),
                            tkinter.PhotoImage(file='gif/stick-L2.gif'),
                            tkinter.PhotoImage(file='gif/stick-L3.gif')]
        self.right_images = [tkinter.PhotoImage(file='gif/stick-R1.gif'),
                             tkinter.PhotoImage(file='gif/stick-R2.gif'),
                             tkinter.PhotoImage(file='gif/stick-R3.gif')]
        self.image_index = 0
        self.image_index_incr = 1
        self.image_time = time.time()
        self.id = canvas.create_image(start_x, start_y - self.left_images[0].height(), image=self.left_images[0], anchor='nw')
        self.direction = Man.Direction.NONE
        self.canvas.bind_all('<KeyPress-Left>', self.on_left_pressed)
        self.canvas.bind_all('<KeyPress-Right>', self.on_right_pressed)
        self.canvas.bind_all('<KeyRelease-Left>', self.on_left_released)
        self.canvas.bind_all('<KeyRelease-Right>', self.on_right_released)

    def on_left_pressed(self, event):
        self.direction = Man.Direction.LEFT
        
    def on_right_pressed(self, event):
        self.direction = Man.Direction.RIGHT
        
    def on_left_released(self, event):
        if self.direction == Man.Direction.LEFT:
            self.direction = Man.Direction.NONE

    def on_right_released(self, event):
        if self.direction == Man.Direction.RIGHT:
            self.direction = Man.Direction.NONE

    def move(self):
        if self.direction == Man.Direction.LEFT:
            dx = -self.normal_move
        elif self.direction == Man.Direction.RIGHT:
            dx = self.normal_move
        else:
            dx = 0
        dx = self.dx_corrected_for_walls(dx)
        self.canvas.move(self.id, dx, 0)
        self.animate(dx)

    def dx_corrected_for_walls(self, dx):
        coords = self.coords()
        new_dx = max(dx, -coords[0])
        new_dx = min(new_dx, self.canvas_width - coords[2])
        return new_dx

    def coords(self):
        coords = self.canvas.coords(self.id)
        return [coords[0], coords[1],
                coords[0] + self.left_images[0].width(), coords[1] + self.left_images[0].height()]

    def animate(self, dx):
        if (time.time() - self.image_time) < 0.1:
            return
        self.image_time = time.time()
        next = self.image_index + self.image_index_incr
        if (next < 0 or next >= len(self.left_images)):
            self.image_index_incr = -self.image_index_incr
            self.image_index += self.image_index_incr
        else:
            self.image_index = next
        if dx < 0:
            canvas.itemconfig(self.id, image=self.left_images[self.image_index])
        elif dx > 0:
            canvas.itemconfig(self.id, image=self.right_images[self.image_index])

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

man = Man(canvas, 6)

def handle_timer_event():
    man.move()
    tk.after(20, handle_timer_event)

handle_timer_event()
tk.mainloop()
