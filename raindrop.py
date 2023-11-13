import pygame

from settings import settings

from pygame.sprite import Sprite

class Raindrop(Sprite):
	"""overall class to represent single raindrop in the game"""

	def __init__(self,rd_game):
		"""Initialize the raindrop and its starting position """
		super().__init__()
		self.screen = rd_game.screen
		self.settings = rd_game.settings
		

		#Load the raindrop in the game and get its rect
		self.image = pygame.image.load("raindrop.png")
		self.rect = self.image.get_rect()


		#start each newdrop near the top left of the screen
		self.rect.x = self.rect.width
		self.rect.y = self.rect.height

		#store the raindrop's exact vertical position
		self.y = float(self.rect.y)

	def update(self):
		"""Move the raindrop down the screen"""
		self.y += self.settings.raindrop_speed
		self.rect.y = self.y




