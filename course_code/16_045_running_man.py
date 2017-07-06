import tkinter
import time

tk = tkinter.Tk()

class Man:
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
        self.id = canvas.create_image(start_x, start_y, image=self.left_images[0], anchor='sw')
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
        self.animate()

    def coords(self):
        coords = self.canvas.coords(self.id)
        return [coords[0], coords[1],
                coords[0] + self.left_images[0].width(), coords[1] + self.left_images[0].height()]

    def check_for_walls(self):
        coords = self.coords()
        if (coords[0] + self.dx) <= 0 or (coords[2] + self.dx) >= self.canvas_width:
            self.dx = 0

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
