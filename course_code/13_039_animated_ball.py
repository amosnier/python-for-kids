import tkinter

tk = tkinter.Tk()

tk.title("Bounce")
tk.resizable(0, 0)
canvas = tkinter.Canvas(tk, width=500, height=400)
canvas.pack()

ball = canvas.create_oval(10, 10, 25, 25, fill='red')

def handle_timer_event():
    canvas.move(ball, 10, 0)
    tk.after(100, handle_timer_event)

handle_timer_event()
tk.mainloop()
