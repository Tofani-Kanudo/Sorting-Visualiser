from main_helper import drawing_list


def insertion_sort(draw_params):
    for i in range(1, len(draw_params.list)):
        key = draw_params.list[i]

        j = i - 1
        while j >= 0 and ((key < draw_params.list[j] and draw_params.ASCENDING) or
                          (key > draw_params.list[j] and not draw_params.ASCENDING)):
            draw_params.list[j + 1] = draw_params.list[j]
            j -= 1
            drawing_list(draw_params, {i: draw_params.GREEN, j : draw_params.RED, j+1 : draw_params.BLUE}, True)
            yield True
        draw_params.list[j + 1] = key
