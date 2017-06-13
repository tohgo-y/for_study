from tkinter import *
tk = Tk()
canvas = Canvas(tk, width=500, height=500)
canvas.pack()

x = (11, 11)
y = (490, 490)

canvas.create_rectangle(x, y)
