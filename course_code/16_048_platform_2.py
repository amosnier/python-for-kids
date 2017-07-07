import tkinter
import time
from enum import Enum, auto

tk = tkinter.Tk()

class Man:
    class Direction(Enum):
        NONE = auto()
        LEFT = auto()
        RIGHT = auto()
        
    def __init__(self, canvas, moving_dx, moving_dy):
        self.canvas = canvas
        self.moving_dx = moving_dx
        self.moving_dy = moving_dy
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
        self.trying_to_jump = False
        self.jump_counter = 0
        self.canvas.bind_all('<KeyPress-Left>', self.on_left_pressed)
        self.canvas.bind_all('<KeyPress-Right>', self.on_right_pressed)
        self.canvas.bind_all('<KeyRelease-Left>', self.on_left_released)
        self.canvas.bind_all('<KeyRelease-Right>', self.on_right_released)
        self.canvas.bind_all('<KeyPress-space>', self.on_space_pressed)
        self.canvas.bind_all('<KeyRelease-space>', self.on_space_released)

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

    def on_space_pressed(self, event):
        self.trying_to_jump = True

    def on_space_released(self, event):
        self.trying_to_jump = False

    def move(self):
        coords = self.coords()
        dx = self.unobstructed_dx()
        dx = self.corrected_dx(dx, coords)
        dy = self.unobstructed_dy(coords)
        dy = self.corrected_dy(dy, coords)
        self.canvas.move(self.id, dx, dy)
        self.animate(dx)

    def unobstructed_dx(self):
        if self.direction == Man.Direction.LEFT:
            return -self.moving_dx
        elif self.direction == Man.Direction.RIGHT:
            return self.moving_dx
        else:
            return 0

    def corrected_dx(self, dx, coords):
        new_dx = max(dx, -coords[0])
        new_dx = min(new_dx, self.canvas_width - coords[2])
        return new_dx

    def unobstructed_dy(self, coords):
        self.jump_counter = self.updated_jump_counter(coords)
        if self.jump_counter > 0:
            return -self.moving_dy # moving up
        else:
            return self.moving_dy # moving down

    def corrected_dy(self, dy, coords):
        new_dy = min(dy, self.canvas_height - coords[3])
        return new_dy

    def updated_jump_counter(self, coords):
        if self.trying_to_jump and coords[3] >= self.canvas_height:
            return 12 # start the jumping down-counter
        if self.jump_counter > 0: # if jumping, decrease jumping steps left.
            return self.jump_counter - 1
        else:
            return 0

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

man = Man(canvas, 6, 8)

def handle_timer_event():
    man.move()
    tk.after(20, handle_timer_event)

handle_timer_event()
tk.mainloop()
