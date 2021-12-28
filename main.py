import pygame
from main_helper import list_init, drawing
from DrawParams import DrawParams
from bubble_sort import bubble_sort
from insertion_sort import insertion_sort
from merge_sort import merge_sort

pygame.init()


if __name__ == "__main__":
    run = True
    clock = pygame.time.Clock()
    n = 50
    minv = 1
    maxv = 100
    lis = list_init(n, minv, maxv)
    draw_params = DrawParams(1920, 1000, lis)
    sorting = False
    algo = bubble_sort
    algo_name = "Bubble Sort"
    algo_generator = None

    while run:
        clock.tick(1)

        if sorting:
            try:
                next(algo_generator)
                # algo_generator
            except StopIteration:
                sorting = False
        else:
            drawing(draw_params)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if event.type != pygame.KEYDOWN:
                continue

            if event.key == pygame.K_r:
                draw_params.list_set(list_init(n, minv, maxv))
            elif event.key == pygame.K_SPACE:
                sorting = not sorting
                algo_generator = algo(draw_params)
            elif event.key == pygame.K_a and not sorting:
                draw_params.ASCENDING = not draw_params.ASCENDING
            elif event.key == pygame.K_i and not sorting:
                algo = insertion_sort
            elif event.key == pygame.K_b and not sorting:
                algo = bubble_sort
            elif event.key == pygame.K_m and not sorting:
                algo = merge_sort

    pygame.quit()
