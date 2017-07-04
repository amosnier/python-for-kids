def hello():
    print('hello there')
        
import tkinter
tk = tkinter.Tk()
button = tkinter.Button(tk, text="click me", command = hello)
button.pack()
tk.mainloop()
