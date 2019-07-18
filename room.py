from item import Item
from random import randint, choice

class Coord():
	def __init__(self, in_coord, item=None):
		self.coord = in_coord
		self.has = item

	def __str__(self):
		return str(self.has)

	def __repr__(self):
		return str(self.has)

	def place(self, in_item):
		self.has = in_item

class Room():
	def __init__(self, characters, width, height):
		self.characters = characters
		self.coord_list = []
		self.width = width
		self.height = height
		
		# Fill the room with coordinates that have no item
		for i in range(height):
			temp = []
			for j in range(width):	
				item = Item('WALL', "☐")
				if (i == 0) or (i == width-1):
					inside = Coord((i, j), item)
					temp.append(inside)
				elif (j == 0) or (j == height-1):
					inside = Coord((i, j), item)
					temp.append(inside)
				else:
					inside = Coord((i,j), Item('Blank', ' '))
					temp.append(inside)
				
			self.coord_list.append(temp)

		# Make a single sample box at 1 down, 5 right
		# single_box = item.Item('box', '☐')
		# self.coord_list[1][5].place(single_box)
	
	def __repr__(self):
		temp_var = ''
		for i in range(self.height):
			for j in range(self.width):
				temp_var += str(self.coord_list[i][j].has.uni) + ' '
			temp_var += '\n'
		return temp_var

	def spawn(self, item, position=(0, 0)):
		i, j = position
		# TODO Change .has to .has.name
		if self.coord_list[i][j].has.name not in ['WALL', 'BOSS', 'Hero', 'Key']: 
			self.coord_list[i][j].has = item
			return True
		return False

	def set_blank(self, pos):
		i, j = pos
		if self.coord_list[i][j].has.name is not 'WALL':
			self.coord_list[i][j].has = Item('Blank', ' ')

	def add_door(self):
		choices = [(0, randint(1,self.width-2)), 
				   (self.height-1, randint(1, self.width-2)),
				   (randint(1, self.height-2), 0),
				   (randint(1, self.height-2), self.width-1)
				  ]
		i, j = choice(choices)
		self.door = Item('Door', 'D')
		self.door.location = (i, j)
		self.coord_list[i][j].has = self.door
		self.door_area = [(self.door.location[0]-1, self.door.location[1]),
				  (self.door.location[0]+1, self.door.location[1]),
				  (self.door.location[0], self.door.location[1]-1),
				  (self.door.location[0], self.door.location[1]+1)]

	def door_check(self, player):
		if player.location in self.door_area:
			if player.keyring[0].name == 'Key':
				i, j = self.door.location
				self.coord_list[i][j].has = Item('Blank', ' ')
				self.door.location = (-1,-1)
				self.set_area()
				player.keyring[0] = None
				return True
		return False


	def set_area(self):
		self.door_area = [(self.door.location[0]-1, self.door.location[1]),
				  (self.door.location[0]+1, self.door.location[1]),
				  (self.door.location[0], self.door.location[1]-1),
				  (self.door.location[0], self.door.location[1]+1)]