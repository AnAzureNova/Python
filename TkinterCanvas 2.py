import tkinter

canvas = tkinter.Canvas()
canvas.pack()

def draw_sequence(basex = 50, basey = 50, size = 50, ammount = 4, offset = 10, colors = None):
    color_index = 0
    order = "asc"
    color_total = len(colors)

    for index in range(ammount):
        if color_index == color_total-1:
            order = "desc"
        if color_index == 0:
            order = "asc"

        curr_offset = index * offset

        canvas.create_rectangle(basex + curr_offset, basey + curr_offset, basex+size + curr_offset, basey+size + curr_offset, fill=colors[color_index])

        if order == "asc":
            color_index += 1
        elif order == "desc":
            color_index -= 1


draw_sequence(basex = 5, basey = 5, size = 100, ammount = 50, offset = 10, colors = ["#6E4473", "#83518A", "#945C9C", "#A86AB0", "#BC76C4", "#D182D9"])

tkinter.mainloop()
exit (0)