import pygame
pygame.init()
class Wind:
    def __init__(self, x = 800, y = 600, caption = 'Числа'):
        self.w = x
        self.h = y
        self.caption = caption
        self.win = pygame.display.set_mode((self.w, self.h))
        pygame.display.set_caption(self.caption)
        self.font = pygame.font.SysFont('arial', 24)
        self.win.fill((255, 255, 255))

        pass