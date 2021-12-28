import pygame
import random


def list_init(n, minv, maxv):
    return [random.randint(minv, maxv) for _ in range(n)]


def drawing(draw_params):
    draw_params.window.fill(draw_params.BACKGROUND)
    if draw_params.ASCENDING:
        control = draw_params.FONT.render("R -> Reset | SPACE -> Start Sorting | A -> Descending", 1, draw_params.BLACK)
    else:
        control = draw_params.FONT.render("R -> Reset | SPACE -> Start Sorting | A -> Ascending", 1, draw_params.BLACK)
    draw_params.window.blit(control, ((draw_params.width - control.get_width()) // 2, 5))
    algo = draw_params.FONT.render("I -> Insertion Sort | B -> Bubble Sort | S -> Selection Sort | M -> Merge Sort", 1, draw_params.BLACK)
    draw_params.window.blit(algo, ((draw_params.width - algo.get_width()) // 2, 40))
    algo1 = draw_params.FONT.render("H -> Heap Sort | Q -> Quick Sort", 1, draw_params.BLACK)
    # draw_params.window.blit(algo1, ((draw_params.width - algo1.get_width()) // 2, 75))
    drawing_list(draw_params)
    pygame.display.update()


def drawing_list(draw_params, posi={}, redraw=False):
    lis = draw_params.list

    if redraw:
        clear = (draw_params.PADDING // 2, (draw_params.PADDING * 1.5)//2, draw_params.width - draw_params.PADDING,
                 draw_params.height - (draw_params.PADDING * 1.5))
        pygame.draw.rect(draw_params.window, draw_params.BACKGROUND, clear)

    for i, val in enumerate(lis):
        x = draw_params.x + i * draw_params.bar_width
        y = draw_params.height - (val - draw_params.min) * draw_params.bar_height

        color = draw_params.SHADES[i % 3]

        if i in posi:
            color = posi[i]

        pygame.draw.rect(draw_params.window, color, (x, y-10, draw_params.bar_width, draw_params.height))

    if redraw:
        pygame.display.update()
