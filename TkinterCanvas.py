import tkinter

canvas = tkinter.Canvas()
canvas.pack()

def draw_flag_stripes(basex = 0, basey = 0, width = 250, height = 150, colors = None, stripecount = 3, direction = None):
    if colors is None:
        colors = ["green", "white", "red"]
    if basex < 0 or basey < 0 or width < 0 or height < 0 or stripecount < 0:
        canvas.create_text(100, 200, text="Invalid size and position parameters")
    else:
        value = 0
        color_index = 0

        match direction:
            case "horizontal":
                height = height / 3
                while value < stripecount:
                    if color_index >= len(colors):
                        color_index = 0
                    curr_color = colors[color_index]
                    canvas.create_rectangle(basex, basey + (value * height), basex + width,
                                            basey + height + (value * height),
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
                                            basey + height,
                                            fill=curr_color)
                    value += 1
                    color_index += 1
            case _:
                canvas.create_text(100, 200, text="Invalid direction parameter")

draw_flag_stripes(basex = 50, basey = 50, width = 270, height = 150, colors = ["green", "white", "darkorange"], stripecount = 3, direction="vertical")

tkinter.mainloop()
exit (0)

