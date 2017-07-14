import tkinter

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

ball = canvas.create_oval(10, 10, 25, 25, fill='red')

def handle_timer_event():
    canvas.move(ball, 10, 0)
    tk.after(100, handle_timer_event)

handle_timer_event()

tk.mainloop()
