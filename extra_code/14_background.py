import tkinter

class Background:
    def __init__(self, canvas):
        self.image = tkinter.PhotoImage(file='gif/background.gif')
        w = canvas.winfo_width()
        h = canvas.winfo_height()
        x_step = w // 5
        y_step = h // 5
        for y in range(0, h, y_step):
            for x in range(0, w, x_step):
                canvas.create_image(x, y, image=self.image, anchor='nw')
class App:
    def __init__(self):
        tk = tkinter.Tk()
        self.tk = tk

        tk.title("Mr. Stickman")
        tk.resizable(0, 0)
        # Keep the window on the top
        tk.wm_attributes("-topmost", 1)

        canvas = tkinter.Canvas(tk, width=500, height=500)
        self.canvas = canvas
        # Remove border. Apparently no effect on Linux, but good on Mac
        canvas.configure(bd=0)
        # Make the 0 horizontal and vertical line apparent
        canvas.configure(highlightthickness=0)
        canvas.pack()

        tk.update()

        self.background = Background(canvas)

    def mainloop(self):
        self.tk.mainloop()

app = App()
app.mainloop()
