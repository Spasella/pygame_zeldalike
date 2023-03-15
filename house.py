import pygame
from settings import *

class House(pygame.sprite.Sprite):
	def __init__(self,pos,groups):
		super().__init__(groups)
		self.image = pygame.image.load('casa2.png').convert()
		# self.image = pygame.transform.rotozoom(self.image, 0, 2)
		self.rect = self.image.get_rect(topleft=pos)
		self.hitbox = self.rect.inflate(0, -10)