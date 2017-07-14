import tkinter
import time

# Simplest possible event loop with timer event

tk = tkinter.Tk()

def handle_timer_event():
    print(time.asctime())
    tk.after(50, handle_timer_event)

handle_timer_event()
tk.mainloop()
