import math

import pygame

pygame.init()


class DrawParams:

    BLACK = 0, 0, 0
    WHITE = 255, 255, 255
    GREEN = 0, 255, 0
    RED = 255, 0, 0
    BLUE = 0, 0, 255
    FONT = pygame.font.SysFont('comicsans', 30)
    L_FONT = pygame.font.SysFont('comicsans', 40)
    GRAY1 = 128, 128, 128
    GRAY2 = 162, 162, 162
    GRAY3 = 190, 190, 190
    BACKGROUND = WHITE
    PADDING = 100
    SHADES = [GRAY1, GRAY2, GRAY3]
    ASCENDING = True

    def __init__(self, wid, hei, lis):
        self.width = wid
        self.height = hei
        self.window = pygame.display.set_mode((wid,hei))
        self.list_set(lis)

        pygame.display.set_caption("Sorting Visualizer")

    def list_set(self, lis):

        self.list = lis
        self.min, self.max = min(lis), max(lis)
        self.bar_width = (self.width - self.PADDING) // len(self.list)
        self.bar_height = (self.height - self.PADDING * 1.5) // (self.max - self.min)
        self.x = self.PADDING // 2
