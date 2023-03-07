import pygame

class Block:
    def __init__(self, pos_x, pos_y, imagen):
        self.__image = pygame.image.load(imagen)
        self.__rect = self.__image.get_rect()
        self.__rect.move_ip(pos_x, pos_y)

    @property
    def image(self):
        return self.__image

    @property
    def rect(self):
        return self.__rect



