from item import Item
class Character:
	def __init__(self, name, uni, location):
		self.location = location
		self.name = name
		self.uni = uni # unicode character representation
		self.health = 100

	def __str__(self):
		return self.name

	def __repr__(self):
		return self.uni


class Player(Character):
	def __init__(self):
		super().__init__('Hero', '@', (8,5))
		self.keyring = []

	def add_key(self, item):
		self.keyring.append(item)

	def view_keyring(self):
		msg = 'You have these keys:'
		for key in self.keyring:
			msg += f'\n{key.name}'
		return msg

class Boss(Character):
	def __init__(self):
		super().__init__('Boss', 'B', (2,5))
		self.set_area()

	def set_area(self):
		self.boss_area = [(self.location[0]-1, self.location[1]),
				  (self.location[0]+1, self.location[1]),
				  (self.location[0], self.location[1]-1),
				  (self.location[0], self.location[1]+1)]

	def check(self, player):
		if player.location in self.boss_area:
			return True
		return False
			

		
