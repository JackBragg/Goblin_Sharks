'''
this is just a test
'''
class Character:
	def __init__(self, name, uni, location=(8, 5)):
		self.location = location
		self.name = name
		self.uni = uni # unicode character representation

	def __str__(self):
		return self.name

	def __repr__(self):
		return self.uni

class Player(Character):
	def __init__(self):
		super().__init__('Hero', '@', (8,5))
		
