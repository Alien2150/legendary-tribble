from animatedObjects import *
from players import *

class GameScene:
	def onEnter(self):
		pass

	def onExit(self):
		pass
	
	def update(self, dt):
		pass

	def on_render(self, screen):
		pass
	
	def finished(self):
		return False

class StartingGameScene(GameScene):

	def onEnter(self):
		print(f"Font: {pygame.font.get_default_font()}")
		self.animatedText = AnimatedCountdownText(30, 50, 5, 4)

	def onExit(self):
		pass 
	
	def update(self, dt):
		self.animatedText.update(dt)

	def on_render(self, screen):
		self.animatedText.on_render(screen)

	def finished(self):
		return self.animatedText.finished()

class RunningGameScene(GameScene):
	def __init__(self, numPlayers):
		# build a sprite group
		self.numPlayers = numPlayers
		self.allPlayers = pygame.sprite.Group()
		for idx in range(self.numPlayers):
			self.allPlayers.add(Player(idx, [1,1,3]))
	
	def update(self, dt):
		# get delta t
		for entity in self.allPlayers:
			entity.update()

	def on_render(self, screen):
		for entity in self.allPlayers:
			screen.blit(entity.image, entity.rect)

	def onEnter(self):
		pass 

	def onExit(self):
		pass 

	def finished(self):
		return False