import pygame
import settings

class Player:
	__player = pygame.Rect(30, 30, 20, 20)

	def __init__(self, name):
		self.__name = name
		pygame.draw.rect(settings.screen, pygame.Color('red'), self.__player)

	def getName(self):
		return self.name