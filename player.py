import pygame
from settings import *

class Player(pygame.sprite.Sprite):
	def __init__(self, pos, groups, obstacle_sprites):
		super().__init__(groups)
		self.image = pygame.image.load('graphics/player/ninjag.png').convert_alpha()
		self.image = pygame.transform.rotozoom(self.image, 0, 3)
		self.rect = self.image.get_rect(topleft=pos)
		self.hitbox = self.rect.inflate(0, -10)
		self.FOOT_OFFSET = 20

		self.direction = pygame.math.Vector2()
		self.speed = 5

		self.obstacle_sprites = obstacle_sprites

	def input(self):
		keys = pygame.key.get_pressed()

		if keys[pygame.K_UP]:
			self.direction.y = -1
		elif keys[pygame.K_DOWN]:
			self.direction.y = 1
		else:
			self.direction.y = 0

		if keys[pygame.K_RIGHT]:
			self.direction.x = 1
		elif keys[pygame.K_LEFT]:
			self.direction.x = -1
		else:
			self.direction.x = 0

	def move(self, speed):
		if self.direction.magnitude() != 0:
			self.direction = self.direction.normalize()

		self.hitbox.x += self.direction.x * speed
		self.collision('horizontal')
		self.hitbox.y += self.direction.y * speed
		self.collision('vertical')
		self.rect.midbottom = self.hitbox.midbottom

	def collision(self, direction):
		if direction == 'horizontal':
			for sprite in self.obstacle_sprites:
				if sprite.hitbox.colliderect(self.hitbox):
					if self.direction.x > 0:
						self.hitbox.right = sprite.hitbox.left
					if self.direction.x < 0:
						self.hitbox.left = sprite.hitbox.right
		elif direction == 'vertical':
			for sprite in self.obstacle_sprites:
				if sprite.hitbox.colliderect(self.hitbox):
					if self.direction.y > 0:
						self.hitbox.bottom = sprite.hitbox.top
						self.rect.bottom = self.hitbox.bottom + self.FOOT_OFFSET - sprite.rect.height/2
					if self.direction.y < 0:
						self.hitbox.top = sprite.hitbox.bottom

	def update(self):
		self.input()
		self.move(self.speed)

		# Aggiorna la posizione dell'immagine in base alla posizione degli ostacoli
		for sprite in self.obstacle_sprites:
			if sprite.hitbox.colliderect(self.hitbox) and self.direction.y > 0:
				self.rect.bottom = sprite.rect.top + self.FOOT_OFFSET - sprite.rect.height/2