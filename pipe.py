import pygame
pygame.init()


class Pipe():

	def __init__(self,game_settings,screen):
		self.game_settings = game_settings
		self.screen = screen

		self.image = pygame.image.load('image/pipe.bmp')
		self.rect = self.image.get_rect()

		self.rect.x = 0
		self.rect.y = 0

	def blitme(self):
		self.screen.blit(self.image,self.rect)


