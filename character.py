from item import Item
class Character:
	def __init__(self, name, uni, location=(8, 5)):
		self.location = location
		self.name = name
		self.uni = uni # unicode character representation
		self.keyring = []

	def __str__(self):
		return self.name

	def __repr__(self):
		return self.uni

	def add_key(self, item):
		if type(item) is type(Item):
			self.keyring.append(item)

	def view_keyring(self):
		msg = 'You have these keys:'
		for key in self.keyring:
			msg += f'\n{key.name}'
		return msg

class Player(Character):
	def __init__(self):
		super().__init__('Hero', '@', (8,5))


		
