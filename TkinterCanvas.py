import tkinter

canvas = tkinter.Canvas()
canvas.pack()

def draw_spiral(basex,basey,size,spread,limit,colors):
    color_amount = len(colors)
    colors = colors.append(str(color_amount))

    value = 0
    color_index = 0
    while value < limit:
        if color_index >= color_amount:
            color_index = 0

        curr_color = colors[color_index]

        canvas.create_rectangle(basex + (value * spread), basey + (value * spread), size + basex - (value * spread),
                                size + basey - (value * spread), fill=curr_color)
        value += 1
        color_index += 1

def draw_flag_stripes(basex = 0, basey = 0, width = 250, heigth = 150, colors = None, stripecount = 3, direction = None):
    if colors is None:
        colors = ["green", "white", "red"]
    if basex < 0 or basey < 0 or width < 0 or heigth < 0 or stripecount < 0:
        canvas.create_text(100, 200, text="Invalid size and position parameters")
    else:
        value = 0
        color_index = 0

        match direction:
            case "horizontal":
                heigth = heigth / 3
                while value < stripecount:
                    if color_index >= len(colors):
                        color_index = 0
                    curr_color = colors[color_index]
                    canvas.create_rectangle(basex, basey + (value * heigth), basex + width,
                                            basey + heigth + (value * heigth),
                                            fill=curr_color)
                    value += 1
                    color_index += 1
            case "vertical":
                width = width / 3
                while value < stripecount:
                    if color_index >= len(colors):
                        color_index = 0
                    curr_color = colors[color_index]
                    canvas.create_rectangle(basex + (value * width), basey, basex + width + (value * width),
                                            basey + heigth,
                                            fill=curr_color)

                    value += 1
                    color_index += 1
            case _:
                canvas.create_text(100, 200, text="Invalid direction parameter")

"""
basex = 100
basey = 10
size = 150
spread = 10
limit = 5
colors = ["pink", "yellow"]
#draw_spiral(basex,basey,size,spread,limit,colors)
"""

draw_flag_stripes(basex = 5, basey = 5, width = 250, heigth = 150, colors = ["green", "white", "red"], stripecount = 3, direction= "vertical")


tkinter.mainloop()

