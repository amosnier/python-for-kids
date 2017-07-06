import tkinter
import time

tk = tkinter.Tk()

class Man:
    def __init__(self, canvas, normal_move):
        self.canvas = canvas 
        self.normal_move = normal_move
        self.jump_move = normal_move * 1.4
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
        self.canvas.bind_all('<KeyPress-Left>', self.turn_left)
        self.canvas.bind_all('<KeyPress-Right>', self.turn_right)
        self.canvas.bind_all('<space>', self.jump)
        self.dx = 0
        self.dy = 0
        self.jump_count = 0

    def turn_left(self, event):
        self.dx = -self.normal_move
            
    def turn_right(self, event):
        self.dx = self.normal_move
        
    def jump(self, event):
        if self.dy == 0:
            self.dy = -self.jump_move
            self.jump_count = 0

    def move(self):
        self.check_for_building()
        self.canvas.move(self.id, self.dx, self.dy)
        self.handle_jumping()
        self.animate()

    def coords(self):
        coords = self.canvas.coords(self.id)
        return [coords[0], coords[1],
                coords[0] + self.left_images[0].width(), coords[1] + self.left_images[0].height()]

    def check_for_building(self):
        coords = self.coords()
        self.dx = max(self.dx, -coords[0]) # left wall
        self.dx = min(self.dx, self.canvas_width - coords[2]) # right wall
        self.dy = min(self.dy, self.canvas_height - coords[3]) # floor

    def handle_jumping(self):
        if self.dy >= 0:
            return # not jumping
        # jumping
        self.jump_count += 1
        if self.jump_count > 12:
            self.dy = self.jump_move # reached the top, start falling

    def animate(self):
        if (time.time() - self.image_time) < 0.1:
            return
        self.image_time = time.time()
        next = self.image_index + self.image_index_incr
        if (next < 0 or next >= len(self.left_images)):
            self.image_index_incr = -self.image_index_incr
            self.image_index += self.image_index_incr
        else:
            self.image_index = next
        if self.dx < 0:
            canvas.itemconfig(self.id, image=self.left_images[self.image_index])
        elif self.dx > 0:
            canvas.itemconfig(self.id, image=self.right_images[self.image_index])

class Platform:
    def __init__(self, canvas, platform_type, x, y):
        self.canvas = canvas
        self.canvas_width = self.canvas.winfo_width()
        self.canvas_height = self.canvas.winfo_height()
        self.image_files = ['gif/platform1.gif', 'gif/platform2.gif', 'gif/platform3.gif']
        self.image = tkinter.PhotoImage(file=self.image_files[platform_type])
        self.id = canvas.create_image(x, y, image=self.image, anchor='nw')

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

platforms = [Platform(canvas, 1, 100, 450),
             Platform(canvas, 0, 300, 450)]
man = Man(canvas, 4)

def handle_timer_event():
    man.move()
    tk.after(20, handle_timer_event)

handle_timer_event()
tk.mainloop()
