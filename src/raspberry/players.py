import pygame
from simple_rpc import Interface

class Player(pygame.sprite.Sprite):
	def __init__(self, idx, score_layout):
		super().__init__() 
		self.image = pygame.image.load("black.jpg")
		self.surf = pygame.Surface((175, 120))
		self.rect = self.surf.get_rect(center = (600, 300))		
		self.playerIdx = idx
		self.score_layout = score_layout
		self.reset()
		

	def reset(self):
		# reset points achived
		self.scored_points = 0
		# establish communication with micro-controller (reconnect as this will also reset the mc-state)
		self.interface = Interface(f"/dev/ttyACM{self.playerIdx}")
		
    
	def update(self):
		# Get button count
		button_state = self.interface.call_method('button_state')
		new_points_scored = 0

		for i in range(len(button_state)):
			new_points_scored = new_points_scored + self.score_layout[i] * button_state[i]

		diff = new_points_scored - self.scored_points
	
		if (diff > 0):
			print(f"Moving {diff} fields")
			# move the sprite along by <diff> fields
			self.rect.move_ip(-10 * diff, 0) # Move to the left
			self.scored_points = new_points_scored