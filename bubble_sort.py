from main_helper import drawing_list


def bubble_sort(draw_params):
    n = len(draw_params.list)

    for i in range(n):
        swapped = False

        for j in range(0, n - i - 1):

            if (draw_params.list[j] > draw_params.list[j + 1] and draw_params.ASCENDING) or \
                    (draw_params.list[j] < draw_params.list[j+1] and not draw_params.ASCENDING):
                draw_params.list[j], draw_params.list[j + 1] = draw_params.list[j + 1], draw_params.list[j]
                drawing_list(draw_params, {j: draw_params.GREEN, j + 1: draw_params.RED}, True)
                swapped = True
                yield True

        if swapped is False:
            break
