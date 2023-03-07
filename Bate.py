import pygame
class Bate:

   def __init__ (self, speed, imagen):
       self.__img = pygame.image.load(imagen)
       self.__rect = self.__img.get_rect()
       self.__speed = speed

   @property
   def rect(self):
       return self.__rect

   @rect.setter
   def rect(self, valor):
       self.__rect = valor

   @property
   def speed(self):
       return self.__speed

   @speed.setter
   def speed(self, valor):
       self.__speed = valor

   @property
   def imagen(self):
       return self.__img

   @imagen.setter
   def imagen(self, valor):
       self.__img = valor