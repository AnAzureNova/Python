import tkinter
import time

canvas = tkinter.Canvas()
canvas.pack()

def draw_target(basex = 10, basey = 10, size = 50, gap = 10, layers = 3, colors = None):
    color_index = 0
    color_total = len(colors)

    for index in range(layers):

        if color_index == color_total:
            color_index = 0

        curr_offset = index * gap

        canvas.create_rectangle(basex + curr_offset, basey + curr_offset, basex+size - curr_offset, basey+size - curr_offset, fill=colors[color_index])
        color_index += 1

draw_target(basex=20, basey=20, size=200, gap=5, layers=20, colors=["black", "white"])

tkinter.mainloop()
exit (0)
