import tkinter
import time
from enum import Enum, auto

tk = tkinter.Tk()

def in_horizontal_contact(coords1, coords2):
    return coords1[2] >= coords2[0] and coords1[0] <= coords2[2]

def in_vertical_contact(coords1, coords2):
    return coords1[3] >= coords2[1] and coords1[1] <= coords2[3]

class Relative_position:
    def __init__(self, left, above, right, below):
        self.left = left
        self.above = above
        self.right = right
        self.below = below
        
    def jump_is_possible(self):
        return self.below <= 0

    def corrected_dx(self, dx):
        dx = max(dx, self.left)
        dx = min(dx, self.right)
        return dx

    def corrected_dy(self, dy):
        dy = max(dy, self.above)
        dy = min(dy, self.below)
        return dy

    def update_with_obstacle(self, item_coords, obstacle_coords):
        if in_vertical_contact(item_coords, obstacle_coords):
            if obstacle_coords[2] <= item_coords[0]:
                self.left = max(self.left, obstacle_coords[2] - item_coords[0])
            if obstacle_coords[0] >= item_coords[2]:
                self.right = min(self.right, obstacle_coords[0] - item_coords[2])
        if in_horizontal_contact(item_coords, obstacle_coords):
            if obstacle_coords[3] <= item_coords[1]:
                self.above = max(self.above, obstacle_coords[3] - item_coords[1])
            if obstacle_coords[1] >= item_coords[3]:
                self.below = min(self.below, obstacle_coords[1] - item_coords[3])

def position_relative_to_canvas(canvas, coords):
    return Relative_position(-coords[0], -coords[1], canvas.winfo_width() - coords[2], canvas.winfo_height() - coords[3])

class Platform:
    def __init__(self, canvas, platform_type, x, y):
        self.canvas = canvas
        self.canvas_width = self.canvas.winfo_width()
        self.canvas_height = self.canvas.winfo_height()
        self.image_files = ['gif/platform1.gif', 'gif/platform2.gif', 'gif/platform3.gif']
        self.image = tkinter.PhotoImage(file=self.image_files[platform_type])
        self.id = canvas.create_image(x, y, image=self.image, anchor='nw')

    def coords(self):
        coords = self.canvas.coords(self.id)
        return [coords[0], coords[1],
                coords[0] + self.image.width(), coords[1] + self.image.height()]

class Man:
    class Direction(Enum):
        NONE = auto()
        LEFT = auto()
        RIGHT = auto()
        
    def __init__(self, canvas, platforms, moving_dx, moving_dy):
        self.canvas = canvas
        self.platforms = platforms
        self.moving_dx = moving_dx
        self.moving_dy = moving_dy
        self.canvas_width = self.canvas.winfo_width()
        self.canvas_height = self.canvas.winfo_height()
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
        relative_position = position_relative_to_canvas(self.canvas, coords)
        for platform in self.platforms:
            relative_position.update_with_obstacle(coords, platform.coords())
        if self.direction == Man.Direction.LEFT:
            dx = -self.moving_dx
        elif self.direction == Man.Direction.RIGHT:
            dx = self.moving_dx
        else:
            dx = 0
        dx = relative_position.corrected_dx(dx)
        if self.trying_to_jump and relative_position.jump_is_possible():
            self.jump_counter = 12
        elif self.jump_counter > 0:
            self.jump_counter -= 1
        if self.jump_counter > 0:
            dy = -self.moving_dy
        else:
            dy = self.moving_dy
        dy = relative_position.corrected_dy(dy)
        # Handle the case were an obstacle might have stopped jumping
        if dy >= 0:
            self.jump_counter = 0
        self.canvas.move(self.id, dx, dy)
        self.animate(dx)

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

platforms = [Platform(canvas, 1, 100, 425),
             Platform(canvas, 0, 300, 425),
             Platform(canvas, 2, 50, 350),
             Platform(canvas, 0, 200, 350),
             Platform(canvas, 2, 400, 350),
             Platform(canvas, 0, 50, 275),
             Platform(canvas, 2, 200, 275),
             Platform(canvas, 0, 350, 275),
             Platform(canvas, 1, 200, 200),
             Platform(canvas, 1, 350, 200),
             Platform(canvas, 2, 150, 125),
             Platform(canvas, 1, 0, 50)]
man = Man(canvas, platforms, 6, 8)

def handle_timer_event():
    man.move()
    tk.after(20, handle_timer_event)

handle_timer_event()
tk.mainloop()
