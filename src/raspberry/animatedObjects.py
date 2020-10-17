import pygame.freetype
import math

class AnimatedObject():
	def update(self, dt):
		pass

	def on_render(self, screen):
		pass

class AnimatedCountdownText(AnimatedObject):
	def __init__(self, min_size, max_size, start_value, speed_factor):
		self.min_size = min_size
		self.max_size = max_size
		self.start_value = start_value
		self.time_left = start_value
		self.speed_factor = speed_factor

	def update(self, dt):
		self.time_left = self.time_left - dt

	def on_render(self, screen):
		scalar = (1 - (self.time_left - int(self.time_left)))  * self.speed_factor
		font_size = ((self.max_size - self.min_size) * scalar) + self.min_size
		
		fontSurface = pygame.font.Font(pygame.font.get_default_font(), int(font_size))

		# text = f"{self.time_left:.2}"
		text = f"{int(self.time_left)}"
		text_surface = fontSurface.render(text, True, (0,0,0))
		screen.blit(text_surface, dest=(400-font_size/2,300 - text_surface.get_height()/2))
	
	def finished(self):
		return self.time_left <= 0