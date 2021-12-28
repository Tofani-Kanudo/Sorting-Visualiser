from main_helper import drawing_list


def merge_sort(draw_params):
    # start with least partition size of 2^0 = 1
    width = 1
    n = len(draw_params.list)
    # subarray size grows by powers of 2
    # since growth of loop condition is exponential,
    # time consumed is logarithmic (log2n)
    while (width < n):
        # always start from leftmost
        l = 0;
        while (l < n):
            r = min(l + (width * 2 - 1), n - 1)
            m = (l + r) // 2
            # final merge should consider
            # unmerged sublist if input arr
            # size is not power of 2
            if (width > n // 2):
                m = r - (n % width)
            merge(draw_params, l, m, r)
            l += width * 2
        # Increasing sub array size by powers of 2
        width *= 2
        # yield True
        drawing_list(draw_params, {l: draw_params.GREEN, m: draw_params.RED, r: draw_params.BLUE}, True)


# Merge Function
def merge(draw_params, l, m, r):
    n1 = m - l + 1
    n2 = r - m
    L = [0] * n1
    R = [0] * n2
    for i in range(0, n1):
        L[i] = draw_params.list[l + i]
    for i in range(0, n2):
        R[i] = draw_params.list[m + i + 1]

    i, j, k = 0, 0, l
    while i < n1 and j < n2:
        if L[i] > R[j]:
            draw_params.list[k] = R[j]
            j += 1
        else:
            draw_params.list[k] = L[i]
            i += 1
        k += 1
    # yield True
    drawing_list(draw_params, {i: draw_params.GREEN, j: draw_params.RED, k: draw_params.BLUE}, True)

    while i < n1:
        draw_params.list[k] = L[i]
        i += 1
        k += 1

    while j < n2:
        draw_params.list[k] = R[j]
        j += 1
        k += 1