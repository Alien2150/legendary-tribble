import pygame
from pygame.locals import *
from gameStates import *
 
class App:
	def __init__(self, numPlayers):
		self._running = True
		self._display_surf = None
		self.size = self.weight, self.height = 800, 600
		self.numPlayers = numPlayers
		self.fps = pygame.time.Clock()
		self.current_scene = StartingGameScene()
		self.running_game_scene = RunningGameScene(1)
 
	def on_init(self):
		pygame.init()
		self._display_surf = pygame.display.set_mode(self.size, pygame.HWSURFACE | pygame.DOUBLEBUF)
		self._running = True
		self.current_scene.onEnter()
 
	def on_event(self, event):
		if event.type == pygame.QUIT:
			self._running = False

	def on_loop(self, dt):
		self.current_scene.update(dt)
		if self.current_scene.finished():
			self.current_scene = self.running_game_scene

	def on_render(self):
		self._display_surf.fill((255, 255, 255))
		self.current_scene.on_render(self._display_surf)
		pygame.display.update()

	def on_cleanup(self):
		pygame.quit()
 
	def on_execute(self):
		if self.on_init() == False:
			self._running = False
 
		while( self._running ):
			dt = self.fps.tick(200) / 1000
			for event in pygame.event.get():
				self.on_event(event)
			# update game logic 
			self.on_loop(dt)
			# render
			self.on_render()
			

		self.on_cleanup()
 
if __name__ == "__main__" :
	app = App(1)
	app.on_execute()
